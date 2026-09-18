"""
Central configuration for TO BE platform.
All brand names, taglines, mentor identifiers, and visual constants are defined here.
"""

# Branding & Identifiers
PROJECT_NAME = "TO BE"
PROJECT_TAGLINE = "Explore what could be next."
PROJECT_SUBTITLE = "TO BE helps you explore what to be, understand why, and discover how."
AI_MENTOR_NAME = "TOBE"

# Core Philosophy: WHAT -> WHY -> HOW
PHILOSOPHY = {
    "what": {
        "title": "WHAT TO BE",
        "tagline": "Explore your possibilities.",
        "description": "Discover careers that connect with your interests, skills, strengths, and goals without feeling pressured into a single predetermined future."
    },
    "why": {
        "title": "WHY TO BE",
        "tagline": "Understand your options.",
        "description": "Understand why specific paths align with you, explore what the work really feels like day-to-day, and compare alternatives side-by-side."
    },
    "how": {
        "title": "HOW TO BE",
        "tagline": "Build your direction.",
        "description": "Turn your chosen direction into a practical, interactive roadmap with curated free and low-cost resources, real projects, and milestone tracking."
    }
}

# Design Palette
THEME = {
    "primary_color": "#2563EB",       # Muted Indigo/Blue
    "primary_light": "#EFF6FF",       # Soft Blue Tint
    "secondary_color": "#0D9488",     # Muted Teal/Blue-Green
    "accent_color": "#4F46E5",        # Deep Indigo
    "bg_light": "#F8FAFC",            # Warm Slate/Off-white
    "bg_card": "#FFFFFF",             # Clean card surface
    "text_main": "#0F172A",           # Deep Slate/Navy Text
    "text_muted": "#64748B",          # Muted slate
    "border_color": "#E2E8F0",        # Subtle border
    "success": "#10B981",             # Emerald
    "warning": "#F59E0B",             # Amber
    "info": "#3B82F6"                 # Sky Blue
}

# Supported Assessment Dimensions (RIASEC)
RIASEC_DIMENSIONS = {
    "R": {"name": "Realistic", "desc": "Practical, hands-on, tools, hardware, physical or tangible systems"},
    "I": {"name": "Investigative", "desc": "Analytical, intellectual, problem-solving, research, logic, data"},
    "A": {"name": "Artistic", "desc": "Creative, intuitive, expressive, visual design, user experience, storytelling"},
    "S": {"name": "Social", "desc": "Helping, teaching, mentoring, collaborating, community, user empathy"},
    "E": {"name": "Enterprising", "desc": "Leadership, decision-making, persuasion, product strategy, business growth"},
    "C": {"name": "Conventional", "desc": "Organized, detail-oriented, systematic, quality assurance, compliance, structured"}
}

# Application Constants
ASSESSMENT_VERSION = "1.0.0"
APP_VERSION = "1.0.0"
DEFAULT_CURRENCY = "PHP"
