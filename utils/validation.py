"""
Validation utilities for inputs, LLM responses, and data models.
"""

import json
import re
from typing import Dict, Any, Optional, List, Tuple

def validate_email(email: str) -> bool:
    """Validate email format."""
    if not email:
        return False
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(pattern, email.strip()))

def validate_password_strength(password: str) -> Tuple[bool, str]:
    """Check password length and complexity."""
    if not password or len(password) < 6:
        return False, "Password must be at least 6 characters long."
    return True, ""

def sanitize_user_input(text: str, max_length: int = 2000) -> str:
    """Sanitize and trim generic text input."""
    if not text:
        return ""
    cleaned = text.strip()
    return cleaned[:max_length]

def parse_and_validate_json_response(raw_text: str, expected_keys: Optional[List[str]] = None) -> Optional[Dict[str, Any]]:
    """
    Safely extract and parse JSON from an LLM response string.
    Extracts code block fences ```json ... ``` or standard JSON object {...}.
    """
    if not raw_text:
        return None

    cleaned = raw_text.strip()

    # Extract markdown code fence if present
    if "```json" in cleaned:
        parts = cleaned.split("```json")
        if len(parts) > 1:
            cleaned = parts[1].split("```")[0].strip()
    elif "```" in cleaned:
        parts = cleaned.split("```")
        if len(parts) > 1:
            cleaned = parts[1].split("```")[0].strip()

    # Locate first '{' and last '}'
    start_idx = cleaned.find("{")
    end_idx = cleaned.rfind("}")
    if start_idx != -1 and end_idx != -1 and end_idx > start_idx:
        cleaned = cleaned[start_idx:end_idx + 1]

    try:
        data = json.loads(cleaned)
        if not isinstance(data, dict):
            return None
        if expected_keys:
            for k in expected_keys:
                if k not in data:
                    return None
        return data
    except Exception:
        return None
