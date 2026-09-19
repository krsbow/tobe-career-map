"""
Response Quality Evaluator for TOBE AI Career Mentor.
Validates whether generated responses directly answer the user query, maintain relevance,
avoid generic canned templates, and adhere strictly to formatting standards (no ** bold).
Triggers targeted regeneration if quality checks fail.
"""

import re
import logging
from typing import Dict, Any, Optional

logger = logging.getLogger(__name__)

# Disallowed canned boilerplate phrases
BANNED_TEMPLATE_PHRASES = [
    "that is a thoughtful question",
    "when exploring this direction",
    "as you shape your pathway",
    "the most practical approach is to focus on hands-on fundamentals",
    "gives you the clearest picture of what the work actually feels like",
    "what specific skill, tool, or goal would you like to explore next"
]

class ResponseEvaluator:
    def __init__(self):
        pass

    def evaluate_response(
        self,
        user_query: str,
        generated_response: str,
        career_context: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Evaluate generated output against mentor quality standards.
        Returns structured evaluation verdict.
        """
        q = user_query.lower().strip()
        resp = generated_response.lower().strip()

        # Check 1: Empty or extremely short response
        if len(resp) < 20:
            return {
                "answers_question": False,
                "relevant": False,
                "uses_context_correctly": False,
                "too_generic": True,
                "needs_clarification": False,
                "reason": "Response is too short or empty."
            }

        # Check 2: Check for forbidden markdown bold syntax (**)
        if "**" in generated_response:
            return {
                "answers_question": True,
                "relevant": True,
                "uses_context_correctly": True,
                "too_generic": False,
                "needs_clarification": False,
                "formatting_violation": True,
                "reason": "Contains forbidden markdown bold syntax (**)."
            }

        # Check 3: Check for canned/boilerplate filler
        for banned in BANNED_TEMPLATE_PHRASES:
            if banned in resp:
                return {
                    "answers_question": False,
                    "relevant": False,
                    "uses_context_correctly": False,
                    "too_generic": True,
                    "needs_clarification": False,
                    "reason": f"Response used canned template phrase: '{banned}'."
                }

        # Check 4: Specific intent responsiveness heuristics
        # Design/drawing
        if any(w in q for w in ["drawing", "draw", "sketch"]) and not any(w in resp for w in ["draw", "sketch", "figma", "art", "illustration"]):
            return {
                "answers_question": False,
                "relevant": False,
                "uses_context_correctly": False,
                "too_generic": True,
                "needs_clarification": False,
                "reason": "Failed to address drawing/sketching query directly."
            }

        # Hours / time constraint
        if any(w in q for w in ["two hours", "2 hours", "how many hours", "hours a day"]) and not any(w in resp for w in ["hour", "minute", "schedule", "daily", "time", "practice"]):
            return {
                "answers_question": False,
                "relevant": False,
                "uses_context_correctly": False,
                "too_generic": True,
                "needs_clarification": False,
                "reason": "Failed to address time/hours constraint directly."
            }

        # Degree / College
        if any(w in q for w in ["degree", "college", "university", "diploma"]) and not any(w in resp for w in ["degree", "portfolio", "prc", "college", "hiring", "proof"]):
            return {
                "answers_question": False,
                "relevant": False,
                "uses_context_correctly": False,
                "too_generic": True,
                "needs_clarification": False,
                "reason": "Failed to address degree requirement directly."
            }

        # Self doubt / smart enough
        if any(w in q for w in ["smart enough", "not smart", "scared", "fear", "good enough"]) and not any(w in resp for w in ["doubt", "fear", "normal", "practice", "patience", "beginner", "intellect", "genius"]):
            return {
                "answers_question": False,
                "relevant": False,
                "uses_context_correctly": False,
                "too_generic": True,
                "needs_clarification": False,
                "reason": "Failed to address user self-doubt/emotional concern directly."
            }

        # Passed all quality checks
        return {
            "answers_question": True,
            "relevant": True,
            "uses_context_correctly": True,
            "too_generic": False,
            "needs_clarification": False,
            "reason": "The response directly answers the user's question with grounded, relevant guidance."
        }

    def build_corrective_instruction(self, user_query: str, eval_result: Dict[str, Any]) -> str:
        """Construct targeted corrective prompt when initial generation fails evaluation."""
        reason = eval_result.get("reason", "Response was too generic.")
        return f"""The previous response failed quality evaluation because: {reason}.
Please provide a direct, specific, and empathetic answer to the user's exact message: "{user_query}".
- Answer the user's specific question in the very first sentence.
- Do NOT use generic opening phrases or career overview brochures.
- DO NOT use markdown bold (no ** syntax).
"""

# Singleton instance
response_evaluator = ResponseEvaluator()
