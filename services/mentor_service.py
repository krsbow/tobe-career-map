"""
TOBE AI Career Companion service.
Provides grounded, empathetic career counseling with user profile and roadmap context.
"""

from typing import Dict, Any, List, Optional
from config import AI_MENTOR_NAME, PROJECT_NAME
from services.llm_service import llm_service
from services.database import db_service
from utils.security import scrub_pii_for_ai, sanitize_chat_prompt

class MentorService:
    def __init__(self):
        self.llm = llm_service
        self.db = db_service

    def get_prompt_starters(self) -> List[str]:
        """Return thoughtful conversation starters for user exploration."""
        return [
            "I'm interested in Cybersecurity, but I'm not sure if I'd actually enjoy the daily work. How can I test the waters?",
            "What is the practical difference between a UX Designer and a Front-End Developer?",
            "I don't have a Computer Science degree. How should I approach building my first technical portfolio?",
            "How do I choose between Full-Stack Development and Data Analytics based on my RIASEC profile?",
            "I'm feeling overwhelmed by everything I need to learn. Where should I focus this week?"
        ]

    def build_system_prompt(self, user_context: Dict[str, Any]) -> str:
        """Construct grounded system prompt for TOBE."""
        preferred_name = user_context.get("preferred_name", "the explorer")
        profile = user_context.get("profile", {})
        active_career = user_context.get("active_career", {})
        roadmap_progress = user_context.get("roadmap_progress", {})

        top_traits = profile.get("top_dimensions", [])
        skills = profile.get("current_skills", [])
        priorities = profile.get("career_priorities", [])

        prompt = f"""You are {AI_MENTOR_NAME}, the supportive and knowledgeable conversational career companion inside the {PROJECT_NAME} platform.

CORE PRINCIPLES:
1. EXPLORATION OVER PREDICTION: Never tell the user "This is your one true career" or "You should become X." Support their exploration and help them think through trade-offs.
2. USER AGENCY: The user always remains the decision-maker. Offer perspectives, mental models, and practical experiments.
3. SKILLS ARE LEARNABLE: Never claim a user is unqualified because they lack current experience. Frame gaps as exciting learning milestones.
4. EVIDENCE OVER INVENTION: Do not fabricate unrealistic salary guarantees, degrees, or certifications.
5. CONCISE, WARM & ENCOURAGING: Keep your responses conversational, structured with short bullet points where helpful, and calm.

CURRENT USER CONTEXT:
- Preferred Name: {preferred_name}
- Top Interests (RIASEC): {', '.join(top_traits) if top_traits else 'Exploring'}
- Current Skills: {', '.join(skills) if skills else 'Starting fresh'}
- Core Priorities: {', '.join(priorities) if priorities else 'Career growth & learning'}
- Current Selected Career: {active_career.get('title', 'Still exploring possibilities')}
- Active Roadmap Progress: {roadmap_progress.get('overall_percentage', 0)}% ({roadmap_progress.get('completed_count', 0)} of {roadmap_progress.get('total_count', 0)} milestones completed)

When responding to {preferred_name}:
- Acknowledge any feelings of uncertainty or hesitation.
- Reference their context naturally when relevant (e.g. 'Since you enjoy visual problem solving...').
- Suggest practical, low-risk steps they can take next.
"""
        return prompt

    def generate_mentor_reply(self, user_id: str, message: str, chat_history: List[Dict[str, str]]) -> str:
        """Generate response from TOBE."""
        sanitized_msg = sanitize_chat_prompt(message)
        if not sanitized_msg:
            return "How can I help you think through your career path today?"

        # Gather user context
        profile_rec = self.db.get_latest_assessment_result(user_id) or {}
        user_prof = self.db.get_profile(user_id) or {}
        active_roadmap = self.db.get_active_roadmap(user_id)
        
        active_career = {}
        progress_info = {}
        if active_roadmap:
            active_career = self.db.get_career_by_id(active_roadmap.get("career_id")) or {}
            # Quick progress calc
            total = sum(len(p.get("items", [])) for p in active_roadmap.get("phases", []))
            completed = sum(1 for p in active_roadmap.get("phases", []) for i in p.get("items", []) if i.get("status") == "completed")
            pct = int((completed / total * 100)) if total > 0 else 0
            progress_info = {"overall_percentage": pct, "completed_count": completed, "total_count": total}

        user_context = {
            "preferred_name": user_prof.get("preferred_name", "Explorer"),
            "profile": profile_rec,
            "active_career": active_career,
            "roadmap_progress": progress_info
        }

        # Scrub PII
        scrubbed_context = scrub_pii_for_ai(user_context)
        system_prompt = self.build_system_prompt(scrubbed_context)

        # Build prompt conversation
        conversation_context = ""
        for turn in chat_history[-6:]:
            role = "User" if turn.get("role") == "user" else AI_MENTOR_NAME
            conversation_context += f"\n{role}: {turn.get('content', '')}"

        full_user_prompt = f"{conversation_context}\nUser: {sanitized_msg}\n{AI_MENTOR_NAME}:"

        response = self.llm.generate_text(system_prompt=system_prompt, user_prompt=full_user_prompt)
        return response

# Singleton instance
mentor_service = MentorService()
