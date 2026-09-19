import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import AppShell from '../components/AppShell';
import { useAuth } from '../context/AuthContext';
import { useCareer } from '../context/CareerContext';

export default function Profile() {
  const { user, logout } = useAuth();
  const {
    careers,
    savedCareerIds,
    toggleSaveCareer,
    createOrSetRoadmap,
    roadmaps,
    assessmentResults,
    calculateCareerMatch,
  } = useCareer();
  const navigate = useNavigate();

  const [searchQuery, setSearchQuery] = useState('');

  // Map saved IDs to full career objects
  const savedCareersList = savedCareerIds
    .map((id) => careers.find((c) => c.id === id))
    .filter(Boolean) as typeof careers;

  const filteredSavedCareers = savedCareersList.filter((c) => {
    if (!searchQuery) return true;
    const q = searchQuery.toLowerCase();
    return (
      c.title.toLowerCase().includes(q) ||
      c.category_name.toLowerCase().includes(q) ||
      c.field.toLowerCase().includes(q)
    );
  });

  const handleStartPath = (careerId: string) => {
    createOrSetRoadmap(careerId);
    navigate('/my-path');
  };

  const handleLogout = () => {
    logout();
    navigate('/');
  };

  return (
    <AppShell>
      <div style={{ maxWidth: 1100, margin: '0 auto', padding: '40px 24px 80px' }}>
        {/* User Account Hero Card */}
        <div
          style={{
            background: 'var(--card)',
            border: '1px solid var(--border)',
            borderRadius: 'calc(var(--radius) * 2)',
            padding: '32px',
            marginBottom: 36,
            boxShadow: '0 4px 20px rgba(0,0,0,0.02)',
            display: 'flex',
            justifyContent: 'space-between',
            alignItems: 'center',
            flexWrap: 'wrap',
            gap: 24,
          }}
        >
          <div style={{ display: 'flex', alignItems: 'center', gap: 20 }}>
            <div
              style={{
                width: 64,
                height: 64,
                borderRadius: '50%',
                background: 'var(--primary)',
                color: 'white',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                fontSize: 26,
                fontWeight: 600,
                fontFamily: 'var(--font-display)',
                flexShrink: 0,
              }}
            >
              {user?.name?.[0]?.toUpperCase() ?? 'U'}
            </div>
            <div>
              <div style={{ display: 'flex', alignItems: 'center', gap: 10, marginBottom: 4 }}>
                <h1
                  style={{
                    fontFamily: 'var(--font-display)',
                    fontSize: 26,
                    fontWeight: 500,
                    color: 'var(--foreground)',
                    margin: 0,
                  }}
                >
                  {user?.name || 'Explorer'}
                </h1>
                <span
                  style={{
                    fontSize: 11,
                    fontWeight: 700,
                    textTransform: 'uppercase',
                    letterSpacing: '0.06em',
                    color: 'var(--sage)',
                    background: 'rgba(122, 158, 142, 0.15)',
                    padding: '3px 8px',
                    borderRadius: 4,
                  }}
                >
                  Member
                </span>
              </div>
              <div style={{ fontSize: 14, color: 'var(--muted-foreground)' }}>{user?.email}</div>
            </div>
          </div>

          <div style={{ display: 'flex', gap: 12, alignItems: 'center' }}>
            <button
              onClick={handleLogout}
              style={{
                background: 'transparent',
                border: '1px solid var(--border)',
                borderRadius: 'var(--radius)',
                padding: '9px 18px',
                fontSize: 13,
                fontWeight: 500,
                color: 'var(--foreground)',
                cursor: 'pointer',
                fontFamily: 'var(--font-body)',
                transition: 'all 0.15s ease',
              }}
              onMouseEnter={(e) => {
                e.currentTarget.style.borderColor = 'var(--navy)';
              }}
              onMouseLeave={(e) => {
                e.currentTarget.style.borderColor = 'var(--border)';
              }}
            >
              Sign out
            </button>
          </div>
        </div>

        {/* Overview Stats Row */}
        <div
          style={{
            display: 'grid',
            gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))',
            gap: 16,
            marginBottom: 36,
          }}
        >
          <div
            style={{
              background: 'var(--card)',
              border: '1px solid var(--border)',
              borderRadius: 'var(--radius-lg)',
              padding: '20px',
            }}
          >
            <div style={{ fontSize: 12, color: 'var(--muted-foreground)', fontWeight: 600, textTransform: 'uppercase', marginBottom: 6 }}>
              Saved Careers
            </div>
            <div style={{ fontFamily: 'var(--font-display)', fontSize: 32, fontWeight: 500, color: 'var(--navy)' }}>
              {savedCareersList.length}
            </div>
          </div>

          <div
            style={{
              background: 'var(--card)',
              border: '1px solid var(--border)',
              borderRadius: 'var(--radius-lg)',
              padding: '20px',
            }}
          >
            <div style={{ fontSize: 12, color: 'var(--muted-foreground)', fontWeight: 600, textTransform: 'uppercase', marginBottom: 6 }}>
              Active Roadmaps
            </div>
            <div style={{ fontFamily: 'var(--font-display)', fontSize: 32, fontWeight: 500, color: 'var(--foreground)' }}>
              {roadmaps.length}
            </div>
          </div>

          <div
            style={{
              background: 'var(--card)',
              border: '1px solid var(--border)',
              borderRadius: 'var(--radius-lg)',
              padding: '20px',
            }}
          >
            <div style={{ fontSize: 12, color: 'var(--muted-foreground)', fontWeight: 600, textTransform: 'uppercase', marginBottom: 6 }}>
              Assessment Status
            </div>
            <div style={{ fontSize: 15, fontWeight: 600, color: assessmentResults ? 'var(--navy)' : 'var(--muted-foreground)', marginTop: 8 }}>
              {assessmentResults?.topTraits?.length
                ? `${assessmentResults.topTraits.join(', ')}`
                : 'Not Taken Yet'}
            </div>
          </div>
        </div>

        {/* Dedicated Saved Careers Section */}
        <div style={{ marginBottom: 48 }}>
          <div
            style={{
              display: 'flex',
              justifyContent: 'space-between',
              alignItems: 'center',
              flexWrap: 'wrap',
              gap: 16,
              marginBottom: 20,
            }}
          >
            <div>
              <h2
                style={{
                  fontFamily: 'var(--font-display)',
                  fontSize: 24,
                  fontWeight: 500,
                  color: 'var(--foreground)',
                  margin: '0 0 4px',
                }}
              >
                Saved Careers
              </h2>
              <p style={{ fontSize: 14, color: 'var(--muted-foreground)', margin: 0 }}>
                Your bookmarked career directions and pathways.
              </p>
            </div>

            {savedCareersList.length > 3 && (
              <input
                type="text"
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                placeholder="Search saved careers..."
                style={{
                  padding: '8px 14px',
                  borderRadius: 'var(--radius)',
                  border: '1px solid var(--border)',
                  background: 'var(--card)',
                  fontSize: 13,
                  fontFamily: 'var(--font-body)',
                  color: 'var(--foreground)',
                  outline: 'none',
                  minWidth: 220,
                }}
              />
            )}
          </div>

          {filteredSavedCareers.length > 0 ? (
            <div
              style={{
                display: 'grid',
                gridTemplateColumns: 'repeat(auto-fill, minmax(320px, 1fr))',
                gap: 20,
              }}
            >
              {filteredSavedCareers.map((c) => {
                const matchScore = assessmentResults ? calculateCareerMatch(c) : null;
                return (
                  <div
                    key={c.id}
                    style={{
                      background: 'var(--card)',
                      border: '1px solid var(--border)',
                      borderRadius: 'calc(var(--radius) * 1.5)',
                      padding: '24px',
                      display: 'flex',
                      flexDirection: 'column',
                      justifyContent: 'space-between',
                      transition: 'all 0.2s ease',
                      boxShadow: '0 2px 8px rgba(0,0,0,0.02)',
                    }}
                  >
                    <div>
                      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: 12 }}>
                        <span
                          style={{
                            fontSize: 11,
                            fontWeight: 700,
                            textTransform: 'uppercase',
                            letterSpacing: '0.05em',
                            color: 'var(--navy)',
                            background: 'var(--secondary)',
                            padding: '3px 8px',
                            borderRadius: 4,
                          }}
                        >
                          {c.category_name}
                        </span>

                        <button
                          onClick={() => toggleSaveCareer(c.id)}
                          title="Remove from saved"
                          style={{
                            background: '#EFF6FF',
                            border: '1px solid #BFDBFE',
                            borderRadius: 6,
                            padding: '6px',
                            cursor: 'pointer',
                            color: 'var(--navy)',
                            display: 'flex',
                            alignItems: 'center',
                            justifyContent: 'center',
                          }}
                        >
                          <svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor" stroke="currentColor" strokeWidth="2">
                            <path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z" />
                          </svg>
                        </button>
                      </div>

                      <h3
                        style={{
                          fontSize: 18,
                          fontWeight: 600,
                          color: 'var(--foreground)',
                          margin: '0 0 8px',
                          lineHeight: 1.3,
                        }}
                      >
                        {c.title}
                      </h3>

                      <p
                        style={{
                          fontSize: 13,
                          color: 'var(--muted-foreground)',
                          lineHeight: 1.5,
                          margin: '0 0 16px',
                          display: '-webkit-box',
                          WebkitLineClamp: 2,
                          WebkitBoxOrient: 'vertical',
                          overflow: 'hidden',
                        }}
                      >
                        {c.tagline}
                      </p>

                      <div
                        style={{
                          padding: '10px 12px',
                          background: 'var(--secondary)',
                          borderRadius: 'var(--radius)',
                          fontSize: 12,
                          color: 'var(--foreground)',
                          marginBottom: 20,
                          display: 'flex',
                          justifyContent: 'space-between',
                          alignItems: 'center',
                        }}
                      >
                        <div>
                          <span style={{ color: 'var(--muted-foreground)', display: 'block', fontSize: 10, textTransform: 'uppercase' }}>
                            PH Entry Benchmark
                          </span>
                          <span style={{ fontWeight: 600 }}>
                            {c.salary_data?.philippines?.entry_level?.split('(')[0] || 'Benchmark pending'}
                          </span>
                        </div>
                        {matchScore !== null && (
                          <div style={{ textAlign: 'right' }}>
                            <span style={{ color: 'var(--muted-foreground)', display: 'block', fontSize: 10, textTransform: 'uppercase' }}>
                              Match
                            </span>
                            <span style={{ fontWeight: 700, color: 'var(--sage)' }}>{matchScore}%</span>
                          </div>
                        )}
                      </div>
                    </div>

                    <div style={{ display: 'flex', gap: 10 }}>
                      <button
                        onClick={() => navigate(`/explore/${c.id}`)}
                        style={{
                          flex: 1,
                          padding: '9px 12px',
                          background: 'transparent',
                          border: '1px solid var(--border)',
                          borderRadius: 'var(--radius)',
                          fontSize: 13,
                          fontWeight: 600,
                          color: 'var(--foreground)',
                          cursor: 'pointer',
                          fontFamily: 'var(--font-body)',
                          textAlign: 'center',
                        }}
                      >
                        Explore Details
                      </button>
                      <button
                        onClick={() => handleStartPath(c.id)}
                        style={{
                          flex: 1,
                          padding: '9px 12px',
                          background: 'var(--primary)',
                          border: 'none',
                          borderRadius: 'var(--radius)',
                          fontSize: 13,
                          fontWeight: 600,
                          color: 'white',
                          cursor: 'pointer',
                          fontFamily: 'var(--font-body)',
                          textAlign: 'center',
                        }}
                      >
                        {roadmaps.some((r) => r.careerId === c.id) ? 'View Roadmap' : 'Start Path'}
                      </button>
                    </div>
                  </div>
                );
              })}
            </div>
          ) : (
            <div
              style={{
                background: 'var(--card)',
                border: '1px solid var(--border)',
                borderRadius: 'calc(var(--radius) * 1.5)',
                padding: '48px 24px',
                textAlign: 'center',
              }}
            >
              <div
                style={{
                  width: 48,
                  height: 48,
                  borderRadius: '50%',
                  background: 'var(--secondary)',
                  color: 'var(--navy)',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  margin: '0 auto 16px',
                }}
              >
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                  <path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z" />
                </svg>
              </div>
              <h3 style={{ fontFamily: 'var(--font-display)', fontSize: 20, fontWeight: 500, margin: '0 0 8px', color: 'var(--foreground)' }}>
                {searchQuery ? 'No saved careers match your search' : 'No saved careers yet'}
              </h3>
              <p style={{ fontSize: 14, color: 'var(--muted-foreground)', maxWidth: 460, margin: '0 auto 20px', lineHeight: 1.5 }}>
                {searchQuery
                  ? 'Try searching with different terms or clear the filter.'
                  : 'As you explore different careers in Explore or Discover, click "Save Career" to bookmark them here for quick access.'}
              </p>
              <button
                onClick={() => navigate('/explore')}
                style={{
                  background: 'var(--navy)',
                  color: 'white',
                  border: 'none',
                  borderRadius: 'var(--radius)',
                  padding: '10px 20px',
                  fontSize: 14,
                  fontWeight: 600,
                  cursor: 'pointer',
                  fontFamily: 'var(--font-body)',
                }}
              >
                Explore Careers →
              </button>
            </div>
          )}
        </div>
      </div>
    </AppShell>
  );
}
