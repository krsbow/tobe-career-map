import { useState, useEffect, useRef } from 'react';
import { createPortal } from 'react-dom';
import { useNavigate } from 'react-router-dom';
import AppShell from '../components/AppShell';
import TOBEWidget from '../components/TOBEWidget';
import { useCareer } from '../context/CareerContext';
import { Career, CAREER_CATEGORIES } from '../data/careersData';

export default function Explore() {
  const navigate = useNavigate();
  const {
    careers,
    toggleSaveCareer,
    isCareerSaved,
    recordView,
    createOrSetRoadmap,
    calculateCareerMatch,
  } = useCareer();

  const [selectedCategory, setSelectedCategory] = useState('all');
  const [search, setSearch] = useState('');
  const [selectedCareer, setSelectedCareer] = useState<Career | null>(null);
  const containerRef = useRef<HTMLDivElement>(null);

  const filteredCareers = careers.filter((c) => {
    const matchesCategory = selectedCategory === 'all' || c.category_id === selectedCategory;
    const matchesSearch =
      search === '' ||
      c.title.toLowerCase().includes(search.toLowerCase()) ||
      c.category_name.toLowerCase().includes(search.toLowerCase()) ||
      c.description.toLowerCase().includes(search.toLowerCase()) ||
      c.core_skills.some((s) => s.toLowerCase().includes(search.toLowerCase())) ||
      c.common_tools.some((t) => t.toLowerCase().includes(search.toLowerCase()));
    return matchesCategory && matchesSearch;
  });

  useEffect(() => {
    if (!containerRef.current) return;
    const observer = new IntersectionObserver(
      (entries) => entries.forEach((e) => e.isIntersecting && e.target.classList.add('visible')),
      { threshold: 0.05 }
    );
    containerRef.current.querySelectorAll('.reveal').forEach((el) => observer.observe(el));
    return () => observer.disconnect();
  }, [selectedCategory, search]);

  useEffect(() => {
    if (selectedCareer) {
      document.body.style.overflow = 'hidden';
    } else {
      document.body.style.overflow = 'auto';
    }
    return () => {
      document.body.style.overflow = 'auto';
    };
  }, [selectedCareer]);

  const handleOpenDetail = (career: Career) => {
    recordView(career.id);
    setSelectedCareer(career);
  };

  return (
    <AppShell>
      <div ref={containerRef} style={{ maxWidth: 1240, margin: '0 auto', padding: '56px 32px 80px' }}>
        {/* Header */}
        <div style={{ marginBottom: 40 }}>
          <p style={{ fontSize: 13, fontWeight: 600, letterSpacing: '0.08em', textTransform: 'uppercase', color: 'var(--muted-foreground)', marginBottom: 8 }}>
            Explore Knowledge Base
          </p>
          <h1 style={{ fontFamily: 'var(--font-display)', fontSize: 'clamp(28px, 5vw, 44px)', fontWeight: 400, letterSpacing: '-0.025em', color: 'var(--foreground)', marginBottom: 24 }}>
            Every path worth considering.
          </h1>

          {/* Search bar */}
          <div style={{ position: 'relative', maxWidth: 480 }}>
            <svg
              width="16"
              height="16"
              viewBox="0 0 16 16"
              fill="none"
              style={{
                position: 'absolute',
                left: 14,
                top: '50%',
                transform: 'translateY(-50%)',
                color: 'var(--muted-foreground)',
                pointerEvents: 'none',
              }}
            >
              <circle cx="7" cy="7" r="5" stroke="currentColor" strokeWidth="1.5" />
              <path d="M11 11l2.5 2.5" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" />
            </svg>
            <input
              type="text"
              placeholder="Search careers, skills (e.g. React, SQL, Figma, AWS)..."
              value={search}
              onChange={(e) => setSearch(e.target.value)}
              style={{
                width: '100%',
                padding: '12px 14px 12px 40px',
                border: '1px solid var(--border)',
                borderRadius: 'var(--radius)',
                fontSize: 15,
                fontFamily: 'var(--font-body)',
                background: 'var(--card)',
                color: 'var(--foreground)',
                outline: 'none',
                boxSizing: 'border-box',
                transition: 'border-color 0.2s ease',
              }}
              onFocus={(e) => { e.target.style.borderColor = 'var(--navy)'; }}
              onBlur={(e) => { e.target.style.borderColor = 'var(--border)'; }}
            />
          </div>
        </div>

        {/* Filter categories */}
        <div style={{ display: 'flex', gap: 8, marginBottom: 36, flexWrap: 'wrap' }}>
          <button
            onClick={() => setSelectedCategory('all')}
            style={{
              padding: '7px 16px',
              borderRadius: 20,
              fontSize: 13,
              fontWeight: 500,
              fontFamily: 'var(--font-body)',
              cursor: 'pointer',
              border: selectedCategory === 'all' ? '1px solid var(--navy)' : '1px solid var(--border)',
              background: selectedCategory === 'all' ? 'var(--navy)' : 'var(--card)',
              color: selectedCategory === 'all' ? 'white' : 'var(--foreground)',
              transition: 'all 0.15s ease',
            }}
          >
            All Fields ({careers.length})
          </button>
          {CAREER_CATEGORIES.map((cat) => {
            const isSelected = selectedCategory === cat.id;
            const count = careers.filter((c) => c.category_id === cat.id).length;
            return (
              <button
                key={cat.id}
                onClick={() => setSelectedCategory(cat.id)}
                style={{
                  padding: '7px 16px',
                  borderRadius: 20,
                  fontSize: 13,
                  fontWeight: 500,
                  fontFamily: 'var(--font-body)',
                  cursor: 'pointer',
                  border: isSelected ? '1px solid var(--navy)' : '1px solid var(--border)',
                  background: isSelected ? 'var(--navy)' : 'var(--card)',
                  color: isSelected ? 'white' : 'var(--foreground)',
                  transition: 'all 0.15s ease',
                }}
              >
                {cat.name} ({count})
              </button>
            );
          })}
        </div>

        {/* Career cards grid */}
        <div
          style={{
            display: 'grid',
            gridTemplateColumns: 'repeat(auto-fill, minmax(350px, 1fr))',
            gap: 20,
          }}
        >
          {filteredCareers.map((career) => {
            const isSaved = isCareerSaved(career.id);
            const matchScore = calculateCareerMatch(career);

            return (
              <div
                key={career.id}
                style={{
                  background: 'var(--card)',
                  border: '1px solid var(--border)',
                  borderRadius: 'calc(var(--radius) * 2)',
                  padding: '24px',
                  display: 'flex',
                  flexDirection: 'column',
                  justifyContent: 'space-between',
                  transition: 'all 0.22s ease',
                  position: 'relative',
                }}
                onMouseEnter={(e) => {
                  e.currentTarget.style.borderColor = 'var(--navy)';
                  e.currentTarget.style.transform = 'translateY(-2px)';
                  e.currentTarget.style.boxShadow = '0 8px 24px rgba(26,31,46,0.06)';
                }}
                onMouseLeave={(e) => {
                  e.currentTarget.style.borderColor = 'var(--border)';
                  e.currentTarget.style.transform = 'translateY(0)';
                  e.currentTarget.style.boxShadow = 'none';
                }}
              >
                <div>
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: 12 }}>
                    <span
                      style={{
                        fontSize: 11,
                        fontWeight: 700,
                        textTransform: 'uppercase',
                        letterSpacing: '0.06em',
                        color: 'var(--sage)',
                        background: 'rgba(122,158,142,0.12)',
                        padding: '3px 8px',
                        borderRadius: 4,
                      }}
                    >
                      {career.category_name}
                    </span>

                    <button
                      onClick={(e) => {
                        e.stopPropagation();
                        toggleSaveCareer(career.id);
                      }}
                      title={isSaved ? 'Remove bookmark' : 'Save career'}
                      style={{
                        background: 'none',
                        border: 'none',
                        cursor: 'pointer',
                        padding: 4,
                        color: isSaved ? 'var(--navy)' : 'var(--muted-foreground)',
                        display: 'flex',
                        alignItems: 'center',
                        justifyContent: 'center',
                      }}
                    >
                      <svg width="18" height="18" viewBox="0 0 24 24" fill={isSaved ? 'currentColor' : 'none'} stroke="currentColor" strokeWidth="2">
                        <path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z" />
                      </svg>
                    </button>
                  </div>

                  <h3
                    style={{
                      fontFamily: 'var(--font-display)',
                      fontSize: 22,
                      fontWeight: 500,
                      color: 'var(--foreground)',
                      margin: '0 0 8px',
                      letterSpacing: '-0.02em',
                    }}
                  >
                    {career.title}
                  </h3>

                  <p
                    style={{
                      fontSize: 14,
                      color: 'var(--muted-foreground)',
                      lineHeight: 1.55,
                      marginBottom: 16,
                      display: '-webkit-box',
                      WebkitLineClamp: 3,
                      WebkitBoxOrient: 'vertical',
                      overflow: 'hidden',
                    }}
                  >
                    {career.description}
                  </p>

                  {/* Skills preview */}
                  <div style={{ display: 'flex', flexWrap: 'wrap', gap: 6, marginBottom: 20 }}>
                    {career.core_skills.slice(0, 4).map((skill) => (
                      <span
                        key={skill}
                        style={{
                          fontSize: 12,
                          padding: '2px 8px',
                          borderRadius: 4,
                          background: '#F0EFEA',
                          color: 'var(--foreground)',
                          fontWeight: 500,
                        }}
                      >
                        {skill}
                      </span>
                    ))}
                    {career.core_skills.length > 4 && (
                      <span style={{ fontSize: 11, color: 'var(--muted-foreground)', alignSelf: 'center' }}>
                        +{career.core_skills.length - 4} more
                      </span>
                    )}
                  </div>
                </div>

                <div>
                  {/* Salary info */}
                  <div
                    style={{
                      paddingTop: 14,
                      borderTop: '1px solid var(--border)',
                      marginBottom: 14,
                      display: 'flex',
                      justifyContent: 'space-between',
                      alignItems: 'center',
                    }}
                  >
                    <div>
                      <div style={{ fontSize: 11, color: 'var(--muted-foreground)', textTransform: 'uppercase', letterSpacing: '0.04em' }}>
                        PH Entry Benchmark
                      </div>
                      <div style={{ fontSize: 13, fontWeight: 600, color: 'var(--foreground)' }}>
                        {career.salary_data.philippines.entry_level.split('(')[0]}
                      </div>
                    </div>
                    {matchScore > 0 && (
                      <div style={{ textAlign: 'right' }}>
                        <div style={{ fontSize: 16, fontWeight: 700, fontFamily: 'var(--font-display)', color: 'var(--navy)' }}>
                          {matchScore}%
                        </div>
                        <div style={{ fontSize: 10, color: 'var(--muted-foreground)' }}>match</div>
                      </div>
                    )}
                  </div>

                  <div style={{ display: 'flex', gap: 8 }}>
                    <button
                      onClick={() => handleOpenDetail(career)}
                      style={{
                        flex: 1,
                        background: 'transparent',
                        border: '1px solid var(--border)',
                        borderRadius: 'var(--radius)',
                        padding: '10px 14px',
                        fontSize: 13,
                        fontWeight: 600,
                        cursor: 'pointer',
                        fontFamily: 'var(--font-body)',
                        color: 'var(--foreground)',
                        textAlign: 'center',
                        transition: 'all 0.15s ease',
                      }}
                      onMouseEnter={(e) => {
                        e.currentTarget.style.borderColor = 'var(--navy)';
                        e.currentTarget.style.background = '#FAF9F6';
                      }}
                      onMouseLeave={(e) => {
                        e.currentTarget.style.borderColor = 'var(--border)';
                        e.currentTarget.style.background = 'transparent';
                      }}
                    >
                      View Deep Dive
                    </button>
                    <button
                      onClick={() => {
                        createOrSetRoadmap(career.id);
                        navigate('/my-path');
                      }}
                      style={{
                        background: 'var(--primary)',
                        color: 'white',
                        border: 'none',
                        borderRadius: 'var(--radius)',
                        padding: '10px 16px',
                        fontSize: 13,
                        fontWeight: 600,
                        cursor: 'pointer',
                        fontFamily: 'var(--font-body)',
                        whiteSpace: 'nowrap',
                      }}
                    >
                      Build Pathway
                    </button>
                  </div>
                </div>
              </div>
            );
          })}
        </div>

        {filteredCareers.length === 0 && (
          <div style={{ textAlign: 'center', padding: '64px 20px', background: 'var(--card)', borderRadius: 'var(--radius)', border: '1px solid var(--border)' }}>
            <p style={{ fontSize: 16, color: 'var(--foreground)', marginBottom: 8, fontWeight: 500 }}>
              No careers found matching "{search}".
            </p>
            <p style={{ fontSize: 14, color: 'var(--muted-foreground)', marginBottom: 20 }}>
              Try searching by skills like "Python", "React", "SQL", or clearing the category filter.
            </p>
            <button
              onClick={() => {
                setSearch('');
                setSelectedCategory('all');
              }}
              style={{
                background: 'var(--secondary)',
                color: 'var(--navy)',
                border: '1px solid var(--border)',
                borderRadius: 'var(--radius)',
                padding: '8px 16px',
                fontSize: 13,
                fontWeight: 600,
                cursor: 'pointer',
                fontFamily: 'var(--font-body)',
              }}
            >
              Reset Filters
            </button>
          </div>
        )}

        {/* Deep Dive Modal mounted via createPortal for glitch-free viewport overlay */}
        {selectedCareer &&
          createPortal(
            <div
              style={{
                position: 'fixed',
                top: 0,
                left: 0,
                right: 0,
                bottom: 0,
                zIndex: 99999,
                background: 'rgba(26, 31, 46, 0.65)',
                backdropFilter: 'blur(6px)',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                padding: '24px 16px',
                boxSizing: 'border-box',
              }}
              onClick={() => setSelectedCareer(null)}
            >
              <div
                style={{
                  background: 'var(--background)',
                  borderRadius: 'calc(var(--radius) * 2)',
                  maxWidth: 820,
                  width: '100%',
                  maxHeight: '88vh',
                  overflowY: 'auto',
                  padding: '36px 32px',
                  position: 'relative',
                  boxShadow: '0 24px 70px rgba(0,0,0,0.3)',
                  border: '1px solid var(--border)',
                }}
                onClick={(e) => e.stopPropagation()}
              >
                {/* Close Button */}
                <button
                  onClick={() => setSelectedCareer(null)}
                  style={{
                    position: 'absolute',
                    top: 20,
                    right: 20,
                    background: 'none',
                    border: 'none',
                    cursor: 'pointer',
                    fontSize: 22,
                    color: 'var(--muted-foreground)',
                    padding: 8,
                    lineHeight: 1,
                  }}
                >
                  ✕
                </button>

                <div style={{ marginBottom: 24 }}>
                  <span
                    style={{
                      fontSize: 12,
                      fontWeight: 700,
                      textTransform: 'uppercase',
                      letterSpacing: '0.08em',
                      color: 'var(--sage)',
                    }}
                  >
                    {selectedCareer.category_name} · Deep Dive
                  </span>
                  <h2
                    style={{
                      fontFamily: 'var(--font-display)',
                      fontSize: 'clamp(28px, 4vw, 36px)',
                      fontWeight: 400,
                      color: 'var(--foreground)',
                      margin: '8px 0 12px',
                    }}
                  >
                    {selectedCareer.title}
                  </h2>
                  <p style={{ fontSize: 16, color: 'var(--muted-foreground)', lineHeight: 1.6 }}>
                    {selectedCareer.description}
                  </p>
                </div>

                {/* Salary benchmarks table */}
                <div style={{ background: 'var(--card)', border: '1px solid var(--border)', borderRadius: 'var(--radius)', padding: '20px', marginBottom: 24 }}>
                  <h4 style={{ fontSize: 14, fontWeight: 700, color: 'var(--navy)', marginBottom: 12, letterSpacing: '0.02em' }}>
                    Authentic Compensation Benchmarks
                  </h4>
                  <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 16 }} className="salary-grid">
                    <div>
                      <div style={{ fontSize: 12, color: 'var(--muted-foreground)', fontWeight: 600 }}>Philippines (PHP)</div>
                      <div style={{ fontSize: 13, marginTop: 4 }}><strong>Entry:</strong> {selectedCareer.salary_data.philippines.entry_level}</div>
                      <div style={{ fontSize: 13, marginTop: 2 }}><strong>Mid:</strong> {selectedCareer.salary_data.philippines.mid_level}</div>
                      <div style={{ fontSize: 13, marginTop: 2 }}><strong>Senior:</strong> {selectedCareer.salary_data.philippines.senior_level}</div>
                      <div style={{ fontSize: 11, color: 'var(--muted-foreground)', marginTop: 4 }}>Source: {selectedCareer.salary_data.philippines.source}</div>
                    </div>
                    <div>
                      <div style={{ fontSize: 12, color: 'var(--muted-foreground)', fontWeight: 600 }}>Global Remote (USD)</div>
                      <div style={{ fontSize: 13, marginTop: 4 }}><strong>Entry:</strong> {selectedCareer.salary_data.global_usd.entry_level}</div>
                      <div style={{ fontSize: 13, marginTop: 2 }}><strong>Mid:</strong> {selectedCareer.salary_data.global_usd.mid_level}</div>
                      <div style={{ fontSize: 13, marginTop: 2 }}><strong>Senior:</strong> {selectedCareer.salary_data.global_usd.senior_level}</div>
                      <div style={{ fontSize: 11, color: 'var(--muted-foreground)', marginTop: 4 }}>Source: {selectedCareer.salary_data.global_usd.source}</div>
                    </div>
                  </div>
                </div>

                {/* Key Responsibilities */}
                <div style={{ marginBottom: 24 }}>
                  <h4 style={{ fontSize: 15, fontWeight: 700, color: 'var(--foreground)', marginBottom: 10 }}>
                    Key Responsibilities
                  </h4>
                  <ul style={{ paddingLeft: 20, margin: 0, fontSize: 14, color: 'var(--foreground)', lineHeight: 1.7 }}>
                    {selectedCareer.responsibilities.map((r, i) => (
                      <li key={i} style={{ marginBottom: 4 }}>{r}</li>
                    ))}
                  </ul>
                </div>

                {/* Skills & Common Tools */}
                <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 20, marginBottom: 24 }} className="skills-grid">
                  <div>
                    <h4 style={{ fontSize: 14, fontWeight: 700, color: 'var(--foreground)', marginBottom: 8 }}>Core Skills</h4>
                    <div style={{ display: 'flex', flexWrap: 'wrap', gap: 6 }}>
                      {selectedCareer.core_skills.map((s) => (
                        <span key={s} style={{ fontSize: 12, padding: '4px 10px', background: 'var(--secondary)', color: 'var(--navy)', borderRadius: 4, fontWeight: 500 }}>
                          {s}
                        </span>
                      ))}
                    </div>
                  </div>
                  <div>
                    <h4 style={{ fontSize: 14, fontWeight: 700, color: 'var(--foreground)', marginBottom: 8 }}>Industry Tools</h4>
                    <div style={{ display: 'flex', flexWrap: 'wrap', gap: 6 }}>
                      {selectedCareer.common_tools.map((t) => (
                        <span key={t} style={{ fontSize: 12, padding: '4px 10px', background: '#EAE8E3', color: 'var(--foreground)', borderRadius: 4, fontWeight: 500 }}>
                          {t}
                        </span>
                      ))}
                    </div>
                  </div>
                </div>

                {/* Real Certifications & Direct Links */}
                <div style={{ marginBottom: 24 }}>
                  <h4 style={{ fontSize: 15, fontWeight: 700, color: 'var(--foreground)', marginBottom: 10 }}>
                    Recommended Industry Certifications
                  </h4>
                  <div style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
                    {selectedCareer.certifications.map((cert) => (
                      <a
                        key={cert.name}
                        href={cert.url}
                        target="_blank"
                        rel="noreferrer"
                        style={{
                          padding: '12px 16px',
                          background: 'var(--card)',
                          border: '1px solid var(--border)',
                          borderRadius: 'var(--radius)',
                          textDecoration: 'none',
                          color: 'inherit',
                          display: 'flex',
                          justifyContent: 'space-between',
                          alignItems: 'center',
                        }}
                      >
                        <div>
                          <div style={{ fontSize: 14, fontWeight: 600, color: 'var(--navy)' }}>{cert.name} ↗</div>
                          <div style={{ fontSize: 12, color: 'var(--muted-foreground)' }}>Provider: {cert.provider}</div>
                        </div>
                        <span style={{ fontSize: 12, background: 'rgba(122,158,142,0.15)', color: 'var(--sage)', padding: '2px 8px', borderRadius: 4, fontWeight: 600 }}>
                          {cert.cost}
                        </span>
                      </a>
                    ))}
                  </div>
                </div>

                {/* Action buttons */}
                <div style={{ display: 'flex', justifyContent: 'flex-end', gap: 12, marginTop: 32, borderTop: '1px solid var(--border)', paddingTop: 20 }}>
                  <button
                    onClick={() => setSelectedCareer(null)}
                    style={{
                      padding: '10px 20px',
                      border: '1px solid var(--border)',
                      background: 'transparent',
                      borderRadius: 'var(--radius)',
                      fontSize: 14,
                      fontWeight: 500,
                      cursor: 'pointer',
                      fontFamily: 'var(--font-body)',
                    }}
                  >
                    Close
                  </button>
                  <button
                    onClick={() => {
                      createOrSetRoadmap(selectedCareer.id);
                      setSelectedCareer(null);
                      navigate('/my-path');
                    }}
                    style={{
                      padding: '10px 24px',
                      border: 'none',
                      background: 'var(--primary)',
                      color: 'white',
                      borderRadius: 'var(--radius)',
                      fontSize: 14,
                      fontWeight: 600,
                      cursor: 'pointer',
                      fontFamily: 'var(--font-body)',
                    }}
                  >
                    Chart Pathway for this Career →
                  </button>
                </div>
              </div>
            </div>,
            document.body
          )}
      </div>
      <style>{`
        @media (max-width: 600px) {
          .salary-grid, .skills-grid {
            grid-template-columns: 1fr !important;
          }
        }
      `}</style>
      <TOBEWidget />
    </AppShell>
  );
}
