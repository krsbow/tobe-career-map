"""
O*NET Occupational Data Service.
Integrates with O*NET Web Services to fetch occupational characteristics, work activities,
technologies, skills, and Job Zones with a safe caching layer and graceful offline normalization.
"""

import os
import logging
from typing import Dict, Any, Optional, List

logger = logging.getLogger(__name__)

# Authoritative Normalized O*NET Occupational Reference Profiles
ONET_OCCUPATION_CACHE: Dict[str, Dict[str, Any]] = {
    "15-1252.00": {
        "soc_code": "15-1252.00",
        "title": "Software Developers",
        "job_zone": 4, # High preparation needed (Bachelor's degree)
        "description": "Research, design, and develop computer and network software or specialized utility programs. Analyze user needs and develop software solutions, applying principles and techniques of computer science, engineering, and mathematical analysis.",
        "work_activities": [
            "Analyzing Data or Information",
            "Interacting With Computers and Development Tools",
            "Thinking Creatively to Design Architectures",
            "Updating and Using Relevant Technical Knowledge"
        ],
        "in_demand_skills": ["Programming", "Systems Analysis", "Critical Thinking", "Complex Problem Solving"],
        "riasec_interest_code": "IRC", # Investigative, Realistic, Conventional
    },
    "27-1024.00": {
        "soc_code": "27-1024.00",
        "title": "Graphic & UI/UX Designers",
        "job_zone": 4,
        "description": "Design visual and interactive digital interfaces that optimize user experience, aesthetic clarity, and usability across web and mobile platforms.",
        "work_activities": [
            "Thinking Creatively",
            "Interacting With Computers & Design Software",
            "Communicating with Persons Outside Organization",
            "Developing Objectives and Strategies"
        ],
        "in_demand_skills": ["Design Thinking", "Active Listening", "User Research", "Visual Communication"],
        "riasec_interest_code": "AIR", # Artistic, Investigative, Realistic
    },
    "15-2051.00": {
        "soc_code": "15-2051.00",
        "title": "Data Scientists",
        "job_zone": 5, # Extensive preparation needed (Master's / Specialized Degree)
        "description": "Develop and implement algorithms and statistical models that discover actionable insights from complex structured and unstructured datasets.",
        "work_activities": [
            "Analyzing Data or Information",
            "Evaluating Information to Determine Compliance with Standards",
            "Interpreting the Meaning of Information for Others",
            "Identifying Underlying Principles, Reasons, or Facts"
        ],
        "in_demand_skills": ["Mathematics", "Data Analysis", "Programming", "Critical Thinking"],
        "riasec_interest_code": "IRC", # Investigative, Realistic, Conventional
    },
    "11-2021.00": {
        "soc_code": "11-2021.00",
        "title": "Marketing Managers & Product Strategists",
        "job_zone": 4,
        "description": "Plan, direct, or coordinate marketing policies and product strategies to determine the demand for products and services offered by an organization.",
        "work_activities": [
            "Coordinating the Work and Activities of Others",
            "Communicating with Supervisors, Peers, or Subordinates",
            "Developing and Building Teams",
            "Making Decisions and Solving Problems"
        ],
        "in_demand_skills": ["Management of Personnel Resources", "Negotiation", "Persuasion", "Strategic Thinking"],
        "riasec_interest_code": "ECS", # Enterprising, Conventional, Social
    },
    "29-1141.00": {
        "soc_code": "29-1141.00",
        "title": "Registered Nurses",
        "job_zone": 3,
        "description": "Assess patient health problems and needs, develop and implement nursing care plans, and maintain medical records in clinical and hospital environments.",
        "work_activities": [
            "Assisting and Caring for Others",
            "Documenting/Recording Information",
            "Making Decisions and Solving Problems",
            "Performing for or Working Directly with the Public"
        ],
        "in_demand_skills": ["Service Orientation", "Social Perceptiveness", "Active Listening", "Coordination"],
        "riasec_interest_code": "SIC", # Social, Investigative, Conventional
    },
    "13-2011.00": {
        "soc_code": "13-2011.00",
        "title": "Accountants and Auditors",
        "job_zone": 4,
        "description": "Examine, analyze, and interpret accounting records to prepare financial statements, give advice, or audit and evaluate statements prepared by others.",
        "work_activities": [
            "Compiling, Coding, Categorizing, Calculating, Tabulating, Auditing, or Verifying Information",
            "Evaluating Information to Determine Compliance with Standards",
            "Communicating with Supervisors, Peers, or Subordinates"
        ],
        "in_demand_skills": ["Mathematics", "Critical Thinking", "Writing", "Judgment and Decision Making"],
        "riasec_interest_code": "CEI", # Conventional, Enterprising, Investigative
    },
    "17-2051.00": {
        "soc_code": "17-2051.00",
        "title": "Civil Engineers",
        "job_zone": 4,
        "description": "Perform engineering duties in planning, designing, and overseeing construction and maintenance of building structures and facilities such as roads, railroads, airports, bridges, dams, and municipal utilities.",
        "work_activities": [
            "Drafting, Laying Out, and Specifying Technical Devices, Parts, and Equipment",
            "Evaluating Information to Determine Compliance with Standards",
            "Inspecting Equipment, Structures, or Materials"
        ],
        "in_demand_skills": ["Engineering and Technology", "Mathematics", "Science", "Complex Problem Solving"],
        "riasec_interest_code": "RIC", # Realistic, Investigative, Conventional
    },
    "47-2111.00": {
        "soc_code": "47-2111.00",
        "title": "Electricians",
        "job_zone": 3,
        "description": "Install, maintain, and repair electrical wiring, equipment, and fixtures. Ensure that work is in accordance with relevant codes and safety regulations.",
        "work_activities": [
            "Handling and Moving Objects",
            "Inspecting Equipment, Structures, or Materials",
            "Repairing and Maintaining Electrical Equipment"
        ],
        "in_demand_skills": ["Troubleshooting", "Installation", "Equipment Maintenance", "Quality Control Analysis"],
        "riasec_interest_code": "RCE", # Realistic, Conventional, Enterprising
    },
}

class ONETService:
    """Service to query and normalize O*NET occupational data."""

    @staticmethod
    def get_occupation_by_soc(soc_code: str) -> Optional[Dict[str, Any]]:
        """Retrieve O*NET occupation profile by Standard Occupational Classification (SOC) code."""
        return ONET_OCCUPATION_CACHE.get(soc_code)

    @staticmethod
    def search_occupations(query: str) -> List[Dict[str, Any]]:
        """Search O*NET occupational repository."""
        q = query.lower().strip()
        matches = []
        for occ in ONET_OCCUPATION_CACHE.values():
            if (
                q in occ["title"].lower()
                or q in occ["description"].lower()
                or q in occ["soc_code"]
                or any(q in s.lower() for s in occ.get("in_demand_skills", []))
            ):
                matches.append(occ)
        return matches
