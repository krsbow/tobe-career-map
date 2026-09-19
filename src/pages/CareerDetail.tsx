import { useState, useEffect } from 'react';
import { useParams, useNavigate, Link } from 'react-router-dom';
import AppShell from '../components/AppShell';
import TOBEWidget from '../components/TOBEWidget';
import { useCareer } from '../context/CareerContext';
import { Career } from '../data/careersData';

export default function CareerDetail() {
  const { careerId } = useParams<{ careerId: string }>();
  const navigate = useNavigate();
  const {
    careers,
    toggleSaveCareer,
    isCareerSaved,
    recordView,
    createOrSetRoadmap,
    getCareerMatchDetails,
    assessmentResults,
  } = useCareer();

  const [activeTab, setActiveTab] = useState<'overview' | 'skills' | 'preparation' | 'pathway'>('overview');

  const career: Career | undefined = careers.find(
    (c) => c.id.toLowerCase() === careerId?.toLowerCase()
  );

  useEffect(() => {
    if (career) {
      recordView(career.id);
      window.scrollTo(0, 0);
    }
  }, [careerId, career?.id]);

  if (!career) {
    return (
      <AppShell>
        <div style={{ maxWidth: 720, margin: '80px auto', padding: '0 24px', textAlign: 'center' }}>
          <div
            style={{
              width: 64,
              height: 64,
              borderRadius: '50%',
              background: 'var(--secondary)',
              color: 'var(--navy)',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              fontSize: 28,
              margin: '0 auto 20px',
            }}
          >
            🔍
          </div>
          <h1 style={{ fontFamily: 'var(--font-display)', fontSize: 32, fontWeight: 500, color: 'var(--foreground)', marginBottom: 12 }}>
            Career Not Found
          </h1>
          <p style={{ fontSize: 16, color: 'var(--muted-foreground)', lineHeight: 1.6, marginBottom: 28 }}>
            We couldn't find the career profile you were looking for. It may have been updated or moved.
          </p>
          <div style={{ display: 'flex', gap: 12, justifyContent: 'center' }}>
            <button
              onClick={() => navigate('/explore')}
              style={{
                background: 'var(--primary)',
                color: 'white',
                border: 'none',
                borderRadius: 'var(--radius)',
                padding: '12px 24px',
                fontSize: 14,
                fontWeight: 600,
                cursor: 'pointer',
              }}
            >
              Browse All Careers
            </button>
            <button
              onClick={() => navigate('/discover')}
              style={{
                background: 'transparent',
                border: '1px solid var(--border)',
                borderRadius: 'var(--radius)',
                padding: '12px 24px',
                fontSize: 14,
                fontWeight: 600,
                color: 'var(--foreground)',
                cursor: 'pointer',
              }}
            >
              Take Assessment
            </button>
          </div>
        </div>
      </AppShell>
    );
  }

  const isSaved = isCareerSaved(career.id);
  const matchDetails = assessmentResults ? getCareerMatchDetails(career) : null;
  const relatedCareersList = careers.filter(
    (c) => career.related_careers?.includes(c.id) || (c.category_id === career.category_id && c.id !== career.id)
  ).slice(0, 3);

  const handleStartPath = () => {
    createOrSetRoadmap(career.id);
    navigate('/my-path');
  };

  const tierStyles: Record<string, { badgeBg: string; badgeColor: string; borderColor: string }> = {
    'Strong alignment': { badgeBg: '#ECFDF5', badgeColor: '#065F46', borderColor: '#A7F3D0' },
    'Worth exploring': { badgeBg: '#EFF6FF', badgeColor: '#1E40AF', borderColor: '#BFDBFE' },
    'Possible fit': { badgeBg: '#F8FAFC', badgeColor: '#475569', borderColor: '#E2E8F0' },
  };
  const tierStyle = matchDetails ? (tierStyles[matchDetails.tier] || tierStyles['Possible fit']) : null;

  return (
    <AppShell>
      <div style={{ maxWidth: 1100, margin: '0 auto', padding: '40px 24px 80px' }}>
        {/* Navigation Breadcrumb */}
        <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 28, fontSize: 13, color: 'var(--muted-foreground)' }}>
          <button
            onClick={() => navigate(-1)}
            style={{
              background: 'none',
              border: 'none',
              color: 'var(--navy)',
              cursor: 'pointer',
              padding: 0,
              display: 'flex',
              alignItems: 'center',
              gap: 4,
              fontWeight: 600,
            }}
          >
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
              <path d="M19 12H5M12 19l-7-7 7-7" />
            </svg>
            Back
          </button>
          <span>/</span>
          <Link to="/explore" style={{ color: 'var(--muted-foreground)', textDecoration: 'none' }}>
            Careers
          </Link>
          <span>/</span>
          <span style={{ color: 'var(--foreground)', fontWeight: 500 }}>{career.title}</span>
        </div>

        {/* Hero Section */}
        <div
          style={{
            background: 'var(--card)',
            border: '1px solid var(--border)',
            borderRadius: 'calc(var(--radius) * 2)',
            padding: '36px 32px',
            marginBottom: 32,
            boxShadow: '0 4px 20px rgba(0,0,0,0.02)',
          }}
        >
          <div style={{ marginBottom: 26 }}>
            {/* Category & Tier Badges */}
            <div style={{ display: 'flex', alignItems: 'center', gap: 10, marginBottom: 12, flexWrap: 'wrap' }}>
              <span
                style={{
                  fontSize: 12,
                  fontWeight: 700,
                  textTransform: 'uppercase',
                  letterSpacing: '0.06em',
                  color: 'var(--navy)',
                  background: 'var(--secondary)',
                  padding: '4px 10px',
                  borderRadius: 6,
                }}
              >
                {career.category_name}
              </span>

              {matchDetails && tierStyle && (
                <span
                  style={{
                    fontSize: 12,
                    fontWeight: 700,
                    padding: '4px 12px',
                    borderRadius: 12,
                    background: tierStyle.badgeBg,
                    color: tierStyle.badgeColor,
                    border: `1px solid ${tierStyle.borderColor}`,
                    display: 'flex',
                    alignItems: 'center',
                    gap: 6,
                  }}
                >
                  ● {matchDetails.tier}
                </span>
              )}
            </div>

            <h1
              style={{
                fontFamily: 'var(--font-display)',
                fontSize: 'clamp(28px, 4vw, 42px)',
                fontWeight: 400,
                color: 'var(--foreground)',
                letterSpacing: '-0.025em',
                margin: '0 0 10px',
                lineHeight: 1.2,
              }}
            >
              {career.title}
            </h1>

            <p style={{ fontSize: 17, color: 'var(--muted-foreground)', lineHeight: 1.6, margin: '0 0 22px', maxWidth: 780 }}>
              {career.tagline}
            </p>

            {/* Actions: Bookmark & Start My Path - Fixed stable positioning */}
            <div style={{ display: 'flex', gap: 12, alignItems: 'center', flexWrap: 'wrap' }}>
              <button
                onClick={() => toggleSaveCareer(career.id)}
                style={{
                  background: isSaved ? '#EFF6FF' : 'transparent',
                  border: isSaved ? '1px solid #BFDBFE' : '1px solid var(--border)',
                  color: isSaved ? 'var(--navy)' : 'var(--foreground)',
                  borderRadius: 'var(--radius)',
                  padding: '11px 18px',
                  fontSize: 14,
                  fontWeight: 600,
                  cursor: 'pointer',
                  display: 'flex',
                  alignItems: 'center',
                  gap: 8,
                  transition: 'all 0.15s ease',
                  minWidth: 130,
                  justifyContent: 'center',
                }}
              >
                <svg width="18" height="18" viewBox="0 0 24 24" fill={isSaved ? 'currentColor' : 'none'} stroke="currentColor" strokeWidth="2">
                  <path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z" />
                </svg>
                {isSaved ? 'Saved' : 'Save Career'}
              </button>

              <button
                onClick={handleStartPath}
                style={{
                  background: 'var(--primary)',
                  color: 'white',
                  border: 'none',
                  borderRadius: 'var(--radius)',
                  padding: '12px 24px',
                  fontSize: 14,
                  fontWeight: 600,
                  cursor: 'pointer',
                  display: 'flex',
                  alignItems: 'center',
                  gap: 8,
                  boxShadow: '0 2px 8px rgba(0,0,0,0.08)',
                  transition: 'all 0.15s ease',
                }}
              >
                Start My Path
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5">
                  <path d="M5 12h14M12 5l7 7-7 7" />
                </svg>
              </button>
            </div>
          </div>

          {/* Quick Metrics Bar */}
          <div
            style={{
              display: 'grid',
              gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))',
              gap: 16,
              paddingTop: 24,
              borderTop: '1px solid var(--border)',
            }}
          >
            <div>
              <div style={{ fontSize: 11, fontWeight: 700, textTransform: 'uppercase', letterSpacing: '0.05em', color: 'var(--muted-foreground)', marginBottom: 4 }}>
                Philippine Entry Benchmark
              </div>
              <div style={{ fontSize: 16, fontWeight: 700, color: 'var(--foreground)' }}>
                {career.salary_data.philippines.entry_level.split('(')[0]}
              </div>
              <div style={{ fontSize: 12, color: 'var(--muted-foreground)' }}>
                Mid-level: {career.salary_data.philippines.mid_level.split('(')[0]}
              </div>
            </div>

            <div>
              <div style={{ fontSize: 11, fontWeight: 700, textTransform: 'uppercase', letterSpacing: '0.05em', color: 'var(--muted-foreground)', marginBottom: 4 }}>
                Global USD Equivalent
              </div>
              <div style={{ fontSize: 16, fontWeight: 700, color: 'var(--foreground)' }}>
                {career.salary_data.global_usd.entry_level.split('(')[0]}
              </div>
              <div style={{ fontSize: 12, color: 'var(--muted-foreground)' }}>
                Senior: {career.salary_data.global_usd.senior_level.split('(')[0]}
              </div>
            </div>

            <div>
              <div style={{ fontSize: 11, fontWeight: 700, textTransform: 'uppercase', letterSpacing: '0.05em', color: 'var(--muted-foreground)', marginBottom: 4 }}>
                Work Style
              </div>
              <div style={{ fontSize: 14, fontWeight: 600, color: 'var(--navy)' }}>
                {career.work_style}
              </div>
            </div>
          </div>
        </div>

        {/* Personalized Fit / Why this appeared for you (if assessment taken) */}
        {matchDetails && (
          <div
            style={{
              background: '#F9FBF9',
              border: '1px solid #D8E6DF',
              borderRadius: 'calc(var(--radius) * 1.5)',
              padding: '24px 28px',
              marginBottom: 32,
            }}
          >
            <div style={{ display: 'flex', alignItems: 'center', gap: 10, marginBottom: 12 }}>
              <span style={{ fontSize: 20 }}>🌿</span>
              <h2 style={{ fontFamily: 'var(--font-display)', fontSize: 20, fontWeight: 500, color: 'var(--foreground)', margin: 0 }}>
                Why this matches your profile
              </h2>
            </div>

            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))', gap: 20 }}>
              <div>
                <span style={{ fontSize: 12, fontWeight: 700, textTransform: 'uppercase', color: 'var(--navy)', display: 'block', marginBottom: 6 }}>
                  Alignment Reasons
                </span>
                <ul style={{ margin: 0, paddingLeft: 18, fontSize: 14, color: 'var(--foreground)', lineHeight: 1.6 }}>
                  {matchDetails.reasons.map((r, idx) => (
                    <li key={idx} style={{ marginBottom: 4 }}>{r}</li>
                  ))}
                </ul>
              </div>

              <div>
                {matchDetails.knownSkills.length > 0 && (
                  <div style={{ marginBottom: 12 }}>
                    <span style={{ fontSize: 12, fontWeight: 700, textTransform: 'uppercase', color: '#065F46', display: 'block', marginBottom: 4 }}>
                      Your Current Strengths
                    </span>
                    <div style={{ display: 'flex', flexWrap: 'wrap', gap: 6 }}>
                      {matchDetails.knownSkills.map((s) => (
                        <span key={s} style={{ fontSize: 12, padding: '3px 8px', borderRadius: 4, background: '#E6F4EA', color: '#065F46', fontWeight: 600 }}>
                          ✓ {s}
                        </span>
                      ))}
                    </div>
                  </div>
                )}

                {matchDetails.skillsToDevelop.length > 0 && (
                  <div>
                    <span style={{ fontSize: 12, fontWeight: 700, textTransform: 'uppercase', color: 'var(--navy)', display: 'block', marginBottom: 4 }}>
                      Skills You Can Build Along the Way
                    </span>
                    <div style={{ display: 'flex', flexWrap: 'wrap', gap: 6 }}>
                      {matchDetails.skillsToDevelop.map((s) => (
                        <span key={s} style={{ fontSize: 12, padding: '3px 8px', borderRadius: 4, background: '#EFF6FF', color: '#1E40AF', fontWeight: 500 }}>
                          + {s}
                        </span>
                      ))}
                    </div>
                  </div>
                )}
              </div>
            </div>
          </div>
        )}

        {/* Detail Tabs */}
        <div style={{ display: 'flex', gap: 12, borderBottom: '1px solid var(--border)', marginBottom: 32, overflowX: 'auto' }}>
          {[
            { id: 'overview', label: 'Overview & Role' },
            { id: 'skills', label: 'Skills & Tools' },
            { id: 'preparation', label: 'Preparation & Learning' },
            { id: 'pathway', label: 'Structured Pathway' },
          ].map((tab) => (
            <button
              key={tab.id}
              onClick={() => setActiveTab(tab.id as any)}
              style={{
                background: 'none',
                border: 'none',
                borderBottom: activeTab === tab.id ? '2px solid var(--navy)' : '2px solid transparent',
                padding: '12px 16px',
                fontSize: 15,
                fontWeight: activeTab === tab.id ? 700 : 500,
                color: activeTab === tab.id ? 'var(--navy)' : 'var(--muted-foreground)',
                cursor: 'pointer',
                whiteSpace: 'nowrap',
                transition: 'all 0.15s ease',
              }}
            >
              {tab.label}
            </button>
          ))}
        </div>

        {/* Tab 1: Overview & Role */}
        {activeTab === 'overview' && (
          <div style={{ display: 'flex', flexDirection: 'column', gap: 32 }}>
            <div style={{ background: 'var(--card)', border: '1px solid var(--border)', borderRadius: 'calc(var(--radius) * 1.5)', padding: '28px' }}>
              <h3 style={{ fontFamily: 'var(--font-display)', fontSize: 22, fontWeight: 500, color: 'var(--foreground)', margin: '0 0 14px' }}>
                What does a {career.title} do?
              </h3>
              <p style={{ fontSize: 15, color: 'var(--foreground)', lineHeight: 1.7, margin: '0 0 24px' }}>
                {career.description}
              </p>

              <h4 style={{ fontSize: 15, fontWeight: 700, color: 'var(--navy)', margin: '0 0 12px', textTransform: 'uppercase', letterSpacing: '0.04em' }}>
                Daily Responsibilities
              </h4>
              <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))', gap: 12 }}>
                {career.responsibilities.map((resp, idx) => (
                  <div key={idx} style={{ display: 'flex', gap: 10, alignItems: 'flex-start', fontSize: 14, color: 'var(--foreground)', lineHeight: 1.5 }}>
                    <span style={{ color: 'var(--navy)', fontWeight: 700 }}>•</span>
                    <span>{resp}</span>
                  </div>
                ))}
              </div>
            </div>

            {/* Work Style & Collaboration */}
            <div style={{ background: 'var(--card)', border: '1px solid var(--border)', borderRadius: 'calc(var(--radius) * 1.5)', padding: '28px' }}>
              <h3 style={{ fontFamily: 'var(--font-display)', fontSize: 22, fontWeight: 500, color: 'var(--foreground)', margin: '0 0 14px' }}>
                What the work is like
              </h3>
              <p style={{ fontSize: 15, color: 'var(--foreground)', lineHeight: 1.7, margin: 0 }}>
                This role is characterized by <strong>{career.work_style}</strong>. Professionals in this domain typically collaborate across interdisciplinary teams, balance creative and analytical problem-solving, and adapt to evolving client or industry standards.
              </p>
            </div>
          </div>
        )}

        {/* Tab 2: Skills & Tools */}
        {activeTab === 'skills' && (
          <div style={{ display: 'flex', flexDirection: 'column', gap: 32 }}>
            <div style={{ background: 'var(--card)', border: '1px solid var(--border)', borderRadius: 'calc(var(--radius) * 1.5)', padding: '28px' }}>
              <h3 style={{ fontFamily: 'var(--font-display)', fontSize: 22, fontWeight: 500, color: 'var(--foreground)', margin: '0 0 16px' }}>
                Core Competencies
              </h3>
              <p style={{ fontSize: 14, color: 'var(--muted-foreground)', marginBottom: 20 }}>
                These are the foundational and practical abilities most valued by employers in this field.
              </p>
              <div style={{ display: 'flex', flexWrap: 'wrap', gap: 10, marginBottom: 28 }}>
                {career.core_skills.map((skill) => (
                  <div
                    key={skill}
                    style={{
                      padding: '8px 16px',
                      borderRadius: 'var(--radius)',
                      background: 'var(--secondary)',
                      border: '1px solid var(--border)',
                      fontSize: 14,
                      fontWeight: 600,
                      color: 'var(--foreground)',
                    }}
                  >
                    {skill}
                  </div>
                ))}
              </div>

              {career.optional_skills && career.optional_skills.length > 0 && (
                <>
                  <h4 style={{ fontSize: 14, fontWeight: 700, color: 'var(--navy)', margin: '0 0 12px', textTransform: 'uppercase', letterSpacing: '0.04em' }}>
                    Specialized & Optional Capabilities
                  </h4>
                  <div style={{ display: 'flex', flexWrap: 'wrap', gap: 8 }}>
                    {career.optional_skills.map((skill) => (
                      <div
                        key={skill}
                        style={{
                          padding: '6px 12px',
                          borderRadius: 'var(--radius)',
                          background: '#FAF9F6',
                          border: '1px solid var(--border)',
                          fontSize: 13,
                          color: 'var(--muted-foreground)',
                        }}
                      >
                        {skill}
                      </div>
                    ))}
                  </div>
                </>
              )}
            </div>

            {/* Tools & Software */}
            <div style={{ background: 'var(--card)', border: '1px solid var(--border)', borderRadius: 'calc(var(--radius) * 1.5)', padding: '28px' }}>
              <h3 style={{ fontFamily: 'var(--font-display)', fontSize: 22, fontWeight: 500, color: 'var(--foreground)', margin: '0 0 16px' }}>
                Common Tools & Technologies
              </h3>
              <div style={{ display: 'flex', flexWrap: 'wrap', gap: 10 }}>
                {career.common_tools.map((tool) => (
                  <div
                    key={tool}
                    style={{
                      padding: '8px 14px',
                      borderRadius: 20,
                      background: 'white',
                      border: '1px solid var(--border)',
                      fontSize: 13,
                      fontWeight: 600,
                      color: 'var(--navy)',
                    }}
                  >
                    🛠️ {tool}
                  </div>
                ))}
              </div>
            </div>

            {/* Portfolio & Practice Projects */}
            {career.portfolio_projects && career.portfolio_projects.length > 0 && (
              <div style={{ background: 'var(--card)', border: '1px solid var(--border)', borderRadius: 'calc(var(--radius) * 1.5)', padding: '28px' }}>
                <h3 style={{ fontFamily: 'var(--font-display)', fontSize: 22, fontWeight: 500, color: 'var(--foreground)', margin: '0 0 8px' }}>
                  Recommended Portfolio Projects
                </h3>
                <p style={{ fontSize: 14, color: 'var(--muted-foreground)', marginBottom: 20 }}>
                  Build hands-on artifacts to demonstrate real capability to clients and hiring managers.
                </p>
                <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))', gap: 16 }}>
                  {career.portfolio_projects.map((proj, idx) => (
                    <div
                      key={idx}
                      style={{
                        background: '#FAF9F6',
                        border: '1px solid var(--border)',
                        borderRadius: 'var(--radius)',
                        padding: '16px 20px',
                      }}
                    >
                      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 8 }}>
                        <span style={{ fontSize: 14, fontWeight: 700, color: 'var(--foreground)' }}>{proj.title}</span>
                        <span
                          style={{
                            fontSize: 11,
                            fontWeight: 700,
                            padding: '2px 8px',
                            borderRadius: 10,
                            background: proj.difficulty === 'Foundational' ? '#ECFDF5' : proj.difficulty === 'Intermediate' ? '#EFF6FF' : '#FFF7ED',
                            color: proj.difficulty === 'Foundational' ? '#065F46' : proj.difficulty === 'Intermediate' ? '#1E40AF' : '#C2410C',
                          }}
                        >
                          {proj.difficulty}
                        </span>
                      </div>
                      <p style={{ fontSize: 13, color: 'var(--muted-foreground)', margin: 0, lineHeight: 1.5 }}>
                        {proj.description}
                      </p>
                    </div>
                  ))}
                </div>
              </div>
            )}
          </div>
        )}

        {/* Tab 3: Preparation & Learning */}
        {activeTab === 'preparation' && (
          <div style={{ display: 'flex', flexDirection: 'column', gap: 32 }}>
            {/* Education paths */}
            <div style={{ background: 'var(--card)', border: '1px solid var(--border)', borderRadius: 'calc(var(--radius) * 1.5)', padding: '28px' }}>
              <h3 style={{ fontFamily: 'var(--font-display)', fontSize: 22, fontWeight: 500, color: 'var(--foreground)', margin: '0 0 16px' }}>
                Educational Pathways & Entry Options
              </h3>
              <div style={{ display: 'flex', flexDirection: 'column', gap: 10 }}>
                {career.education_paths.map((edu, idx) => (
                  <div key={idx} style={{ display: 'flex', gap: 12, alignItems: 'center', fontSize: 14, color: 'var(--foreground)' }}>
                    <span style={{ width: 22, height: 22, borderRadius: '50%', background: 'var(--secondary)', display: 'flex', alignItems: 'center', justifyContent: 'center', fontSize: 12, fontWeight: 700, color: 'var(--navy)', flexShrink: 0 }}>
                      {idx + 1}
                    </span>
                    <span>{edu}</span>
                  </div>
                ))}
              </div>
            </div>

            {/* Certifications */}
            {career.certifications && career.certifications.length > 0 && (
              <div style={{ background: 'var(--card)', border: '1px solid var(--border)', borderRadius: 'calc(var(--radius) * 1.5)', padding: '28px' }}>
                <h3 style={{ fontFamily: 'var(--font-display)', fontSize: 22, fontWeight: 500, color: 'var(--foreground)', margin: '0 0 8px' }}>
                  Accredited Certifications & Licensures
                </h3>
                <p style={{ fontSize: 14, color: 'var(--muted-foreground)', marginBottom: 20 }}>
                  Recognized credentials that validate your expertise in the Philippines and globally.
                </p>
                <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))', gap: 16 }}>
                  {career.certifications.map((cert, idx) => (
                    <div
                      key={idx}
                      style={{
                        background: '#FAF9F6',
                        border: '1px solid var(--border)',
                        borderRadius: 'var(--radius)',
                        padding: '16px 20px',
                        display: 'flex',
                        flexDirection: 'column',
                        justifyContent: 'space-between',
                      }}
                    >
                      <div>
                        <div style={{ fontSize: 14, fontWeight: 700, color: 'var(--foreground)', marginBottom: 4 }}>
                          {cert.name}
                        </div>
                        <div style={{ fontSize: 12, color: 'var(--muted-foreground)', marginBottom: 12 }}>
                          Provider: <strong>{cert.provider}</strong> · Estimated: {cert.cost}
                        </div>
                      </div>
                      {cert.url && (
                        <a
                          href={cert.url}
                          target="_blank"
                          rel="noreferrer"
                          style={{
                            fontSize: 12,
                            fontWeight: 600,
                            color: 'var(--navy)',
                            textDecoration: 'none',
                            display: 'flex',
                            alignItems: 'center',
                            gap: 4,
                          }}
                        >
                          Learn more
                          <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                            <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6M15 3h6v6M10 14L21 3" />
                          </svg>
                        </a>
                      )}
                    </div>
                  ))}
                </div>
              </div>
            )}

            {/* Learning Resources */}
            {career.learning_resources && career.learning_resources.length > 0 && (
              <div style={{ background: 'var(--card)', border: '1px solid var(--border)', borderRadius: 'calc(var(--radius) * 1.5)', padding: '28px' }}>
                <h3 style={{ fontFamily: 'var(--font-display)', fontSize: 22, fontWeight: 500, color: 'var(--foreground)', margin: '0 0 8px' }}>
                  Curated Learning Resources
                </h3>
                <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))', gap: 14 }}>
                  {career.learning_resources.map((res, idx) => (
                    <a
                      key={idx}
                      href={res.url}
                      target="_blank"
                      rel="noreferrer"
                      style={{
                        background: 'white',
                        border: '1px solid var(--border)',
                        borderRadius: 'var(--radius)',
                        padding: '14px 18px',
                        textDecoration: 'none',
                        display: 'flex',
                        justifyContent: 'space-between',
                        alignItems: 'center',
                        transition: 'all 0.15s ease',
                      }}
                      onMouseEnter={(e) => {
                        e.currentTarget.style.borderColor = 'var(--navy)';
                      }}
                      onMouseLeave={(e) => {
                        e.currentTarget.style.borderColor = 'var(--border)';
                      }}
                    >
                      <div>
                        <div style={{ fontSize: 14, fontWeight: 600, color: 'var(--foreground)', marginBottom: 2 }}>
                          {res.title}
                        </div>
                        <div style={{ fontSize: 12, color: 'var(--muted-foreground)' }}>
                          {res.provider} · {res.cost}
                        </div>
                      </div>
                      <span style={{ fontSize: 12, color: 'var(--navy)', fontWeight: 600 }}>Visit ↗</span>
                    </a>
                  ))}
                </div>
              </div>
            )}
          </div>
        )}

        {/* Tab 4: Structured Pathway */}
        {activeTab === 'pathway' && (
          <div style={{ background: 'var(--card)', border: '1px solid var(--border)', borderRadius: 'calc(var(--radius) * 1.5)', padding: '32px' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 24, flexWrap: 'wrap', gap: 16 }}>
              <div>
                <h3 style={{ fontFamily: 'var(--font-display)', fontSize: 24, fontWeight: 500, color: 'var(--foreground)', margin: '0 0 6px' }}>
                  Your Pathway to {career.title}
                </h3>
                <p style={{ fontSize: 14, color: 'var(--muted-foreground)', margin: 0 }}>
                  A structured, progressive roadmap designed to take you from foundational understanding to industry readiness.
                </p>
              </div>
              <button
                onClick={handleStartPath}
                style={{
                  background: 'var(--primary)',
                  color: 'white',
                  border: 'none',
                  borderRadius: 'var(--radius)',
                  padding: '12px 24px',
                  fontSize: 14,
                  fontWeight: 600,
                  cursor: 'pointer',
                }}
              >
                Start My Path →
              </button>
            </div>

            <div style={{ display: 'flex', flexDirection: 'column', gap: 16 }}>
              {[
                { phase: 'Phase 1: Foundations', desc: 'Core fundamentals, industry principles, and domain environment setup.' },
                { phase: 'Phase 2: Core Competencies', desc: 'Hands-on practical skills, tools mastery, and guided mini-projects.' },
                { phase: 'Phase 3: Applied Practice', desc: 'Real-world problem solving, complex workflows, and collaborative tools.' },
                { phase: 'Phase 4: Capstone & Portfolio', desc: 'End-to-end portfolio projects and accredited certification prep.' },
                { phase: 'Phase 5: Career Readiness', desc: 'Industry resumes, technical interviews, and job market networking.' },
              ].map((step, idx) => (
                <div
                  key={idx}
                  style={{
                    background: '#FAF9F6',
                    border: '1px solid var(--border)',
                    borderRadius: 'var(--radius)',
                    padding: '16px 20px',
                    display: 'flex',
                    gap: 16,
                    alignItems: 'center',
                  }}
                >
                  <div
                    style={{
                      width: 32,
                      height: 32,
                      borderRadius: '50%',
                      background: 'var(--secondary)',
                      color: 'var(--navy)',
                      display: 'flex',
                      alignItems: 'center',
                      justifyContent: 'center',
                      fontWeight: 700,
                      fontSize: 13,
                      flexShrink: 0,
                    }}
                  >
                    {idx + 1}
                  </div>
                  <div>
                    <div style={{ fontSize: 14, fontWeight: 700, color: 'var(--foreground)', marginBottom: 2 }}>
                      {step.phase}
                    </div>
                    <div style={{ fontSize: 13, color: 'var(--muted-foreground)' }}>
                      {step.desc}
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* Related Careers */}
        {relatedCareersList.length > 0 && (
          <div style={{ marginTop: 48 }}>
            <h3 style={{ fontFamily: 'var(--font-display)', fontSize: 22, fontWeight: 500, color: 'var(--foreground)', marginBottom: 20 }}>
              Related Careers to Explore
            </h3>
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))', gap: 16 }}>
              {relatedCareersList.map((rel) => (
                <div
                  key={rel.id}
                  onClick={() => navigate(`/career/${rel.id}`)}
                  style={{
                    background: 'var(--card)',
                    border: '1px solid var(--border)',
                    borderRadius: 'var(--radius)',
                    padding: '20px',
                    cursor: 'pointer',
                    transition: 'all 0.15s ease',
                  }}
                  onMouseEnter={(e) => {
                    e.currentTarget.style.borderColor = 'var(--navy)';
                    e.currentTarget.style.transform = 'translateY(-2px)';
                  }}
                  onMouseLeave={(e) => {
                    e.currentTarget.style.borderColor = 'var(--border)';
                    e.currentTarget.style.transform = 'translateY(0)';
                  }}
                >
                  <div style={{ fontSize: 11, color: 'var(--muted-foreground)', textTransform: 'uppercase', fontWeight: 700, marginBottom: 4 }}>
                    {rel.category_name}
                  </div>
                  <h4 style={{ fontFamily: 'var(--font-display)', fontSize: 18, fontWeight: 500, color: 'var(--foreground)', margin: '0 0 6px' }}>
                    {rel.title}
                  </h4>
                  <p style={{ fontSize: 13, color: 'var(--muted-foreground)', margin: '0 0 12px', lineHeight: 1.4, display: '-webkit-box', WebkitLineClamp: 2, WebkitBoxOrient: 'vertical', overflow: 'hidden' }}>
                    {rel.tagline}
                  </p>
                  <span style={{ fontSize: 13, fontWeight: 600, color: 'var(--navy)' }}>
                    Explore Details →
                  </span>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* Quiet Information Sources Footer */}
        <div
          style={{
            marginTop: 56,
            paddingTop: 24,
            borderTop: '1px solid var(--border)',
            fontSize: 12,
            color: 'var(--muted-foreground)',
            lineHeight: 1.6,
          }}
        >
          <div style={{ fontWeight: 600, color: 'var(--foreground)', marginBottom: 6 }}>
            Information Sources & Industry Grounding
          </div>
          <p style={{ margin: 0 }}>
            Grounding data compiled from official occupational classifications and labor market benchmarks:
            {career.sources && career.sources.length > 0
              ? ` ${career.sources.join(' · ')}.`
              : ' Philippine Statistics Authority, O*NET OnLine, and recognized industry salary surveys.'}
          </p>
        </div>
      </div>

      <TOBEWidget careerId={career.id} prompt={`Have questions about becoming a ${career.title}? Ask TOBE.`} />
    </AppShell>
  );
}
