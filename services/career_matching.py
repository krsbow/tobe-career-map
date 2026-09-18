"""
Explainable Career Recommendation & Matching Engine for TO BE.
Matches user's multi-dimensional profile to career opportunities without false precision or skill disqualification.
"""

from typing import Dict, Any, List
from data.seed_data import CAREERS_SEED

class CareerMatchingEngine:
    @staticmethod
    def match_careers(profile: Dict[str, Any], careers_catalog: List[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        Evaluate career possibilities against user profile.
        Returns multiple possibilities with explainable alignment and growth roadmaps.
        """
        if careers_catalog is None:
            careers_catalog = CAREERS_SEED

        riasec_scores = profile.get("riasec_scores", {})
        current_skills = [s.lower() for s in profile.get("current_skills", [])]
        user_top_dims = profile.get("top_dimensions", ["I", "A", "R"])
        career_priorities = [p.lower() for p in profile.get("career_priorities", [])]
        work_prefs = [w.lower() for w in profile.get("work_preferences", [])]

        matched_results = []

        for career in careers_catalog:
            career_id = career.get("id")
            career_title = career.get("title")
            career_traits = career.get("riasec_traits", [])
            core_skills = career.get("core_skills", [])
            optional_skills = career.get("optional_skills", [])
            all_career_skills = [s.lower() for s in core_skills + optional_skills]

            # 1. Calculate Interest Overlap (Primary driver)
            trait_match_score = 0
            for trait in career_traits:
                dim_data = riasec_scores.get(trait, {})
                score = dim_data.get("score", 0)
                trait_match_score += score

            # Normalize trait score (0 - 100)
            avg_trait_score = trait_match_score / max(1, len(career_traits))

            # 2. Identify Overlapping Existing Skills vs Skills to Develop
            known_skills = []
            skills_to_develop = []

            for s in core_skills:
                s_lower = s.lower()
                # Check fuzzy or direct match
                if any(k in s_lower or s_lower in k for k in current_skills):
                    known_skills.append(s)
                else:
                    skills_to_develop.append(s)

            # 3. Determine Alignment Tier (Transparent, no pseudo-exact decimals)
            # Alignment is driven primarily by interest/style match, plus positive boost from existing skills
            skill_boost = min(20, len(known_skills) * 5)
            total_alignment_metric = avg_trait_score + skill_boost

            if total_alignment_metric >= 55:
                alignment_tier = "Strong alignment"
                badge_color = "#2563EB"
            else:
                alignment_tier = "Worth exploring"
                badge_color = "#0D9488"

            # 4. Generate Explainable "Why this career appeared"
            reasons = []
            
            # Primary RIASEC trait explanation
            if "A" in career_traits and riasec_scores.get("A", {}).get("level") in ["High", "Medium"]:
                reasons.append("Your profile reflects strong creative, visual, and user-centered interests.")
            if "I" in career_traits and riasec_scores.get("I", {}).get("level") in ["High", "Medium"]:
                reasons.append("You enjoy analytical problem-solving, structured logic, and investigating systems.")
            if "R" in career_traits and riasec_scores.get("R", {}).get("level") in ["High", "Medium"]:
                reasons.append("You appreciate hands-on technical architecture, building tangible tools, or system foundations.")
            if "E" in career_traits and riasec_scores.get("E", {}).get("level") in ["High", "Medium"]:
                reasons.append("You have an affinity for strategic decision-making, product direction, and impact.")
            if "C" in career_traits and riasec_scores.get("C", {}).get("level") in ["High", "Medium"]:
                reasons.append("You value methodical quality, structured workflows, and data accuracy.")
            if "S" in career_traits and riasec_scores.get("S", {}).get("level") in ["High", "Medium"]:
                reasons.append("You value human empathy, clear communication, and collaborative work.")

            # Existing skill alignment explanation
            if known_skills:
                reasons.append(f"You already have relevant experience with {', '.join(known_skills[:3])}.")
            else:
                reasons.append("Your curiosity and interests align well with this domain even without prior background.")

            if not reasons:
                reasons.append("This role connects with your problem-solving style and growth goals.")

            matched_results.append({
                "career_id": career_id,
                "title": career_title,
                "category_id": career.get("category_id"),
                "category_name": career.get("category_name"),
                "tagline": career.get("tagline"),
                "description": career.get("description"),
                "alignment_tier": alignment_tier,
                "badge_color": badge_color,
                "alignment_score": total_alignment_metric,
                "why_it_appeared": reasons,
                "what_to_develop": skills_to_develop[:4],
                "known_skills": known_skills,
                "core_skills": core_skills[:4],
                "salary_summary": career.get("salary_data", {}).get("philippines", {}).get("mid_level", "Competitive")
            })

        # Sort by total alignment metric
        matched_results = sorted(matched_results, key=lambda x: x["alignment_score"], reverse=True)
        return matched_results

# Singleton instance
matching_engine = CareerMatchingEngine()
