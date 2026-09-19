"""
Philippine Technical-Vocational Education and Training (TVET / TESDA) Service.
Provides verified Philippine qualification and competency standards (National Certificates NC I - NC IV).
Strictly adheres to policy: ZERO un-authorized web scraping.
Operates via curated Training Regulations repository with pluggable provider architecture.
"""

from typing import Dict, Any, List, Optional
from abc import ABC, abstractmethod

# Verified TESDA National Qualifications & Training Regulations
TESDA_CURATED_QUALIFICATIONS: Dict[str, List[Dict[str, Any]]] = {
    "ux-designer": [
        {
            "qualification": "Visual Graphic Design NC III",
            "code": "TESDA-VGD-NC3",
            "sector": "Information and Communications Technology (ICT)",
            "description": "Competency in creating visual graphic design for print, web, digital interface layouts, and multimedia branding.",
            "duration_hours": "487 Hours",
            "agency": "TESDA (Technical Education and Skills Development Authority)",
            "url": "https://www.tesda.gov.ph"
        }
    ],
    "graphic-designer": [
        {
            "qualification": "Visual Graphic Design NC III",
            "code": "TESDA-VGD-NC3",
            "sector": "Information and Communications Technology (ICT)",
            "description": "Competency in creating visual graphic design for print, web, digital interface layouts, and multimedia branding.",
            "duration_hours": "487 Hours",
            "agency": "TESDA (Technical Education and Skills Development Authority)",
            "url": "https://www.tesda.gov.ph"
        }
    ],
    "frontend-developer": [
        {
            "qualification": "Web Development NC III",
            "code": "TESDA-WD-NC3",
            "sector": "Information and Communications Technology (ICT)",
            "description": "Competency in front-end and client-side web application programming, responsive UI implementation, and database integration.",
            "duration_hours": "540 Hours",
            "agency": "TESDA",
            "url": "https://www.tesda.gov.ph"
        }
    ],
    "fullstack-developer": [
        {
            "qualification": "Programming (.NET Technology / Java) NC IV",
            "code": "TESDA-PROG-NC4",
            "sector": "Information and Communications Technology (ICT)",
            "description": "Advanced programming, multi-tier software architecture design, object-oriented software engineering, and production deployment.",
            "duration_hours": "640 Hours",
            "agency": "TESDA",
            "url": "https://www.tesda.gov.ph"
        }
    ],
    "cloud-engineer": [
        {
            "qualification": "Broadband Installation & Maintenance (Fixed Wireless / Fiber) NC II",
            "code": "TESDA-ICT-NC2",
            "sector": "Information and Communications Technology (ICT)",
            "description": "Infrastructure hardware, structured cabling, network switch configuration, and enterprise telecommunications.",
            "duration_hours": "260 Hours",
            "agency": "TESDA",
            "url": "https://www.tesda.gov.ph"
        }
    ],
    "electrician": [
        {
            "qualification": "Electrical Installation and Maintenance (EIM) NC II",
            "code": "TESDA-EIM-NC2",
            "sector": "Electrical & Electronics",
            "description": "Standard electrical wiring, residential and commercial distribution panel installation, circuit testing, and safety protocols.",
            "duration_hours": "402 Hours",
            "agency": "TESDA",
            "url": "https://www.tesda.gov.ph"
        }
    ],
    "commercial-electrician": [
        {
            "qualification": "Electrical Installation and Maintenance (EIM) NC II",
            "code": "TESDA-EIM-NC2",
            "sector": "Electrical & Utilities",
            "description": "Install and maintain electrical wiring, lighting fixtures, circuit breakers, and control devices according to the Philippine Electrical Code (PEC).",
            "duration_hours": "402 Hours",
            "agency": "TESDA",
            "url": "https://www.tesda.gov.ph"
        },
        {
            "qualification": "Electrical Installation and Maintenance (EIM) NC III",
            "code": "TESDA-EIM-NC3",
            "sector": "Electrical & Utilities",
            "description": "Advanced commercial wiring, motor control circuits, three-phase transformers, and industrial troubleshooting.",
            "duration_hours": "360 Hours",
            "agency": "TESDA",
            "url": "https://www.tesda.gov.ph"
        }
    ],

    "accountant": [
        {
            "qualification": "Bookkeeping NC III",
            "code": "TESDA-BK-NC3",
            "sector": "Business, Financial and Other Services",
            "description": "Maintain general ledger accounts, prepare trial balance, complete monthly financial statements, and prepare internal audit schedules.",
            "duration_hours": "292 Hours",
            "agency": "TESDA",
            "url": "https://www.tesda.gov.ph"
        }
    ],
    "digital-marketing-specialist": [
        {
            "qualification": "Social Media Marketing and E-Commerce Services",
            "code": "TESDA-ECOM-NC",
            "sector": "Business & ICT",
            "description": "Digital ad campaign management, audience analytics, content creation, and search engine optimization.",
            "duration_hours": "320 Hours",
            "agency": "TESDA",
            "url": "https://www.tesda.gov.ph"
        }
    ],
    "registered-nurse": [
        {
            "qualification": "Caregiving NC II",
            "code": "TESDA-CG-NC2",
            "sector": "Human Health / Healthcare",
            "description": "Foundational healthcare support, vital signs monitoring, patient hygiene, and emergency first response.",
            "duration_hours": "786 Hours",
            "agency": "TESDA",
            "url": "https://www.tesda.gov.ph"
        },
        {
            "qualification": "Emergency Medical Services (EMS) NC II",
            "code": "TESDA-EMS-NC2",
            "sector": "Healthcare & Public Safety",
            "description": "Pre-hospital emergency care, patient stabilization, trauma care, and clinical coordination.",
            "duration_hours": "960 Hours",
            "agency": "TESDA",
            "url": "https://www.tesda.gov.ph"
        }
    ]
}

class TrainingProvider(ABC):
    @abstractmethod
    def search_training(self, query: str) -> List[Dict[str, Any]]:
        pass

    @abstractmethod
    def get_training_for_career(self, career_id: str) -> List[Dict[str, Any]]:
        pass

class CuratedTESDATrainingProvider(TrainingProvider):
    def search_training(self, query: str) -> List[Dict[str, Any]]:
        q = query.lower().strip()
        results = []
        for list_of_quals in TESDA_CURATED_QUALIFICATIONS.values():
            for qual in list_of_quals:
                if (
                    q in qual["qualification"].lower()
                    or q in qual["description"].lower()
                    or q in qual["sector"].lower()
                ):
                    results.append(qual)
        return results

    def get_training_for_career(self, career_id: str) -> List[Dict[str, Any]]:
        return TESDA_CURATED_QUALIFICATIONS.get(career_id, [])

class TrainingService:
    """Service to retrieve verified Philippine TVET and TESDA training qualifications."""

    _provider: TrainingProvider = CuratedTESDATrainingProvider()

    @classmethod
    def set_provider(cls, provider: TrainingProvider):
        cls._provider = provider

    @classmethod
    def search_training(cls, query: str) -> List[Dict[str, Any]]:
        return cls._provider.search_training(query)

    @classmethod
    def get_training_for_career(cls, career_id: str) -> List[Dict[str, Any]]:
        return cls._provider.get_training_for_career(career_id)

    @classmethod
    def get_qualifications_for_career(cls, career_id: str) -> List[Dict[str, Any]]:
        return cls._provider.get_training_for_career(career_id)
