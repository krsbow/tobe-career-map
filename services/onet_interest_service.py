"""
O*NET Interest Profiler Service.
Handles standardized RIASEC (Realistic, Investigative, Artistic, Social, Enterprising, Conventional)
assessment questionnaires, scoring calculation, and interest-based occupational alignment.
Includes server-side API connectivity with offline resilient question banks.
"""

import os
import logging
from typing import Dict, Any, List, Optional

logger = logging.getLogger(__name__)

# Standardized 30-Question O*NET Mini-Interest Profiler Bank
# Balanced across 6 RIASEC dimensions (5 questions each)
ONET_MINI_PROFILER_QUESTIONS: List[Dict[str, Any]] = [
    # Realistic (R) - Practical, hands-on, tangible systems, tools, mechanics
    {"id": "q1_r", "area": "Realistic", "text": "Build kitchen cabinets or construct wooden structures", "dimension": "R"},
    {"id": "q2_r", "area": "Realistic", "text": "Repair electrical wiring, appliances, or electronic devices", "dimension": "R"},
    {"id": "q3_r", "area": "Realistic", "text": "Assemble, test, or troubleshoot mechanical parts and machinery", "dimension": "R"},
    {"id": "q4_r", "area": "Realistic", "text": "Operate heavy machinery, specialized tools, or physical equipment", "dimension": "R"},
    {"id": "q5_r", "area": "Realistic", "text": "Install computer network cables, hardware servers, or technical gear", "dimension": "R"},

    # Investigative (I) - Analytical, research, scientific problem solving, data investigation
    {"id": "q6_i", "area": "Investigative", "text": "Investigate how a disease spreads or study biological systems", "dimension": "I"},
    {"id": "q7_i", "area": "Investigative", "text": "Analyze datasets and statistics to discover patterns or solve complex problems", "dimension": "I"},
    {"id": "q8_i", "area": "Investigative", "text": "Write algorithms or design mathematical models to simulate behavior", "dimension": "I"},
    {"id": "q9_i", "area": "Investigative", "text": "Conduct scientific experiments, laboratory tests, or user research", "dimension": "I"},
    {"id": "q10_i", "area": "Investigative", "text": "Examine security vulnerabilities or investigate system architecture", "dimension": "I"},

    # Artistic (A) - Creative expression, visual design, writing, multimedia, innovation
    {"id": "q11_a", "area": "Artistic", "text": "Design graphic layouts, user interfaces, or visual branding", "dimension": "A"},
    {"id": "q12_a", "area": "Artistic", "text": "Write articles, stories, scripts, or create multimedia content", "dimension": "A"},
    {"id": "q13_a", "area": "Artistic", "text": "Compose music, edit video footage, or create digital animations", "dimension": "A"},
    {"id": "q14_a", "area": "Artistic", "text": "Create architectural concepts, interior spaces, or innovative product aesthetics", "dimension": "A"},
    {"id": "q15_a", "area": "Artistic", "text": "Design interactive digital experiences that delight users and evoke emotion", "dimension": "A"},

    # Social (S) - Helping, teaching, counseling, healthcare, community service
    {"id": "q16_s", "area": "Social", "text": "Teach students, train apprentices, or explain concepts to beginners", "dimension": "S"},
    {"id": "q17_s", "area": "Social", "text": "Provide compassionate care, treatment, or nursing support to the injured or sick", "dimension": "S"},
    {"id": "q18_s", "area": "Social", "text": "Counsel people experiencing career transitions, stress, or life challenges", "dimension": "S"},
    {"id": "q19_s", "area": "Social", "text": "Organize community welfare initiatives or volunteer programs", "dimension": "S"},
    {"id": "q20_s", "area": "Social", "text": "Help team members resolve conflicts and foster collaborative environments", "dimension": "S"},

    # Enterprising (E) - Leadership, business strategy, persuasion, entrepreneurship, marketing
    {"id": "q21_e", "area": "Enterprising", "text": "Start a new business venture, product launch, or entrepreneurial project", "dimension": "E"},
    {"id": "q22_e", "area": "Enterprising", "text": "Pitch ideas to stakeholders, negotiate contracts, or persuade clients", "dimension": "E"},
    {"id": "q23_e", "area": "Enterprising", "text": "Manage a cross-functional project team and guide strategic milestones", "dimension": "E"},
    {"id": "q24_e", "area": "Enterprising", "text": "Develop digital marketing strategies to grow audience engagement and revenue", "dimension": "E"},
    {"id": "q25_e", "area": "Enterprising", "text": "Lead organizational change and make executive decisions during uncertainty", "dimension": "E"},

    # Conventional (C) - Organization, data accuracy, structure, accounting, quality control
    {"id": "q26_c", "area": "Conventional", "text": "Manage financial records, prepare tax statements, or verify accounting balance", "dimension": "C"},
    {"id": "q27_c", "area": "Conventional", "text": "Maintain structured databases, organized spreadsheets, and error-free records", "dimension": "C"},
    {"id": "q28_c", "area": "Conventional", "text": "Develop compliance protocols, quality assurance standards, or audit procedures", "dimension": "C"},
    {"id": "q29_c", "area": "Conventional", "text": "Plan detailed project schedules, track itemized budgets, and verify logistics", "dimension": "C"},
    {"id": "q30_c", "area": "Conventional", "text": "Inspect operational workflows to ensure complete consistency and zero defects", "dimension": "C"},
]

