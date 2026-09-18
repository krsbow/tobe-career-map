import { createClient, SupabaseClient } from '@supabase/supabase-js';

// Environment configuration for Supabase
const supabaseUrl = import.meta.env.VITE_SUPABASE_URL || '';
const supabaseAnonKey = import.meta.env.VITE_SUPABASE_ANON_KEY || '';

export const isSupabaseConfigured = Boolean(
  supabaseUrl &&
  supabaseAnonKey &&
  supabaseUrl !== 'https://your-project-ref.supabase.co' &&
  !supabaseUrl.includes('placeholder')
);

// Fallback mock client wrapper if keys are not yet configured in environment
export const supabase: SupabaseClient = createClient(
  supabaseUrl || 'https://placeholder-tobe.supabase.co',
  supabaseAnonKey || 'placeholder-anon-key',
  {
    auth: {
      autoRefreshToken: true,
      persistSession: true,
      detectSessionInUrl: true,
    },
  }
);

/**
 * Validates whether an email address belongs strictly to @gmail.com
 */
export function isGmailAddress(email: string): boolean {
  if (!email) return false;
  const trimmed = email.trim().toLowerCase();
  return /^[a-zA-Z0-9._%+-]+@gmail\.com$/.test(trimmed);
}

/**
 * Initiates Google OAuth authentication flow through Supabase
 */
export async function signInWithGoogle() {
  if (!isSupabaseConfigured) {
    // In local demo mode when Supabase credentials are pending
    console.warn('Supabase not configured with VITE_SUPABASE_URL. Using mock Google auth session.');
    return { data: null, error: null, isDemo: true };
  }

  const redirectUrl = `${window.location.origin}/auth/callback`;

  const { data, error } = await supabase.auth.signInWithOAuth({
    provider: 'google',
    options: {
      redirectTo: redirectUrl,
      queryParams: {
        access_type: 'offline',
        prompt: 'select_account',
      },
    },
  });

  return { data, error, isDemo: false };
}
