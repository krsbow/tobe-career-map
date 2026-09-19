"""
Selective context builder for TOBE AI Career Mentor.
Extracts only query-relevant user profile attributes (skills, traits, constraints, roadmap)
and structures supporting career facts without overriding user intent.
"""

from typing import Dict, Any, List, Optional
from services.career_retrieval import career_retrieval_service
from services.conversation import conversation_manager
from utils.security import scrub_pii_for_ai

class ContextBuilder:
    def __init__(self):
        self.retrieval_svc = career_retrieval_service
        self.conv_mgr = conversation_manager

    def build_prompt_context(
        self,
        query: str,
        chat_history: List[Dict[str, str]],
        user_context: Optional[Dict[str, Any]] = None,
        page_career: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Builds a streamlined, secure context package for the AI mentor turn.
        User intent remains the primary driver; career and user profile act as supporting signals.
        """
        q = query.lower()
        scrubbed_user = scrub_pii_for_ai(user_context or {})
        
        # 1. Resolve Active Career Context
        inferred_subject = self.conv_mgr.resolve_subject_from_history(query, chat_history)
        active_career_title = None
        if page_career and page_career.get("title"):
            active_career_title = page_career.get("title")
        elif inferred_subject:
            active_career_title = inferred_subject
        elif scrubbed_user.get("active_career", {}).get("title"):
            active_career_title = scrubbed_user.get("active_career", {}).get("title")

        # 2. Retrieve targeted knowledge facts for this query
        retrieved_facts = self.retrieval_svc.retrieve_relevant_facts(query, active_career_title)

        # 3. Selectively extract relevant user attributes (only if helpful for the query)
        relevant_user_signals = []
        preferred_name = scrubbed_user.get("preferred_name", "Explorer")
        
        # Check if user has relevant skills or traits mentioned in profile
        profile = scrubbed_user.get("profile", {})
        known_skills = profile.get("current_skills", [])
        top_traits = profile.get("top_dimensions", [])
        
        if any(w in q for w in ["fit", "right for me", "match", "capable", "background"]):
            if known_skills:
                relevant_user_signals.append(f"User known skills: {', '.join(known_skills[:5])}")
            if top_traits:
                relevant_user_signals.append(f"User top interest dimensions: {', '.join(top_traits)}")

        roadmap_prog = scrubbed_user.get("roadmap_progress", {})
        if any(w in q for w in ["progress", "next step", "where was i", "roadmap"]):
            if roadmap_prog.get("total_count", 0) > 0:
                relevant_user_signals.append(
                    f"Roadmap progress: {roadmap_prog.get('overall_percentage', 0)}% completed ({roadmap_prog.get('completed_count', 0)} of {roadmap_prog.get('total_count', 0)} milestones)"
                )

        # 4. Windowed Conversation History String
        formatted_history = self.conv_mgr.format_history_for_prompt(chat_history)

        return {
            "preferred_name": preferred_name,
            "active_career_title": active_career_title,
            "retrieved_facts": retrieved_facts,
            "user_signals": relevant_user_signals,
            "formatted_history": formatted_history,
            "sanitized_query": query.strip()
        }

    def build_system_instruction(self, context_pack: Dict[str, Any]) -> str:
        """Construct grounded, human-mentor system prompt."""
        name = context_pack.get("preferred_name", "Explorer")
        career_title = context_pack.get("active_career_title", "General Exploration")
        facts = context_pack.get("retrieved_facts", [])
        signals = context_pack.get("user_signals", [])

        facts_block = "\n".join(f"• {f}" for f in facts) if facts else "No specific career facts needed for this general query."
        signals_block = "\n".join(f"• {s}" for s in signals) if signals else "User is exploring freely without rigid constraints."

        return f"""You are TOBE, a calm, supportive, and knowledgeable conversational AI career mentor for the TO BE career discovery platform.

CORE PRINCIPLES & RULES:
1. ALWAYS DIRECTLY ANSWER THE USER'S ACTUAL QUESTION FIRST:
   - If the user asks about drawing, difficulty, time constraints, or degrees, directly answer that question.
   - Do NOT deflect to generic career overviews or roadmap summaries.
   - Supporting career context ({career_title}) is provided for context, but MUST NEVER override the user's specific intent.

2. CONVERSATION TONE & WRITING STYLE:
   - Warm, natural, concise, and grounded like a real mentor speaking to one person.
   - DO NOT USE MARKDOWN BOLD (NO ** SYNTAX ANYWHERE).
   - Use short paragraphs and simple bullet points (•) when providing actionable steps.
   - NEVER start with generic canned openings like "That is a thoughtful question...", "When exploring this direction...", "The most practical approach...", or "To answer your question directly...".

3. RELEVANT FACTS & KNOWLEDGE:
{facts_block}

4. USER SIGNALS:
{signals_block}
"""

# Singleton instance
context_builder = ContextBuilder()
