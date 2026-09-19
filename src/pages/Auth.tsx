import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import { isGmailAddress } from '../lib/supabase';

export default function Auth() {
  const [mode, setMode] = useState<'login' | 'signup'>('signup');
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [errorMsg, setErrorMsg] = useState<string | null>(null);
  const [submitting, setSubmitting] = useState(false);
  const [mounted, setMounted] = useState(false);

  const { loginWithGoogle, loginWithEmail, signUpWithEmail } = useAuth();
  const navigate = useNavigate();

  useEffect(() => {
    setTimeout(() => setMounted(true), 30);
  }, []);

  const handleGoogleAuth = async () => {
    setErrorMsg(null);
    setSubmitting(true);
    try {
      const res = await loginWithGoogle();
      if (!res.success) {
        setErrorMsg(res.error || 'Google authentication failed. Please ensure you are using a @gmail.com account.');
      } else {
        navigate('/home');
      }
    } catch (err: any) {
      setErrorMsg(err?.message || 'Unable to connect to Google Auth.');
    } finally {
      setSubmitting(false);
    }
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setErrorMsg(null);

    const cleanEmail = email.trim().toLowerCase();

    // Enforce @gmail.com
    if (!isGmailAddress(cleanEmail)) {
      setErrorMsg('Access restricted: Please use a valid @gmail.com email address to sign in.');
      return;
    }

    if (password.length < 6) {
      setErrorMsg('Password must be at least 6 characters long.');
      return;
    }

    setSubmitting(true);
    try {
      if (mode === 'signup') {
        const res = await signUpWithEmail(cleanEmail, name, password);
        if (!res.success) {
          setErrorMsg(res.error || 'Registration failed.');
        } else {
          navigate('/home');
        }
      } else {
        const res = await loginWithEmail(cleanEmail, password);
        if (!res.success) {
          setErrorMsg(res.error || 'Invalid email or password.');
        } else {
          navigate('/home');
        }
      }
    } catch (err: any) {
      setErrorMsg(err?.message || 'Authentication error occurred.');
    } finally {
      setSubmitting(false);
    }
  };

  return (
    <div
      style={{
        minHeight: '100vh',
        background: 'var(--background)',
        display: 'grid',
        gridTemplateColumns: '1fr 1fr',
        position: 'relative',
      }}
    >
      {/* Left panel — visual brand */}
      <div
        style={{
          background: 'var(--primary)',
          display: 'flex',
          flexDirection: 'column',
          justifyContent: 'space-between',
          padding: '48px',
          position: 'relative',
          overflow: 'hidden',
        }}
        className="auth-left-panel"
      >
        <div
          style={{
            position: 'absolute',
            bottom: -80,
            left: -80,
            width: 400,
            height: 400,
            borderRadius: '50%',
            background: 'rgba(91,127,166,0.2)',
            pointerEvents: 'none',
          }}
        />
        <div
          style={{
            position: 'absolute',
            top: 60,
            right: -60,
            width: 260,
            height: 260,
            borderRadius: '50%',
            background: 'rgba(122,158,142,0.12)',
            pointerEvents: 'none',
          }}
        />

        <button
          onClick={() => navigate('/')}
          style={{
            background: 'none',
            border: 'none',
            color: 'rgba(255,255,255,0.9)',
            cursor: 'pointer',
            fontFamily: 'var(--font-display)',
            fontSize: 22,
            fontWeight: 500,
            letterSpacing: '-0.03em',
            padding: 0,
            textAlign: 'left',
            display: 'flex',
            alignItems: 'center',
            gap: 10,
          }}
        >
          <svg width="26" height="26" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg" style={{ flexShrink: 0 }}>
            <rect width="64" height="64" rx="16" fill="rgba(255,255,255,0.12)" stroke="rgba(255,255,255,0.2)" strokeWidth="2" />
            <circle cx="20" cy="34" r="9.5" stroke="#FFFFFF" strokeWidth="3" fill="none" />
            <circle cx="20" cy="34" r="6.5" fill="#7A9E8E" fillOpacity="0.6" />
            <circle cx="44" cy="34" r="9.5" stroke="#FFFFFF" strokeWidth="3" fill="none" />
            <circle cx="44" cy="34" r="6.5" fill="#7A9E8E" fillOpacity="0.6" />
            <path d="M 29.5 33 C 30.7 30.5, 33.3 30.5, 34.5 33" stroke="#FFFFFF" strokeWidth="3" strokeLinecap="round" fill="none" />
            <path d="M 10.5 33 L 4 30" stroke="#FFFFFF" strokeWidth="3" strokeLinecap="round" fill="none" />
            <path d="M 53.5 33 L 60 30" stroke="#FFFFFF" strokeWidth="3" strokeLinecap="round" fill="none" />
          </svg>
          TO BE
        </button>

        <div style={{ position: 'relative' }}>
          <p style={{ fontSize: 12, fontWeight: 700, letterSpacing: '0.12em', textTransform: 'uppercase', color: 'rgba(255,255,255,0.45)', marginBottom: 20 }}>
            Secure Career Discovery
          </p>
          <h2
            style={{
              fontFamily: 'var(--font-display)',
              fontSize: 40,
              fontWeight: 400,
              color: 'white',
              lineHeight: 1.15,
              marginBottom: 24,
              letterSpacing: '-0.03em',
            }}
          >
            The first step to finding your path is simply beginning.
          </h2>
          <p style={{ fontSize: 15, color: 'rgba(255,255,255,0.7)', lineHeight: 1.65 }}>
            TO BE provides personal, private career pathways. Every account's data is strictly isolated and protected.
          </p>

          <div style={{ marginTop: 44, display: 'flex', flexDirection: 'column', gap: 14 }}>
            {[
              'Personalized interest & strength discovery',
              'Real Philippine & Global salary benchmarks',
              'TOBE — your private AI career mentor',
              'Personalized milestone roadmaps & notes',
            ].map((feature) => (
              <div key={feature} style={{ display: 'flex', alignItems: 'center', gap: 10 }}>
                <div
                  style={{
                    width: 20,
                    height: 20,
                    borderRadius: '50%',
                    background: 'rgba(122,158,142,0.25)',
                    border: '1px solid var(--sage)',
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                    flexShrink: 0,
                  }}
                >
                  <svg width="10" height="10" viewBox="0 0 10 10" fill="none">
                    <path d="M2 5l2 2 4-4" stroke="var(--sage)" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round" />
                  </svg>
                </div>
                <span style={{ fontSize: 14, color: 'rgba(255,255,255,0.8)' }}>{feature}</span>
              </div>
            ))}
          </div>
        </div>

        <div style={{ fontSize: 12, color: 'rgba(255,255,255,0.4)' }}>
          &copy; 2026 TO BE · created by krsbow
        </div>
      </div>

      {/* Right panel — authentication */}
      <div
        style={{
          display: 'flex',
          flexDirection: 'column',
          justifyContent: 'center',
          padding: '64px 64px',
          opacity: mounted ? 1 : 0,
          transform: mounted ? 'translateY(0)' : 'translateY(16px)',
          transition: 'opacity 0.5s ease, transform 0.5s ease',
        }}
        className="auth-right-panel"
      >
        <div style={{ maxWidth: 400, width: '100%', margin: '0 auto' }}>
          <div style={{ marginBottom: 32 }}>
            <h1
              style={{
                fontFamily: 'var(--font-display)',
                fontSize: 32,
                fontWeight: 400,
                color: 'var(--foreground)',
                marginBottom: 8,
                letterSpacing: '-0.025em',
              }}
            >
              {mode === 'login' ? 'Welcome back.' : 'Start your journey.'}
            </h1>
            <p style={{ fontSize: 15, color: 'var(--muted-foreground)' }}>
              {mode === 'login'
                ? 'Sign in to access your personal career pathway.'
                : 'Create your account to save goals, assessments, and roadmaps.'}
            </p>
          </div>

          {/* Error message banner */}
          {errorMsg && (
            <div
              style={{
                background: 'rgba(197, 48, 48, 0.08)',
                border: '1px solid rgba(197, 48, 48, 0.3)',
                borderRadius: 'var(--radius)',
                padding: '12px 16px',
                marginBottom: 20,
                display: 'flex',
                alignItems: 'center',
                gap: 10,
              }}
            >
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#C53030" strokeWidth="2">
                <circle cx="12" cy="12" r="10" />
                <line x1="12" y1="8" x2="12" y2="12" />
                <line x1="12" y1="16" x2="12.01" y2="16" />
              </svg>
              <span style={{ fontSize: 13, color: '#C53030', lineHeight: 1.4 }}>{errorMsg}</span>
            </div>
          )}

          {/* Primary Action: Continue with Google */}
          <div style={{ marginBottom: 24 }}>
            <button
              onClick={handleGoogleAuth}
              disabled={submitting}
              style={{
                width: '100%',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                gap: 12,
                background: 'var(--card)',
                border: '1.5px solid var(--border)',
                borderRadius: 'var(--radius)',
                padding: '12px 20px',
                fontSize: 15,
                fontWeight: 600,
                color: 'var(--foreground)',
                cursor: submitting ? 'not-allowed' : 'pointer',
                fontFamily: 'var(--font-body)',
                transition: 'all 0.2s ease',
                boxShadow: '0 2px 6px rgba(0,0,0,0.03)',
              }}
              onMouseEnter={(e) => {
                e.currentTarget.style.borderColor = 'var(--navy)';
                e.currentTarget.style.background = '#FAF9F6';
              }}
              onMouseLeave={(e) => {
                e.currentTarget.style.borderColor = 'var(--border)';
                e.currentTarget.style.background = 'var(--card)';
              }}
            >
              {/* Google G Logo SVG */}
              <svg width="18" height="18" viewBox="0 0 24 24">
                <path
                  fill="#4285F4"
                  d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"
                />
                <path
                  fill="#34A853"
                  d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"
                />
                <path
                  fill="#FBBC05"
                  d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.06H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.94l2.85-2.22.81-.63z"
                />
                <path
                  fill="#EA4335"
                  d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.06l3.66 2.84c.87-2.6 3.3-4.52 6.16-4.52z"
                />
              </svg>
              <span>Continue with Google</span>
            </button>
          </div>

          {/* Divider */}
          <div style={{ display: 'flex', alignItems: 'center', gap: 12, margin: '24px 0' }}>
            <div style={{ flex: 1, height: 1, background: 'var(--border)' }} />
            <span style={{ fontSize: 12, color: 'var(--muted-foreground)', textTransform: 'uppercase', letterSpacing: '0.06em' }}>
              or continue with email
            </span>
            <div style={{ flex: 1, height: 1, background: 'var(--border)' }} />
          </div>

          {/* Mode toggle */}
          <div
            style={{
              display: 'flex',
              background: 'var(--muted)',
              borderRadius: 'var(--radius)',
              padding: 3,
              marginBottom: 24,
            }}
          >
            {(['signup', 'login'] as const).map((m) => (
              <button
                key={m}
                type="button"
                onClick={() => {
                  setMode(m);
                  setErrorMsg(null);
                }}
                style={{
                  flex: 1,
                  padding: '9px',
                  border: 'none',
                  borderRadius: 'calc(var(--radius) - 1px)',
                  fontSize: 14,
                  fontWeight: 600,
                  cursor: 'pointer',
                  fontFamily: 'var(--font-body)',
                  background: mode === m ? 'var(--card)' : 'transparent',
                  color: mode === m ? 'var(--foreground)' : 'var(--muted-foreground)',
                  boxShadow: mode === m ? '0 1px 4px rgba(26,31,46,0.08)' : 'none',
                  transition: 'all 0.2s ease',
                }}
              >
                {m === 'signup' ? 'Sign Up' : 'Log In'}
              </button>
            ))}
          </div>

          <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', gap: 16 }}>
            {mode === 'signup' && (
              <div>
                <label style={{ display: 'block', fontSize: 13, fontWeight: 600, color: 'var(--foreground)', marginBottom: 6 }}>
                  Preferred Name
                </label>
                <input
                  type="text"
                  placeholder="e.g. Alex"
                  value={name}
                  onChange={(e) => setName(e.target.value)}
                  style={{
                    width: '100%',
                    padding: '11px 14px',
                    border: '1px solid var(--border)',
                    borderRadius: 'var(--radius)',
                    fontSize: 15,
                    fontFamily: 'var(--font-body)',
                    background: 'var(--card)',
                    color: 'var(--foreground)',
                    outline: 'none',
                    transition: 'border-color 0.2s ease',
                    boxSizing: 'border-box',
                  }}
                  onFocus={(e) => { e.target.style.borderColor = 'var(--navy)'; }}
                  onBlur={(e) => { e.target.style.borderColor = 'var(--border)'; }}
                />
              </div>
            )}

            <div>
              <label style={{ display: 'block', fontSize: 13, fontWeight: 600, color: 'var(--foreground)', marginBottom: 6 }}>
                Gmail Address
              </label>
              <input
                type="email"
                placeholder="yourname@gmail.com"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                required
                style={{
                  width: '100%',
                  padding: '11px 14px',
                  border: '1px solid var(--border)',
                  borderRadius: 'var(--radius)',
                  fontSize: 15,
                  fontFamily: 'var(--font-body)',
                  background: 'var(--card)',
                  color: 'var(--foreground)',
                  outline: 'none',
                  transition: 'border-color 0.2s ease',
                  boxSizing: 'border-box',
                }}
                onFocus={(e) => { e.target.style.borderColor = 'var(--navy)'; }}
                onBlur={(e) => { e.target.style.borderColor = 'var(--border)'; }}
              />
            </div>

            <div>
              <label style={{ display: 'block', fontSize: 13, fontWeight: 600, color: 'var(--foreground)', marginBottom: 6 }}>
                Password
              </label>
              <input
                type="password"
                placeholder="At least 6 characters"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                required
                style={{
                  width: '100%',
                  padding: '11px 14px',
                  border: '1px solid var(--border)',
                  borderRadius: 'var(--radius)',
                  fontSize: 15,
                  fontFamily: 'var(--font-body)',
                  background: 'var(--card)',
                  color: 'var(--foreground)',
                  outline: 'none',
                  transition: 'border-color 0.2s ease',
                  boxSizing: 'border-box',
                }}
                onFocus={(e) => { e.target.style.borderColor = 'var(--navy)'; }}
                onBlur={(e) => { e.target.style.borderColor = 'var(--border)'; }}
              />
            </div>

            <button
              type="submit"
              disabled={submitting}
              style={{
                marginTop: 8,
                background: 'var(--primary)',
                color: 'white',
                border: 'none',
                borderRadius: 'var(--radius)',
                padding: '13px',
                fontSize: 15,
                fontWeight: 600,
                cursor: submitting ? 'not-allowed' : 'pointer',
                fontFamily: 'var(--font-body)',
                letterSpacing: '-0.01em',
                transition: 'all 0.2s ease',
              }}
              onMouseEnter={(e) => { e.currentTarget.style.opacity = '0.9'; }}
              onMouseLeave={(e) => { e.currentTarget.style.opacity = '1'; }}
            >
              {submitting ? 'Please wait...' : mode === 'signup' ? 'Create Account' : 'Sign In'}
            </button>
          </form>
        </div>
      </div>

      <style>{`
        @media (max-width: 768px) {
          div[style*="grid-template-columns: 1fr 1fr"] {
            grid-template-columns: 1fr !important;
          }
          .auth-left-panel {
            display: none !important;
          }
          .auth-right-panel {
            padding: 48px 24px !important;
          }
        }
      `}</style>
    </div>
  );
}
