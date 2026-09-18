-- TO BE Platform: Supabase PostgreSQL Initial Migration
-- Production-ready schema with UUIDs, foreign keys, RLS security policies, and performance indexes.

-- Enable UUID extension
create extension if not exists "uuid-ossp";

-- 1. PROFILES TABLE
create table if not exists public.profiles (
    id uuid primary key references auth.users(id) on delete cascade,
    preferred_name text,
    age_group text,
    education_level text,
    field_of_interest text,
    target_income_currency text default 'PHP',
    target_income_amount numeric,
    geographic_preference text default 'Philippines / Remote',
    terms_accepted boolean default false,
    terms_accepted_at timestamp with time zone,
    ai_consent boolean default false,
    created_at timestamp with time zone default timezone('utc'::text, now()) not null,
    updated_at timestamp with time zone default timezone('utc'::text, now()) not null
);

-- 2. CAREER CATEGORIES TABLE
create table if not exists public.career_categories (
    id text primary key,
    name text not null,
    icon text,
    created_at timestamp with time zone default timezone('utc'::text, now()) not null
);

-- 3. CAREERS KNOWLEDGE BASE TABLE
create table if not exists public.careers (
    id text primary key,
    title text not null,
    field text not null,
    category_id text references public.career_categories(id) on delete set null,
    tagline text,
    description text not null,
    responsibilities jsonb default '[]'::jsonb,
    riasec_traits jsonb default '[]'::jsonb,
    work_style text,
    core_skills jsonb default '[]'::jsonb,
    optional_skills jsonb default '[]'::jsonb,
    common_tools jsonb default '[]'::jsonb,
    education_paths jsonb default '[]'::jsonb,
    certifications jsonb default '[]'::jsonb,
    portfolio_projects jsonb default '[]'::jsonb,
    salary_data jsonb default '{}'::jsonb,
    learning_resources jsonb default '[]'::jsonb,
    related_careers jsonb default '[]'::jsonb,
    sources jsonb default '[]'::jsonb,
    last_updated text,
    created_at timestamp with time zone default timezone('utc'::text, now()) not null
);

-- 4. ASSESSMENTS TABLE
create table if not exists public.assessments (
    id uuid primary key default uuid_generate_v4(),
    user_id uuid references public.profiles(id) on delete cascade not null,
    version text default '1.0.0' not null,
    created_at timestamp with time zone default timezone('utc'::text, now()) not null,
    updated_at timestamp with time zone default timezone('utc'::text, now()) not null
);

-- 5. ASSESSMENT RESPONSES TABLE
create table if not exists public.assessment_responses (
    id uuid primary key default uuid_generate_v4(),
    assessment_id uuid references public.assessments(id) on delete cascade not null,
    question_id text not null,
    response_data jsonb not null,
    created_at timestamp with time zone default timezone('utc'::text, now()) not null
);

-- 6. ASSESSMENT RESULTS TABLE
create table if not exists public.assessment_results (
    id uuid primary key default uuid_generate_v4(),
    assessment_id uuid references public.assessments(id) on delete cascade not null,
    user_id uuid references public.profiles(id) on delete cascade not null,
    riasec_scores jsonb not null,
    strengths jsonb default '[]'::jsonb,
    work_preferences jsonb default '[]'::jsonb,
    career_priorities jsonb default '[]'::jsonb,
    current_skills jsonb default '[]'::jsonb,
    matched_careers jsonb default '[]'::jsonb,
    is_current boolean default true,
    created_at timestamp with time zone default timezone('utc'::text, now()) not null
);

-- 7. USER CAREER SELECTIONS TABLE
create table if not exists public.user_career_selections (
    id uuid primary key default uuid_generate_v4(),
    user_id uuid references public.profiles(id) on delete cascade not null,
    career_id text references public.careers(id) on delete cascade not null,
    is_current boolean default true,
    selected_at timestamp with time zone default timezone('utc'::text, now()) not null,
    created_at timestamp with time zone default timezone('utc'::text, now()) not null
);

-- 8. ROADMAPS TABLE
create table if not exists public.roadmaps (
    id uuid primary key default uuid_generate_v4(),
    user_id uuid references public.profiles(id) on delete cascade not null,
    career_id text references public.careers(id) on delete cascade not null,
    title text not null,
    description text,
    status text default 'active' check (status in ('active', 'paused', 'completed', 'archived')),
    is_active boolean default true,
    created_at timestamp with time zone default timezone('utc'::text, now()) not null,
    updated_at timestamp with time zone default timezone('utc'::text, now()) not null
);

