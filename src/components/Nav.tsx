import { useState } from 'react';
import { NavLink, useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';

const links = [
  { to: '/home', label: 'Home' },
  { to: '/discover', label: 'Discover' },
  { to: '/explore', label: 'Explore' },
  { to: '/my-path', label: 'My Path' },
];

export default function Nav() {
  const { user, logout } = useAuth();
  const navigate = useNavigate();
  const [menuOpen, setMenuOpen] = useState(false);
  const [profileOpen, setProfileOpen] = useState(false);

  const handleLogout = () => {
    logout();
    navigate('/');
  };

  return (
    <nav
      style={{
        position: 'fixed',
        top: 0,
        left: 0,
        right: 0,
        zIndex: 100,
        background: 'rgba(249, 248, 245, 0.92)',
        backdropFilter: 'blur(12px)',
        borderBottom: '1px solid var(--border)',
      }}
    >
      <div style={{ maxWidth: 1280, margin: '0 auto', padding: '0 24px', display: 'flex', alignItems: 'center', height: 60 }}>
        {/* Logo */}
        <NavLink
          to="/home"
          style={{ textDecoration: 'none', marginRight: 40, display: 'flex', alignItems: 'center', gap: 8 }}
        >
          {/* Spectacles / Glasses Brand Icon */}
          <svg width="22" height="22" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg" style={{ flexShrink: 0 }}>
            <rect width="64" height="64" rx="16" fill="var(--navy)" />
            <circle cx="20" cy="34" r="9.5" stroke="#F9F8F5" strokeWidth="3" fill="none" />
            <circle cx="20" cy="34" r="6.5" fill="#7A9E8E" fillOpacity="0.4" />
            <circle cx="44" cy="34" r="9.5" stroke="#F9F8F5" strokeWidth="3" fill="none" />
            <circle cx="44" cy="34" r="6.5" fill="#7A9E8E" fillOpacity="0.4" />
            <path d="M 29.5 33 C 33 28, 37 28, 40.5 33" stroke="#F9F8F5" strokeWidth="3" strokeLinecap="round" fill="none" />
            <path d="M 10.5 33 L 4 30" stroke="#F9F8F5" strokeWidth="3" strokeLinecap="round" fill="none" />
            <path d="M 53.5 33 L 60 30" stroke="#F9F8F5" strokeWidth="3" strokeLinecap="round" fill="none" />
          </svg>
          <span style={{ fontFamily: 'var(--font-display)', fontSize: 20, fontWeight: 500, color: 'var(--navy)', letterSpacing: '-0.03em' }}>
            TO BE
          </span>
        </NavLink>

        {/* Desktop links */}
        <div style={{ display: 'flex', gap: 4, flex: 1 }} className="hide-mobile">
          {links.map((link) => (
            <NavLink
              key={link.to}
              to={link.to}
              style={({ isActive }) => ({
                textDecoration: 'none',
                padding: '6px 14px',
                borderRadius: 'var(--radius)',
                fontSize: 14,
                fontWeight: 500,
                fontFamily: 'var(--font-body)',
                color: isActive ? 'var(--navy)' : 'var(--muted-foreground)',
                background: isActive ? 'var(--secondary)' : 'transparent',
                transition: 'all 0.2s ease',
              })}
            >
              {link.label}
            </NavLink>
          ))}
        </div>

        {/* Profile */}
        <div style={{ marginLeft: 'auto', position: 'relative' }} className="hide-mobile">
          <button
            onClick={() => setProfileOpen(!profileOpen)}
            style={{
              display: 'flex',
              alignItems: 'center',
              gap: 8,
              background: 'none',
              border: '1px solid var(--border)',
              borderRadius: 40,
              padding: '6px 14px 6px 8px',
              cursor: 'pointer',
              color: 'var(--foreground)',
              fontSize: 14,
              fontFamily: 'var(--font-body)',
            }}
          >
            <span
              style={{
                width: 28,
                height: 28,
                borderRadius: '50%',
                background: 'var(--primary)',
                color: 'white',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                fontSize: 12,
                fontWeight: 600,
              }}
            >
              {user?.name?.[0]?.toUpperCase() ?? 'U'}
            </span>
            <span style={{ fontWeight: 500 }}>{user?.name}</span>
          </button>

          {profileOpen && (
            <div
              style={{
                position: 'absolute',
                top: '100%',
                right: 0,
                marginTop: 8,
                background: 'var(--card)',
                border: '1px solid var(--border)',
                borderRadius: 'var(--radius-lg)',
                boxShadow: '0 8px 32px rgba(26,31,46,0.10)',
                minWidth: 180,
                overflow: 'hidden',
              }}
            >
              <div style={{ padding: '12px 16px', borderBottom: '1px solid var(--border)' }}>
                <div style={{ fontSize: 13, fontWeight: 600 }}>{user?.name}</div>
                <div style={{ fontSize: 12, color: 'var(--muted-foreground)' }}>{user?.email}</div>
              </div>
              <button
                onClick={handleLogout}
                style={{
                  width: '100%',
                  padding: '11px 16px',
                  background: 'none',
                  border: 'none',
                  textAlign: 'left',
                  fontSize: 14,
                  cursor: 'pointer',
                  color: 'var(--foreground)',
                  fontFamily: 'var(--font-body)',
                }}
              >
                Sign out
              </button>
            </div>
          )}
        </div>

        {/* Mobile hamburger */}
        <button
          onClick={() => setMenuOpen(!menuOpen)}
          className="show-mobile"
          style={{
            marginLeft: 'auto',
            background: 'none',
            border: 'none',
            cursor: 'pointer',
            padding: 8,
            color: 'var(--foreground)',
          }}
          aria-label="Menu"
        >
          <svg width="20" height="20" viewBox="0 0 20 20" fill="none" stroke="currentColor" strokeWidth="1.5">
            {menuOpen ? (
              <>
                <line x1="4" y1="4" x2="16" y2="16" />
                <line x1="16" y1="4" x2="4" y2="16" />
              </>
            ) : (
              <>
                <line x1="3" y1="6" x2="17" y2="6" />
                <line x1="3" y1="10" x2="17" y2="10" />
                <line x1="3" y1="14" x2="17" y2="14" />
              </>
            )}
          </svg>
        </button>
      </div>

      {/* Mobile menu */}
      {menuOpen && (
        <div
          style={{
            background: 'var(--card)',
            borderTop: '1px solid var(--border)',
            padding: '12px 24px 20px',
          }}
        >
          {links.map((link) => (
            <NavLink
              key={link.to}
              to={link.to}
              onClick={() => setMenuOpen(false)}
              style={({ isActive }) => ({
                display: 'block',
                textDecoration: 'none',
                padding: '11px 0',
                fontSize: 16,
                fontWeight: 500,
                fontFamily: 'var(--font-body)',
                color: isActive ? 'var(--navy)' : 'var(--foreground)',
                borderBottom: '1px solid var(--border)',
              })}
            >
              {link.label}
            </NavLink>
          ))}
          <button
            onClick={handleLogout}
            style={{
              display: 'block',
              marginTop: 16,
              background: 'none',
              border: 'none',
              fontSize: 14,
              color: 'var(--muted-foreground)',
              cursor: 'pointer',
              fontFamily: 'var(--font-body)',
              padding: 0,
            }}
          >
            Sign out
          </button>
        </div>
      )}

      <style>{`
        @media (max-width: 768px) {
          .hide-mobile { display: none !important; }
          .show-mobile { display: flex !important; }
        }
        @media (min-width: 769px) {
          .show-mobile { display: none !important; }
          .hide-mobile { display: flex !important; }
        }
      `}</style>
    </nav>
  );
}
