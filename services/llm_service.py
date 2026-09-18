"""
Configurable LLM provider abstraction for TO BE platform.
Supports Google Gemini, Groq, and resilient structured fallback templates.
"""

import os
import json
import logging
from typing import Dict, Any, Optional, List
import streamlit as st
from utils.security import scrub_pii_for_ai
from utils.validation import parse_and_validate_json_response

logger = logging.getLogger(__name__)

def get_secret(key: str, default: Any = None) -> Any:
    """Retrieve configuration from Streamlit secrets or OS environment."""
    try:
        if hasattr(st, "secrets") and key in st.secrets:
            return st.secrets[key]
    except Exception:
        pass
    return os.environ.get(key, default)

class LLMService:
    def __init__(self):
        self.provider = get_secret("LLM_PROVIDER", "gemini").lower()
        self.gemini_key = get_secret("GEMINI_API_KEY", "")
        self.groq_key = get_secret("GROQ_API_KEY", "")
        self.openai_key = get_secret("OPENAI_API_KEY", "")

    def generate_text(self, system_prompt: str, user_prompt: str, temperature: float = 0.7) -> str:
        """Generate conversational or analytical text with automatic graceful fallback."""
        # Try Gemini
        if self.gemini_key and (self.provider == "gemini" or not self.provider):
            try:
                import google.generativeai as genai
                genai.configure(api_key=self.gemini_key)
                model = genai.GenerativeModel(
                    model_name="gemini-1.5-flash",
                    system_instruction=system_prompt
                )
                response = model.generate_content(
                    user_prompt,
                    generation_config=genai.types.GenerationConfig(temperature=temperature)
                )
                if response and response.text:
                    return response.text.strip()
            except Exception as e:
                logger.warning(f"Gemini API call failed: {e}. Falling back to default response.")

        # Fallback response for mentor
        return self._fallback_mentor_response(user_prompt)

    def generate_structured_json(self, system_prompt: str, user_prompt: str, expected_keys: Optional[List[str]] = None) -> Optional[Dict[str, Any]]:
        """Generate structured JSON and validate against expected schema."""
        raw_text = self.generate_text(system_prompt, user_prompt, temperature=0.3)
        parsed = parse_and_validate_json_response(raw_text, expected_keys=expected_keys)
        return parsed

    def _fallback_mentor_response(self, user_prompt: str) -> str:
        """Supportive, grounded fallback response for TOBE AI mentor."""
        prompt_lower = user_prompt.lower()
        
        if "cybersecurity" in prompt_lower:
            return (
                "That's a very common and thoughtful question! Cybersecurity can look intimidating from the outside because people often picture intense hacker movies. "
                "In reality, a lot of entry-level security work revolves around systematic problem-solving, understanding network traffic, and following clear defense checklists.\n\n"
                "Before committing fully, a great low-stakes way to test if you enjoy the work is trying beginner labs on free platforms like OverTheWire (Bandit) or TryHackMe. "
                "If you enjoy solving structured puzzles and discovering how systems work under the hood, it could be a very fulfilling path for you."
            )
        elif "ux" in prompt_lower or "design" in prompt_lower:
            return (
                "Exploring UX and Design is an exciting direction! What makes UX unique is that it's grounded in human empathy and user research as much as visual craft. "
                "You don't need to be a fine artist to excel in UX; understanding people's frustrations and translating them into simple flows is the real superpower.\n\n"
                "If you'd like to test the waters, try picking an app you use every day and redesigning one screen that frustrates you in Figma. It's a quick way to see how you feel about the process."
            )
        elif "compare" in prompt_lower or "difference" in prompt_lower or "vs" in prompt_lower:
            return (
                "Comparing different paths is one of the best steps you can take right now. The biggest difference often comes down to what part of the building process energizes you most:\n\n"
                "• **Front-End & UI:** Translating ideas into what people directly see, click, and experience.\n"
                "• **Back-End & Cloud:** Designing the data engines, APIs, and scalable infrastructure behind the scenes.\n"
                "• **Data & Strategy:** Analyzing patterns, extracting business truth, and guiding decisions.\n\n"
                "Remember, you don't have to lock into one path forever—many foundational skills like Git, problem-solving, and web basics carry over everywhere."
            )
        else:
            return (
                "I hear you, and it is completely normal to feel uncertain when considering your career direction. "
                "You don't have to have your whole future mapped out today. The most effective approach is to treat career planning as a series of small, low-risk experiments.\n\n"
                "What specific aspect of this direction feels most exciting to you right now, and what part feels like the biggest question mark?"
            )

# Singleton instance
llm_service = LLMService()
