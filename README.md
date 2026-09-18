# TO BE — AI Career Discovery & Roadmap Platform

> **WHAT TO BE. WHY TO BE. HOW TO BE.**  
> *TO BE helps you explore what to be, understand why, and discover how.*

---

## Overview & Product Concept

**TO BE** is a modern, production-ready career discovery platform featuring:
- **Interactive RIASEC Discovery Assessment**: Multi-dimensional interest & skill assessment engine.
- **19+ Real Career Profiles**: Verified Philippine & Global salary benchmarks, day-in-the-life routines, core skills, and learning paths.
- **Concurrent Multi-Pathway Roadmaps**: Step-by-step 4-phase milestone roadmaps with individual progress tracking.
- **TOBE AI Career Mentor & Python Services**: Context-aware AI engine assisting users with career exploration, transitions, and skill pathways.
- **Secure Supabase Authentication**: Google OAuth with Row-Level Security (RLS) ensuring strict multi-tenant data isolation.

---

## Tech Stack & Architecture

- **Backend & AI Services**: Python 3.10+, Gemini LLM Services, RIASEC Assessment Engines
- **Frontend**: React 19, TypeScript, Tailwind CSS v4, Vite 8
- **Database & Auth**: Supabase (PostgreSQL, Row Level Security, Auth triggers)

```
tobe-career-map/
├── src/                    # React 19 + TypeScript + Tailwind CSS Frontend
│   ├── components/         # Reusable UI components
│   ├── context/            # AuthContext & CareerContext (RLS data isolation)
│   ├── data/               # Career data & Assessment questions
│   ├── hooks/              # Interaction & animation hooks
│   ├── lib/                # Supabase client & Google OAuth helpers
│   ├── pages/              # Landing, Home, Discover, Explore, Compare, MyPath, TOBE, Auth
│   ├── App.tsx             # Root router
│   ├── index.css           # Global typography & Tailwind tokens
│   └── main.tsx            # App entrypoint
├── services/               # Python AI Mentor & Assessment Business Logic
│   ├── assessment.py       # RIASEC multi-dimensional calculation
│   ├── career_matching.py  # Career recommendation algorithm
│   ├── mentor_service.py   # Grounded TOBE AI guidance
│   ├── llm_service.py      # LLM provider orchestration
│   └── database.py         # Database services
├── data/                   # Structured career database & question banks
├── supabase/
│   └── migrations/         # PostgreSQL RLS policies & triggers
├── .env.example            # Setup template
├── package.json            # Node dependencies
└── requirements.txt        # Python dependencies
```

---

## Getting Started & Local Development

### 1. Prerequisites
- Node.js 20+ & Python 3.10+
- A free [Supabase](https://supabase.com) project

### 2. Frontend Setup
```bash
npm install
npm run dev
```
Open `http://localhost:8443` in your browser.

---

*created by krsbow*
