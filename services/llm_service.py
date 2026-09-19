"""
Configurable LLM provider abstraction for TO BE platform.
Supports Google Gemini, Groq, and resilient structured fallback templates.
Enforces zero markdown bold syntax (no **) in responses.
"""

import os
import re
import json
import logging
from typing import Dict, Any, Optional, List
import streamlit as st
from utils.security import scrub_pii_for_ai
from utils.validation import parse_and_validate_json_response

logger = logging.getLogger(__name__)

def clean_no_bold(text: str) -> str:
    """Strip markdown bold syntax (**) to ensure clean natural writing."""
    if not text:
        return ""
    cleaned = re.sub(r'\*\*(.*?)\*\*', r'\1', text)
    cleaned = re.sub(r'__(.*?)__', r'\1', cleaned)
    return cleaned.strip()

def get_secret(key: str, default: Any = None) -> Any:
    """Retrieve configuration from Streamlit secrets or OS environment."""
    try:
        if hasattr(st, "secrets") and key in st.secrets:
            return st.secrets[key]
    except Exception:
        pass
    return os.environ.get(key, default)

class LLMService:
    def __init__(self):
        self.provider = get_secret("LLM_PROVIDER", "gemini").lower()
        self.gemini_key = get_secret("GEMINI_API_KEY", "")
        self.groq_key = get_secret("GROQ_API_KEY", "")
        self.openai_key = get_secret("OPENAI_API_KEY", "")

    def generate_text(self, system_prompt: str, user_prompt: str, temperature: float = 0.7) -> str:
        """Generate conversational or analytical text with automatic graceful fallback."""
        # Try Gemini
        if self.gemini_key and (self.provider == "gemini" or not self.provider):
            try:
                import google.generativeai as genai
                genai.configure(api_key=self.gemini_key)
                model = genai.GenerativeModel(
                    model_name="gemini-1.5-flash",
                    system_instruction=system_prompt
                )
                response = model.generate_content(
                    user_prompt,
                    generation_config=genai.types.GenerationConfig(temperature=temperature)
                )
                if response and response.text:
                    return clean_no_bold(response.text.strip())
            except Exception as e:
                logger.warning(f"Gemini API call failed: {e}. Falling back to conversational engine.")

        # Conversational fallback for mentor
        return clean_no_bold(self._fallback_mentor_response(user_prompt))

    def generate_structured_json(self, system_prompt: str, user_prompt: str, expected_keys: Optional[List[str]] = None) -> Optional[Dict[str, Any]]:
        """Generate structured JSON and validate against expected schema."""
        raw_text = self.generate_text(system_prompt, user_prompt, temperature=0.3)
        parsed = parse_and_validate_json_response(raw_text, expected_keys=expected_keys)
        return parsed

    def _fallback_mentor_response(self, user_prompt: str) -> str:
        """Supportive, natural conversational fallback for TOBE AI mentor without markdown bold."""
        # Extract latest message from prompt to determine primary intent
        parts = user_prompt.split("User:")
        latest_query = parts[-1].split("TOBE:")[0].lower().strip() if parts else user_prompt.lower().strip()
        history_context = user_prompt.lower()

        # 1. Need to be good at design / Design requirements
        if any(w in latest_query for w in ["good at design", "need design", "know design", "design skills", "need to be good at design", "require design"]):
            return (
                "Not necessarily. If you are exploring UI/UX design or web development, having a good eye for layout, hierarchy, spacing, and how people interact with an interface is useful, but those skills are learned through practice rather than innate talent.\n\n"
                "You do not need fine art skills or natural graphic design genius to start. What matters most is learning core usability principles and understanding why certain interfaces feel easy or confusing to users. Everything from color harmony to spacing systems can be learned step by step with modern design guidelines."
            )

        # 2. Drawing ability
        if any(w in latest_query for w in ["drawing", "draw", "sketching", "artistic", "illustration"]):
            return (
                "You do not need drawing or sketching skills for UI/UX design, software development, or digital technology careers.\n\n"
                "UI/UX design is about digital usability, layout hierarchy, component structure, and user flows in tools like Figma, which rely on geometric frames, typography, and standard UI elements rather than freehand illustration. Developers and analysts similarly focus on logic, architecture, and code.\n\n"
                "Unless you are specifically pursuing digital illustration, concept art, or animation, a lack of drawing ability will not hold you back at all."
            )

        # 3. Imposter syndrome, self-doubt & intelligence concerns
        if any(w in latest_query for w in ["good enough", "smart enough", "not smart", "scared", "afraid", "fear", "intimidated", "imposter", "doubt", "can i really", "not capable", "stupid", "fail"]):
            return (
                "That self-doubt is very common, especially when stepping into a new field where everyone else seems experienced. But capability in any career is built on consistency and patience with errors, not inborn brilliance.\n\n"
                "Experienced practitioners did not start out knowing everything; they accumulated pattern recognition over time. When you see someone build complex systems easily, you are seeing years of practice, not superior intellect.\n\n"
                "If you focus on completing one small exercise at a time and give yourself permission to be a beginner, your confidence and skills will grow naturally."
            )

        # 4. Uncertainty about career fit
        if (
            any(w in latest_query for w in ["lost", "unsure", "hesitant", "confused", "second guess", "second thoughts"]) or
            ("not sure" in latest_query and any(w in latest_query for w in ["like", "want", "fit", "right", "good", "career", "this"])) or
            ("know" in latest_query and any(w in latest_query for w in ["like", "want", "fit", "choose", "what i", "this", "career"]) and any(w in latest_query for w in ["dont", "don't", "do not", "not", "no idea"]))
        ):
            return (
                "It is completely okay to feel uncertain. The best way to find out isn't by committing to a massive roadmap or overthinking it—it is by doing a tiny, low-stakes sample of the actual work.\n\n"
                "Spend an afternoon building one mini-project (such as a 3-screen Figma layout, a simple interactive web page, or a basic spreadsheet query) and observe how the problem-solving rhythm feels to you.\n\n"
                "If the work feels draining rather than engaging, that is valuable insight that helps narrow down what genuinely fits you. Exploration is about discovery, not forced commitment."
            )

        # 5. Time constraints & schedule ("only have 2 hours", "have school", "busy")
        if any(w in latest_query for w in ["two hours", "2 hours", "1 hour", "limited time", "have school", "in college", "working full", "busy", "how much time", "balance", "schedule"]):
            return (
                "Two hours a day is actually plenty of time to make meaningful progress without burning out alongside school. In fact, consistent 1 to 2 hour daily sessions are much better for long-term retention than cramming on weekends.\n\n"
                "Here is a practical way to structure your two hours to make steady progress without burning out:\n\n"
                "• First 45 minutes: Learn one focused concept (read documentation or follow a guided tutorial).\n"
                "• Next 60–75 minutes: Build something hands-on with that concept immediately (write code, build a component, or test queries).\n\n"
                "If you protect those two hours 4 to 5 days a week, you will build genuine competence within 2 to 3 months while keeping your schoolwork on track."
            )

        # 6. Changing mind / Switching later
        if any(w in latest_query for w in ["change my mind", "switch later", "wrong path", "wrong career", "change direction", "change career", "regret"]):
            return (
                "Changing your mind is completely normal, and it is a healthy part of discovering what you actually enjoy.\n\n"
                "Exploring a career path is not a permanent contract; it is a low-risk experiment. The fundamental skills you build along the way are highly transferable:\n\n"
                "• Logical thinking and structured problem-solving apply across development, product management, data, and operations.\n"
                "• Digital tool literacy and technical communication make you stronger in almost any modern workplace.\n"
                "• Understanding how software or digital products are built gives you an edge even if you pivot to design, marketing, or management.\n\n"
                "If you explore a direction for a few weeks and decide it is not for you, you will walk away with valuable practical skills and much clearer insight into what you want next."
            )

        # 7. Follow-ups (e.g. what should I learn first? / how to start?)
        if any(w in latest_query for w in ["what should i learn first", "where should i start", "how do i start", "where do i start", "first step", "what to learn first", "what to do first", "what next", "where to begin"]):
            if any(w in latest_query for w in ["design", "ux", "ui"]) or (any(w in history_context for w in ["design", "ux", "ui"]) and not any(w in latest_query for w in ["program", "code"])):
                return (
                    "Start with Figma fundamentals—specifically frames, Auto-layout, basic components, and typography hierarchy.\n\n"
                    "Once comfortable with the tool, study basic usability heuristics (such as Nielsen Norman Group principles) and practice by recreating 2 or 3 screens of an existing app you use daily to build visual intuition."
                )
            if any(w in latest_query for w in ["data", "analyst"]) or any(w in history_context for w in ["data", "analyst"]):
                return (
                    "Start with advanced spreadsheets (Excel/Google Sheets formulas and Pivot Tables) for data cleaning, then learn SQL fundamentals (SELECT, WHERE, JOINs, GROUP BY) to query databases.\n\n"
                    "Once you have the basics down, practice building interactive dashboards in Power BI or Tableau using public datasets."
                )
            return (
                "When starting out in programming, focus on one clean foundation before trying to learn complex frameworks:\n\n"
                "• Step 1: HTML and Modern CSS (2–3 weeks) — learn how web pages are structured and styled with Flexbox and responsive layouts.\n"
                "• Step 2: JavaScript Fundamentals (3–4 weeks) — master variables, loops, functions, array methods, and manipulating the browser DOM.\n"
                "• Step 3: Git and Version Control (1 week) — learn how to track your code and push projects to GitHub.\n\n"
                "Platforms like freeCodeCamp and The Odin Project provide structured, hands-on lessons to guide each step with real mini-projects."
            )

        # 8. Difficulty questions (e.g. is it easy / hard to be a programmer?)
        if any(w in latest_query for w in ["easy", "hard", "difficult", "tough", "struggle", "can i still"]):
            if any(w in latest_query for w in ["ux", "design", "ui"]) or (any(w in history_context for w in ["design", "ux"]) and not any(w in latest_query for w in ["program", "code"])):
                return (
                    "UI/UX design is very approachable for beginners because it is rooted in human empathy and clear communication rather than heavy technical prerequisites.\n\n"
                    "The challenging part is developing an eye for layout hierarchy, visual rhythm, and understanding what frustrates users when they interact with a product. You do not need fine art drawing skills; you need curiosity about how people think and use apps.\n\n"
                    "If you start with Figma and practice redesigning screens from apps you use every day, you can build a strong portfolio foundation in a few months."
                )
            elif any(w in latest_query for w in ["data", "analyst"]) or any(w in history_context for w in ["data", "analyst"]):
                return (
                    "Data analytics is accessible to beginners, especially if you enjoy asking questions, finding patterns, and organizing information.\n\n"
                    "The initial learning curve centers on SQL for querying databases and tools like Excel, Power BI, or Python for summarizing findings. You do not need advanced mathematical statistics to start in junior data roles; clear arithmetic, curiosity, and good communication will take you a long way."
                )
            return (
                "Learning to program is challenging at first, but it is entirely learnable with consistent practice.\n\n"
                "What makes it feel difficult early on is getting used to the precision required. Computers execute exactly what you write, so syntax errors and unexpected bugs can feel frustrating in the first few weeks.\n\n"
                "What makes it manageable is that you do not need to memorize every command or be a math genius. Programming is mostly about breaking down larger problems into small, logical steps and getting comfortable reading documentation.\n\n"
                "If you spend 45 to 60 minutes a day building small, practical exercises, the core concepts will begin clicking within 3 to 4 weeks."
            )

        # 9. Degree vs Portfolio vs Self-Taught
        if any(w in latest_query for w in ["degree", "college", "university", "diploma", "certificate", "self-taught", "self taught"]):
            if any(w in latest_query for w in ["nurse", "engineer", "cpa"]) or any(w in history_context for w in ["nurse", "nursing", "engineer", "civil", "cpa", "accountant"]):
                return (
                    "For regulated professions like Nursing, Civil Engineering, or CPA Accounting, an accredited bachelor's degree and passing the official PRC Board Licensure Examination are required by Philippine law.\n\n"
                    "Unlike purely digital careers, licensed professions require formal clinical hours or accredited engineering units to practice legally. Supplemental certifications give you a strong edge."
                )
            return (
                "In software development, UI/UX design, and digital operations, a degree is rarely a strict requirement if you have demonstrable proof of work.\n\n"
                "Hiring managers in tech prioritize:\n"
                "• A clean portfolio showing live, working projects that solve real problems.\n"
                "• A clear understanding of core tools, clean code practices, and problem-solving.\n"
                "• Strong communication and the ability to explain your thought process.\n\n"
                "While a degree can help with university recruitment fairs, self-taught developers and career changers regularly land junior roles by showcasing their GitHub repositories and personal projects."
            )

        # 10. Normal Workday / Daily Routine
        if any(w in latest_query for w in ["workday", "work day", "day look like", "daily routine", "day in the life", "typical day"]):
            if any(w in latest_query for w in ["civil", "construction"]) or any(w in history_context for w in ["civil", "construction"]):
                return (
                    "A civil engineer's workday usually splits between field site inspections and office technical work:\n\n"
                    "• Site Visits: Checking construction quality, verifying structural tolerances, and coordinating with foremen and contractors.\n"
                    "• Office Design & Analysis: Reviewing structural calculations, checking CAD drawings, and preparing cost estimates and compliance permits."
                )
            return (
                "In digital, design, and software roles, a typical workday revolves around a healthy split between focused building and team coordination:\n\n"
                "• Morning (30–45 mins): A quick team sync (standup) to align on current tasks, review pull requests or design feedback, and plan the day.\n"
                "• Core Focus Block (2–4 hours): Deep, uninterrupted work time—writing code, building Figma prototypes, conducting user research, or analyzing queries.\n"
                "• Afternoon (1–2 hours): Cross-functional collaboration with product managers, QA testers, or developers to refine features and document solutions.\n\n"
                "Most teams prioritize written, asynchronous communication so you have quiet time to actually solve problems."
            )

        # 11. Shy / Introvert
        if any(w in latest_query for w in ["shy", "introvert", "quiet", "social anxiety"]):
            return (
                "Not at all. Many successful software engineers, UI/UX designers, data analysts, and technical writers are introverts.\n\n"
                "These fields reward deep concentration, thoughtful analysis, and clear written communication. Most daily interactions happen asynchronously in team chat channels, design comments, and pull request reviews rather than high-pressure public speaking or constant meetings.\n\n"
                "As long as you are willing to ask for clarification when you are blocked and communicate clearly in writing, being shy or introverted is completely fine."
            )

        # 12. Math / Background concerns
        if any(w in latest_query for w in ["math", "bad at math", "no experience", "no background", "not good at math"]):
            return (
                "You do not need advanced mathematics for the vast majority of software development, UX design, or business technology roles.\n\n"
                "Everyday programming involves basic arithmetic, logic, and organizational thinking (like understanding conditions and lists) rather than calculus or complex formulas. Unless you choose to specialize in 3D game engines, cryptography, or deep machine learning research, standard algebra and logical problem-solving are plenty.\n\n"
                "Persistence when troubleshooting and the patience to read error messages calmly matter much more than mathematical prowess."
            )

        # 13. Role comparisons (e.g. UX vs Frontend, Frontend vs Backend, UI vs UX, Certificate vs Degree)
        if any(w in latest_query for w in ["difference", "vs", "compare"]):
            if any(w in latest_query for w in ["ux", "design"]) and any(w in latest_query for w in ["frontend", "front-end"]):
                return (
                    "The main distinction between UX Design and Front-End Development comes down to what part of the creation process you enjoy most:\n\n"
                    "• UX Designer (The Architect & Researcher): Focuses on user research, wireframes, user testing, and visual design in Figma.\n"
                    "• Front-End Developer (The Builder): Takes those Figma designs and translates them into real, interactive, responsive code using HTML, CSS, JavaScript, and React."
                )
            if any(w in latest_query for w in ["frontend", "front-end"]) and any(w in latest_query for w in ["backend", "back-end"]):
                return (
                    "The difference between Front-End and Back-End development:\n\n"
                    "• Front-End: What users interact with directly in the browser (HTML, CSS, JavaScript, React).\n"
                    "• Back-End: The behind-the-scenes engine managing databases, user authentication, APIs, and business logic (Node.js, Python, PostgreSQL)."
                )
            if any(w in latest_query for w in ["certificate", "certification"]) and any(w in latest_query for w in ["degree", "college"]):
                return (
                    "Certificates versus degrees:\n\n"
                    "• Certificate/Bootcamp: Focuses narrowly on practical, hands-on tool proficiencies over a few weeks or months to build portfolio projects quickly.\n"
                    "• Degree: Provides broad theoretical foundations across 4 years, along with university campus recruiting pipelines."
                )
            if "ui" in latest_query.split() or "ui/ux" in latest_query or ("ui" in latest_query and "ux" in latest_query):
                return (
                    "The difference between UI and UX comes down to the visual interface versus the underlying experience:\n\n"
                    "• UI (User Interface): What users see—colors, typography, button styles, visual layout, and animations.\n"
                    "• UX (User Experience): How the product feels and functions—user research, information architecture, wireframes, and eliminating friction in user journeys."
                )

        # 14. Salary & Earnings
        if any(w in latest_query for w in ["salary", "pay", "earn", "compensation", "make in", "rates"]):
            return (
                "Entry-level salary benchmarks in the Philippines typically range as follows:\n\n"
                "• Junior Software Developers: ₱25,000 – ₱45,000/month (moving to ₱60,000–₱120,000 at mid-level).\n"
                "• Junior UI/UX Designers: ₱28,000 – ₱45,000/month (moving to ₱65,000–₱130,000 at mid-level).\n"
                "• Junior Data Analysts: ₱28,000 – ₱50,000/month.\n"
                "• Global Remote roles for proficient developers and designers regularly range from $1,500 to $4,000+ monthly as you gain practical experience."
            )

        # 15. Family / Parents expectations
        if any(w in latest_query for w in ["parents", "family", "mom", "dad", "support this"]):
            return (
                "It is understandable that parents often prefer traditional paths like accounting, engineering, or nursing because they want financial stability and clear career safety for you.\n\n"
                "The most constructive way to bridge that gap is to show tangible progress rather than just arguing your interest:\n\n"
                "• Share concrete data on tech industry job demand and local starting salary ranges in the Philippines.\n"
                "• Build 1 or 2 working portfolio projects to show that you are taking your preparation seriously.\n"
                "• Keep your communication calm and open, reassuring them that building digital capability is a practical, high-demand investment."
            )

        # 16. Budget laptop / Hardware constraints
        if any(w in latest_query for w in ["budget laptop", "cheap laptop", "pc", "computer", "hardware", "spec"]):
            return (
                "Yes, you can absolutely learn programming and web development on a budget laptop.\n\n"
                "Web technologies (HTML, CSS, JavaScript, Python) and code editors like VS Code require very modest hardware. A basic laptop with an Intel Core i3 or Ryzen 3 processor and 8GB of RAM is more than enough to learn and build real projects.\n\n"
                "Free cloud tools like CodeSandbox, Replit, and GitHub allow you to run and host code without straining your local machine."
            )

        # 17. AI replacing developers
        if any(w in latest_query for w in ["ai", "replace", "artificial intelligence", "copilot", "gpt", "taking over"]):
            return (
                "AI is transforming how developers write code, but it is not replacing the need for skilled problem-solvers.\n\n"
                "AI tools act as powerful accelerators for drafting boilerplate code and suggesting syntax, but they cannot independently understand user business needs, make architectural tradeoffs, debug subtle logic issues, or maintain complex production systems.\n\n"
                "Developers who learn to collaborate effectively with AI tools become significantly faster and more valuable."
            )

        # 18. Free practice platforms
        if any(w in latest_query for w in ["free", "where should i find", "platforms", "resources", "practice project"]):
            return (
                "Here are the most respected free platforms for hands-on project practice:\n\n"
                "• freeCodeCamp: Comprehensive, hands-on curriculum with interactive coding challenges and certifications.\n"
                "• The Odin Project: Full-stack web development curriculum that teaches you to build real local projects from scratch.\n"
                "• Frontend Mentor: Real Figma design specs for building responsive front-end components and landing pages.\n"
                "• Kaggle: Free datasets, tutorials, and guided notebooks for aspiring data analysts."
            )

        # 19. Data analyst tools
        if any(w in latest_query for w in ["tools do data", "data analyst use", "data tools"]):
            return (
                "The core toolkit for a modern data analyst includes:\n\n"
                "• SQL: The most critical tool for querying, filtering, and joining relational database tables.\n"
                "• Advanced Excel / Google Sheets: For quick exploratory data cleaning, pivot tables, and formulas (VLOOKUP/XLOOKUP).\n"
                "• Power BI or Tableau: For building interactive business dashboards and visual reports.\n"
                "• Python (Pandas, Matplotlib): For automated data processing and advanced analytical workflows."
            )

        # 20. Electrician / Trade licensing (TESDA & RME)
        if any(w in latest_query for w in ["electrician", "trade", "rme", "electrical"]):
            return (
                "In the Philippines, commercial electrical work is regulated through TESDA certifications and PRC licensure:\n\n"
                "• TESDA NC II & NC III in Electrical Installation & Maintenance: Essential vocational qualification certifying practical competency.\n"
                "• Registered Master Electrician (RME): Official PRC licensure examination allowing you to legally supervise and certify electrical wiring installations."
            )

        # 21. Overwhelm & Pacing
        if any(w in latest_query for w in ["overwhelm", "too much", "lost in all", "anxious", "information overload"]):
            return (
                "Feeling overwhelmed is completely natural given the huge number of languages, frameworks, and tools talked about online.\n\n"
                "The remedy is radical simplification: ignore advanced frameworks, cloud tools, and hot trends for now. Pick exactly one foundation (like HTML and CSS, or SQL basics) and spend 45 minutes a day building tiny exercises with just that.\n\n"
                "You do not need to learn everything at once; mastery is built one narrow milestone at a time."
            )

        # 22. Switching from Marketing to UI/UX
        if any(w in latest_query for w in ["switch from marketing", "marketing to ui", "marketing to ux"]):
            return (
                "Marketing is one of the strongest backgrounds for transitioning into UI/UX design.\n\n"
                "You already understand user psychology, copywriting, conversion funnels, and customer pain points. The main new skill you need to develop is digital interface mechanics in Figma—learning layout grids, auto-layout, and interactive prototyping.\n\n"
                "Your ability to tie user experience directly to business metrics will make you a very competitive designer."
            )

        # 23. First portfolio project
        if any(w in latest_query for w in ["first portfolio", "first project", "starter project"]):
            return (
                "For your first portfolio project, focus on solving one clear, small problem well rather than building a massive clone:\n\n"
                "• For Developers: Build an interactive task/budget tracker or a weather dashboard with clean responsive design and API data fetching.\n"
                "• For UI/UX Designers: Redesign a 3-to-4 screen flow of a local Philippine app (like a delivery or banking app) addressing specific user friction.\n"
                "• For Data Analysts: Analyze an open public dataset (like Kaggle or government open data) and present key findings in a 2-page interactive dashboard."
            )

        # 24. Age concerns / Switching at 28, 30, 40+
        if any(w in latest_query for w in ["old", "age", "28", "30", "35", "40", "too late"]):
            return (
                "You are definitely not too old. Switching careers in your late twenties, thirties, or beyond is extremely common in technology and design.\n\n"
                "Adult career changers often progress faster than teenagers because you bring professional communication, time management, and real-world domain knowledge to the table.\n\n"
                "Tech hiring is fundamentally merit-based and proof-of-work driven. If your portfolio shows clean projects and solid problem solving, your age is not a barrier."
            )

        # 25. Coding errors & debugging
        if any(w in latest_query for w in ["stuck", "coding error", "error message", "bug", "troubleshoot"]):
            return (
                "Getting stuck on errors is a daily reality for every software engineer, regardless of experience level.\n\n"
                "Here is an effective 4-step debugging routine:\n\n"
                "• Read the exact error line and message carefully—it usually tells you the exact line number and variable causing the issue.\n"
                "• Use console logging (or print statements) to inspect the value of your variables right before the error happens.\n"
                "• Search the specific error message on Stack Overflow or official documentation.\n"
                "• Isolate the problem by commenting out unrelated code until only the broken logic remains."
            )

        # 26. Figma internship prerequisite
        if any(w in latest_query for w in ["figma", "internship", "know figma"]):
            return (
                "Yes, having baseline practical familiarity with Figma is expected before applying for UI/UX internships.\n\n"
                "You do not need to be an advanced design system architect, but you should be comfortable with frames, Auto-layout, basic components, text styles, and creating simple interactive prototypes.\n\n"
                "Spending 1 to 2 weeks completing free Figma tutorials and building 2 sample app screens will give you the baseline confidence you need."
            )

        # 27. Learning timeline (e.g. Learn Python in 2 months)
        if any(w in latest_query for w in ["two months", "2 months", "3 months", "how long does it take"]):
            return (
                "With 1 to 2 hours of focused daily practice, you can build solid practical competence in Python fundamentals within 2 months.\n\n"
                "• Month 1: Variables, data structures (lists, dictionaries), loops, functions, and file handling.\n"
                "• Month 2: Working with libraries (Pandas for data or Requests for APIs) and building 2 small end-to-end scripts or data summaries.\n\n"
                "Two months is enough to become dangerous and build real tools; ongoing project work will deepen your expertise."
            )

        # 28. Job application readiness
        if any(w in latest_query for w in ["ready to apply", "when to apply", "applying for jobs"]):
            return (
                "You are ready to start applying for junior roles when you meet these three practical benchmarks:\n\n"
                "• You have 2 to 3 completed, polished portfolio projects that you built yourself and can explain in detail.\n"
                "• You understand foundational tool workflows (like Git/GitHub for developers or Figma prototyping for designers).\n"
                "• You can explain your problem-solving choices and talk through how you debugged issues.\n\n"
                "You do not need to know everything on a job posting before applying—meeting 60% of listed requirements is plenty."
            )

        # 29. Direct fallback for any other question
        return (
            "Developing proficiency in this area comes down to consistent, hands-on practice with the core tools of the craft.\n\n"
            "Focus on building small, working exercises rather than getting bogged down in abstract theory. As you work through practical problems, the concepts will become intuitive."
        )

# Singleton instance
llm_service = LLMService()
