"""
Learning Resources & Course Provider Service.
Provides curated educational resources, free/open courses, and official documentation for skills and careers.
Strictly adheres to policy: ZERO un-authorized web scraping.
Operates via curated repository with pluggable provider architecture.
"""

from typing import Dict, Any, List, Optional
from abc import ABC, abstractmethod

# Curated High-Quality Open & Free Learning Resources
CURATED_LEARNING_RESOURCES: Dict[str, List[Dict[str, Any]]] = {
    "ux-designer": [
        {
            "title": "Google UX Design Professional Certificate",
            "provider": "Coursera / Google",
            "type": "Interactive Certification",
            "cost": "Free to Audit / Financial Aid Available",
            "url": "https://www.coursera.org/professional-certificates/google-ux-design",
            "skill": "User Research, Wireframing, Figma, Usability Testing"
        },
        {
            "title": "Figma Learn & Design Systems Library",
            "provider": "Figma Official",
            "type": "Interactive Guides",
            "cost": "Free",
            "url": "https://help.figma.com/hc/en-us/categories/360002051613",
            "skill": "Auto-Layout, Component Variants, Prototyping"
        }
    ],
    "frontend-developer": [
        {
            "title": "MDN Web Docs Front-End Curriculum",
            "provider": "Mozilla Developer Network",
            "type": "Documentation & Hands-on Tutorials",
            "cost": "Free",
            "url": "https://developer.mozilla.org/en-US/docs/Learn",
            "skill": "HTML5, CSS3, Modern JavaScript, Web Accessibility"
        },
        {
            "title": "Full Stack Open (React & TypeScript)",
            "provider": "University of Helsinki",
            "type": "Open University Course",
            "cost": "Free",
            "url": "https://fullstackopen.com/en/",
            "skill": "React, TypeScript, State Management, REST APIs"
        }
    ],
    "data-scientist": [
        {
            "title": "Harvard CS109: Introduction to Data Science",
            "provider": "Harvard University",
            "type": "OpenCourseWare",
            "cost": "Free",
            "url": "https://cs109.github.io/2015/",
            "skill": "Python Pandas, Statistical Modeling, Machine Learning"
        },
        {
            "title": "Kaggle Micro-Courses for Data Analysis & ML",
            "provider": "Kaggle",
            "type": "Interactive Coding",
            "cost": "Free",
            "url": "https://www.kaggle.com/learn",
            "skill": "SQL, Feature Engineering, XGBoost, Data Visualization"
        }
    ],
    "registered-nurse": [
        {
            "title": "Clinical Skills & Patient Care Fundamentals",
            "provider": "Open Michigan / University of Michigan",
            "type": "Open Clinical Curriculum",
            "cost": "Free",
            "url": "https://open.umich.edu",
            "skill": "Patient Assessment, Pharmacology Basics, Infection Control"
        }
    ],
    "accountant": [
        {
            "title": "Financial Accounting Fundamentals",
            "provider": "MIT OpenCourseWare (Sloan School of Management)",
            "type": "Lecture Notes & Problem Sets",
            "cost": "Free",
            "url": "https://ocw.mit.edu",
            "skill": "Balance Sheets, Cash Flow Statements, Accrual Accounting"
        }
    ],
    "civil-engineer": [
        {
            "title": "Structural Mechanics & Materials",
            "provider": "MIT OpenCourseWare",
            "type": "Engineering Curriculum",
            "cost": "Free",
            "url": "https://ocw.mit.edu",
            "skill": "Static Analysis, Stress-Strain Relations, Beam Deflection"
        }
    ],
    "electrician": [
        {
            "title": "National Electrical Code (PEC) Essentials & Safety",
            "provider": "IIEE (Institute of Integrated Electrical Engineers)",
            "type": "Technical Safety Standards",
            "cost": "Free Reference Guides",
            "url": "https://iiee.org.ph",
            "skill": "Electrical Circuit Protection, Grounding, Single & 3-Phase Wiring"
        }
    ]
}

class LearningProvider(ABC):
    @abstractmethod
    def search_resources(self, query: str) -> List[Dict[str, Any]]:
        pass

    @abstractmethod
    def get_resources_for_career(self, career_id: str) -> List[Dict[str, Any]]:
        pass

class CuratedLearningProvider(LearningProvider):
    def search_resources(self, query: str) -> List[Dict[str, Any]]:
        q = query.lower().strip()
        matches = []
        for resource_list in CURATED_LEARNING_RESOURCES.values():
            for res in resource_list:
                if (
                    q in res["title"].lower()
                    or q in res["provider"].lower()
                    or q in res.get("skill", "").lower()
                ):
                    matches.append(res)
        return matches

    def get_resources_for_career(self, career_id: str) -> List[Dict[str, Any]]:
        return CURATED_LEARNING_RESOURCES.get(career_id, [])

class LearningService:
    """Service to discover accredited, open, and verified learning materials."""

    _provider: LearningProvider = CuratedLearningProvider()

    @classmethod
    def set_provider(cls, provider: LearningProvider):
        cls._provider = provider

    @classmethod
    def search_resources(cls, query: str) -> List[Dict[str, Any]]:
        return cls._provider.search_resources(query)

    @classmethod
    def get_resources_for_career(cls, career_id: str) -> List[Dict[str, Any]]:
        return cls._provider.get_resources_for_career(career_id)

    @classmethod
    def get_learning_resources_for_career(cls, career_id: str) -> List[Dict[str, Any]]:
        return cls._provider.get_resources_for_career(career_id)

