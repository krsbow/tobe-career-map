"""
Career catalog service for TO BE platform.
Handles career search, category filters, related roles, and side-by-side comparison.
"""

from typing import Dict, Any, List, Optional
from services.database import db_service

class CareerService:
    def __init__(self):
        self.db = db_service

    def get_all_categories(self) -> List[Dict[str, Any]]:
        """Return all career categories."""
        return self.db.get_categories()

    def get_careers(self, category_id: Optional[str] = None, search_query: Optional[str] = None) -> List[Dict[str, Any]]:
        """Fetch filtered or searched careers."""
        return self.db.get_careers(category_id=category_id, search_query=search_query)

    def get_career_details(self, career_id: str) -> Optional[Dict[str, Any]]:
        """Fetch complete career information by ID."""
        return self.db.get_career_by_id(career_id)

    def get_related_careers(self, career_id: str) -> List[Dict[str, Any]]:
        """Fetch full objects for related careers."""
        career = self.get_career_details(career_id)
        if not career:
            return []
        related_ids = career.get("related_careers", [])
        related_objects = []
        for r_id in related_ids:
            r_obj = self.get_career_details(r_id)
            if r_obj:
                related_objects.append(r_obj)
        return related_objects

    def build_comparison_matrix(self, career_id_a: str, career_id_b: str) -> Dict[str, Any]:
        """
        Build a side-by-side structured comparison between two careers.
        Does not declare an arbitrary 'winner', but helps users understand distinctions.
        """
        career_a = self.get_career_details(career_id_a)
        career_b = self.get_career_details(career_id_b)

        if not career_a or not career_b:
            return {}

        return {
            "career_a": career_a,
            "career_b": career_b,
            "comparison_points": [
                {
                    "dimension": "What they do",
                    "a": career_a.get("tagline"),
                    "b": career_b.get("tagline")
                },
                {
                    "dimension": "Primary Work Style",
                    "a": career_a.get("work_style"),
                    "b": career_b.get("work_style")
                },
                {
                    "dimension": "Key Responsibilities",
                    "a": career_a.get("responsibilities", [])[:3],
                    "b": career_b.get("responsibilities", [])[:3]
                },
                {
                    "dimension": "Core Skills Required",
                    "a": career_a.get("core_skills", []),
                    "b": career_b.get("core_skills", [])
                },
                {
                    "dimension": "Common Tools",
                    "a": career_a.get("common_tools", []),
                    "b": career_b.get("common_tools", [])
                },
                {
                    "dimension": "Typical Portfolio Projects",
                    "a": [p["title"] for p in career_a.get("portfolio_projects", [])[:2]],
                    "b": [p["title"] for p in career_b.get("portfolio_projects", [])[:2]]
                },
                {
                    "dimension": "Salary Benchmark (Philippines)",
                    "a": career_a.get("salary_data", {}).get("philippines", {}).get("mid_level", "Competitive"),
                    "b": career_b.get("salary_data", {}).get("philippines", {}).get("mid_level", "Competitive")
                },
                {
                    "dimension": "Salary Benchmark (Global USD)",
                    "a": career_a.get("salary_data", {}).get("global_usd", {}).get("mid_level", "Competitive"),
                    "b": career_b.get("salary_data", {}).get("global_usd", {}).get("mid_level", "Competitive")
                }
            ]
        }

# Singleton instance
career_service = CareerService()
