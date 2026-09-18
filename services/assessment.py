"""
Assessment scoring and Career Profile computation service for TO BE.
Implements multi-dimensional RIASEC calculation, strengths synthesis, and preference aggregation.
"""

from typing import Dict, Any, List, Tuple
from config import RIASEC_DIMENSIONS
from data.assessment_questions import ASSESSMENT_QUESTIONS

class AssessmentService:
    @staticmethod
    def get_questions() -> List[Dict[str, Any]]:
        """Return the assessment question bank."""
        return ASSESSMENT_QUESTIONS

    @staticmethod
    def calculate_results(responses: List[Dict[str, Any]], selected_skills: List[str]) -> Dict[str, Any]:
        """
        Compute RIASEC scores, strengths, work preferences, and career priorities from user responses.
        """
        # 1. Initialize RIASEC raw scores
        riasec_raw = {"R": 0, "I": 0, "A": 0, "S": 0, "E": 0, "C": 0}
        work_preferences = []
        career_priorities = []
        desired_impact = []

        question_map = {q["id"]: q for q in ASSESSMENT_QUESTIONS}

        for resp in responses:
            q_id = resp.get("question_id")
            selected_option_ids = resp.get("response_data", [])
            if not isinstance(selected_option_ids, list):
                selected_option_ids = [selected_option_ids]

            q_def = question_map.get(q_id)
            if not q_def:
                continue

            # Process option scores
            for opt in q_def.get("options", []):
                if opt.get("id") in selected_option_ids:
                    # Accumulate RIASEC scores
                    for dim, pts in opt.get("scores", {}).items():
                        if dim in riasec_raw:
                            riasec_raw[dim] += pts

                    # Collect preference tags
                    if "preference" in opt:
                        work_preferences.append(opt["preference"])
                    if "impact" in opt:
                        desired_impact.append(opt["impact"])
                    if q_def.get("category") == "priorities":
                        career_priorities.append(opt.get("text"))

        # 2. Normalize RIASEC scores to percentages (0 - 100) and Level (High, Medium, Low)
        max_possible_points = 8.0 # typical max per dimension with current questions
        riasec_profile = {}
        for dim, raw in riasec_raw.items():
            pct = min(100, int((raw / max_possible_points) * 100))
            # Level categorization
            if pct >= 60:
                level = "High"
            elif pct >= 30:
                level = "Medium"
            else:
                level = "Low"
            
            dim_info = RIASEC_DIMENSIONS.get(dim, {})
            riasec_profile[dim] = {
                "name": dim_info.get("name", dim),
                "description": dim_info.get("desc", ""),
                "score": pct,
                "level": level,
                "raw": raw
            }

        # 3. Derive Core Strengths based on top RIASEC dimensions & skills
        sorted_dims = sorted(riasec_profile.items(), key=lambda x: x[1]["score"], reverse=True)
        strengths = []
        top_codes = [d[0] for d in sorted_dims[:3] if d[1]["score"] > 20]

        if "A" in top_codes:
            strengths.append("Visual thinking, design empathy, and creative problem solving")
        if "I" in top_codes:
            strengths.append("Logical investigation, analytical reasoning, and data curiosity")
        if "R" in top_codes:
            strengths.append("Hands-on architecture, technical foundations, and tooling")
        if "S" in top_codes:
            strengths.append("User empathy, communication, and cross-functional teamwork")
        if "E" in top_codes:
            strengths.append("Strategic prioritization, product vision, and decisive leadership")
        if "C" in top_codes:
            strengths.append("Methodical quality assurance, precision, and systems organization")

        if not strengths:
            strengths = ["Curious learner", "Adaptable problem solver", "Technology enthusiast"]

        return {
            "riasec_scores": riasec_profile,
            "top_dimensions": [d[0] for d in sorted_dims[:3]],
            "strengths": strengths,
            "work_preferences": work_preferences or ["Collaborative & Flexible"],
            "career_priorities": career_priorities or ["Continuous Learning", "Creativity"],
            "desired_impact": desired_impact or ["Meaningful Human-Centered Utility"],
            "current_skills": selected_skills
        }

# Singleton instance
assessment_service = AssessmentService()
