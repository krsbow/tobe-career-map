import { useEffect, useRef } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import { useCareer } from '../context/CareerContext';
import AppShell from '../components/AppShell';

const quickLinks = [
  { label: 'Discover', desc: 'What to be — take the assessment & find your match', path: '/discover', color: 'var(--navy)' },
  { label: 'Explore', desc: 'Why to be — understand real salaries, skills & tools', path: '/explore', color: 'var(--sage)' },
  { label: 'My Path', desc: 'How to be — your step-by-step career milestone plan', path: '/my-path', color: '#5B7FA6' },
];

export default function Home() {
  const { user } = useAuth();
  const { careers, recentlyViewed, savedCareerIds, activeRoadmap, calculateCareerMatch } = useCareer();
  const navigate = useNavigate();
  const containerRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (!containerRef.current) return;
    const observer = new IntersectionObserver(
      (entries) => entries.forEach((e) => e.isIntersecting && e.target.classList.add('visible')),
      { threshold: 0.1 }
    );
    containerRef.current.querySelectorAll('.reveal').forEach((el) => observer.observe(el));
    return () => observer.disconnect();
  }, []);

  const hour = new Date().getHours();
  const greeting = hour < 12 ? 'Good morning' : hour < 17 ? 'Good afternoon' : 'Good evening';

  // Resolve recently viewed careers from IDs
  const recentCareersList = recentlyViewed
    .map((item) => {
      const career = careers.find((c) => c.id === item.careerId);
      if (!career) return null;
      return {
        ...career,
        viewedAt: item.viewedAt,
        matchScore: calculateCareerMatch(career),
      };
    })
    .filter(Boolean)
    .slice(0, 4);

  // Roadmap progress computation
  const totalTasks = activeRoadmap
    ? activeRoadmap.milestones.reduce((acc, m) => acc + m.tasks.length, 0)
    : 0;
  const completedTasks = activeRoadmap
    ? activeRoadmap.milestones.reduce(
        (acc, m) => acc + m.tasks.filter((t) => t.completed).length,
        0
      )
    : 0;
  const roadmapProgress = totalTasks > 0 ? Math.round((completedTasks / totalTasks) * 100) : 0;

  return (
    <AppShell>
      <div ref={containerRef} style={{ maxWidth: 1100, margin: '0 auto', padding: '56px 32px 80px' }}>
        {/* Greeting */}
        <div className="reveal" style={{ marginBottom: 48 }}>
          <p style={{ fontSize: 14, color: 'var(--muted-foreground)', marginBottom: 8 }}>
            {greeting}, {user?.name || 'Explorer'}
          </p>
          <h1
            style={{
              fontFamily: 'var(--font-display)',
              fontSize: 'clamp(32px, 5vw, 52px)',
              fontWeight: 400,
              letterSpacing: '-0.03em',
              color: 'var(--foreground)',
              lineHeight: 1.15,
            }}
          >
            Where do you want to go today?
          </h1>
        </div>

        {/* Quick navigation */}
        <div
          className="reveal"
          style={{
            display: 'grid',
            gridTemplateColumns: 'repeat(auto-fit, minmax(240px, 1fr))',
            gap: 16,
            marginBottom: 56,
          }}
        >
          {quickLinks.map((link, i) => (
            <button
              key={link.label}
              onClick={() => navigate(link.path)}
              style={{
                background: 'var(--card)',
                border: '1px solid var(--border)',
                borderRadius: 'calc(var(--radius) * 2)',
                padding: '28px 24px',
                textAlign: 'left',
                cursor: 'pointer',
                fontFamily: 'var(--font-body)',
                transition: 'all 0.22s ease',
                transitionDelay: `${i * 0.05}s`,
                display: 'flex',
                flexDirection: 'column',
                justifyContent: 'space-between',
              }}
              onMouseEnter={(e) => {
                e.currentTarget.style.transform = 'translateY(-2px)';
                e.currentTarget.style.boxShadow = '0 8px 28px rgba(26,31,46,0.08)';
                e.currentTarget.style.borderColor = link.color;
              }}
              onMouseLeave={(e) => {
                e.currentTarget.style.transform = 'translateY(0)';
                e.currentTarget.style.boxShadow = 'none';
                e.currentTarget.style.borderColor = 'var(--border)';
              }}
            >
              <div>
                <div
                  style={{
                    width: 10,
                    height: 10,
                    borderRadius: '50%',
                    background: link.color,
                    marginBottom: 16,
                  }}
                />
                <div style={{ fontSize: 18, fontWeight: 600, color: 'var(--foreground)', marginBottom: 6 }}>
                  {link.label}
                </div>
                <div style={{ fontSize: 13, color: 'var(--muted-foreground)', lineHeight: 1.5 }}>
                  {link.desc}
                </div>
              </div>
              <div
                style={{
                  marginTop: 20,
                  fontSize: 13,
                  fontWeight: 600,
                  color: 'var(--navy)',
                  display: 'flex',
                  alignItems: 'center',
                  gap: 4,
                }}
              >
                Get Started
                <svg width="14" height="14" viewBox="0 0 16 16" fill="none">
                  <path d="M6 3L11 8L6 13" stroke="currentColor" strokeWidth="1.75" strokeLinecap="round" strokeLinejoin="round" />
                </svg>
              </div>
            </button>
          ))}
        </div>

        {/* First time user helper banner if no assessment or roadmap */}
        {!activeRoadmap && recentlyViewed.length === 0 && (
          <div
            className="reveal"
            style={{
              background: 'rgba(235, 240, 236, 0.6)',
              border: '1px solid rgba(122, 158, 142, 0.3)',
              borderRadius: 'calc(var(--radius) * 2)',
              padding: '28px 32px',
              marginBottom: 48,
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'space-between',
              flexWrap: 'wrap',
              gap: 20,
            }}
          >
            <div style={{ maxWidth: 600 }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 6 }}>
                <span
                  style={{
                    fontSize: 11,
                    fontWeight: 700,
                    textTransform: 'uppercase',
                    letterSpacing: '0.08em',
                    color: 'var(--sage)',
                    background: 'white',
                    padding: '2px 8px',
                    borderRadius: 4,
                    border: '1px solid var(--border)',
                  }}
                >
                  New Explorer
                </span>
                <h3 style={{ fontFamily: 'var(--font-display)', fontSize: 18, fontWeight: 500, color: 'var(--foreground)', margin: 0 }}>
                  Ready to discover your ideal career path?
                </h3>
              </div>
              <p style={{ fontSize: 14, color: 'var(--muted-foreground)', margin: 0, lineHeight: 1.5 }}>
                Take the 3-minute Discovery Assessment to get personalized career recommendations based on real industry data and RIASEC alignment.
              </p>
            </div>
            <button
              onClick={() => navigate('/discover')}
              style={{
                background: 'var(--primary)',
                color: 'white',
                border: 'none',
                borderRadius: 'var(--radius)',
                padding: '12px 24px',
                fontSize: 14,
                fontWeight: 600,
                cursor: 'pointer',
                fontFamily: 'var(--font-body)',
                whiteSpace: 'nowrap',
                transition: 'all 0.2s ease',
              }}
              onMouseEnter={(e) => { e.currentTarget.style.opacity = '0.9'; }}
              onMouseLeave={(e) => { e.currentTarget.style.opacity = '1'; }}
            >
              Start Discovery
            </button>
          </div>
        )}

        <div style={{ display: 'grid', gridTemplateColumns: '1fr 380px', gap: 32 }} className="home-grid">
          {/* Recently viewed or recommended */}
          <div className="reveal">
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'baseline', marginBottom: 20 }}>
              <h2 style={{ fontFamily: 'var(--font-display)', fontSize: 22, fontWeight: 400, color: 'var(--foreground)', margin: 0, letterSpacing: '-0.02em' }}>
                {recentCareersList.length > 0 ? 'Recently explored' : 'Featured paths to explore'}
              </h2>
              <button
                onClick={() => navigate('/explore')}
                style={{
                  background: 'none',
                  border: 'none',
                  fontSize: 13,
                  fontWeight: 500,
                  color: 'var(--navy)',
                  cursor: 'pointer',
                  fontFamily: 'var(--font-body)',
                  textDecoration: 'underline',
                  textUnderlineOffset: 3,
                }}
              >
                Browse all {careers.length} careers
              </button>
            </div>

            {recentCareersList.length > 0 ? (
              <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>
                {recentCareersList.map((career: any, i: number) => (
                  <div
                    key={career.id}
                    onClick={() => navigate('/explore')}
                    style={{
                      display: 'flex',
                      alignItems: 'center',
                      gap: 16,
                      padding: '16px 20px',
                      background: 'var(--card)',
                      border: '1px solid var(--border)',
                      borderRadius: 'var(--radius)',
                      cursor: 'pointer',
                      transition: 'all 0.2s ease',
                      transitionDelay: `${i * 0.05}s`,
                    }}
                    onMouseEnter={(e) => {
                      e.currentTarget.style.borderColor = 'var(--navy)';
                      e.currentTarget.style.transform = 'translateX(4px)';
                    }}
                    onMouseLeave={(e) => {
                      e.currentTarget.style.borderColor = 'var(--border)';
                      e.currentTarget.style.transform = 'translateX(0)';
                    }}
                  >
                    <div
                      style={{
                        width: 44,
                        height: 44,
                        borderRadius: 'var(--radius)',
                        background: 'var(--secondary)',
                        display: 'flex',
                        alignItems: 'center',
                        justifyContent: 'center',
                        fontSize: 18,
                        fontFamily: 'var(--font-display)',
                        fontWeight: 400,
                        color: 'var(--navy)',
                        flexShrink: 0,
                      }}
                    >
                      {career.title[0]}
                    </div>
                    <div style={{ flex: 1, minWidth: 0 }}>
                      <div style={{ fontSize: 15, fontWeight: 600, color: 'var(--foreground)', whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis' }}>
                        {career.title}
                      </div>
                      <div style={{ fontSize: 13, color: 'var(--muted-foreground)' }}>
                        {career.category_name} · {career.salary_data.philippines.entry_level.split(' ')[0]}
                      </div>
                    </div>
                    {career.matchScore > 0 ? (
                      <div style={{ textAlign: 'right' }}>
                        <div style={{ fontSize: 18, fontWeight: 700, fontFamily: 'var(--font-display)', color: 'var(--navy)' }}>
                          {career.matchScore}%
                        </div>
                        <div style={{ fontSize: 11, color: 'var(--muted-foreground)' }}>match</div>
                      </div>
                    ) : (
                      <div style={{ fontSize: 12, color: 'var(--navy)', fontWeight: 500 }}>
                        View Details →
                      </div>
                    )}
                  </div>
                ))}
              </div>
            ) : (
              /* Clean zero-state for first time users with real top careers previews */
              <div style={{ display: 'flex', flexDirection: 'column', gap: 10 }}>
                {careers.slice(0, 3).map((career) => (
                  <div
                    key={career.id}
                    onClick={() => navigate('/explore')}
                    style={{
                      display: 'flex',
                      alignItems: 'center',
                      gap: 16,
                      padding: '16px 20px',
                      background: 'var(--card)',
                      border: '1px solid var(--border)',
                      borderRadius: 'var(--radius)',
                      cursor: 'pointer',
                      transition: 'all 0.2s ease',
                    }}
                    onMouseEnter={(e) => {
                      e.currentTarget.style.borderColor = 'var(--navy)';
                      e.currentTarget.style.transform = 'translateX(4px)';
                    }}
                    onMouseLeave={(e) => {
                      e.currentTarget.style.borderColor = 'var(--border)';
                      e.currentTarget.style.transform = 'translateX(0)';
                    }}
                  >
                    <div
                      style={{
                        width: 44,
                        height: 44,
                        borderRadius: 'var(--radius)',
                        background: 'var(--secondary)',
                        display: 'flex',
                        alignItems: 'center',
                        justifyContent: 'center',
                        fontSize: 18,
                        fontFamily: 'var(--font-display)',
                        fontWeight: 400,
                        color: 'var(--navy)',
                        flexShrink: 0,
                      }}
                    >
                      {career.title[0]}
                    </div>
                    <div style={{ flex: 1, minWidth: 0 }}>
                      <div style={{ fontSize: 15, fontWeight: 600, color: 'var(--foreground)' }}>
                        {career.title}
                      </div>
                      <div style={{ fontSize: 13, color: 'var(--muted-foreground)' }}>
                        {career.category_name} · {career.salary_data.philippines.entry_level.split('(')[0]}
                      </div>
                    </div>
                    <div style={{ fontSize: 12, fontWeight: 600, color: 'var(--navy)' }}>
                      Explore →
                    </div>
                  </div>
                ))}
              </div>
            )}
          </div>

          {/* TOBE prompt */}
          <div className="reveal reveal-delay-2">
            <div
              style={{
                background: 'var(--primary)',
                borderRadius: 'calc(var(--radius) * 2)',
                padding: '28px',
                height: '100%',
                display: 'flex',
                flexDirection: 'column',
                minHeight: 260,
                boxSizing: 'border-box',
              }}
            >
              <div style={{ display: 'flex', alignItems: 'center', gap: 10, marginBottom: 20 }}>
                <div
                  style={{
                    width: 32,
                    height: 32,
                    borderRadius: 'var(--radius)',
                    background: 'rgba(122,158,142,0.25)',
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                  }}
                >
                  <svg width="16" height="16" viewBox="0 0 16 16" fill="none">
                    <circle cx="8" cy="8" r="6" stroke="var(--sage)" strokeWidth="1.5" />
                    <path d="M8 5v3l2 2" stroke="var(--sage)" strokeWidth="1.5" strokeLinecap="round" />
                  </svg>
                </div>
                <div>
                  <div style={{ fontSize: 13, fontWeight: 700, color: 'white', letterSpacing: '0.04em' }}>TOBE</div>
                  <div style={{ fontSize: 11, color: 'rgba(255,255,255,0.45)', letterSpacing: '0.06em', textTransform: 'uppercase' }}>Your AI mentor</div>
                </div>
              </div>

              <p style={{ fontSize: 15, color: 'rgba(255,255,255,0.75)', lineHeight: 1.65, flex: 1 }}>
                {activeRoadmap
                  ? `You're currently following the pathway for ${activeRoadmap.careerTitle}. Need help breaking down your next milestone or practicing interview questions?`
                  : `"Whether you're curious about software engineering, UX design, cybersecurity, or data science, I'm here to help you uncover what fits your unique style."`}
              </p>

              <button
                onClick={() => navigate('/tobe')}
                style={{
                  marginTop: 24,
                  background: 'rgba(255,255,255,0.1)',
                  border: '1px solid rgba(255,255,255,0.15)',
                  borderRadius: 'var(--radius)',
                  padding: '10px 16px',
                  fontSize: 14,
                  fontWeight: 600,
                  color: 'white',
                  cursor: 'pointer',
                  fontFamily: 'var(--font-body)',
                  transition: 'all 0.2s ease',
                  textAlign: 'center',
                }}
                onMouseEnter={(e) => { e.currentTarget.style.background = 'rgba(255,255,255,0.16)'; }}
                onMouseLeave={(e) => { e.currentTarget.style.background = 'rgba(255,255,255,0.1)'; }}
              >
                Chat with TOBE
              </button>
            </div>
          </div>
        </div>

        {/* Progress strip */}
        <div className="reveal" style={{ marginTop: 56, padding: '32px 0', borderTop: '1px solid var(--border)' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 20 }}>
            <h2 style={{ fontFamily: 'var(--font-display)', fontSize: 20, fontWeight: 400, color: 'var(--foreground)', margin: 0 }}>
              Your journey summary
            </h2>
            <button
              onClick={() => navigate('/my-path')}
              style={{
                background: 'none',
                border: 'none',
                fontSize: 14,
                fontWeight: 500,
                color: 'var(--navy)',
                cursor: 'pointer',
                fontFamily: 'var(--font-body)',
                textDecoration: 'underline',
                textUnderlineOffset: 3,
              }}
            >
              View full pathway
            </button>
          </div>
          <div style={{ display: 'flex', gap: 24, flexWrap: 'wrap' }}>
            {[
              { label: 'Careers explored', value: recentlyViewed.length, max: careers.length },
              { label: 'Saved careers', value: savedCareerIds.length, max: careers.length },
              {
                label: activeRoadmap ? `${activeRoadmap.careerTitle} progress` : 'Pathway status',
                value: roadmapProgress,
                max: 100,
                isPercent: true,
              },
            ].map((stat) => (
              <div key={stat.label} style={{ flex: '1 1 200px', background: 'var(--card)', padding: '16px 20px', borderRadius: 'var(--radius)', border: '1px solid var(--border)' }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: 8 }}>
                  <span style={{ fontSize: 13, color: 'var(--muted-foreground)' }}>{stat.label}</span>
                  <span style={{ fontSize: 13, fontWeight: 600, color: 'var(--foreground)' }}>
                    {stat.isPercent ? `${stat.value}%` : `${stat.value} / ${stat.max}`}
                  </span>
                </div>
                <div style={{ height: 4, background: 'var(--border)', borderRadius: 2, overflow: 'hidden' }}>
                  <div
                    style={{
                      height: '100%',
                      width: `${stat.isPercent ? stat.value : Math.min(100, (stat.value / stat.max) * 100)}%`,
                      background: 'var(--navy)',
                      borderRadius: 2,
                      transition: 'width 0.6s ease',
                    }}
                  />
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
      <style>{`
        @media (max-width: 860px) {
          .home-grid {
            grid-template-columns: 1fr !important;
          }
        }
      `}</style>
    </AppShell>
  );
}
