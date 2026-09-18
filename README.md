# TO BE — AI Career Discovery & Roadmap Platform

> **WHAT TO BE. WHY TO BE. HOW TO BE.**  
> *TO BE helps you explore what to be, understand why, and discover how.*

---

## Overview & Product Concept

**TO BE** is a modular, production-ready full-stack web application designed for anyone exploring career directions—including high school students, university undergraduates, career changers, and working professionals.

### The Core Philosophy
Traditional career tools often make rigid claims like *"Find your one true career"* or *"AI will choose your destiny."* **TO BE is built on the opposite foundation: exploration over prediction.**

1. **WHAT TO BE — Explore Your Possibilities:**  
   Discover career domains connecting to your interests, strengths, and goals without being pigeonholed.
2. **WHY TO BE — Understand Your Options:**  
   Understand *why* particular careers align with your RIASEC profile and work styles, inspect realistic day-to-day responsibilities, and compare alternatives side-by-side.
3. **HOW TO BE — Build Your Direction:**  
   Turn chosen career paths into personalized, interactive 5-phase roadmaps with curated free/low-cost learning resources, practical portfolio projects, and persistent progress tracking.

### TOBE — The Conversational Career Companion
**TOBE** is the AI mentor within the platform. Rather than making prescriptive decisions, TOBE acts as an empathetic, grounded counselor helping you think through trade-offs, explore day-to-day realities, identify skill milestones, and navigate career uncertainty.

---

## Architecture & Project Structure

```
to be/
│
├── .streamlit/
│   ├── config.toml                 # Modern UI styling & server configuration
│   └── secrets.toml.example        # Configuration template for Supabase & LLM API keys
│
├── config.py                       # Central branding, RIASEC dimensions & theme constants
├── app.py                          # Main router & top navigation bar controller
│
├── views/                          # Modular page views
│   ├── home.py                     # Landing experience & Active Roadmap dashboard
│   ├── discover.py                 # Conversational RIASEC assessment & explainable results
│   ├── explore.py                  # Filterable career catalog & comprehensive detail views
│   ├── compare.py                  # Side-by-side career comparison matrix
│   ├── my_path.py                  # Interactive roadmap tracker & review flow
│   ├── mentor.py                   # TOBE AI Career Companion chat
│   └── profile.py                  # Assessment history, profile settings & account deletion
│
├── components/                     # Reusable UI widgets & Vector Icons
│   ├── icons.py                    # Lightweight SVG UI icon library (zero emojis)
│   ├── theme.py                    # Duolingo-inspired friendly CSS styling engine & footer tag
│   ├── navbar.py                   # Header with TO BE wordmark & user session pill
│   ├── career_card.py              # Career cards with alignment badges & reasons
│   ├── career_profile.py           # RIASEC polar/radar chart & strengths display
│   ├── assessment_ui.py            # Multi-step conversational assessment wizard
│   ├── roadmap_ui.py               # Interactive phase tracker with status toggles
│   └── mentor_ui.py                # Grounded chat interface with prompt starters
│
├── services/                       # Decoupled business logic layer
│   ├── auth.py                     # Supabase Auth + Guest / Demo Mode fallback
│   ├── database.py                 # Supabase PostgreSQL client + local persistent fallback
│   ├── assessment.py               # Multi-dimensional RIASEC calculation engine
│   ├── career_matching.py          # Explainable matching logic (Non-exclusion principle)
│   ├── career_service.py           # Catalog search, category filters & comparisons
│   ├── roadmap_service.py          # 5-phase personalized pathway generator
│   ├── mentor_service.py           # TOBE grounding engine & prompt orchestrator
│   └── llm_service.py              # Multi-provider LLM abstraction (Gemini, Groq, Fallback)
│
├── data/                           # Curated knowledge base
│   ├── assessment_questions.py     # Question bank (Interests, Preferences, Skills, Priorities)
│   └── seed_data.py                # 20+ structured careers with PH/Global salaries & curated resources
│
├── utils/                          # Common utilities
│   ├── formatting.py               # Currency, dates, and status formatting
│   ├── validation.py               # Input sanitization and LLM JSON schema parsers
│   └── security.py                 # PII scrubbing & privacy safeguards
│
├── supabase/
│   ├── migrations/
│   │   └── 01_initial_schema.sql   # PostgreSQL schema with UUIDs, RLS policies & indexes
│   └── seed.sql                    # Initial SQL seed data for categories & careers
│
├── requirements.txt                # Python package dependencies
└── README.md                       # Documentation
```

---

## Getting Started & Local Development

### 1. Prerequisites
- Python 3.10+
- (Optional) A free [Supabase](https://supabase.com) project
- (Optional) A [Google Gemini API Key](https://aistudio.google.com/) or Groq API Key

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run Locally
```bash
python -m streamlit run app.py
```

---
*created by krsbow*
