import { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { supabase, isSupabaseConfigured, isGmailAddress } from '../lib/supabase';

export default function AuthCallback() {
  const navigate = useNavigate();

  useEffect(() => {
    async function handleCallback() {
      if (!isSupabaseConfigured) {
        navigate('/home', { replace: true });
        return;
      }

      try {
        const { data: { session }, error } = await supabase.auth.getSession();
        if (error || !session?.user) {
          navigate('/auth', { replace: true });
          return;
        }

        const email = session.user.email || '';
        if (!isGmailAddress(email)) {
          await supabase.auth.signOut();
          navigate('/auth', { replace: true });
          return;
        }

        navigate('/home', { replace: true });
      } catch (err) {
        console.error('Error handling auth callback:', err);
        navigate('/auth', { replace: true });
      }
    }

    handleCallback();
  }, [navigate]);

  return (
    <div
      style={{
        minHeight: '100vh',
        background: 'var(--background)',
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
        fontFamily: 'var(--font-body)',
        color: 'var(--foreground)',
      }}
    >
      <div
        style={{
          width: 36,
          height: 36,
          borderRadius: '50%',
          border: '3px solid var(--border)',
          borderTopColor: 'var(--navy)',
          animation: 'spin 0.8s linear infinite',
          marginBottom: 16,
        }}
      />
      <p style={{ fontSize: 14, color: 'var(--muted-foreground)' }}>
        Authenticating with Google...
      </p>
      <style>{`
        @keyframes spin {
          to { transform: rotate(360deg); }
        }
      `}</style>
    </div>
  );
}
