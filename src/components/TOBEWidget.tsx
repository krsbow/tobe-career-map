import { useState } from 'react';
import { useNavigate } from 'react-router-dom';

interface TOBEWidgetProps {
  prompt?: string;
  careerId?: string;
}

export default function TOBEWidget({ prompt, careerId }: TOBEWidgetProps) {
  const [expanded, setExpanded] = useState(false);
  const navigate = useNavigate();

  const handleOpenChat = () => {
    if (careerId) {
      navigate(`/tobe?career=${careerId}`);
    } else {
      navigate('/tobe');
    }
  };

  return (
    <div
      style={{
        position: 'fixed',
        bottom: 28,
        right: 28,
        zIndex: 90,
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'flex-end',
        gap: 10,
      }}
    >
      {expanded && (
        <div
          style={{
            background: 'var(--primary)',
            borderRadius: 'calc(var(--radius) * 2)',
            padding: '20px',
            width: 290,
            boxShadow: '0 12px 40px rgba(26,31,46,0.18)',
            animation: 'slideUp 0.25s cubic-bezier(0.4, 0, 0.2, 1) both',
          }}
        >
          <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 12 }}>
            <div
              style={{
                width: 6,
                height: 6,
                borderRadius: '50%',
                background: 'var(--sage)',
              }}
            />
            <span style={{ fontSize: 11, fontWeight: 700, letterSpacing: '0.1em', textTransform: 'uppercase', color: 'rgba(255,255,255,0.5)' }}>
              TOBE Mentor
            </span>
          </div>
          <p style={{ fontSize: 14, color: 'rgba(255,255,255,0.85)', lineHeight: 1.6, marginBottom: 16 }}>
            {prompt ?? "Want guided clarity on what you're exploring? Explore with TOBE."}
          </p>
          <button
            onClick={handleOpenChat}
            style={{
              width: '100%',
              padding: '10px',
              background: 'rgba(255,255,255,0.12)',
              border: '1px solid rgba(255,255,255,0.2)',
              borderRadius: 'var(--radius)',
              fontSize: 13,
              fontWeight: 600,
              color: 'white',
              cursor: 'pointer',
              fontFamily: 'var(--font-body)',
              transition: 'background 0.2s ease',
            }}
            onMouseEnter={(e) => { (e.target as HTMLElement).style.background = 'rgba(255,255,255,0.2)'; }}
            onMouseLeave={(e) => { (e.target as HTMLElement).style.background = 'rgba(255,255,255,0.12)'; }}
          >
            Explore with TOBE →
          </button>
        </div>
      )}

      <button
        onClick={() => setExpanded(!expanded)}
        title="Explore with TOBE"
        style={{
          width: 48,
          height: 48,
          borderRadius: '50%',
          background: expanded ? 'var(--foreground)' : 'var(--primary)',
          border: 'none',
          cursor: 'pointer',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          boxShadow: '0 4px 20px rgba(26,31,46,0.18)',
          transition: 'all 0.25s cubic-bezier(0.4, 0, 0.2, 1)',
          transform: expanded ? 'rotate(45deg)' : 'rotate(0deg)',
        }}
        onMouseEnter={(e) => { (e.currentTarget).style.transform = expanded ? 'rotate(45deg) scale(1.06)' : 'scale(1.06)'; }}
        onMouseLeave={(e) => { (e.currentTarget).style.transform = expanded ? 'rotate(45deg)' : 'rotate(0deg)'; }}
      >
        {expanded ? (
          <svg width="16" height="16" viewBox="0 0 16 16" fill="none" stroke="white" strokeWidth="1.8" strokeLinecap="round">
            <line x1="4" y1="4" x2="12" y2="12" />
            <line x1="12" y1="4" x2="4" y2="12" />
          </svg>
        ) : (
          <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
            <circle cx="10" cy="10" r="8" stroke="rgba(255,255,255,0.35)" strokeWidth="1.5" />
            <circle cx="10" cy="10" r="4.5" stroke="white" strokeWidth="1.5" />
            <circle cx="10" cy="10" r="2" fill="var(--sage)" />
          </svg>
        )}
      </button>
    </div>
  );
}
