-- =============================================================================
-- TO BE Career Discovery Platform: Security & RLS Database Migration
-- Enforces strict multi-tenant data isolation using Supabase Auth (auth.uid())
-- Enforces server-side @gmail.com domain validation
-- =============================================================================

-- 1. EXTENSIONS
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- 2. SERVER-SIDE GMAIL VALIDATION TRIGGER ON auth.users
-- Ensures that only @gmail.com email addresses can register or authenticate.
CREATE OR REPLACE FUNCTION public.validate_gmail_domain()
RETURNS TRIGGER
LANGUAGE plpgsql
SECURITY DEFINER
AS $$
BEGIN
  IF NEW.email IS NULL OR LOWER(NEW.email) NOT LIKE '%@gmail.com' THEN
    RAISE EXCEPTION 'Access restricted: Only @gmail.com email accounts are permitted to register on TO BE.';
  END IF;
  RETURN NEW;
END;
$$;

-- Drop trigger if already exists and recreate
DROP TRIGGER IF EXISTS tr_validate_gmail_domain ON auth.users;
CREATE TRIGGER tr_validate_gmail_domain
BEFORE INSERT OR UPDATE OF email ON auth.users
FOR EACH ROW
EXECUTE FUNCTION public.validate_gmail_domain();

-- 3. PROFILES TABLE
CREATE TABLE IF NOT EXISTS public.profiles (
  id UUID PRIMARY KEY REFERENCES auth.users(id) ON DELETE CASCADE,
  email TEXT NOT NULL,
  full_name TEXT,
  avatar_url TEXT,
  preferred_name TEXT,
  terms_accepted BOOLEAN DEFAULT TRUE,
  terms_accepted_at TIMESTAMPTZ DEFAULT NOW(),
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

ALTER TABLE public.profiles ENABLE ROW LEVEL SECURITY;

-- Profile RLS Policies: Authenticated users can only view, insert, update, or delete their own profile
DROP POLICY IF EXISTS "Users can view own profile" ON public.profiles;
CREATE POLICY "Users can view own profile"
  ON public.profiles FOR SELECT
  TO authenticated
  USING (auth.uid() = id);

DROP POLICY IF EXISTS "Users can insert own profile" ON public.profiles;
CREATE POLICY "Users can insert own profile"
  ON public.profiles FOR INSERT
  TO authenticated
  WITH CHECK (auth.uid() = id);

DROP POLICY IF EXISTS "Users can update own profile" ON public.profiles;
CREATE POLICY "Users can update own profile"
  ON public.profiles FOR UPDATE
  TO authenticated
  USING (auth.uid() = id)
  WITH CHECK (auth.uid() = id);

DROP POLICY IF EXISTS "Users can delete own profile" ON public.profiles;
CREATE POLICY "Users can delete own profile"
  ON public.profiles FOR DELETE
  TO authenticated
  USING (auth.uid() = id);

-- 4. AUTOMATIC PROFILE CREATION TRIGGER
CREATE OR REPLACE FUNCTION public.handle_new_user()
RETURNS TRIGGER
LANGUAGE plpgsql
SECURITY DEFINER
SET search_path = public
AS $$
BEGIN
  INSERT INTO public.profiles (id, email, full_name, preferred_name, avatar_url)
  VALUES (
    NEW.id,
    NEW.email,
    COALESCE(NEW.raw_user_meta_data->>'full_name', NEW.raw_user_meta_data->>'name', split_part(NEW.email, '@', 1)),
    COALESCE(NEW.raw_user_meta_data->>'preferred_name', NEW.raw_user_meta_data->>'name', split_part(NEW.email, '@', 1)),
    NEW.raw_user_meta_data->>'avatar_url'
  )
  ON CONFLICT (id) DO UPDATE
  SET
    email = EXCLUDED.email,
    full_name = COALESCE(EXCLUDED.full_name, profiles.full_name),
    updated_at = NOW();
  RETURN NEW;
END;
$$;

DROP TRIGGER IF EXISTS on_auth_user_created ON auth.users;
CREATE TRIGGER on_auth_user_created
AFTER INSERT ON auth.users
FOR EACH ROW
EXECUTE FUNCTION public.handle_new_user();

-- 5. ASSESSMENTS TABLE
CREATE TABLE IF NOT EXISTS public.assessments (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  user_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
  riasec_scores JSONB NOT NULL DEFAULT '{}'::jsonb,
  top_traits TEXT[] NOT NULL DEFAULT '{}',
  selected_skills TEXT[] NOT NULL DEFAULT '{}',
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

ALTER TABLE public.assessments ENABLE ROW LEVEL SECURITY;

DROP POLICY IF EXISTS "Users can view own assessments" ON public.assessments;
CREATE POLICY "Users can view own assessments"
  ON public.assessments FOR SELECT
  TO authenticated
  USING (auth.uid() = user_id);

DROP POLICY IF EXISTS "Users can insert own assessments" ON public.assessments;
CREATE POLICY "Users can insert own assessments"
  ON public.assessments FOR INSERT
  TO authenticated
  WITH CHECK (auth.uid() = user_id);

DROP POLICY IF EXISTS "Users can update own assessments" ON public.assessments;
CREATE POLICY "Users can update own assessments"
  ON public.assessments FOR UPDATE
  TO authenticated
  USING (auth.uid() = user_id)
  WITH CHECK (auth.uid() = user_id);

DROP POLICY IF EXISTS "Users can delete own assessments" ON public.assessments;
CREATE POLICY "Users can delete own assessments"
  ON public.assessments FOR DELETE
  TO authenticated
  USING (auth.uid() = user_id);

-- 6. CAREER MATCHES TABLE
CREATE TABLE IF NOT EXISTS public.career_matches (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  user_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
  career_id TEXT NOT NULL,
  match_score INTEGER NOT NULL,
  breakdown JSONB DEFAULT '{}'::jsonb,
  created_at TIMESTAMPTZ DEFAULT NOW()
);

ALTER TABLE public.career_matches ENABLE ROW LEVEL SECURITY;

DROP POLICY IF EXISTS "Users can view own matches" ON public.career_matches;
CREATE POLICY "Users can view own matches"
  ON public.career_matches FOR SELECT
  TO authenticated
  USING (auth.uid() = user_id);

DROP POLICY IF EXISTS "Users can insert own matches" ON public.career_matches;
CREATE POLICY "Users can insert own matches"
  ON public.career_matches FOR INSERT
  TO authenticated
  WITH CHECK (auth.uid() = user_id);

DROP POLICY IF EXISTS "Users can delete own matches" ON public.career_matches;
CREATE POLICY "Users can delete own matches"
  ON public.career_matches FOR DELETE
  TO authenticated
  USING (auth.uid() = user_id);

-- 7. SAVED CAREERS TABLE
CREATE TABLE IF NOT EXISTS public.saved_careers (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  user_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
  career_id TEXT NOT NULL,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  UNIQUE(user_id, career_id)
);

ALTER TABLE public.saved_careers ENABLE ROW LEVEL SECURITY;

DROP POLICY IF EXISTS "Users can view own saved careers" ON public.saved_careers;
CREATE POLICY "Users can view own saved careers"
  ON public.saved_careers FOR SELECT
  TO authenticated
  USING (auth.uid() = user_id);

DROP POLICY IF EXISTS "Users can insert own saved careers" ON public.saved_careers;
CREATE POLICY "Users can insert own saved careers"
  ON public.saved_careers FOR INSERT
  TO authenticated
  WITH CHECK (auth.uid() = user_id);

DROP POLICY IF EXISTS "Users can delete own saved careers" ON public.saved_careers;
CREATE POLICY "Users can delete own saved careers"
  ON public.saved_careers FOR DELETE
  TO authenticated
  USING (auth.uid() = user_id);

-- 8. RECENTLY VIEWED CAREERS TABLE
CREATE TABLE IF NOT EXISTS public.recent_views (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  user_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
  career_id TEXT NOT NULL,
  viewed_at TIMESTAMPTZ DEFAULT NOW()
);

ALTER TABLE public.recent_views ENABLE ROW LEVEL SECURITY;

DROP POLICY IF EXISTS "Users can view own recent views" ON public.recent_views;
CREATE POLICY "Users can view own recent views"
  ON public.recent_views FOR SELECT
  TO authenticated
  USING (auth.uid() = user_id);

DROP POLICY IF EXISTS "Users can insert own recent views" ON public.recent_views;
CREATE POLICY "Users can insert own recent views"
  ON public.recent_views FOR INSERT
  TO authenticated
  WITH CHECK (auth.uid() = user_id);

DROP POLICY IF EXISTS "Users can delete own recent views" ON public.recent_views;
CREATE POLICY "Users can delete own recent views"
  ON public.recent_views FOR DELETE
  TO authenticated
  USING (auth.uid() = user_id);

-- 9. ROADMAPS TABLE (Parent)
CREATE TABLE IF NOT EXISTS public.roadmaps (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  user_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
  career_id TEXT NOT NULL,
  career_title TEXT NOT NULL,
  status TEXT NOT NULL DEFAULT 'active',
  notes TEXT DEFAULT '',
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

ALTER TABLE public.roadmaps ENABLE ROW LEVEL SECURITY;

DROP POLICY IF EXISTS "Users can view own roadmaps" ON public.roadmaps;
CREATE POLICY "Users can view own roadmaps"
  ON public.roadmaps FOR SELECT
  TO authenticated
  USING (auth.uid() = user_id);

DROP POLICY IF EXISTS "Users can insert own roadmaps" ON public.roadmaps;
CREATE POLICY "Users can insert own roadmaps"
  ON public.roadmaps FOR INSERT
  TO authenticated
  WITH CHECK (auth.uid() = user_id);

DROP POLICY IF EXISTS "Users can update own roadmaps" ON public.roadmaps;
CREATE POLICY "Users can update own roadmaps"
  ON public.roadmaps FOR UPDATE
  TO authenticated
  USING (auth.uid() = user_id)
  WITH CHECK (auth.uid() = user_id);

DROP POLICY IF EXISTS "Users can delete own roadmaps" ON public.roadmaps;
CREATE POLICY "Users can delete own roadmaps"
  ON public.roadmaps FOR DELETE
  TO authenticated
  USING (auth.uid() = user_id);

-- 10. ROADMAP MILESTONES TABLE (Child - Inherited Ownership)
CREATE TABLE IF NOT EXISTS public.roadmap_milestones (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  roadmap_id UUID NOT NULL REFERENCES public.roadmaps(id) ON DELETE CASCADE,
  phase TEXT NOT NULL,
  title TEXT NOT NULL,
  category TEXT NOT NULL DEFAULT 'Foundation',
  status TEXT NOT NULL DEFAULT 'upcoming',
  estimated_weeks TEXT,
  description TEXT,
  tasks JSONB NOT NULL DEFAULT '[]'::jsonb,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

ALTER TABLE public.roadmap_milestones ENABLE ROW LEVEL SECURITY;

-- Inherited RLS: User can only access milestones if they own the parent roadmap
DROP POLICY IF EXISTS "Users can view own roadmap milestones" ON public.roadmap_milestones;
CREATE POLICY "Users can view own roadmap milestones"
  ON public.roadmap_milestones FOR SELECT
  TO authenticated
  USING (
    EXISTS (
      SELECT 1 FROM public.roadmaps
      WHERE public.roadmaps.id = public.roadmap_milestones.roadmap_id
        AND public.roadmaps.user_id = auth.uid()
    )
  );

DROP POLICY IF EXISTS "Users can insert own roadmap milestones" ON public.roadmap_milestones;
CREATE POLICY "Users can insert own roadmap milestones"
  ON public.roadmap_milestones FOR INSERT
  TO authenticated
  WITH CHECK (
    EXISTS (
      SELECT 1 FROM public.roadmaps
      WHERE public.roadmaps.id = public.roadmap_milestones.roadmap_id
        AND public.roadmaps.user_id = auth.uid()
    )
  );

DROP POLICY IF EXISTS "Users can update own roadmap milestones" ON public.roadmap_milestones;
CREATE POLICY "Users can update own roadmap milestones"
  ON public.roadmap_milestones FOR UPDATE
  TO authenticated
  USING (
    EXISTS (
      SELECT 1 FROM public.roadmaps
      WHERE public.roadmaps.id = public.roadmap_milestones.roadmap_id
        AND public.roadmaps.user_id = auth.uid()
    )
  )
  WITH CHECK (
    EXISTS (
      SELECT 1 FROM public.roadmaps
      WHERE public.roadmaps.id = public.roadmap_milestones.roadmap_id
        AND public.roadmaps.user_id = auth.uid()
    )
  );

DROP POLICY IF EXISTS "Users can delete own roadmap milestones" ON public.roadmap_milestones;
CREATE POLICY "Users can delete own roadmap milestones"
  ON public.roadmap_milestones FOR DELETE
  TO authenticated
  USING (
    EXISTS (
      SELECT 1 FROM public.roadmaps
      WHERE public.roadmaps.id = public.roadmap_milestones.roadmap_id
        AND public.roadmaps.user_id = auth.uid()
    )
  );

-- 11. CAREER NOTES TABLE
CREATE TABLE IF NOT EXISTS public.career_notes (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  user_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
  career_id TEXT,
  career_title TEXT,
  title TEXT,
  content TEXT NOT NULL,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

ALTER TABLE public.career_notes ENABLE ROW LEVEL SECURITY;

DROP POLICY IF EXISTS "Users can view own career notes" ON public.career_notes;
CREATE POLICY "Users can view own career notes"
  ON public.career_notes FOR SELECT
  TO authenticated
  USING (auth.uid() = user_id);

DROP POLICY IF EXISTS "Users can insert own career notes" ON public.career_notes;
CREATE POLICY "Users can insert own career notes"
  ON public.career_notes FOR INSERT
  TO authenticated
  WITH CHECK (auth.uid() = user_id);

DROP POLICY IF EXISTS "Users can update own career notes" ON public.career_notes;
CREATE POLICY "Users can update own career notes"
  ON public.career_notes FOR UPDATE
  TO authenticated
  USING (auth.uid() = user_id)
  WITH CHECK (auth.uid() = user_id);

DROP POLICY IF EXISTS "Users can delete own career notes" ON public.career_notes;
CREATE POLICY "Users can delete own career notes"
  ON public.career_notes FOR DELETE
  TO authenticated
  USING (auth.uid() = user_id);

-- 12. CHAT SESSIONS & MESSAGES (AI Mentor TOBE)
CREATE TABLE IF NOT EXISTS public.chat_sessions (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  user_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
  title TEXT DEFAULT 'Conversation with TOBE',
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

ALTER TABLE public.chat_sessions ENABLE ROW LEVEL SECURITY;

DROP POLICY IF EXISTS "Users can view own chat sessions" ON public.chat_sessions;
CREATE POLICY "Users can view own chat sessions"
  ON public.chat_sessions FOR SELECT
  TO authenticated
  USING (auth.uid() = user_id);

DROP POLICY IF EXISTS "Users can insert own chat sessions" ON public.chat_sessions;
CREATE POLICY "Users can insert own chat sessions"
  ON public.chat_sessions FOR INSERT
  TO authenticated
  WITH CHECK (auth.uid() = user_id);

DROP POLICY IF EXISTS "Users can delete own chat sessions" ON public.chat_sessions;
CREATE POLICY "Users can delete own chat sessions"
  ON public.chat_sessions FOR DELETE
  TO authenticated
  USING (auth.uid() = user_id);

CREATE TABLE IF NOT EXISTS public.chat_messages (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  session_id UUID NOT NULL REFERENCES public.chat_sessions(id) ON DELETE CASCADE,
  user_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
  role TEXT NOT NULL CHECK (role IN ('user', 'assistant', 'system')),
  content TEXT NOT NULL,
  created_at TIMESTAMPTZ DEFAULT NOW()
);

ALTER TABLE public.chat_messages ENABLE ROW LEVEL SECURITY;

DROP POLICY IF EXISTS "Users can view own chat messages" ON public.chat_messages;
CREATE POLICY "Users can view own chat messages"
  ON public.chat_messages FOR SELECT
  TO authenticated
  USING (auth.uid() = user_id);

DROP POLICY IF EXISTS "Users can insert own chat messages" ON public.chat_messages;
CREATE POLICY "Users can insert own chat messages"
  ON public.chat_messages FOR INSERT
  TO authenticated
  WITH CHECK (auth.uid() = user_id);

DROP POLICY IF EXISTS "Users can delete own chat messages" ON public.chat_messages;
CREATE POLICY "Users can delete own chat messages"
  ON public.chat_messages FOR DELETE
  TO authenticated
  USING (auth.uid() = user_id);

-- INDEXES FOR MAXIMUM QUERY PERFORMANCE UNDER RLS
CREATE INDEX IF NOT EXISTS idx_assessments_user_id ON public.assessments(user_id);
CREATE INDEX IF NOT EXISTS idx_career_matches_user_id ON public.career_matches(user_id);
CREATE INDEX IF NOT EXISTS idx_saved_careers_user_id ON public.saved_careers(user_id);
CREATE INDEX IF NOT EXISTS idx_recent_views_user_id ON public.recent_views(user_id);
CREATE INDEX IF NOT EXISTS idx_roadmaps_user_id ON public.roadmaps(user_id);
CREATE INDEX IF NOT EXISTS idx_roadmap_milestones_roadmap_id ON public.roadmap_milestones(roadmap_id);
CREATE INDEX IF NOT EXISTS idx_career_notes_user_id ON public.career_notes(user_id);
CREATE INDEX IF NOT EXISTS idx_chat_sessions_user_id ON public.chat_sessions(user_id);
CREATE INDEX IF NOT EXISTS idx_chat_messages_user_id ON public.chat_messages(user_id);
