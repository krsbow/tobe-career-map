"""
Decoupled Downstream Suggestion Generator for TOBE.
Generates 2 to 3 contextual follow-up chips strictly AFTER the final response
is confirmed. Suggestions never determine routing, replace responses, or restrict user input.
"""

from typing import List, Optional

class SuggestionService:
    def __init__(self):
        pass

    def generate_follow_ups(
        self,
        user_query: str,
        response_text: str,
        active_career: Optional[str] = None
    ) -> List[str]:
        """
        Generate natural next-step exploratory questions based on the topic discussed.
        """
        q = user_query.lower()
        resp = response_text.lower()

        # 1. Design / Drawing topics
        if any(w in q for w in ["design", "draw", "drawing", "sketch", "figma", "ui", "ux"]):
            return [
                "What tools do UI/UX designers actually use daily?",
                "What is the difference between UI and UX?",
                "What should I learn first in Figma?"
            ]

        # 2. Self-Doubt / Imposter Syndrome
        if any(w in q for w in ["smart", "scared", "afraid", "good enough", "doubt", "fail"]):
            return [
                "How many hours a day should I practice?",
                "What should I learn first?",
                "What if I get completely stuck on a problem?"
            ]

        # 3. Schedule / Time constraints
        if any(w in q for w in ["two hours", "2 hours", "schedule", "busy", "time", "school"]):
            return [
                "What beginner projects fit a 2-hour daily schedule?",
                "What should I learn first?",
                "How do I track my learning milestones?"
            ]

        # 4. Uncertainty about career fit
        if any(w in q for w in ["unsure", "not sure", "dont know", "don't know", "lost", "like this"]):
            return [
                "What are other careers that might fit me?",
                "How can I test a career in one weekend?",
                "Can I combine creative and technical work?"
            ]

        # 5. Starting Sequence / "What to learn first"
        if any(w in q for w in ["learn first", "start", "begin", "first step"]):
            return [
                "How long does it usually take to become job-ready?",
                "What kind of projects should I build first?",
                "Do I need a degree to get hired?"
            ]

        # 6. Degree vs Portfolio
        if any(w in q for w in ["degree", "college", "university", "license", "prc"]):
            return [
                "What kind of projects should I put in my portfolio?",
                "What certifications carry weight with employers?",
                "How do I land an entry-level role without experience?"
            ]

        # 7. Switching / Changing mind
        if any(w in q for w in ["change my mind", "switch", "wrong path", "pivot"]):
            return [
                "What related careers use these skills?",
                "How do I know if a career is truly right for me?",
                "Can I combine technical and creative skills?"
            ]

        # General exploratory fallback follow-ups
        return [
            "What should I learn first?",
            "What does a normal workday look like?",
            "How much time should I invest each week?"
        ]

# Singleton instance
suggestion_service = SuggestionService()
