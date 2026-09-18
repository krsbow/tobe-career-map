"""
Assessment Question Bank for TO BE Career Discovery Platform.
Stored separately from application logic with dimension categories and scoring weights.
"""

from typing import List, Dict, Any

ASSESSMENT_VERSION = "1.0.0"

# Predefined Skills Knowledge Bank with Categories
SKILL_CATEGORIES = {
    "Programming & Core Tech": [
        "Python", "JavaScript", "TypeScript", "Java", "C++", "C#", "Kotlin", "Swift", "Go", "Rust", "PHP", "Ruby"
    ],
    "Web & Frontend": [
        "HTML", "CSS", "React", "Vue.js", "Angular", "Next.js", "Tailwind CSS", "Node.js", "REST APIs", "GraphQL"
    ],
    "Design & User Experience": [
        "Figma", "UI Design", "UX Research", "Wireframing", "Prototyping", "Design Systems", "Usability Testing", "Adobe XD"
    ],
    "Data, AI & Analytics": [
        "SQL", "Python (Pandas/NumPy)", "Tableau", "Power BI", "Data Analysis", "Machine Learning", "Data Visualization", "Excel / Spreadsheets"
    ],
    "Cloud, DevOps & Systems": [
        "Git & GitHub", "Linux", "Docker", "AWS", "Google Cloud", "Azure", "CI/CD", "Kubernetes", "System Architecture"
    ],
    "Cybersecurity": [
        "Network Security", "Vulnerability Assessment", "Ethical Hacking", "Cryptography", "Security Compliance", "Incident Response"
    ],
    "Product, Business & Professional": [
        "Problem Solving", "Project Management", "Agile / Scrum", "Communication", "Technical Writing", "Presentation", "Critical Thinking", "Team Collaboration"
    ]
}

