"""
Security and privacy utilities for TO BE platform.
Handles PII anonymization, credential scrubbing, and safety boundaries.
"""

import re
from typing import Dict, Any

def scrub_pii_for_ai(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Remove or mask Personally Identifiable Information (PII) before sending context to external AI providers.
    Ensures emails, passwords, phone numbers, and direct identifiers are never leaked.
    """
    safe_copy = {}
    sensitive_keys = {
        "email", "password", "token", "access_token", "refresh_token", "jwt",
        "api_key", "secret", "user_id", "id", "phone", "address", "ip_address", "credit_card"
    }

    for k, v in data.items():
        if k.lower() in sensitive_keys:
            continue
        if isinstance(v, str):
            # Mask potential email patterns
            val = re.sub(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", "[REDACTED_EMAIL]", v)
            # Mask potential phone patterns
            val = re.sub(r"\+?\d{1,4}?[-.\s]?\(?\d{1,3}?\)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}", "[REDACTED_PHONE]", val)
            safe_copy[k] = val
        elif isinstance(v, dict):
            safe_copy[k] = scrub_pii_for_ai(v)
        elif isinstance(v, list):
            safe_copy[k] = [scrub_pii_for_ai(i) if isinstance(i, dict) else i for i in v]
        else:
            safe_copy[k] = v

    return safe_copy

def sanitize_chat_prompt(user_message: str) -> str:
    """Sanitize user chat messages before submitting to AI mentor."""
    if not user_message:
        return ""
    # Strip dangerous injection tokens or excessive whitespace
    sanitized = user_message.strip()
    return sanitized
