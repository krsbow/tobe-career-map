import { useState, useEffect, useRef } from 'react';
import { useNavigate } from 'react-router-dom';
import AppShell from '../components/AppShell';
import TOBEWidget from '../components/TOBEWidget';
import { useCareer } from '../context/CareerContext';
import { ASSESSMENT_QUESTIONS, SKILL_CATEGORIES } from '../data/assessmentData';

export default function Discover() {
  const navigate = useNavigate();
  const { careers, assessmentResults, saveAssessment, clearAssessment, createOrSetRoadmap, recordView } = useCareer();
  const [step, setStep] = useState<'intro' | 'questions' | 'skills' | 'results'>(
    assessmentResults ? 'results' : 'intro'
  );
  const [currentQIndex, setCurrentQIndex] = useState(0);
  const [selectedOptionId, setSelectedOptionId] = useState<string | null>(null);
  const [riasecTotals, setRiasecTotals] = useState<Record<string, number>>({
    R: 0,
    I: 0,
    A: 0,
    S: 0,
    E: 0,
    C: 0,
  });
  const [selectedSkills, setSelectedSkills] = useState<string[]>([]);
  const [isTransitioning, setIsTransitioning] = useState(false);
  const containerRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (!containerRef.current) return;
    const observer = new IntersectionObserver(
      (entries) => entries.forEach((e) => e.isIntersecting && e.target.classList.add('visible')),
      { threshold: 0.05 }
    );
    containerRef.current.querySelectorAll('.reveal').forEach((el) => observer.observe(el));
    return () => observer.disconnect();
  }, [step, currentQIndex]);

  const currentQuestion = ASSESSMENT_QUESTIONS[currentQIndex];

  const handleOptionSelect = (option: any) => {
    setSelectedOptionId(option.id);

    setTimeout(() => {
      // Accumulate scores
      const updatedTotals = { ...riasecTotals };
      if (option.scores) {
        Object.entries(option.scores).forEach(([trait, val]) => {
          updatedTotals[trait] = (updatedTotals[trait] || 0) + (val as number);
        });
      }
      setRiasecTotals(updatedTotals);

      setIsTransitioning(true);
      setTimeout(() => {
        if (currentQIndex < ASSESSMENT_QUESTIONS.length - 1) {
          setCurrentQIndex(currentQIndex + 1);
          setSelectedOptionId(null);
        } else {
          // Go to skills selection step
          setStep('skills');
        }
        setIsTransitioning(false);
      }, 250);
    }, 350);
  };

  const toggleSkill = (skill: string) => {
    setSelectedSkills((prev) =>
      prev.includes(skill) ? prev.filter((s) => s !== skill) : [...prev, skill]
    );
  };

  const computeAndSaveResults = () => {
    // Sort RIASEC traits to get dominant archetype
    const sortedTraits = Object.entries(riasecTotals).sort((a, b) => b[1] - a[1]);
    const topTraits = sortedTraits.slice(0, 3).map(([t]) => t);

    // Compute matches across all 19 real careers
    const matched = careers.map((career) => {
      // RIASEC match (60% weight)
      let riasecScore = 0;
      let maxRiasecPossible = 0;
      career.riasec_traits.forEach((trait, idx) => {
        const weight = 3 - idx * 0.5;
        riasecScore += (riasecTotals[trait] || 0) * weight;
        maxRiasecPossible += 15 * weight;
      });
      const interestPct = Math.min(100, Math.round((riasecScore / (maxRiasecPossible || 1)) * 100));

      // Skills match (40% weight)
      const allCareerSkills = [...career.core_skills, ...career.optional_skills];
      const matchedSkillCount = selectedSkills.filter((s) =>
        allCareerSkills.some((cs) => cs.toLowerCase().includes(s.toLowerCase()) || s.toLowerCase().includes(cs.toLowerCase()))
      ).length;
      const skillPct =
        selectedSkills.length > 0
          ? Math.min(100, Math.round((matchedSkillCount / Math.max(1, selectedSkills.length)) * 100) + 50)
          : 75; // Baseline if no skills chosen yet

      const finalMatch = Math.min(98, Math.max(62, Math.round(interestPct * 0.6 + skillPct * 0.4)));

      return {
        careerId: career.id,
        matchScore: finalMatch,
        breakdown: {
          interests: interestPct,
          skills: skillPct,
        },
      };
    });

    matched.sort((a, b) => b.matchScore - a.matchScore);

    const resultPayload = {
      completedAt: new Date().toISOString(),
      riasecScores: riasecTotals,
      topTraits,
      selectedSkills,
      matchedCareers: matched,
    };

    saveAssessment(resultPayload);
    setStep('results');
  };

  const handleRetake = () => {
    clearAssessment();
    setRiasecTotals({ R: 0, I: 0, A: 0, S: 0, E: 0, C: 0 });
    setSelectedSkills([]);
    setCurrentQIndex(0);
    setSelectedOptionId(null);
    setStep('intro');
  };

  // Get resolved matched careers for results view
  const topMatchedCareers = (assessmentResults?.matchedCareers || [])
    .map((item) => {
      const c = careers.find((car) => car.id === item.careerId);
      if (!c) return null;
      return { ...c, matchScore: item.matchScore };
    })
    .filter(Boolean) as (typeof careers[0] & { matchScore: number })[];

  const questionProgress = ((currentQIndex + (selectedOptionId ? 1 : 0)) / ASSESSMENT_QUESTIONS.length) * 100;

  return (
    <AppShell>
      <div ref={containerRef} style={{ maxWidth: 780, margin: '0 auto', padding: '56px 32px 80px' }}>
        {/* Step 1: Intro */}
        {step === 'intro' && (
          <div className="reveal" style={{ textAlign: 'center', padding: '40px 0' }}>
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
                margin: '0 auto 24px',
              }}
            >
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                <circle cx="12" cy="12" r="10" />
                <polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76" />
              </svg>
            </div>
            <p style={{ fontSize: 13, fontWeight: 600, letterSpacing: '0.08em', textTransform: 'uppercase', color: 'var(--muted-foreground)', marginBottom: 8 }}>
              Discovery Assessment
            </p>
            <h1
              style={{
                fontFamily: 'var(--font-display)',
                fontSize: 'clamp(32px, 5vw, 48px)',
                fontWeight: 400,
                color: 'var(--foreground)',
                marginBottom: 16,
                letterSpacing: '-0.025em',
              }}
            >
              Let's discover what drives you.
            </h1>
            <p style={{ fontSize: 16, color: 'var(--muted-foreground)', maxWidth: 540, margin: '0 auto 36px', lineHeight: 1.6 }}>
              A scientific 18-question evaluation grounded in the Holland Occupational Codes (RIASEC) and practical skill assessment. Takes 3 minutes with zero tests and zero pressure.
            </p>
            <button
              onClick={() => setStep('questions')}
              style={{
                background: 'var(--primary)',
                color: 'white',
                border: 'none',
                borderRadius: 'var(--radius)',
                padding: '14px 36px',
                fontSize: 16,
                fontWeight: 600,
                cursor: 'pointer',
                fontFamily: 'var(--font-body)',
                transition: 'all 0.2s ease',
              }}
              onMouseEnter={(e) => { e.currentTarget.style.opacity = '0.9'; }}
              onMouseLeave={(e) => { e.currentTarget.style.opacity = '1'; }}
            >
              Start Assessment
            </button>
          </div>
        )}

        {/* Step 2: 18 Questions */}
        {step === 'questions' && currentQuestion && (
          <div>
            <div style={{ marginBottom: 40 }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 12 }}>
                <span style={{ fontSize: 12, fontWeight: 700, letterSpacing: '0.08em', textTransform: 'uppercase', color: 'var(--muted-foreground)' }}>
                  Question {currentQIndex + 1} of {ASSESSMENT_QUESTIONS.length}
                </span>
                <span style={{ fontSize: 12, color: 'var(--muted-foreground)' }}>
                  {currentQuestion.dimension || 'Core Profile'}
                </span>
              </div>

              {/* Progress bar */}
              <div style={{ height: 4, background: 'var(--border)', borderRadius: 2, overflow: 'hidden' }}>
                <div
                  style={{
                    height: '100%',
                    width: `${questionProgress}%`,
                    background: 'var(--navy)',
                    borderRadius: 2,
                    transition: 'width 0.4s cubic-bezier(0.4, 0, 0.2, 1)',
                  }}
                />
              </div>
            </div>

            <div
              style={{
                opacity: isTransitioning ? 0 : 1,
                transform: isTransitioning ? 'translateY(8px)' : 'translateY(0)',
                transition: 'all 0.25s ease',
              }}
            >
              <h2
                style={{
                  fontFamily: 'var(--font-display)',
                  fontSize: 'clamp(24px, 4vw, 32px)',
                  fontWeight: 400,
                  color: 'var(--foreground)',
                  marginBottom: 8,
                  letterSpacing: '-0.02em',
                  lineHeight: 1.25,
                }}
              >
                {currentQuestion.title}
              </h2>
              {currentQuestion.subtitle && (
                <p style={{ fontSize: 15, color: 'var(--muted-foreground)', marginBottom: 32 }}>
                  {currentQuestion.subtitle}
                </p>
              )}

              <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
                {currentQuestion.options.map((opt) => {
                  const isSelected = selectedOptionId === opt.id;
                  return (
                    <button
                      key={opt.id}
                      onClick={() => handleOptionSelect(opt)}
                      style={{
                        background: isSelected ? 'var(--secondary)' : 'var(--card)',
                        border: isSelected ? '1.5px solid var(--navy)' : '1px solid var(--border)',
                        borderRadius: 'calc(var(--radius) * 1.5)',
                        padding: '18px 24px',
                        textAlign: 'left',
                        cursor: 'pointer',
                        fontSize: 16,
                        fontFamily: 'var(--font-body)',
                        color: 'var(--foreground)',
                        lineHeight: 1.5,
                        transition: 'all 0.18s ease',
                        display: 'flex',
                        alignItems: 'center',
                        justifyContent: 'space-between',
                      }}
                      onMouseEnter={(e) => {
                        if (!isSelected) {
                          e.currentTarget.style.borderColor = 'var(--foreground)';
                          e.currentTarget.style.background = '#FAF9F6';
                        }
                      }}
                      onMouseLeave={(e) => {
                        if (!isSelected) {
                          e.currentTarget.style.borderColor = 'var(--border)';
                          e.currentTarget.style.background = 'var(--card)';
                        }
                      }}
                    >
                      <span>{opt.text}</span>
                      <div
                        style={{
                          width: 20,
                          height: 20,
                          borderRadius: '50%',
                          border: isSelected ? '6px solid var(--navy)' : '1.5px solid var(--border)',
                          flexShrink: 0,
                          marginLeft: 16,
                          background: 'white',
                          transition: 'all 0.18s ease',
                        }}
                      />
                    </button>
                  );
                })}
              </div>
            </div>
          </div>
        )}

        {/* Step 3: Skills selection */}
        {step === 'skills' && (
          <div>
            <div style={{ marginBottom: 32 }}>
              <p style={{ fontSize: 13, fontWeight: 600, letterSpacing: '0.08em', textTransform: 'uppercase', color: 'var(--muted-foreground)', marginBottom: 8 }}>
                Step 2: Technical & Domain Skills
              </p>
              <h2 style={{ fontFamily: 'var(--font-display)', fontSize: 'clamp(26px, 4vw, 36px)', fontWeight: 400, color: 'var(--foreground)', marginBottom: 12 }}>
                Which skills do you already have or want to learn?
              </h2>
              <p style={{ fontSize: 15, color: 'var(--muted-foreground)' }}>
                Select any tools, languages, or proficiencies that interest you (or skip if you're starting fresh).
              </p>
            </div>

            <div style={{ display: 'flex', flexDirection: 'column', gap: 24, marginBottom: 40 }}>
              {Object.entries(SKILL_CATEGORIES).map(([categoryName, skillsList]) => (
                <div key={categoryName} style={{ background: 'var(--card)', border: '1px solid var(--border)', borderRadius: 'calc(var(--radius) * 1.5)', padding: '20px' }}>
                  <h4 style={{ fontSize: 14, fontWeight: 700, color: 'var(--navy)', marginBottom: 12, letterSpacing: '0.02em' }}>
                    {categoryName}
                  </h4>
                  <div style={{ display: 'flex', flexWrap: 'wrap', gap: 8 }}>
                    {skillsList.map((skill) => {
                      const isSelected = selectedSkills.includes(skill);
                      return (
                        <button
                          key={skill}
                          onClick={() => toggleSkill(skill)}
                          style={{
                            background: isSelected ? 'var(--navy)' : 'white',
                            color: isSelected ? 'white' : 'var(--foreground)',
                            border: isSelected ? '1px solid var(--navy)' : '1px solid var(--border)',
                            borderRadius: 20,
                            padding: '6px 14px',
                            fontSize: 13,
                            fontWeight: 500,
                            cursor: 'pointer',
                            fontFamily: 'var(--font-body)',
                            transition: 'all 0.15s ease',
                          }}
                        >
                          {isSelected ? '✓ ' : '+ '}
                          {skill}
                        </button>
                      );
                    })}
                  </div>
                </div>
              ))}
            </div>

            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <button
                onClick={() => setStep('questions')}
                style={{
                  background: 'none',
                  border: 'none',
                  fontSize: 14,
                  fontWeight: 500,
                  color: 'var(--muted-foreground)',
                  cursor: 'pointer',
                  fontFamily: 'var(--font-body)',
                }}
              >
                ← Back to Questions
              </button>
              <button
                onClick={computeAndSaveResults}
                style={{
                  background: 'var(--primary)',
                  color: 'white',
                  border: 'none',
                  borderRadius: 'var(--radius)',
                  padding: '14px 32px',
                  fontSize: 15,
                  fontWeight: 600,
                  cursor: 'pointer',
                  fontFamily: 'var(--font-body)',
                  transition: 'all 0.2s ease',
                }}
                onMouseEnter={(e) => { e.currentTarget.style.opacity = '0.9'; }}
                onMouseLeave={(e) => { e.currentTarget.style.opacity = '1'; }}
              >
                Calculate My Career Matches →
              </button>
            </div>
          </div>
        )}

        {/* Step 4: Results */}
        {step === 'results' && (
          <div>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: 40, flexWrap: 'wrap', gap: 16 }}>
              <div>
                <p style={{ fontSize: 13, fontWeight: 600, letterSpacing: '0.08em', textTransform: 'uppercase', color: 'var(--muted-foreground)', marginBottom: 8 }}>
                  Your Discovery Results
                </p>
                <h1 style={{ fontFamily: 'var(--font-display)', fontSize: 'clamp(28px, 4.5vw, 42px)', fontWeight: 400, color: 'var(--foreground)', margin: 0, letterSpacing: '-0.025em' }}>
                  Curated pathways matched to you.
                </h1>
              </div>
              <button
                onClick={handleRetake}
                style={{
                  background: 'transparent',
                  border: '1px solid var(--border)',
                  borderRadius: 'var(--radius)',
                  padding: '8px 16px',
                  fontSize: 13,
                  fontWeight: 500,
                  color: 'var(--foreground)',
                  cursor: 'pointer',
                  fontFamily: 'var(--font-body)',
                }}
              >
                Retake Assessment
              </button>
            </div>

            {/* Dominant archetype summary badge */}
            {assessmentResults?.topTraits && (
              <div
                style={{
                  background: 'var(--card)',
                  border: '1px solid var(--border)',
                  borderRadius: 'calc(var(--radius) * 1.5)',
                  padding: '20px 24px',
                  marginBottom: 36,
                  display: 'flex',
                  alignItems: 'center',
                  gap: 16,
                  flexWrap: 'wrap',
                }}
              >
                <div>
                  <span style={{ fontSize: 12, color: 'var(--muted-foreground)', textTransform: 'uppercase', letterSpacing: '0.06em' }}>
                    Dominant RIASEC Archetypes:
                  </span>
                  <div style={{ display: 'flex', gap: 8, marginTop: 4 }}>
                    {assessmentResults.topTraits.map((t) => {
                      const labels: Record<string, string> = {
                        R: 'Realistic (Hands-on & Infrastructure)',
                        I: 'Investigative (Analytical & Logic)',
                        A: 'Artistic (Creative & Design)',
                        S: 'Social (Empathetic & People)',
                        E: 'Enterprising (Leadership & Strategy)',
                        C: 'Conventional (Structured & Systems)',
                      };
                      return (
                        <span
                          key={t}
                          style={{
                            fontSize: 12,
                            fontWeight: 600,
                            padding: '4px 10px',
                            background: 'var(--secondary)',
                            color: 'var(--navy)',
                            borderRadius: 'var(--radius)',
                          }}
                        >
                          {labels[t] || t}
                        </span>
                      );
                    })}
                  </div>
                </div>
              </div>
            )}

            {/* Ranked matched careers list */}
            <div style={{ display: 'flex', flexDirection: 'column', gap: 20 }}>
              {topMatchedCareers.map((career, i) => (
                <div
                  key={career.id}
                  style={{
                    background: 'var(--card)',
                    border: '1px solid var(--border)',
                    borderRadius: 'calc(var(--radius) * 2)',
                    padding: '28px',
                    transition: 'all 0.22s ease',
                  }}
                  onMouseEnter={(e) => {
                    e.currentTarget.style.borderColor = 'var(--navy)';
                    e.currentTarget.style.boxShadow = '0 6px 20px rgba(26,31,46,0.06)';
                  }}
                  onMouseLeave={(e) => {
                    e.currentTarget.style.borderColor = 'var(--border)';
                    e.currentTarget.style.boxShadow = 'none';
                  }}
                >
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: 12, gap: 16 }}>
                    <div>
                      <span style={{ fontSize: 12, fontWeight: 700, color: 'var(--sage)', textTransform: 'uppercase', letterSpacing: '0.06em' }}>
                        Rank #{i + 1} · {career.category_name}
                      </span>
                      <h3 style={{ fontFamily: 'var(--font-display)', fontSize: 24, fontWeight: 500, color: 'var(--foreground)', margin: '4px 0 6px' }}>
                        {career.title}
                      </h3>
                    </div>
                    <div style={{ textAlign: 'right', flexShrink: 0 }}>
                      <div style={{ fontSize: 28, fontWeight: 700, fontFamily: 'var(--font-display)', color: 'var(--navy)', lineHeight: 1 }}>
                        {career.matchScore}%
                      </div>
                      <div style={{ fontSize: 11, color: 'var(--muted-foreground)', marginTop: 2 }}>overall match</div>
                    </div>
                  </div>

                  <p style={{ fontSize: 14, color: 'var(--muted-foreground)', lineHeight: 1.6, marginBottom: 18 }}>
                    {career.tagline}
                  </p>

                  <div style={{ display: 'flex', flexWrap: 'wrap', gap: 8, marginBottom: 24 }}>
                    {career.core_skills.slice(0, 5).map((skill) => (
                      <span
                        key={skill}
                        style={{
                          fontSize: 12,
                          padding: '3px 10px',
                          borderRadius: 'var(--radius)',
                          background: '#F0EFEA',
                          color: 'var(--foreground)',
                          fontWeight: 500,
                        }}
                      >
                        {skill}
                      </span>
                    ))}
                  </div>

                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', paddingTop: 18, borderTop: '1px solid var(--border)', flexWrap: 'wrap', gap: 12 }}>
                    <div>
                      <span style={{ fontSize: 12, color: 'var(--muted-foreground)' }}>PH Salary Benchmark: </span>
                      <span style={{ fontSize: 13, fontWeight: 600, color: 'var(--foreground)' }}>
                        {career.salary_data.philippines.entry_level.split('(')[0]}
                      </span>
                    </div>
                    <div style={{ display: 'flex', gap: 10 }}>
                      <button
                        onClick={() => {
                          recordView(career.id);
                          navigate('/explore');
                        }}
                        style={{
                          background: 'transparent',
                          border: '1px solid var(--border)',
                          borderRadius: 'var(--radius)',
                          padding: '8px 16px',
                          fontSize: 13,
                          fontWeight: 500,
                          cursor: 'pointer',
                          fontFamily: 'var(--font-body)',
                          color: 'var(--foreground)',
                        }}
                      >
                        Explore Role
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
                          padding: '8px 18px',
                          fontSize: 13,
                          fontWeight: 600,
                          cursor: 'pointer',
                          fontFamily: 'var(--font-body)',
                        }}
                      >
                        Chart Pathway →
                      </button>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}
      </div>
      <TOBEWidget />
    </AppShell>
  );
}
