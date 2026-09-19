"""
Guided Career Mentor Service & Question Catalog for TO BE (Python / Streamlit counterpart).

Provides structured question intents across WHAT / WHY / HOW / PRACTICAL,
priority-based question progression, career-adaptive wording, and
grounded, intent-specific answer generation from seed career data.
"""

from typing import Dict, Any, List, Optional
from data.seed_data import CAREERS_SEED

class GuidedMentorEngine:
    """Guided Career Mentor logic engine for structured discovery."""

    def __init__(self):
        self.careers_by_id = {c["id"]: c for c in CAREERS_SEED}

    def get_career(self, career_id_or_title: str) -> Optional[Dict[str, Any]]:
        """Look up career by id or fuzzy title."""
        if not career_id_or_title:
            return CAREERS_SEED[0] if CAREERS_SEED else None

        cid = career_id_or_title.lower().strip()
        if cid in self.careers_by_id:
            return self.careers_by_id[cid]

        # Match title or substring
        for c in CAREERS_SEED:
            if c["id"].lower() == cid or c["title"].lower() == cid or cid in c["title"].lower():
                return c
        return CAREERS_SEED[0] if CAREERS_SEED else None

    def get_prerequisite_question(self, career: Dict[str, Any]) -> str:
        """Adaptive wording for prerequisite questions."""
        cid = career.get("id", "").lower()
        title = career.get("title", "").lower()

        if "ai-ml" in cid or "machine learning" in title or "ai" in title:
            return "Do I need to be good at math and algorithms?"
        if "ui-ux" in cid or "ux-designer" in cid or "design" in title:
            return "Do I need to be good at drawing or visual art?"
        if "cybersecurity" in cid or "security" in title:
            return "Do I need strong programming experience to start?"
        if "data-analyst" in cid or "data" in title:
            return "How much statistics and math do I need to know?"
        if "project-manager" in cid or "product-manager" in cid or "manager" in title:
            return "Do I need deep technical skills to be a project manager?"
        if "frontend" in cid:
            return "Do I need to be a graphic designer to do front-end?"
        if "nurse" in cid:
            return "What is the emotional and physical demand of bedside nursing?"
        if "civil" in cid:
            return "How much physics and advanced calculus is required?"
        if "electrician" in cid:
            return "Is commercial electrical work dangerous or physically heavy?"
        if "accountant" in cid or "cpa" in cid:
            return "Is the CPA board exam necessary to get hired?"
        return f"What background or prerequisites are needed for {career.get('title', 'this role')}?"

    def get_prerequisite_answer(self, career: Dict[str, Any]) -> str:
        """Adaptive grounded answer for prerequisite questions."""
        cid = career.get("id", "").lower()
        title = career.get("title", "this role")

        if "ai-ml" in cid or "machine-learning" in cid:
            return (
                "For AI & Machine Learning Engineering, you need a comfortable working foundation in linear algebra "
                "(matrices, vectors), calculus (gradients, partial derivatives), and probability.\n\n"
                "You do not need to be a pure mathematical theorist to start; applied machine learning relies heavily "
                "on using established libraries (PyTorch, TensorFlow, Scikit-learn) and understanding how algorithms optimize weights.\n\n"
                "Solid Python programming and data manipulation skills are just as important as mathematical foundations."
            )
        if "ui-ux" in cid or "ux-designer" in cid or "design" in cid:
            return (
                "You do not need fine-art drawing or sketching talent for UI/UX design.\n\n"
                "UI/UX design is about digital usability, layout hierarchy, spacing systems, and user flows inside tools like Figma. "
                "These rely on structured geometric components, typographic scales, and design heuristics rather than freehand illustration.\n\n"
                "Empathy for user friction and curiosity about how people interact with software matter far more than drawing ability."
            )
        if "cybersecurity" in cid:
            return (
                "You do not need to be a master programmer to begin in Cybersecurity, but foundational scripting (Python or Bash) "
                "and a solid grasp of computer networking (TCP/IP, DNS, routing) and operating system internals (Linux and Windows admin) are essential.\n\n"
                "Many entry-level analysts start with network defense, log analysis in SIEM tools, and vulnerability scanning before learning advanced exploit analysis."
            )
        if "data-analyst" in cid or "data" in cid:
            return (
                "Junior Data Analysts do not need advanced mathematical statistics or multivariable calculus.\n\n"
                "You need solid working comfort with descriptive statistics (mean, median, standard deviation, percentiles, correlation) and clean arithmetic logic.\n\n"
                "The majority of everyday data analysis centers on SQL querying, data cleaning in Excel or Python, and communicating visual trends effectively through dashboards."
            )
        if "project-manager" in cid or "product-manager" in cid:
            return (
                "Project Managers do not write production code or create Figma components daily, but having high 'technical literacy' is extremely valuable.\n\n"
                "Understanding software development cycles (Agile, Scrum), sprint planning, API dependencies, and how engineers estimate effort helps you communicate with credibility and eliminate blockers."
            )
        return f"For {title}, core prerequisites center on practical problem solving and foundational tool literacy. Proof of hands-on capability is prioritized over rigid academic hurdles."

    def get_catalog(self, career: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Returns the complete question catalog mapped for the given career."""
        title = career.get("title", "this career")
        tagline = career.get("tagline", "")
        desc = career.get("description", "")
        tools = career.get("common_tools", [])
        skills = career.get("core_skills", [])
        opt_skills = career.get("optional_skills", [])
        sal_ph = career.get("salary_data", {}).get("philippines", {})
        projects = career.get("portfolio_projects", [])
        related = career.get("related_careers", [])

        return [
            # WHAT TO BE
            {
                "intent": "overview",
                "category": "WHAT",
                "priority": "HIGH",
                "question": f"What does a {title} actually do?",
                "answer": f"{tagline}\n\n{desc}\n\nTheir primary focus is translating domain objectives into dependable, high-quality outcomes." if tagline else f"{desc}\n\nTheir primary focus is delivering dependable outcomes.",
            },
            {
                "intent": "daily_work",
                "category": "WHAT",
                "priority": "HIGH",
                "question": f"What does a typical day look like for a {title}?",
                "answer": (
                    f"A typical workday for a {title} balances focused execution and collaborative review:\n\n"
                    "• Morning (30–45 mins): A quick team sync or standup to review priorities and unblock tasks.\n"
                    "• Core Focus Block (2–4 hours): Deep, uninterrupted work time dedicated to primary deliverables.\n"
                    "• Afternoon (1–2 hours): Cross-functional reviews with teammates, testing, and refining deliverables.\n\n"
                    f"Work Style: {career.get('work_style', 'Focused individual execution combined with team collaboration')}."
                ),
            },
            {
                "intent": "responsibilities",
                "category": "WHAT",
                "priority": "MEDIUM",
                "question": "What are the core responsibilities of this role?",
                "answer": (
                    f"As a {title}, key responsibilities center on:\n\n" +
                    "\n".join([f"• Executing and maintaining high standards in {s}." for s in skills[:4]]) +
                    "\n\nYou are responsible for delivering reliable outcomes, documenting work clearly, and collaborating with project stakeholders."
                ) if skills else f"The primary responsibilities of a {title} involve planning, building, and maintaining core deliverables.",
            },
            {
                "intent": "tools",
                "category": "WHAT",
                "priority": "MEDIUM",
                "question": "What tools and technologies are commonly used?",
                "answer": (
                    f"Standard industry tools used by {title}s include:\n\n" +
                    "\n".join([f"• {t}" for t in tools[:6]]) +
                    "\n\nBecoming comfortable with these tools builds the foundation for everyday workflow efficiency."
                ) if tools else "Tools vary based on specialization, but include standard planning, production, and testing software.",
            },
            # WHY TO BE
            {
                "intent": "required_skills",
                "category": "WHY",
                "priority": "HIGH",
                "question": "What skills should I have for this career?",
                "answer": (
                    f"To thrive as a {title}, you want to develop both core functional capabilities and supportive strengths:\n\n"
                    "Core Foundations:\n" +
                    "\n".join([f"• {s}" for s in skills[:4]]) +
                    (("\n\nValuable Differentiators:\n" + "\n".join([f"• {s}" for s in opt_skills[:3]])) if opt_skills else "")
                ),
            },
            {
                "intent": "prerequisite_concern",
                "category": "WHY",
                "priority": "HIGH",
                "question": self.get_prerequisite_question(career),
                "answer": self.get_prerequisite_answer(career),
            },
            {
                "intent": "challenges",
                "category": "WHY",
                "priority": "MEDIUM",
                "question": "What are the most challenging parts of this career?",
                "answer": (
                    f"Every career has real tradeoffs. For a {title}, primary challenges often include:\n\n"
                    "• Continuous Evolution: Tools and best practices advance quickly, requiring ongoing self-learning.\n"
                    "• Problem Complexity: Troubleshooting unexpected bugs or bottlenecks requires patience and structured thinking.\n"
                    "• Scope Balancing: Balancing quality polish with deadlines and stakeholder requirements."
                ),
            },
            {
                "intent": "related_careers",
                "category": "WHY",
                "priority": "LOW",
                "question": "What careers are closely related to this one?",
                "answer": (
                    f"If you find {title} interesting, you may also want to explore these related pathways:\n\n" +
                    "\n".join([f"• {r.replace('-', ' ').title()}" for r in related[:4]]) +
                    "\n\nThese roles share foundational competencies and offer flexible pivot opportunities."
                ) if related else f"Related roles span adjacent areas in {career.get('field', 'this field')}.",
            },
            # HOW TO BE
            {
                "intent": "learn_first",
                "category": "HOW",
                "priority": "HIGH",
                "question": "What should I learn first?",
                "answer": (
                    f"When starting out in {title}, focus on one clean foundation before trying to learn advanced specializations:\n\n"
                    f"• Step 1 (Weeks 1–3): Master fundamental concepts of {skills[0] if skills else 'core theory'}.\n"
                    f"• Step 2 (Weeks 4–6): Get hands-on with essential industry tools like {tools[0] if tools else 'standard workflow tools'}.\n"
                    "• Step 3 (Weeks 7–8): Build your first small, end-to-end beginner project to cement the workflow.\n\n"
                    "Protecting 1 to 2 focused hours a day will give you noticeable momentum within a couple of months."
                ),
            },
            {
                "intent": "projects",
                "category": "HOW",
                "priority": "HIGH",
                "question": "What kind of projects can I build for my portfolio?",
                "answer": (
                    f"Here are realistic portfolio projects suitable for a {title}:\n\n" +
                    "\n\n".join([f"• {p.get('title', '')} ({p.get('difficulty', '')}): {p.get('description', '')}" for p in projects[:3]]) +
                    "\n\nFocus on finishing 2 to 3 polished projects that solve real problems."
                ) if projects else "Build 2 or 3 small, working projects that solve clear practical problems.",
            },
            {
                "intent": "next_step",
                "category": "HOW",
                "priority": "HIGH",
                "question": "What should I do next to get started?",
                "answer": (
                    f"Here are the 3 most practical next steps you can take today for {title}:\n\n"
                    f"1. Build Your Personalized Roadmap: Add {title} to your TO BE pathway to get milestone-by-milestone guided tasks.\n"
                    f"2. Test in One Afternoon: Build one mini-exercise with {tools[0] if tools else 'core tools'} to see how the work feels.\n"
                    "3. Bookmark Curated Free Resources: Check the Learning Resources section for free, high-quality learning materials."
                ),
            },
            # PRACTICAL MARKET
            {
                "intent": "salary",
                "category": "PRACTICAL",
                "priority": "MEDIUM",
                "question": "What is the entry-level salary benchmark in the Philippines?",
                "answer": (
                    f"Verified compensation benchmarks in the Philippines for {title}:\n\n"
                    f"• Entry-Level: {sal_ph.get('entry_level', '₱25k - ₱45k/mo')}\n"
                    f"• Mid-Level: {sal_ph.get('mid_level', '₱50k - ₱100k/mo')}\n"
                    f"• Senior-Level: {sal_ph.get('senior_level', '₱100k - ₱200k+/mo')}\n\n"
                    f"Source: {sal_ph.get('source', 'Industry Benchmarks')}."
                ) if sal_ph else f"Salary benchmarks for {title} in the Philippines typically start between ₱25,000 and ₱45,000 monthly.",
            },
            {
                "intent": "remote_work",
                "category": "PRACTICAL",
                "priority": "LOW",
                "question": "Can this career be done remotely or freelance?",
                "answer": (
                    f"Yes. {title} is among the most remote-friendly careers in the modern job market.\n\n"
                    "Because work deliverables are digital and team communication happens asynchronously, "
                    "many professionals work for distributed international companies or maintain freelance clients from the Philippines."
                ),
            },
        ]

    def get_initial_questions(self, career: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Get 3 initial questions spanning WHAT, WHY, and HOW."""
        catalog = self.get_catalog(career)
        what = next((q for q in catalog if q["category"] == "WHAT" and q["priority"] == "HIGH"), None)
        why = next((q for q in catalog if q["category"] == "WHY" and q["priority"] == "HIGH"), None)
        how = next((q for q in catalog if q["category"] == "HOW" and q["priority"] == "HIGH"), None)

        selected = [q for q in [what, why, how] if q]
        return selected[:3]

    def get_next_questions(self, career: Dict[str, Any], explored_intents: List[str]) -> List[Dict[str, Any]]:
        """Get next 3 questions based on priority and variety."""
        catalog = self.get_catalog(career)
        unexplored = [q for q in catalog if q["intent"] not in explored_intents]

        if not unexplored:
            return []

        priority_weight = {"HIGH": 3, "MEDIUM": 2, "LOW": 1}
        sorted_qs = sorted(unexplored, key=lambda x: priority_weight.get(x["priority"], 1), reverse=True)

        selected = []
        used_cats = set()

        for q in sorted_qs:
            if q["category"] not in used_cats and len(selected) < 3:
                selected.append(q)
                used_cats.add(q["category"])

        for q in sorted_qs:
            if len(selected) < 3 and q not in selected:
                selected.append(q)

        return selected[:3]

    def generate_answer(self, intent: str, career: Dict[str, Any]) -> str:
        """Retrieve grounded answer for a specific intent."""
        catalog = self.get_catalog(career)
        for item in catalog:
            if item["intent"] == intent:
                return item["answer"]
        return f"For {career.get('title', 'this role')}, focusing on foundational fundamentals and building real projects is the most dependable path forward."

    def check_completion(self, explored_intents: List[str]) -> bool:
        """Check if user has explored enough topics for completion state."""
        return len(explored_intents) >= 5

guided_mentor = GuidedMentorEngine()