# Questions bank categorized by dimension
ASSESSMENT_QUESTIONS: List[Dict[str, Any]] = [
    # 1. RIASEC & Interests
    {
        "id": "interest_1",
        "category": "interests",
        "dimension": "RIASEC",
        "title": "What kind of challenge sounds most satisfying to you?",
        "subtitle": "Think about what genuinely sparks your curiosity or flow state.",
        "type": "single_choice",
        "options": [
            {
                "id": "i1_artistic",
                "text": "Designing an intuitive, visually stunning experience that people love using",
                "scores": {"A": 3, "S": 1}
            },
            {
                "id": "i1_investigative",
                "text": "Investigating a complex bug, analyzing data patterns, or solving logical puzzles",
                "scores": {"I": 3, "R": 1}
            },
            {
                "id": "i1_enterprising",
                "text": "Shaping a product vision, leading strategy, and deciding what gets built",
                "scores": {"E": 3, "S": 1}
            },
            {
                "id": "i1_realistic",
                "text": "Configuring infrastructure, automating servers, and building robust technical foundations",
                "scores": {"R": 3, "C": 1}
            }
        ]
    },
    {
        "id": "interest_2",
        "category": "interests",
        "dimension": "RIASEC",
        "title": "If you had a free weekend to build a project, what would you naturally gravitate toward?",
        "subtitle": "There are no wrong answers — pick the one closest to your curiosity.",
        "type": "single_choice",
        "options": [
            {
                "id": "i2_artistic_investigative",
                "text": "Redesigning an app interface and testing how real people interact with it",
                "scores": {"A": 2, "I": 2, "S": 1}
            },
            {
                "id": "i2_investigative_realistic",
                "text": "Building a script to analyze interesting data or train an intelligent machine learning model",
                "scores": {"I": 3, "R": 2}
            },
            {
                "id": "i2_conventional_realistic",
                "text": "Setting up a secure home server, cloud pipeline, or automated security scanner",
                "scores": {"R": 2, "C": 3, "I": 1}
            },
            {
                "id": "i2_enterprising_social",
                "text": "Brainstorming a tech startup concept, mapping user needs, and planning a roadmap",
                "scores": {"E": 3, "S": 2}
            }
        ]
    },
    {
        "id": "interest_3",
        "category": "interests",
        "dimension": "RIASEC",
        "title": "Which type of problem-solving feels most energizing?",
        "subtitle": "Consider how your mind prefers to work with information.",
        "type": "single_choice",
        "options": [
            {
                "id": "i3_visual_human",
                "text": "Visual & Human: Crafting layouts, user journeys, colors, and empathy-driven flows",
                "scores": {"A": 3, "S": 2}
            },
            {
                "id": "i3_logical_algorithmic",
                "text": "Logical & Algorithmic: Writing clean code, optimizing performance, designing data structures",
                "scores": {"I": 3, "R": 2}
            },
            {
                "id": "i3_systems_defensive",
                "text": "Systems & Reliability: Protecting data from vulnerabilities, scaling architecture, uptime",
                "scores": {"C": 2, "R": 2, "I": 2}
            },
            {
                "id": "i3_strategic_organizational",
                "text": "Strategic & Organizational: Coordinating teams, defining metrics, prioritizing features",
                "scores": {"E": 3, "C": 1, "S": 1}
            }
        ]
    },

    # 2. Work Preferences
    {
        "id": "work_preference_1",
        "category": "work_preferences",
        "dimension": "Work Environment",
        "title": "What kind of day-to-day work rhythm do you thrive in?",
        "subtitle": "Select the environment that aligns best with your energy.",
        "type": "single_choice",
        "options": [
            {
                "id": "wp1_independent_deep",
                "text": "Deep focus: Long stretches of independent problem-solving and building",
                "preference": "Deep Focus / Independent",
                "scores": {"I": 2, "R": 1}
            },
            {
                "id": "wp1_collaborative_team",
                "text": "Collaborative: Bouncing ideas with cross-functional teammates, designers, and engineers",
                "preference": "High Collaboration / Cross-Functional",
                "scores": {"S": 2, "E": 1}
            },
            {
                "id": "wp1_hybrid_varied",
                "text": "Balanced: A mix of solo deep work and regular team brainstorming",
                "preference": "Balanced / Hybrid Rhythm",
                "scores": {"A": 1, "I": 1, "S": 1}
            },
            {
                "id": "wp1_client_user",
                "text": "User-facing: Interviewing users, understanding customer pain points, and presenting findings",
                "preference": "User-Facing & Consultative",
                "scores": {"S": 2, "E": 2}
            }
        ]
    },

    # 3. Career Priorities
    {
        "id": "career_priorities",
        "category": "priorities",
        "dimension": "Values & Motivation",
        "title": "What matters most to you in your next career step?",
        "subtitle": "Select up to 3 core priorities.",
        "type": "multi_select",
        "max_select": 3,
        "options": [
            {"id": "p_creativity", "text": "Creative expression & craft"},
            {"id": "p_earning", "text": "High earning potential & financial growth"},
            {"id": "p_meaning", "text": "Meaningful social impact & helping people"},
            {"id": "p_learning", "text": "Continuous technical learning & curiosity"},
            {"id": "p_flexibility", "text": "Work flexibility / remote options"},
            {"id": "p_stability", "text": "Job stability & high industry demand"},
            {"id": "p_leadership", "text": "Leadership & strategic ownership"}
        ]
    },

    # 4. Desired Impact
    {
        "id": "desired_impact",
        "category": "impact",
        "dimension": "Impact Style",
        "title": "Where would you feel proudest seeing your work make a difference?",
        "subtitle": "Choose the impact style that resonates most.",
        "type": "single_choice",
        "options": [
            {
                "id": "imp_user_joy",
                "text": "In the hands of everyday users who find technology easier, faster, and more accessible",
                "impact": "User Delight & Human-Centered Utility"
            },
            {
                "id": "imp_intelligence",
                "text": "In uncovering actionable insights, discovering data truth, or automating intelligent workflows",
                "impact": "Data Intelligence & Discovery"
            },
            {
                "id": "imp_infrastructure",
                "text": "In the backbone of tech: Keeping millions of users' data safe, private, fast, and always online",
                "impact": "Security, Privacy & Infrastructure Resilience"
            },
            {
                "id": "imp_business_scale",
                "text": "In bringing new product ideas to market, scaling teams, and driving business innovation",
                "impact": "Product Strategy & Business Growth"
            }
        ]
    }
]