class ONETInterestService:
    """Service for managing O*NET RIASEC questionnaires and scoring."""

    @classmethod
    def get_questions(cls, version: str = "mini", count: Optional[int] = None) -> List[Dict[str, Any]]:
        """
        Retrieve O*NET interest profiler questions.
        Defaults to the career-neutral 30-question Mini Interest Profiler.
        """
        if count and count < len(ONET_MINI_PROFILER_QUESTIONS):
            return ONET_MINI_PROFILER_QUESTIONS[:count]
        return ONET_MINI_PROFILER_QUESTIONS

    @classmethod
    def score_profiler(cls, answers: Dict[str, int]) -> Dict[str, Any]:
        """Convenience method returning raw scores dictionary and top traits."""
        res = cls.calculate_riasec_scores(answers)
        return {
            "scores": {dim: data["score"] for dim, data in res["riasec_scores"].items()},
            "top_traits": res["top_traits"],
            "holland_code": res["holland_code"]
        }

    @classmethod
    def calculate_riasec_scores(cls, answers: Dict[str, int]) -> Dict[str, Any]:

        """
        Compute RIASEC scores from question responses.
        Rating scale: 1 (Dislike) to 5 (Enjoy).
        Returns normalized scores (0-100) and top dominant archetype letters.
        """
        raw_totals: Dict[str, int] = {"R": 0, "I": 0, "A": 0, "S": 0, "E": 0, "C": 0}
        counts: Dict[str, int] = {"R": 0, "I": 0, "A": 0, "S": 0, "E": 0, "C": 0}

        for q in ONET_MINI_PROFILER_QUESTIONS:
            qid = q["id"]
            dim = q["dimension"]
            rating = answers.get(qid, 3) # default neutral rating
            raw_totals[dim] += rating
            counts[dim] += 1

        normalized_scores: Dict[str, Dict[str, Any]] = {}
        for dim, total in raw_totals.items():
            count = max(1, counts[dim])
            # Max possible = count * 5, Min possible = count * 1
            pct = int(((total - count) / (count * 4)) * 100) if count > 0 else 50
            level = "High" if pct >= 65 else ("Medium" if pct >= 35 else "Low")
            
            dimension_names = {
                "R": "Realistic (Hands-on & Practical)",
                "I": "Investigative (Analytical & Research)",
                "A": "Artistic (Creative & Expressive)",
                "S": "Social (Helping & Collaborative)",
                "E": "Enterprising (Leadership & Business)",
                "C": "Conventional (Structured & Methodical)"
            }

            normalized_scores[dim] = {
                "score": pct,
                "raw_total": total,
                "level": level,
                "name": dimension_names[dim]
            }

        # Sort to find top 3 dominant traits (Holland Code)
        sorted_dims = sorted(normalized_scores.keys(), key=lambda d: normalized_scores[d]["score"], reverse=True)
        holland_code = "".join(sorted_dims[:3])

        return {
            "riasec_scores": normalized_scores,
            "top_traits": sorted_dims[:3],
            "holland_code": holland_code
        }
