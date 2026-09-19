"""
Personalized Roadmap and Progress Tracking service for TO BE.
Generates structured 5-phase career pathways, calculates live completion metrics, and tracks next steps.
"""

from typing import Dict, Any, List, Optional
from services.database import db_service
from services.career_service import career_service
from services.training_service import TrainingService
from services.learning_service import LearningService

class RoadmapService:
    def __init__(self):
        self.db = db_service
        self.career_srv = career_service
        self.training_srv = TrainingService()
        self.learning_srv = LearningService()

    def generate_personalized_roadmap(self, career_id: str, user_profile: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Synthesize a 5-phase actionable career roadmap tailored to the career and user background.
        Calculates skill gaps: CareerRequirements - UserSkills = Gaps.
        Enriches phases with TVET/TESDA regulations and curated open educational courses.
        """
        career = self.career_srv.get_career_details(career_id)
        if not career:
            raise ValueError(f"Career ID {career_id} not found.")

        current_skills = [s.lower() for s in (user_profile.get("current_skills", []) if user_profile else [])]
        core_skills = career.get("core_skills", [])
        certifications = career.get("certifications", [])
        projects = career.get("portfolio_projects", [])
        resources = career.get("learning_resources", [])
        psoc_code = career.get("psoc_code")

        # 1. Skill Gap Analysis
        known_skills = []
        missing_skills = []
        for s in core_skills:
            if any(k in s.lower() or s.lower() in k for k in current_skills):
                known_skills.append(s)
            else:
                missing_skills.append(s)

        # 2. TVET and Learning Resource Enriched Lookup
        training_regs = self.training_srv.get_qualifications_for_career(career_id)
        learning_recs = self.learning_srv.get_learning_resources_for_career(career_id)
        combined_resources = resources + [
            {"title": r["title"], "type": r["type"], "cost": r["cost"], "provider": r["provider"], "url": r["url"]}
            for r in learning_recs if r.get("url") not in [res.get("url") for res in resources]
        ]

        # Phase 1: Foundations
        phase1_items = []
        foundational_skills = core_skills[:3]
        for skill in foundational_skills:
            is_known = any(k in skill.lower() for k in current_skills)
            desc = f"Master the fundamental mental models, syntax, and principles of {skill}."
            if is_known:
                desc += " (You noted familiarity with this—use this phase to consolidate and verify key concepts)."
            else:
                desc += " (Identified Skill Gap: Prioritize establishing core fundamentals here)."
            
            phase1_items.append({
                "title": f"Master {skill} Fundamentals",
                "description": desc,
                "type": "skill",
                "is_gap": not is_known,
                "estimated_effort": "2–3 weeks",
                "resources": combined_resources[:2]
            })

        # Phase 2: Core Skills & Ecosystem
        phase2_items = []
        advanced_skills = core_skills[3:] or ["Version Control & Git", "System Architecture", "API Integration"]
        for skill in advanced_skills[:3]:
            phase2_items.append({
                "title": f"Deep Dive into {skill}",
                "description": f"Learn practical development workflows, tooling, and best practices with {skill}.",
                "type": "skill",
                "estimated_effort": "3–4 weeks",
                "resources": resources[1:]
            })

        if certifications:
            primary_cert = certifications[0]
            phase2_items.append({
                "title": f"Complete {primary_cert['name']}",
                "description": f"Gain structured credibility through this {primary_cert.get('cost', 'free')} credential offered by {primary_cert.get('provider', 'industry leaders')}.",
                "type": "certification",
                "estimated_effort": "Self-paced",
                "resources": [{"title": primary_cert["name"], "url": primary_cert.get("url", ""), "cost": primary_cert.get("cost", "Free"), "provider": primary_cert.get("provider", "")}]
            })

        # Phase 3: Hands-on Projects
        phase3_items = []
        for proj in projects[:2]:
            phase3_items.append({
                "title": f"Build: {proj.get('title')}",
                "description": proj.get("description", "Practical real-world project demonstrating core competencies."),
                "type": "project",
                "estimated_effort": "2–4 weeks",
                "resources": []
            })

        # Phase 4: Portfolio & Showcase
        phase4_items = [
            {
                "title": "Document Project Case Studies",
                "description": "Write clear READMEs and architecture summaries explaining the problem, your technical choices, and challenges solved.",
                "type": "portfolio",
                "estimated_effort": "1 week",
                "resources": []
            },
            {
                "title": "Deploy Live Demos to Free Cloud Hosting",
                "description": "Host your projects live on platforms like Vercel, Netlify, or GitHub Pages with clean domain links.",
                "type": "portfolio",
                "estimated_effort": "3–5 days",
                "resources": []
            }
        ]

        if len(projects) > 2:
            adv_proj = projects[2]
            phase4_items.insert(0, {
                "title": f"Capstone Project: {adv_proj.get('title')}",
                "description": adv_proj.get("description"),
                "type": "project",
                "estimated_effort": "4 weeks",
                "resources": []
            })

        # Phase 5: Career Ready & Applications
        phase5_items = [
            {
                "title": "Tailor Tech Resume & LinkedIn Profile",
                "description": f"Highlight your projects, {career['title']} core competencies, and verified coursework clearly.",
                "type": "career_preparation",
                "estimated_effort": "1 week",
                "resources": []
            },
            {
                "title": "Practice Domain Technical & Behavioral Interviews",
                "description": "Rehearse explaining your architectural decisions and practicing standard technical questions.",
                "type": "career_preparation",
                "estimated_effort": "2 weeks",
                "resources": []
            },
            {
                "title": "Begin Targeted Applications & Community Networking",
                "description": "Connect with practitioners on LinkedIn, attend local/virtual meetups, and start applying to entry-level or junior opportunities.",
                "type": "career_preparation",
                "estimated_effort": "Ongoing",
                "resources": []
            }
        ]

        phases = [
            {
                "title": "Phase 1 — Foundations",
                "description": "Core concepts, essential syntax, and foundational mental models.",
                "items": phase1_items
            },
            {
                "title": "Phase 2 — Core Skills & Tooling",
                "description": "Frameworks, industry-standard tools, and structured certifications.",
                "items": phase2_items
            },
            {
                "title": "Phase 3 — Hands-On Projects",
                "description": "Building practical, resume-worthy applications of increasing complexity.",
                "items": phase3_items
            },
            {
                "title": "Phase 4 — Portfolio & Showcase",
                "description": "Packaging your work with public case studies, clean code, and live demos.",
                "items": phase4_items
            },
            {
                "title": "Phase 5 — Career Ready",
                "description": "Resume optimization, interview preparation, and entering the job market.",
                "items": phase5_items
            }
        ]

        # Assign unique item IDs and default status to each item
        for p_idx, phase in enumerate(phases):
            for i_idx, item in enumerate(phase["items"]):
                if "id" not in item:
                    item["id"] = f"item_{p_idx}_{i_idx}"
                if "status" not in item:
                    item["status"] = "not_started"

        return {
            "career_id": career_id,
            "title": f"Personalized Path to {career['title']}",
            "description": f"A step-by-step roadmap built to guide your growth toward becoming a {career['title']}.",
            "phases": phases
        }

    def save_and_start_path(self, user_id: str, roadmap_data: Dict[str, Any]) -> str:
        """Save generated roadmap to database and set as active."""
        career_id = roadmap_data.get("career_id")
        title = roadmap_data.get("title")
        description = roadmap_data.get("description", "")
        phases = roadmap_data.get("phases", [])

        # Record career selection
        self.db.save_career_selection(user_id, career_id)

        # Save roadmap
        roadmap_id = self.db.save_full_roadmap(
            user_id=user_id,
            career_id=career_id,
            title=title,
            description=description,
            phases_data=phases
        )
        return roadmap_id

    def calculate_progress(self, roadmap: Dict[str, Any]) -> Dict[str, Any]:
        """Calculate dynamic progress metrics across all phases and overall."""
        if not roadmap or not roadmap.get("phases"):
            return {
                "overall_percentage": 0,
                "completed_count": 0,
                "total_count": 0,
                "in_progress_count": 0,
                "phase_breakdowns": []
            }

        total_items = 0
        completed_items = 0
        in_progress_items = 0
        phase_breakdowns = []

        for p in roadmap.get("phases", []):
            p_items = p.get("items", [])
            p_total = len(p_items)
            p_completed = sum(1 for i in p_items if i.get("status") == "completed")
            p_in_progress = sum(1 for i in p_items if i.get("status") == "in_progress")

            p_pct = int((p_completed / p_total * 100)) if p_total > 0 else 0

            phase_breakdowns.append({
                "phase_id": p.get("id"),
                "title": p.get("title"),
                "total": p_total,
                "completed": p_completed,
                "in_progress": p_in_progress,
                "percentage": p_pct
            })

            total_items += p_total
            completed_items += p_completed
            in_progress_items += p_in_progress

        overall_pct = int((completed_items / total_items * 100)) if total_items > 0 else 0

        return {
            "overall_percentage": overall_pct,
            "completed_count": completed_items,
            "total_count": total_items,
            "in_progress_count": in_progress_items,
            "phase_breakdowns": phase_breakdowns
        }

    def get_next_recommended_step(self, roadmap: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Identify the single next unfinished task to reduce overwhelm."""
        if not roadmap or not roadmap.get("phases"):
            return None

        # First priority: Any task actively in_progress
        for phase in roadmap.get("phases", []):
            for item in phase.get("items", []):
                if item.get("status") == "in_progress":
                    return {
                        "item": item,
                        "phase_title": phase.get("title"),
                        "status": "in_progress"
                    }

        # Second priority: First not_started/incomplete item in earliest incomplete phase
        for phase in roadmap.get("phases", []):
            for item in phase.get("items", []):
                if item.get("status", "not_started") != "completed":
                    return {
                        "item": item,
                        "phase_title": phase.get("title"),
                        "status": item.get("status", "not_started")
                    }

        return None

# Singleton instance
roadmap_service = RoadmapService()