-- 9. ROADMAP PHASES TABLE
create table if not exists public.roadmap_phases (
    id uuid primary key default uuid_generate_v4(),
    roadmap_id uuid references public.roadmaps(id) on delete cascade not null,
    title text not null,
    description text,
    order_index integer not null,
    created_at timestamp with time zone default timezone('utc'::text, now()) not null,
    updated_at timestamp with time zone default timezone('utc'::text, now()) not null
);

-- 10. ROADMAP ITEMS TABLE
create table if not exists public.roadmap_items (
    id uuid primary key default uuid_generate_v4(),
    roadmap_id uuid references public.roadmaps(id) on delete cascade not null,
    phase_id uuid references public.roadmap_phases(id) on delete cascade not null,
    title text not null,
    description text,
    type text default 'skill' check (type in ('skill', 'course', 'certification', 'project', 'portfolio', 'career_preparation', 'custom')),
    order_index integer not null,
    status text default 'not_started' check (status in ('not_started', 'in_progress', 'completed')),
    is_user_created boolean default false,
    estimated_effort text,
    resources jsonb default '[]'::jsonb,
    completed_at timestamp with time zone,
    created_at timestamp with time zone default timezone('utc'::text, now()) not null,
    updated_at timestamp with time zone default timezone('utc'::text, now()) not null
);

-- 11. CHAT SESSIONS (TOBE AI MENTOR) TABLE
create table if not exists public.chat_sessions (
    id uuid primary key default uuid_generate_v4(),
    user_id uuid references public.profiles(id) on delete cascade not null,
    title text default 'Career Guidance Session',
    career_id text references public.careers(id) on delete set null,
    created_at timestamp with time zone default timezone('utc'::text, now()) not null,
    updated_at timestamp with time zone default timezone('utc'::text, now()) not null
);

-- 12. CHAT MESSAGES TABLE
create table if not exists public.chat_messages (
    id uuid primary key default uuid_generate_v4(),
    session_id uuid references public.chat_sessions(id) on delete cascade not null,
    role text not null check (role in ('user', 'assistant', 'system')),
    content text not null,
    created_at timestamp with time zone default timezone('utc'::text, now()) not null
);

-- ==========================================================
-- INDEXES FOR PERFORMANCE
-- ==========================================================
create index if not exists idx_assessments_user_id on public.assessments(user_id);
create index if not exists idx_assessment_results_user_id on public.assessment_results(user_id);
create index if not exists idx_user_career_selections_user on public.user_career_selections(user_id);
create index if not exists idx_roadmaps_user_id on public.roadmaps(user_id);
create index if not exists idx_roadmap_items_roadmap_id on public.roadmap_items(roadmap_id);
create index if not exists idx_roadmap_items_phase_id on public.roadmap_items(phase_id);
create index if not exists idx_chat_messages_session_id on public.chat_messages(session_id);

-- ==========================================================
-- ROW LEVEL SECURITY (RLS) POLICIES
-- ==========================================================
-- Enable RLS on all tables
alter table public.profiles enable row level security;
alter table public.career_categories enable row level security;
alter table public.careers enable row level security;
alter table public.assessments enable row level security;
alter table public.assessment_responses enable row level security;
alter table public.assessment_results enable row level security;
alter table public.user_career_selections enable row level security;
alter table public.roadmaps enable row level security;
alter table public.roadmap_phases enable row level security;
alter table public.roadmap_items enable row level security;
alter table public.chat_sessions enable row level security;
alter table public.chat_messages enable row level security;

-- Public read policies for knowledge catalog
create policy "Allow public read access to career_categories" on public.career_categories for select using (true);
create policy "Allow public read access to careers" on public.careers for select using (true);

-- User-scoped policies for profiles
create policy "Users can view own profile" on public.profiles for select using (auth.uid() = id);
create policy "Users can insert own profile" on public.profiles for insert with check (auth.uid() = id);
create policy "Users can update own profile" on public.profiles for update using (auth.uid() = id);
create policy "Users can delete own profile" on public.profiles for delete using (auth.uid() = id);

-- User-scoped policies for assessments
create policy "Users can view own assessments" on public.assessments for select using (auth.uid() = user_id);
create policy "Users can insert own assessments" on public.assessments for insert with check (auth.uid() = user_id);
create policy "Users can update own assessments" on public.assessments for update using (auth.uid() = user_id);
create policy "Users can delete own assessments" on public.assessments for delete using (auth.uid() = user_id);

