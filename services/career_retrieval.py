"""
Career Knowledge Retrieval (RAG) Service for TOBE AI Career Mentor.
Retrieves targeted, query-specific career facts (responsibilities, skills, tools,
math/drawing relevance, degree/licensure requirements, salary benchmarks)
without overloading prompts with full database dumps.
"""

from typing import Dict, Any, List, Optional
from services.career_service import career_service
from services.psoc_service import PSOCService
from services.training_service import TrainingService

class CareerRetrievalService:
    def __init__(self):
        self.career_svc = career_service
        self.training_svc = TrainingService()

    def retrieve_relevant_facts(self, query: str, career_id_or_title: Optional[str] = None) -> List[str]:
        """
        Extract only the relevant facts from the career database and taxonomies
        matching the specific user inquiry.
        """
        if not career_id_or_title:
            return []

        q = query.lower()
        facts: List[str] = []

        # Resolve career details
        career = None
        # Try ID lookup first
        career = self.career_svc.get_career_details(career_id_or_title.lower().replace(" ", "-"))
        if not career:
            # Search by title in catalog
            all_careers = self.career_svc.get_careers()
            for c in all_careers:
                if c.get("title", "").lower() == career_id_or_title.lower() or c.get("id") == career_id_or_title.lower():
                    career = c
                    break

        if not career:
            return []

        title = career.get("title", "Selected Career")

        # 1. Design & Drawing inquiries
        if any(w in q for w in ["draw", "drawing", "art", "sketch", "design", "good at design"]):
            if "design" in title.lower() or "ux" in title.lower():
                facts.append(f"{title} focuses on digital layout hierarchy, component structure, usability heuristics, and user flows in Figma; fine-art drawing or freehand sketching is not required.")
            elif "developer" in title.lower() or "engineer" in title.lower() or "analyst" in title.lower():
                facts.append(f"{title} emphasizes problem solving, logic, and implementation; artistic drawing is completely unrelated.")

        # 2. Math & Intelligence inquiries
        if any(w in q for w in ["math", "calculus", "smart", "genius", "intelligence", "bad at math"]):
            if "developer" in title.lower() or "software" in title.lower() or "web" in title.lower():
                facts.append(f"Standard software development relies on basic logic, arithmetic, and problem decomposition; calculus or advanced higher math is rarely needed for general web/app development.")
            elif "civil" in title.lower() or "structural" in title.lower():
                facts.append(f"{title} uses applied algebra, geometry, and structural mechanics, supported heavily by specialized calculation and CAD software.")
            elif "data" in title.lower() or "analyst" in title.lower():
                facts.append(f"Junior {title} roles focus on descriptive statistics, SQL querying, and clear arithmetic rather than pure mathematical theory.")

        # 3. Education, Degree & Philippine Licensure (PRC)
        if any(w in q for w in ["degree", "college", "university", "license", "board exam", "prc", "certification"]):
            psoc_code = career.get("psoc_code", "")
            psoc_info = PSOCService.get_psoc_by_code(psoc_code) if psoc_code else None
            
            if any(w in title.lower() for w in ["nurse", "civil engineer", "accountant", "cpa", "doctor", "lawyer"]):
                facts.append(f"{title} is a legally regulated profession in the Philippines requiring a CHED-accredited bachelor's degree and passing the official PRC Board Examination.")
            else:
                facts.append(f"In {title}, proof of practical capability (real portfolio projects, GitHub code repositories, and problem-solving ability) is the primary hiring signal; a formal degree is rarely a strict blocker.")

        # 4. Starting Out / Learning Sequence
        if any(w in q for w in ["learn first", "start", "begin", "first step", "roadmap", "tools"]):
            tools = career.get("tools", [])
            skills = career.get("required_skills", [])
            if tools:
                facts.append(f"Core industry tools for {title}: {', '.join(tools[:4])}.")
            if skills:
                facts.append(f"Essential foundation skills for {title}: {', '.join(skills[:4])}.")

        # 5. Salary Benchmarks
        if any(w in q for w in ["salary", "pay", "earn", "income", "compensation", "rate"]):
            entry_sal = career.get("salary_entry_ph", "₱25,000 – ₱45,000/mo")
            facts.append(f"Philippine entry-level compensation benchmark for {title}: {entry_sal}.")

        # 6. Daily Routine & Work Environment
        if any(w in q for w in ["workday", "day look like", "routine", "daily", "life like", "hours"]):
            work_style = career.get("work_style", "Collaborative problem-solving and focused execution")
            facts.append(f"Work style and day-to-day focus for {title}: {work_style}.")

        return facts

# Singleton instance
career_retrieval_service = CareerRetrievalService()
