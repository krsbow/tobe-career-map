import React, { createContext, useContext, useState, useEffect, ReactNode } from 'react';
import { supabase, isSupabaseConfigured, isGmailAddress, signInWithGoogle } from '../lib/supabase';

export interface AuthUser {
  id: string; // The Supabase Auth UUID (auth.uid())
  email: string;
  name: string;
  avatarUrl?: string;
}

interface AuthContextType {
  isAuthenticated: boolean;
  user: AuthUser | null;
  loading: boolean;
  loginWithGoogle: () => Promise<{ success: boolean; error?: string }>;
  loginWithEmail: (email: string, password?: string) => Promise<{ success: boolean; error?: string }>;
  signUpWithEmail: (email: string, name?: string, password?: string) => Promise<{ success: boolean; error?: string }>;
  logout: () => Promise<void>;
}

const AuthContext = createContext<AuthContextType>({
  isAuthenticated: false,
  user: null,
  loading: true,
  loginWithGoogle: async () => ({ success: false }),
  loginWithEmail: async () => ({ success: false }),
  signUpWithEmail: async () => ({ success: false }),
  logout: async () => {},
});

export function AuthProvider({ children }: { children: ReactNode }) {
  const [user, setUser] = useState<AuthUser | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // 1. Check active Supabase session
    async function initAuth() {
      try {
        if (isSupabaseConfigured) {
          const { data: { session }, error } = await supabase.auth.getSession();
          if (error) {
            console.warn('Error fetching Supabase session:', error.message);
          }

          if (session?.user) {
            // Verify @gmail.com restriction
            const email = session.user.email || '';
            if (isGmailAddress(email)) {
              setUser({
                id: session.user.id,
                email: email,
                name:
                  session.user.user_metadata?.full_name ||
                  session.user.user_metadata?.name ||
                  session.user.user_metadata?.preferred_name ||
                  email.split('@')[0],
                avatarUrl: session.user.user_metadata?.avatar_url,
              });
            } else {
              // Sign out immediately if not @gmail.com
              await supabase.auth.signOut();
              setUser(null);
            }
          }
        } else {
          // Local fallback session check if stored
          const savedLocalUser = localStorage.getItem('tobe_active_user');
          if (savedLocalUser) {
            try {
              const parsed = JSON.parse(savedLocalUser);
              if (isGmailAddress(parsed.email)) {
                setUser(parsed);
              } else {
                localStorage.removeItem('tobe_active_user');
              }
            } catch {
              localStorage.removeItem('tobe_active_user');
            }
          }
        }
      } catch (err) {
        console.error('Auth initialization error:', err);
      } finally {
        setLoading(false);
      }
    }

    initAuth();

    // 2. Listen to Supabase auth state changes
    if (isSupabaseConfigured) {
      const { data: { subscription } } = supabase.auth.onAuthStateChange(async (event, session) => {
        if (session?.user) {
          const email = session.user.email || '';
          if (isGmailAddress(email)) {
            setUser({
              id: session.user.id,
              email: email,
              name:
                session.user.user_metadata?.full_name ||
                session.user.user_metadata?.name ||
                session.user.user_metadata?.preferred_name ||
                email.split('@')[0],
              avatarUrl: session.user.user_metadata?.avatar_url,
            });
          } else {
            await supabase.auth.signOut();
            setUser(null);
          }
        } else if (event === 'SIGNED_OUT') {
          setUser(null);
        }
      });

      return () => {
        subscription.unsubscribe();
      };
    }
  }, []);

  const loginWithGoogle = async (): Promise<{ success: boolean; error?: string }> => {
    try {
      if (isSupabaseConfigured) {
        const { error } = await signInWithGoogle();
        if (error) {
          return { success: false, error: error.message };
        }
        return { success: true };
      }

      // Demo mock Google login with sample Gmail account
      const demoUser: AuthUser = {
        id: 'google_user_' + Math.random().toString(36).substring(2, 10),
        email: 'explorer.demo@gmail.com',
        name: 'Google Explorer',
        avatarUrl: undefined,
      };
      setUser(demoUser);
      localStorage.setItem('tobe_active_user', JSON.stringify(demoUser));
      return { success: true };
    } catch (err: any) {
      return { success: false, error: err?.message || 'Google sign-in failed.' };
    }
  };

  const loginWithEmail = async (email: string, password = 'DefaultPassword123!'): Promise<{ success: boolean; error?: string }> => {
    const cleanEmail = email.trim().toLowerCase();

    // Strict Gmail check
    if (!isGmailAddress(cleanEmail)) {
      return { success: false, error: 'Access restricted: Please use a valid @gmail.com email address.' };
    }

    try {
      if (isSupabaseConfigured) {
        const { data, error } = await supabase.auth.signInWithPassword({
          email: cleanEmail,
          password: password,
        });

        if (error) {
          return { success: false, error: error.message };
        }

        if (data.user) {
          const authUser: AuthUser = {
            id: data.user.id,
            email: cleanEmail,
            name:
              data.user.user_metadata?.full_name ||
              data.user.user_metadata?.name ||
              cleanEmail.split('@')[0],
            avatarUrl: data.user.user_metadata?.avatar_url,
          };
          setUser(authUser);
          return { success: true };
        }
      }

      // Local fallback
      const mockId = 'user_' + cleanEmail.replace(/[^a-zA-Z0-9]/g, '_');
      const authUser: AuthUser = {
        id: mockId,
        email: cleanEmail,
        name: cleanEmail.split('@')[0],
      };
      setUser(authUser);
      localStorage.setItem('tobe_active_user', JSON.stringify(authUser));
      return { success: true };
    } catch (err: any) {
      return { success: false, error: err?.message || 'Sign in failed.' };
    }
  };

  const signUpWithEmail = async (
    email: string,
    name = '',
    password = 'DefaultPassword123!'
  ): Promise<{ success: boolean; error?: string }> => {
    const cleanEmail = email.trim().toLowerCase();

    if (!isGmailAddress(cleanEmail)) {
      return { success: false, error: 'Access restricted: Only @gmail.com accounts are permitted to register.' };
    }

    try {
      if (isSupabaseConfigured) {
        const { data, error } = await supabase.auth.signUp({
          email: cleanEmail,
          password: password,
          options: {
            data: {
              full_name: name || cleanEmail.split('@')[0],
              preferred_name: name || cleanEmail.split('@')[0],
            },
          },
        });

        if (error) {
          return { success: false, error: error.message };
        }

        if (data.user) {
          const authUser: AuthUser = {
            id: data.user.id,
            email: cleanEmail,
            name: name || cleanEmail.split('@')[0],
          };
          setUser(authUser);
          return { success: true };
        }
      }

      // Local fallback
      const mockId = 'user_' + cleanEmail.replace(/[^a-zA-Z0-9]/g, '_');
      const authUser: AuthUser = {
        id: mockId,
        email: cleanEmail,
        name: name || cleanEmail.split('@')[0],
      };
      setUser(authUser);
      localStorage.setItem('tobe_active_user', JSON.stringify(authUser));
      return { success: true };
    } catch (err: any) {
      return { success: false, error: err?.message || 'Sign up failed.' };
    }
  };

  const logout = async () => {
    try {
      if (isSupabaseConfigured) {
        await supabase.auth.signOut();
      }
    } catch (err) {
      console.warn('Error during Supabase sign-out:', err);
    } finally {
      setUser(null);
      localStorage.removeItem('tobe_active_user');
      // Purge any lingering unpartitioned legacy keys
      localStorage.removeItem('tobe_saved_careers');
      localStorage.removeItem('tobe_recent_careers');
      localStorage.removeItem('tobe_assessment');
      localStorage.removeItem('tobe_roadmap');
      localStorage.removeItem('tobe_career_notes');
    }
  };

  return (
    <AuthContext.Provider
      value={{
        isAuthenticated: !!user,
        user,
        loading,
        loginWithGoogle,
        loginWithEmail,
        signUpWithEmail,
        logout,
      }}
    >
      {children}
    </AuthContext.Provider>
  );
}

export const useAuth = () => useContext(AuthContext);