-- User-scoped policies for assessment responses
create policy "Users can view own assessment responses" on public.assessment_responses for select
using (exists (select 1 from public.assessments where assessments.id = assessment_responses.assessment_id and assessments.user_id = auth.uid()));
create policy "Users can insert own assessment responses" on public.assessment_responses for insert
with check (exists (select 1 from public.assessments where assessments.id = assessment_responses.assessment_id and assessments.user_id = auth.uid()));

-- User-scoped policies for assessment results
create policy "Users can view own assessment results" on public.assessment_results for select using (auth.uid() = user_id);
create policy "Users can insert own assessment results" on public.assessment_results for insert with check (auth.uid() = user_id);
create policy "Users can update own assessment results" on public.assessment_results for update using (auth.uid() = user_id);

-- User-scoped policies for career selections
create policy "Users can view own career selections" on public.user_career_selections for select using (auth.uid() = user_id);
create policy "Users can insert own career selections" on public.user_career_selections for insert with check (auth.uid() = user_id);
create policy "Users can update own career selections" on public.user_career_selections for update using (auth.uid() = user_id);
create policy "Users can delete own career selections" on public.user_career_selections for delete using (auth.uid() = user_id);

-- User-scoped policies for roadmaps
create policy "Users can view own roadmaps" on public.roadmaps for select using (auth.uid() = user_id);
create policy "Users can insert own roadmaps" on public.roadmaps for insert with check (auth.uid() = user_id);
create policy "Users can update own roadmaps" on public.roadmaps for update using (auth.uid() = user_id);
create policy "Users can delete own roadmaps" on public.roadmaps for delete using (auth.uid() = user_id);

-- User-scoped policies for roadmap phases
create policy "Users can view own roadmap phases" on public.roadmap_phases for select
using (exists (select 1 from public.roadmaps where roadmaps.id = roadmap_phases.roadmap_id and roadmaps.user_id = auth.uid()));
create policy "Users can insert own roadmap phases" on public.roadmap_phases for insert
with check (exists (select 1 from public.roadmaps where roadmaps.id = roadmap_phases.roadmap_id and roadmaps.user_id = auth.uid()));
create policy "Users can update own roadmap phases" on public.roadmap_phases for update
using (exists (select 1 from public.roadmaps where roadmaps.id = roadmap_phases.roadmap_id and roadmaps.user_id = auth.uid()));
create policy "Users can delete own roadmap phases" on public.roadmap_phases for delete
using (exists (select 1 from public.roadmaps where roadmaps.id = roadmap_phases.roadmap_id and roadmaps.user_id = auth.uid()));

-- User-scoped policies for roadmap items
create policy "Users can view own roadmap items" on public.roadmap_items for select
using (exists (select 1 from public.roadmaps where roadmaps.id = roadmap_items.roadmap_id and roadmaps.user_id = auth.uid()));
create policy "Users can insert own roadmap items" on public.roadmap_items for insert
with check (exists (select 1 from public.roadmaps where roadmaps.id = roadmap_items.roadmap_id and roadmaps.user_id = auth.uid()));
create policy "Users can update own roadmap items" on public.roadmap_items for update
using (exists (select 1 from public.roadmaps where roadmaps.id = roadmap_items.roadmap_id and roadmaps.user_id = auth.uid()));
create policy "Users can delete own roadmap items" on public.roadmap_items for delete
using (exists (select 1 from public.roadmaps where roadmaps.id = roadmap_items.roadmap_id and roadmaps.user_id = auth.uid()));

-- User-scoped policies for chat sessions and messages
create policy "Users can view own chat sessions" on public.chat_sessions for select using (auth.uid() = user_id);
create policy "Users can insert own chat sessions" on public.chat_sessions for insert with check (auth.uid() = user_id);
create policy "Users can delete own chat sessions" on public.chat_sessions for delete using (auth.uid() = user_id);

create policy "Users can view own chat messages" on public.chat_messages for select
using (exists (select 1 from public.chat_sessions where chat_sessions.id = chat_messages.session_id and chat_sessions.user_id = auth.uid()));
create policy "Users can insert own chat messages" on public.chat_messages for insert
with check (exists (select 1 from public.chat_sessions where chat_sessions.id = chat_messages.session_id and chat_sessions.user_id = auth.uid()));
