"""
Conversation state and multi-turn context resolution service for TOBE.
Manages windowed conversation history, formats dialog turns, and
resolves multi-turn references (e.g. 'it', 'that', 'this career', 'first step').
"""

from typing import List, Dict, Any, Optional

class ConversationManager:
    def __init__(self, max_history_turns: int = 6):
        self.max_history_turns = max_history_turns

    def prune_history(self, history: List[Dict[str, str]]) -> List[Dict[str, str]]:
        """Return clean, windowed recent turns to prevent context blowup."""
        if not history:
            return []
        return history[-self.max_history_turns:]

    def format_history_for_prompt(self, history: List[Dict[str, str]], mentor_name: str = "TOBE") -> str:
        """Format history turns into a readable dialog context string."""
        if not history:
            return ""
        
        pruned = self.prune_history(history)
        lines = []
        for turn in pruned:
            role = "User" if turn.get("role") == "user" else mentor_name
            content = turn.get("content", "").strip()
            if content:
                lines.append(f"{role}: {content}")
        return "\n".join(lines)

    def resolve_subject_from_history(self, current_query: str, history: List[Dict[str, str]]) -> Optional[str]:
        """
        Infer the subject/career topic if the user asks a follow-up with pronouns or ellipsis
        (e.g., 'is it hard?', 'what should I learn first?', 'would I need a degree?').
        """
        q = current_query.lower()
        
        # Check current query first
        if any(w in q for w in ["program", "code", "developer", "software", "web dev", "frontend", "backend"]):
            return "Software Developer"
        if any(w in q for w in ["design", "ux", "ui", "figma", "product design"]):
            return "UI/UX Designer"
        if any(w in q for w in ["data", "sql", "analyst", "analytics"]):
            return "Data Analyst"
        if any(w in q for w in ["nurse", "nursing", "health", "hospital", "patient"]):
            return "Registered Nurse"
        if any(w in q for w in ["civil", "construction", "autocad", "structural"]):
            return "Civil Engineer"
        if any(w in q for w in ["electrician", "electrical", "wiring"]):
            return "Commercial Electrician"
        if any(w in q for w in ["accountant", "cpa", "audit", "tax", "accounting"]):
            return "CPA Accountant"
        if any(w in q for w in ["marketing", "seo", "social media", "content"]):
            return "Digital Marketing Specialist"

        # If current query is ambiguous, scan recent history backwards
        for turn in reversed(history[-6:]):
            text = turn.get("content", "").lower()
            if any(w in text for w in ["program", "code", "developer", "software"]):
                return "Software Developer"
            if any(w in text for w in ["design", "ux", "ui", "figma"]):
                return "UI/UX Designer"
            if any(w in text for w in ["data", "analyst", "sql"]):
                return "Data Analyst"
            if any(w in text for w in ["nurse", "nursing"]):
                return "Registered Nurse"
            if any(w in text for w in ["civil", "engineer", "construction"]):
                return "Civil Engineer"
            if any(w in text for w in ["electrician"]):
                return "Commercial Electrician"
            if any(w in text for w in ["accountant", "cpa"]):
                return "CPA Accountant"
            if any(w in text for w in ["marketing"]):
                return "Digital Marketing Specialist"

        return None

# Singleton instance
conversation_manager = ConversationManager()
