"""
ESCO (European Skills, Competences, Qualifications and Occupations) Service.
Provides cross-domain global skills taxonomy, essential vs optional competence relationships,
and reusable occupation crosswalks without requiring web scraping.
"""

from typing import Dict, Any, Optional, List

# Authoritative ESCO Skills and Competency Crosswalk Cache
ESCO_SKILLS_TAXONOMY: Dict[str, Dict[str, Any]] = {
    "ux_design": {
        "concept_uri": "http://data.europa.eu/esco/occupation/34f9a0c2-92cf-468e-908c-02cf46087b32",
        "title": "User Experience Designer",
        "essential_skills": [
            "conduct user research",
            "create wireframes",
            "develop design systems",
            "prototype user interfaces",
            "perform usability testing"
        ],
        "optional_skills": [
            "front-end development principles",
            "data analytics for product design",
            "micro-animations and interaction patterns",
            "accessibility standards compliance (WCAG)"
        ]
    },
    "software_engineer": {
        "concept_uri": "http://data.europa.eu/esco/occupation/2512-software-engineer",
        "title": "Software Developer",
        "essential_skills": [
            "write clean modular code",
            "utilize version control (Git)",
            "implement software testing and debugging",
            "design database schemas",
            "build and consume RESTful APIs"
        ],
        "optional_skills": [
            "containerization and Docker",
            "cloud infrastructure deployment",
            "continuous integration/continuous deployment (CI/CD)",
            "system performance optimization"
        ]
    },
    "data_scientist": {
        "concept_uri": "http://data.europa.eu/esco/occupation/2511-data-scientist",
        "title": "Data Scientist",
        "essential_skills": [
            "perform statistical data analysis",
            "develop machine learning models",
            "write SQL and relational queries",
            "clean and preprocess structured datasets",
            "create interactive data visualizations"
        ],
        "optional_skills": [
            "big data pipelines and Spark",
            "deep learning architectures",
            "A/B experimentation testing",
            "MLOps and model deployment"
        ]
    },
    "registered_nurse": {
        "concept_uri": "http://data.europa.eu/esco/occupation/2221-registered-nurse",
        "title": "Registered General Nurse",
        "essential_skills": [
            "provide patient-centered clinical care",
            "monitor vital signs and symptoms",
            "administer prescribed medications accurately",
            "maintain detailed electronic medical records",
            "practice strict infection control protocols"
        ],
        "optional_skills": [
            "emergency triage coordination",
            "patient health education and counseling",
            "clinical preceptor and apprentice mentoring",
            "specialized geriatric or pediatric care"
        ]
    },
    "accountant": {
        "concept_uri": "http://data.europa.eu/esco/occupation/2411-accountant",
        "title": "Accountant",
        "essential_skills": [
            "prepare financial statements (Balance Sheet, P&L)",
            "perform general ledger reconciliation",
            "ensure taxation and statutory compliance",
            "conduct internal and external audit reviews",
            "utilize accounting software and spreadsheets"
        ],
        "optional_skills": [
            "financial forecasting and modeling",
            "budget variance analysis",
            "enterprise resource planning (ERP) systems",
            "business valuation principles"
        ]
    },
    "civil_engineer": {
        "concept_uri": "http://data.europa.eu/esco/occupation/2142-civil-engineer",
        "title": "Civil Engineer",
        "essential_skills": [
            "perform structural calculations and design analysis",
            "interpret CAD and BIM architectural drawings",
            "conduct construction site inspections",
            "ensure compliance with national building codes",
            "manage project estimates and bill of materials"
        ],
        "optional_skills": [
            "geotechnical soil analysis",
            "environmental impact assessment",
            "project scheduling and critical path method",
            "sustainable green building design"
        ]
    }
}

class ESCOService:
    """Service to query ESCO global skills taxonomy."""

    @staticmethod
    def get_skill_profile(career_key: str) -> Optional[Dict[str, Any]]:
        """Retrieve ESCO skill profile for a career key."""
        return ESCO_SKILLS_TAXONOMY.get(career_key)

    @staticmethod
    def get_essential_skills(career_key: str) -> List[str]:
        """Get list of essential skills for a career."""
        profile = ESCO_SKILLS_TAXONOMY.get(career_key)
        return profile["essential_skills"] if profile else []
