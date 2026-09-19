"""
Philippine Standard Occupational Classification (PSOC) Service.
Authoritative occupational taxonomy integration referencing PSA PSOC classification codes.
Provides local occupational taxonomy crosswalks and metadata for careers in the Philippines.
"""

from typing import Dict, Any, Optional, List

# Official PSA PSOC Reference Taxonomy for Target Careers
PSOC_TAXONOMY: Dict[str, Dict[str, Any]] = {
    "2512": {
        "psoc_code": "2512",
        "title": "Software Developers",
        "major_group": "2 - Professionals",
        "sub_major_group": "25 - Information and Communications Technology Professionals",
        "minor_group": "251 - Software and Applications Developers and Analysts",
        "unit_group": "2512 - Software Developers",
        "description": "Research, analyze and evaluate requirements for existing or new software applications and operating systems, and design, develop, test and maintain software solutions.",
    },
    "2513": {
        "psoc_code": "2513",
        "title": "Web and Multimedia Developers",
        "major_group": "2 - Professionals",
        "sub_major_group": "25 - Information and Communications Technology Professionals",
        "minor_group": "251 - Software and Applications Developers and Analysts",
        "unit_group": "2513 - Web and Multimedia Developers",
        "description": "Combine design and technical knowledge to research, analyze, evaluate, design, create and maintain websites and multimedia applications.",
    },
    "2166": {
        "psoc_code": "2166",
        "title": "Graphic and Multimedia Designers",
        "major_group": "2 - Professionals",
        "sub_major_group": "21 - Science and Engineering Professionals",
        "minor_group": "216 - Architects, Planners, Surveyors and Designers",
        "unit_group": "2166 - Graphic and Multimedia Designers",
        "description": "Design visual and multimedia content using creative design, user research, typography, and digital interface tools.",
    },
    "2511": {
        "psoc_code": "2511",
        "title": "Systems Analysts and Data Scientists",
        "major_group": "2 - Professionals",
        "sub_major_group": "25 - Information and Communications Technology Professionals",
        "minor_group": "251 - Software and Applications Developers and Analysts",
        "unit_group": "2511 - Systems Analysts",
        "description": "Conduct research, analyze data structures and system requirements, and develop predictive models and data architectures.",
    },
    "2521": {
        "psoc_code": "2521",
        "title": "Database Designers and Administrators",
        "major_group": "2 - Professionals",
        "sub_major_group": "25 - Information and Communications Technology Professionals",
        "minor_group": "252 - Database and Network Professionals",
        "unit_group": "2521 - Database Designers and Administrators",
        "description": "Design, develop, maintain, and secure data storage systems and infrastructure.",
    },
    "2529": {
        "psoc_code": "2529",
        "title": "Information and Communications Technology Security Specialists",
        "major_group": "2 - Professionals",
        "sub_major_group": "25 - Information and Communications Technology Professionals",
        "minor_group": "252 - Database and Network Professionals",
        "unit_group": "2529 - ICT Security Specialists",
        "description": "Plan, implement, and monitor security measures for information systems to protect data and infrastructure against cybersecurity threats.",
    },
    "1219": {
        "psoc_code": "1219",
        "title": "Business Services and Administration Managers",
        "major_group": "1 - Managers",
        "sub_major_group": "12 - Administrative and Commercial Managers",
        "minor_group": "121 - Business Services and Administration Managers",
        "unit_group": "1219 - Product & Business Strategy Managers",
        "description": "Formulate, direct and coordinate product development, business operations, and organizational strategy.",
    },
    "2221": {
        "psoc_code": "2221",
        "title": "Nursing Professionals",
        "major_group": "2 - Professionals",
        "sub_major_group": "22 - Health Professionals",
        "minor_group": "222 - Nursing and Midwifery Professionals",
        "unit_group": "2221 - Nursing Professionals",
        "description": "Provide treatment, support and care services for patients suffering from physical and mental illnesses and injuries in healthcare settings.",
    },
    "2411": {
        "psoc_code": "2411",
        "title": "Accountants and Financial Analysts",
        "major_group": "2 - Professionals",
        "sub_major_group": "24 - Business and Administration Professionals",
        "minor_group": "241 - Finance Professionals",
        "unit_group": "2411 - Accountants",
        "description": "Plan, organize and administer accounting systems and analyze financial information for individuals and organizations.",
    },
    "2142": {
        "psoc_code": "2142",
        "title": "Civil Engineers",
        "major_group": "2 - Professionals",
        "sub_major_group": "21 - Science and Engineering Professionals",
        "minor_group": "214 - Engineering Professionals",
        "unit_group": "2142 - Civil Engineers",
        "description": "Conduct research, advise on, design, and direct construction of bridges, buildings, roads, and municipal infrastructure.",
    },
    "2330": {
        "psoc_code": "2330",
        "title": "Secondary Education Teachers",
        "major_group": "2 - Professionals",
        "sub_major_group": "23 - Teaching Professionals",
        "minor_group": "233 - Secondary Education Teachers",
        "unit_group": "2330 - Secondary Education Teachers",
        "description": "Teach one or more subjects for educational or vocational purposes to students in secondary and senior high schools.",
    },
    "7411": {
        "psoc_code": "7411",
        "title": "Building and Related Electricians",
        "major_group": "7 - Craft and Related Trades Workers",
        "sub_major_group": "74 - Electrical and Electronic Trades Workers",
        "minor_group": "741 - Electrical Equipment Installers and Repairers",
        "unit_group": "7411 - Building and Related Electricians",
        "description": "Install, maintain, and repair electrical wiring systems, fixtures, and related equipment in domestic, commercial, and industrial facilities.",
    },
    "2431": {
        "psoc_code": "2431",
        "title": "Advertising and Marketing Professionals",
        "major_group": "2 - Professionals",
        "sub_major_group": "24 - Business and Administration Professionals",
        "minor_group": "243 - Sales, Marketing and Public Relations Professionals",
        "unit_group": "2431 - Advertising and Marketing Professionals",
        "description": "Develop and coordinate advertising and marketing campaigns to promote products and services across digital and traditional media.",
    },
}

class PSOCService:
    """Service to query and map Philippine Standard Occupational Classification data."""

    @staticmethod
    def get_psoc_by_code(code: str) -> Optional[Dict[str, Any]]:
        """Retrieve PSOC record by 4-digit classification code."""
        return PSOC_TAXONOMY.get(code)

    @staticmethod
    def search_psoc(query: str) -> List[Dict[str, Any]]:
        """Search PSOC classification titles and descriptions."""
        q = query.lower().strip()
        results = []
        for rec in PSOC_TAXONOMY.values():
            if (
                q in rec["title"].lower()
                or q in rec["description"].lower()
                or q in rec["psoc_code"]
                or q in rec["unit_group"].lower()
            ):
                results.append(rec)
        return results

    @staticmethod
    def get_all_psoc() -> List[Dict[str, Any]]:
        """Return all supported PSOC taxonomy entries."""
        return list(PSOC_TAXONOMY.values())
