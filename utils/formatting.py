"""
Formatting utilities for the TO BE platform.
"""

from typing import Dict, Any, Optional
import datetime

def format_currency(amount: Optional[float], currency: str = "PHP") -> str:
    """Format numeric values into standard currency strings."""
    if amount is None:
        return "N/A"
    if currency.upper() == "PHP":
        return f"PHP {amount:,.2f}"
    elif currency.upper() == "USD":
        return f"${amount:,.2f}"
    return f"{currency} {amount:,.2f}"

def format_percentage(value: float, decimal_places: int = 0) -> str:
    """Format float (0-100) into a percentage string."""
    val = max(0.0, min(100.0, value))
    if decimal_places == 0:
        return f"{int(round(val))}%"
    return f"{val:.{decimal_places}f}%"

def format_date_human(date_str_or_dt: Any) -> str:
    """Format an ISO date string or datetime into a clean human-readable date."""
    if not date_str_or_dt:
        return "N/A"
    try:
        if isinstance(date_str_or_dt, str):
            cleaned = date_str_or_dt.replace("Z", "+00:00")
            dt = datetime.datetime.fromisoformat(cleaned)
        elif isinstance(date_str_or_dt, (datetime.datetime, datetime.date)):
            dt = date_str_or_dt
        else:
            return str(date_str_or_dt)
        return dt.strftime("%B %d, %Y")
    except Exception:
        return str(date_str_or_dt)[:10]

def get_status_badge(status: str) -> Dict[str, str]:
    """Return styling badge info for roadmap item statuses."""
    status_map = {
        "not_started": {"label": "Not Started", "color": "#94A3B8", "bg": "#F1F5F9"},
        "in_progress": {"label": "In Progress", "color": "#2563EB", "bg": "#EFF6FF"},
        "completed": {"label": "Completed", "color": "#10B981", "bg": "#ECFDF5"}
    }
    return status_map.get(status.lower(), {"label": status.capitalize(), "color": "#64748B", "bg": "#F8FAFC"})
