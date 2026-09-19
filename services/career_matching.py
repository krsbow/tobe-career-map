"""
Explainable Career Recommendation & Matching Engine for TO BE.
Matches user multi-dimensional profile (RIASEC, multi-domain skills, work preferences, priorities)
to verified career opportunities across technology, design, healthcare, engineering, business, finance, and trades.
Zero fake precision (e.g. 97.4% match). Produces transparent qualitative tiers and natural-language explanations.
"""

from typing import Dict, Any, List, Optional
from services.psoc_service import PSOCService
from services.onet_service import ONETService

class CareerMatchingEngine:
    @staticmethod
    def match_careers(profile: Dict[str, Any], careers_catalog: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Evaluate career possibilities against user profile.
        Returns multiple possibilities categorized into qualitative alignment tiers with human-readable explanations.
        """
        riasec_scores = profile.get("riasec_scores", {})
        current_skills = [s.lower() for s in profile.get("current_skills", [])]
        work_prefs = [w.lower() for w in profile.get("work_preferences", [])]
        career_priorities = [p.lower() for p in profile.get("career_priorities", [])]
        user_top_traits = profile.get("top_traits", [])

        matched_results = []

        for career in careers_catalog:
            career_id = career.get("id")
            career_title = career.get("title")
            career_traits = career.get("riasec_traits", [])
            core_skills = career.get("core_skills", [])
            optional_skills = career.get("optional_skills", [])
            psoc_code = career.get("psoc_code")
            soc_code = career.get("soc_code")

            # 1. RIASEC Alignment Scoring (0 to 100)
            trait_points = 0
            for idx, trait in enumerate(career_traits):
                dim_data = riasec_scores.get(trait, {})
                score = dim_data.get("score", 50) if isinstance(dim_data, dict) else dim_data
                weight = 1.0 - (idx * 0.15) # primary trait gets highest weight
                trait_points += score * weight

            max_possible_points = sum(100 * (1.0 - (idx * 0.15)) for idx in range(len(career_traits))) or 100
            riasec_match_score = (trait_points / max_possible_points) * 100

            # 2. Skill Overlap & Gap Identification
            known_skills = []
            skills_to_develop = []

            for s in core_skills:
                s_lower = s.lower()
                if any(k in s_lower or s_lower in k for k in current_skills):
                    known_skills.append(s)
                else:
                    skills_to_develop.append(s)

            skill_match_ratio = len(known_skills) / max(1, len(core_skills))

            # 3. Work Preference & Priority Alignment
            preference_bonus = 0
            career_style = career.get("work_style", "").lower()

            for pref in work_prefs:
                if (
                    ("independent" in pref and "independent" in career_style)
                    or ("collaborative" in pref and ("team" in career_style or "collaborative" in career_style))
                    or ("structured" in pref and ("structured" in career_style or "methodical" in career_style))
                    or ("creative" in pref and ("creative" in career_style or "design" in career_style or "innovative" in career_style))
                    or ("people" in pref and ("people" in career_style or "patient" in career_style or "client" in career_style))
                    or ("analytical" in pref and ("analytical" in career_style or "data" in career_style or "investigative" in career_style))
                    or ("hands-on" in pref and ("hands-on" in career_style or "physical" in career_style or "practical" in career_style))
                ):
                    preference_bonus += 5

            # Priority Boost
            priority_bonus = 0
            for prio in career_priorities:
                if "income" in prio and "senior_level" in str(career.get("salary_data", {})):
                    priority_bonus += 4
                elif "stability" in prio and career.get("category_id") in ["healthcare", "engineering", "finance", "education"]:
                    priority_bonus += 4
                elif "flexibility" in prio and career.get("category_id") in ["development", "design", "data_ai", "marketing"]:
                    priority_bonus += 4
                elif "creativity" in prio and career.get("category_id") in ["design", "development", "marketing"]:
                    priority_bonus += 4
            # Matched Holland traits
            matched_dominant_traits = [t for t in career_traits if t in user_top_traits]

            # 4. Synthesize Qualitative Alignment Tier (No fake decimals)
            composite_metric = (riasec_match_score * 0.55) + (skill_match_ratio * 30) + preference_bonus + priority_bonus

            if composite_metric >= 55 or (riasec_match_score >= 65 and len(matched_dominant_traits) >= 2):
                tier = "Strong alignment"
                badge_style = "strong"
            elif composite_metric >= 38 or riasec_match_score >= 45:
                tier = "Worth exploring"
                badge_style = "worth_exploring"
            else:
                tier = "Possible fit"
                badge_style = "possible_fit"

            # 5. Generate Natural-Language Explainability
            reasons = []
            trait_names = {
                "R": "hands-on practical problem solving",
                "I": "analytical and research-driven investigation",
                "A": "creative, visual, and expressive design",
                "S": "helping people, mentoring, and collaborative service",
                "E": "strategic leadership, communication, and business impact",
                "C": "structured organization, financial precision, and quality control"
            }


            if matched_dominant_traits:
                traits_str = " and ".join(trait_names.get(t, t) for t in matched_dominant_traits[:2])
                reasons.append(f"Your interest profile reflects strong affinity for {traits_str}.")
            elif career_traits:
                first_trait = trait_names.get(career_traits[0], career_traits[0])
                reasons.append(f"This role aligns with {first_trait}.")

            # Explaining skill connections
            if known_skills:
                reasons.append(f"You already have relevant experience with {', '.join(known_skills[:3])}.")
            elif current_skills:
                reasons.append("Your transferable problem-solving skills provide a strong foundation to build upon.")
            else:
                reasons.append("Your natural working style connects well with this pathway even without prior background.")

            # PSOC classification annotation
            psoc_rec = PSOCService.get_psoc_by_code(psoc_code) if psoc_code else None
            psoc_title = psoc_rec["title"] if psoc_rec else None

            matched_results.append({
                "career_id": career_id,
                "title": career_title,
                "field": career.get("field", "Professional"),
                "category_id": career.get("category_id"),
                "category_name": career.get("category_name"),
                "tagline": career.get("tagline"),
                "alignment_tier": tier,
                "badge_style": badge_style,
                "reasons": reasons,
                "known_skills": known_skills,
                "skills_to_develop": skills_to_develop,
                "psoc_code": psoc_code,
                "psoc_title": psoc_title,
                "soc_code": soc_code,
                "salary_philippines": career.get("salary_data", {}).get("philippines", {}).get("entry_level"),
                "salary_global": career.get("salary_data", {}).get("global_usd", {}).get("entry_level"),
                "composite_metric": composite_metric
            })

        # Sort: "Strong alignment" first, then "Worth exploring", then "Possible fit"
        tier_priority = {"Strong alignment": 3, "Worth exploring": 2, "Possible fit": 1}
        matched_results.sort(
            key=lambda x: (tier_priority.get(x["alignment_tier"], 0), x["composite_metric"]),
            reverse=True
        )

        # Ensure compatibility fields for legacy / test expectations
        for m in matched_results:
            m["why_it_appeared"] = m["reasons"]
            m["what_to_develop"] = m["skills_to_develop"]

        return matched_results

class MatchingEngineWrapper:
    def match_careers(self, profile: Dict[str, Any], careers_catalog: Optional[List[Dict[str, Any]]] = None) -> List[Dict[str, Any]]:
        if careers_catalog is None:
            from services.career_service import career_service
            careers_catalog = career_service.get_careers()
        return CareerMatchingEngine.match_careers(profile, careers_catalog)

matching_engine = MatchingEngineWrapper()

