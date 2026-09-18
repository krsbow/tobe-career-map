# TO BE — AI Career Discovery & Roadmap Platform

> **WHAT TO BE. WHY TO BE. HOW TO BE.**  
> *TO BE helps you explore what to be, understand why, and discover how.*

---

## Overview & Product Concept

**TO BE** is a modern, production-ready career discovery web application featuring:
- **Interactive RIASEC Discovery Assessment**: Multi-dimensional interest & skill assessment engine.
- **19+ Real Career Profiles**: Verified Philippine & Global salary benchmarks, day-in-the-life routines, core skills, and learning paths.
- **Concurrent Multi-Pathway Roadmaps**: Step-by-step 4-phase milestone roadmaps with individual progress tracking.
- **Secure Supabase Authentication**: Google OAuth with Row-Level Security (RLS) ensuring strict multi-tenant data isolation.
- **TOBE AI Career Mentor**: Context-aware guidance assisting users with career transitions and skill building.

---

## Tech Stack & Architecture

- **Frontend**: React 19, TypeScript, Tailwind CSS v4, Vite 8
- **Database & Auth**: Supabase (PostgreSQL, Row Level Security, Auth triggers)
- **Styling**: Minimalist, warm editorial theme (`Fraunces` + `Instrument Sans`)

```
tobe-career-map/
+-- public/                 # Public static assets & favicon
+-- src/
¦   +-- components/         # Reusable UI components (Nav, AppShell, TOBEWidget)
¦   +-- context/            # AuthContext & CareerContext (RLS data isolation)
¦   +-- data/               # Verified career data & RIASEC assessment questions
¦   +-- hooks/              # Scroll animations & interaction hooks
¦   +-- lib/                # Supabase client & Google OAuth helpers
¦   +-- pages/              # Landing, Home, Discover, Explore, Compare, MyPath, TOBE, Auth
¦   +-- App.tsx             # Root router & layout wrapper
¦   +-- index.css           # Global typography & Tailwind CSS v4 tokens
¦   +-- main.tsx            # Application entrypoint
+-- supabase/
¦   +-- migrations/         # PostgreSQL RLS policies & security triggers
+-- .env.example            # Environment variables template
+-- index.html              # Vite HTML entrypoint
+-- package.json            # Node dependencies & scripts
```

---

## Getting Started & Local Development

### 1. Prerequisites
- Node.js 20+ & pnpm / npm
- A free [Supabase](https://supabase.com) project

### 2. Install Dependencies
```bash
npm install
```

### 3. Configure Environment Variables
Copy `.env.example` to `.env` and fill in your Supabase credentials:
```env
VITE_SUPABASE_URL=https://your-project-id.supabase.co
VITE_SUPABASE_ANON_KEY=your-supabase-anon-key
```

### 4. Run Locally
```bash
npm run dev
```

Open `http://localhost:8443` in your browser.

---

*created by krsbow*
