import { useState, useEffect, useRef } from 'react';
import { useNavigate } from 'react-router-dom';
import AppShell from '../components/AppShell';
import TOBEWidget from '../components/TOBEWidget';
import { useCareer } from '../context/CareerContext';
import { ASSESSMENT_QUESTIONS, SKILL_CATEGORIES, RIASEC_DESCRIPTIONS } from '../data/assessmentData';

export default function Discover() {
  const navigate = useNavigate();
  const { careers, assessmentResults, saveAssessment, clearAssessment, createOrSetRoadmap, recordView } = useCareer();
  
  const [step, setStep] = useState<'intro' | 'questions' | 'skills' | 'results'>(
    assessmentResults ? 'results' : 'intro'
  );
  const [currentQIndex, setCurrentQIndex] = useState(0);
  const [selectedOptionId, setSelectedOptionId] = useState<string | null>(null);
  const [multiSelectedOptionIds, setMultiSelectedOptionIds] = useState<string[]>([]);
  const [activeTierTab, setActiveTierTab] = useState<'all' | 'Strong alignment' | 'Worth exploring' | 'Possible fit'>('all');
  const [searchSkillQuery, setSearchSkillQuery] = useState('');
  
  const [riasecTotals, setRiasecTotals] = useState<Record<string, number>>({
    R: 0,
    I: 0,
    A: 0,
    S: 0,
    E: 0,
    C: 0,
  });
  const [selectedSkills, setSelectedSkills] = useState<string[]>([]);
  const [workPreferences, setWorkPreferences] = useState<string[]>([]);
  const [careerPriorities, setCareerPriorities] = useState<string[]>([]);
  const [educationBackground, setEducationBackground] = useState<string>('');
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

  const handleSingleSelect = (option: any) => {
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

      if (currentQuestion.category === 'work_preferences' && option.preference) {
        setWorkPreferences((prev) => [...prev, option.preference]);
      }
      if (currentQuestion.category === 'background') {
        setEducationBackground(option.text);
      }

      setIsTransitioning(true);
      setTimeout(() => {
        if (currentQIndex < ASSESSMENT_QUESTIONS.length - 1) {
          setCurrentQIndex(currentQIndex + 1);
          setSelectedOptionId(null);
          setMultiSelectedOptionIds([]);
        } else {
          // Go to skills selection step
          setStep('skills');
        }
        setIsTransitioning(false);
      }, 200);
    }, 280);
  };

  const handleMultiSelectToggle = (optionId: string, maxSelect: number = 3) => {
    setMultiSelectedOptionIds((prev) => {
      if (prev.includes(optionId)) {
        return prev.filter((id) => id !== optionId);
      }
      if (prev.length >= maxSelect) {
        return [...prev.slice(1), optionId];
      }
      return [...prev, optionId];
    });
  };

  const handleMultiSelectConfirm = () => {
    if (currentQuestion.category === 'priorities') {
      const selectedTexts = currentQuestion.options
        .filter((o) => multiSelectedOptionIds.includes(o.id))
        .map((o) => o.text);
      setCareerPriorities(selectedTexts);
    }

    setIsTransitioning(true);
    setTimeout(() => {
      if (currentQIndex < ASSESSMENT_QUESTIONS.length - 1) {
        setCurrentQIndex(currentQIndex + 1);
        setSelectedOptionId(null);
        setMultiSelectedOptionIds([]);
      } else {
        setStep('skills');
      }
      setIsTransitioning(false);
    }, 200);
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

    // Compute explainable qualitative matches across all multi-domain careers
    const matched = careers.map((career) => {
      // 1. RIASEC Alignment
      let traitPoints = 0;
      career.riasec_traits.forEach((trait, idx) => {
        const dimScore = riasecTotals[trait] || 0;
        const weight = 1.0 - idx * 0.15;
        traitPoints += dimScore * weight;
      });
      const maxPossible = career.riasec_traits.reduce((acc, _, idx) => acc + 9 * (1.0 - idx * 0.15), 0) || 9;
      const riasecNorm = Math.min(100, Math.round((traitPoints / maxPossible) * 100));

      // 2. Skill Overlap & Gaps
      const knownSkills = career.core_skills.filter((s) =>
        selectedSkills.some((u) => s.toLowerCase().includes(u.toLowerCase()) || u.toLowerCase().includes(s.toLowerCase()))
      );
      const skillsToDevelop = career.core_skills.filter((s) => !knownSkills.includes(s));
      const skillRatio = knownSkills.length / Math.max(1, career.core_skills.length);
      const compositeScore = Math.round(riasecNorm * 0.65 + skillRatio * 35);

      // Qualitative Tier Classification
      let tier: 'Strong alignment' | 'Worth exploring' | 'Possible fit' = 'Possible fit';
      if (compositeScore >= 65 || (riasecNorm >= 60 && career.riasec_traits.some((t) => topTraits.slice(0, 2).includes(t)))) {
        tier = 'Strong alignment';
      } else if (compositeScore >= 40 || riasecNorm >= 45) {
        tier = 'Worth exploring';
      }

      // Natural language explanation
      const traitNames: Record<string, string> = {
        R: 'practical, hands-on problem solving (Realistic)',
        I: 'analytical inquiry and systematic research (Investigative)',
        A: 'creative craft, visual expression, and human empathy (Artistic)',
        S: 'teaching, mentoring, and direct healthcare/service (Social)',
        E: 'strategic leadership, initiatives, and business growth (Enterprising)',
        C: 'procedural precision, financial accuracy, and standards (Conventional)',
      };

      const reasons: string[] = [];
      if (career.riasec_traits.length > 0 && traitNames[career.riasec_traits[0]]) {
        reasons.push(`Strongly connects with your interest in ${traitNames[career.riasec_traits[0]]}.`);
      }
      if (knownSkills.length > 0) {
        reasons.push(`Directly leverages your current skills: ${knownSkills.slice(0, 3).join(', ')}.`);
      } else {
        reasons.push(`A rewarding domain where your problem-solving style provides a natural advantage.`);
      }

      return {
        careerId: career.id,
        matchScore: compositeScore,
        alignmentTier: tier,
        reasons,
        knownSkills,
        skillsToDevelop,
        breakdown: {
          interests: riasecNorm,
          skills: Math.round(skillRatio * 100),
        },
      };
    });

    // Sort by tier priority then score
    const tierOrder = { 'Strong alignment': 3, 'Worth exploring': 2, 'Possible fit': 1 };
    matched.sort((a, b) => {
      const pDiff = (tierOrder[b.alignmentTier || 'Possible fit'] || 0) - (tierOrder[a.alignmentTier || 'Possible fit'] || 0);
      if (pDiff !== 0) return pDiff;
      return b.matchScore - a.matchScore;
    });

    saveAssessment({
      completedAt: new Date().toISOString(),
      riasecScores: riasecTotals,
      topTraits,
      selectedSkills,
      matchedCareers: matched,
    });

    setStep('results');
  };

  const handleRetake = async () => {
    await clearAssessment();
    setRiasecTotals({ R: 0, I: 0, A: 0, S: 0, E: 0, C: 0 });
    setSelectedSkills([]);
    setWorkPreferences([]);
    setCareerPriorities([]);
    setEducationBackground('');
    setCurrentQIndex(0);
    setSelectedOptionId(null);
    setMultiSelectedOptionIds([]);
    setStep('questions');
  };

  const questionProgress = Math.round(((currentQIndex + 1) / ASSESSMENT_QUESTIONS.length) * 100);

  // Filter matched careers by active tab in Results step
  const matchedList = (assessmentResults?.matchedCareers || []).map((m) => {
    const career = careers.find((c) => c.id === m.careerId);
    return {
      ...career!,
      matchScore: m.matchScore,
      alignmentTier: m.alignmentTier || 'Possible fit',
      reasons: m.reasons || [],
      knownSkills: m.knownSkills || [],
      skillsToDevelop: m.skillsToDevelop || [],
    };
  }).filter((c) => Boolean(c && c.id));

  const filteredCareers = activeTierTab === 'all'
    ? matchedList
    : matchedList.filter((c) => c.alignmentTier === activeTierTab);

  return (
    <AppShell>
      <div ref={containerRef} style={{ maxWidth: 960, margin: '0 auto', padding: '40px 24px 100px' }}>
        
        {/* Step 1: Introduction */}
        {step === 'intro' && (
          <div style={{ textAlign: 'center', maxWidth: 680, margin: '60px auto 0' }}>
            <h1
              style={{
                fontFamily: 'var(--font-display)',
                fontSize: 'clamp(32px, 5vw, 48px)',
                fontWeight: 400,
                letterSpacing: '-0.025em',
                lineHeight: 1.18,
                color: 'var(--foreground)',
                marginBottom: 20,
              }}
            >
              Discover where your curiosity, skills, and strengths truly fit.
            </h1>

            <p style={{ fontSize: 17, color: 'var(--muted-foreground)', lineHeight: 1.65, marginBottom: 36 }}>
              A holistic discovery experience designed to understand your natural interests, practical strengths, and work preferences. Clear, honest guidance without artificial match percentages.
            </p>

            <div style={{ display: 'flex', justifyContent: 'center', gap: 16, flexWrap: 'wrap', marginBottom: 44 }}>
              <div style={{ background: 'var(--card)', border: '1px solid var(--border)', borderRadius: 'var(--radius)', padding: '12px 18px', fontSize: 13, color: 'var(--foreground)', textAlign: 'left' }}>
                <span style={{ fontWeight: 600, display: 'block', color: 'var(--navy)' }}>Interest Profile</span>
                <span style={{ color: 'var(--muted-foreground)' }}>Understand work that naturally energizes you</span>
              </div>
              <div style={{ background: 'var(--card)', border: '1px solid var(--border)', borderRadius: 'var(--radius)', padding: '12px 18px', fontSize: 13, color: 'var(--foreground)', textAlign: 'left' }}>
                <span style={{ fontWeight: 600, display: 'block', color: 'var(--navy)' }}>Skills & Strengths</span>
                <span style={{ color: 'var(--muted-foreground)' }}>Recognize your existing capabilities</span>
              </div>
              <div style={{ background: 'var(--card)', border: '1px solid var(--border)', borderRadius: 'var(--radius)', padding: '12px 18px', fontSize: 13, color: 'var(--foreground)', textAlign: 'left' }}>
                <span style={{ fontWeight: 600, display: 'block', color: 'var(--navy)' }}>Clear Pathways</span>
                <span style={{ color: 'var(--muted-foreground)' }}>Step-by-step guidance to reach your goals</span>
              </div>
            </div>

            <button
              onClick={() => setStep('questions')}
              style={{
                background: 'var(--primary)',
                color: 'white',
                border: 'none',
                borderRadius: 'var(--radius)',
                padding: '16px 40px',
                fontSize: 16,
                fontWeight: 600,
                cursor: 'pointer',
                fontFamily: 'var(--font-body)',
                boxShadow: '0 4px 14px rgba(26,31,46,0.12)',
                transition: 'all 0.2s ease',
              }}
              onMouseEnter={(e) => { e.currentTarget.style.opacity = '0.9'; }}
              onMouseLeave={(e) => { e.currentTarget.style.opacity = '1'; }}
            >
              Start Career Assessment →
            </button>
          </div>
        )}

        {/* Step 2: Assessment Questions */}
        {step === 'questions' && currentQuestion && (
          <div>
            <div style={{ marginBottom: 36 }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 12 }}>
                <span style={{ fontSize: 12, fontWeight: 700, letterSpacing: '0.08em', textTransform: 'uppercase', color: 'var(--muted-foreground)' }}>
                  Question {currentQIndex + 1} of {ASSESSMENT_QUESTIONS.length}
                </span>
                <span style={{ fontSize: 12, color: 'var(--navy)', fontWeight: 600, background: 'var(--secondary)', padding: '3px 10px', borderRadius: 12 }}>
                  {currentQuestion.dimension}
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
                    transition: 'width 0.3s ease',
                  }}
                />
              </div>
            </div>

            <div
              style={{
                opacity: isTransitioning ? 0 : 1,
                transform: isTransitioning ? 'translateY(6px)' : 'translateY(0)',
                transition: 'all 0.2s ease',
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
                <p style={{ fontSize: 15, color: 'var(--muted-foreground)', marginBottom: 28 }}>
                  {currentQuestion.subtitle}
                </p>
              )}

              {/* Options rendering: Single choice vs Multi select */}
              {currentQuestion.type === 'single_choice' ? (
                <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
                  {currentQuestion.options.map((opt) => {
                    const isSelected = selectedOptionId === opt.id;
                    return (
                      <button
                        key={opt.id}
                        onClick={() => handleSingleSelect(opt)}
                        style={{
                          background: isSelected ? 'var(--secondary)' : 'var(--card)',
                          border: isSelected ? '1.5px solid var(--navy)' : '1px solid var(--border)',
                          borderRadius: 'calc(var(--radius) * 1.5)',
                          padding: '18px 24px',
                          textAlign: 'left',
                          cursor: 'pointer',
                          fontSize: 15,
                          fontFamily: 'var(--font-body)',
                          color: 'var(--foreground)',
                          lineHeight: 1.5,
                          transition: 'all 0.15s ease',
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
                            transition: 'all 0.15s ease',
                          }}
                        />
                      </button>
                    );
                  })}
                </div>
              ) : (
                /* Multi-Select */
                <div>
                  <div style={{ display: 'flex', flexDirection: 'column', gap: 12, marginBottom: 24 }}>
                    {currentQuestion.options.map((opt) => {
                      const isSelected = multiSelectedOptionIds.includes(opt.id);
                      return (
                        <button
                          key={opt.id}
                          onClick={() => handleMultiSelectToggle(opt.id, currentQuestion.max_select || 3)}
                          style={{
                            background: isSelected ? 'var(--secondary)' : 'var(--card)',
                            border: isSelected ? '1.5px solid var(--navy)' : '1px solid var(--border)',
                            borderRadius: 'calc(var(--radius) * 1.5)',
                            padding: '16px 22px',
                            textAlign: 'left',
                            cursor: 'pointer',
                            fontSize: 15,
                            fontFamily: 'var(--font-body)',
                            color: 'var(--foreground)',
                            display: 'flex',
                            alignItems: 'center',
                            justifyContent: 'space-between',
                          }}
                        >
                          <span>{opt.text}</span>
                          <div
                            style={{
                              width: 20,
                              height: 20,
                              borderRadius: 4,
                              border: isSelected ? 'none' : '1.5px solid var(--border)',
                              background: isSelected ? 'var(--navy)' : 'white',
                              color: 'white',
                              display: 'flex',
                              alignItems: 'center',
                              justifyContent: 'center',
                              fontSize: 12,
                              fontWeight: 'bold',
                            }}
                          >
                            {isSelected ? '✓' : ''}
                          </div>
                        </button>
                      );
                    })}
                  </div>

                  <div style={{ display: 'flex', justifyContent: 'flex-end' }}>
                    <button
                      onClick={handleMultiSelectConfirm}
                      disabled={multiSelectedOptionIds.length === 0}
                      style={{
                        background: multiSelectedOptionIds.length > 0 ? 'var(--primary)' : 'var(--border)',
                        color: 'white',
                        border: 'none',
                        borderRadius: 'var(--radius)',
                        padding: '12px 28px',
                        fontSize: 14,
                        fontWeight: 600,
                        cursor: multiSelectedOptionIds.length > 0 ? 'pointer' : 'not-allowed',
                      }}
                    >
                      Continue ({multiSelectedOptionIds.length}/{currentQuestion.max_select || 3}) →
                    </button>
                  </div>
                </div>
              )}
            </div>
          </div>
        )}

        {/* Step 3: Multi-Domain Skills Selection */}
        {step === 'skills' && (
          <div>
            <div style={{ marginBottom: 32 }}>
              <p style={{ fontSize: 12, fontWeight: 700, letterSpacing: '0.08em', textTransform: 'uppercase', color: 'var(--muted-foreground)', marginBottom: 6 }}>
                Section 2: Multi-Domain Skills & Tools
              </p>
              <h2 style={{ fontFamily: 'var(--font-display)', fontSize: 'clamp(26px, 4vw, 36px)', fontWeight: 400, color: 'var(--foreground)', marginBottom: 10 }}>
                Select your existing skills or domains of interest.
              </h2>
              <p style={{ fontSize: 15, color: 'var(--muted-foreground)', marginBottom: 20 }}>
                Choose any technical tools, software, or practical proficiencies you know (or leave blank if starting fresh).
              </p>

              {/* Search filter for skills */}
              <input
                type="text"
                placeholder="Search skills (e.g., Python, Figma, Accounting, Patient Care, AutoCAD)..."
                value={searchSkillQuery}
                onChange={(e) => setSearchSkillQuery(e.target.value)}
                style={{
                  width: '100%',
                  padding: '12px 18px',
                  borderRadius: 'var(--radius)',
                  border: '1px solid var(--border)',
                  fontSize: 14,
                  fontFamily: 'var(--font-body)',
                  background: 'var(--card)',
                  color: 'var(--foreground)',
                }}
              />
            </div>

            <div style={{ display: 'flex', flexDirection: 'column', gap: 20, marginBottom: 40 }}>
              {Object.entries(SKILL_CATEGORIES).map(([categoryName, skillsList]) => {
                const filtered = searchSkillQuery.trim()
                  ? skillsList.filter((s) => s.toLowerCase().includes(searchSkillQuery.toLowerCase()))
                  : skillsList;

                if (filtered.length === 0) return null;

                return (
                  <div key={categoryName} style={{ background: 'var(--card)', border: '1px solid var(--border)', borderRadius: 'calc(var(--radius) * 1.5)', padding: '18px 22px' }}>
                    <h4 style={{ fontSize: 13, fontWeight: 700, color: 'var(--navy)', marginBottom: 12, textTransform: 'uppercase', letterSpacing: '0.05em' }}>
                      {categoryName}
                    </h4>
                    <div style={{ display: 'flex', flexWrap: 'wrap', gap: 8 }}>
                      {filtered.map((skill) => {
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
                );
              })}
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
              >
                Generate Career Matches & Explanations →
              </button>
            </div>
          </div>
        )}

        {/* Step 4: Results View */}
        {step === 'results' && (
          <div>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: 36, flexWrap: 'wrap', gap: 16 }}>
              <div>
                <p style={{ fontSize: 12, fontWeight: 700, letterSpacing: '0.08em', textTransform: 'uppercase', color: 'var(--muted-foreground)', marginBottom: 6 }}>
                  Verified Career Intelligence
                </p>
                <h1 style={{ fontFamily: 'var(--font-display)', fontSize: 'clamp(28px, 4.5vw, 40px)', fontWeight: 400, color: 'var(--foreground)', margin: 0, letterSpacing: '-0.025em' }}>
                  Your Career Possibilities & Alignment Tiers
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
                }}
              >
                Retake Assessment
              </button>
            </div>

            {/* RIASEC Archetype Summary */}
            {assessmentResults?.topTraits && (
              <div
                style={{
                  background: 'var(--card)',
                  border: '1px solid var(--border)',
                  borderRadius: 'calc(var(--radius) * 1.5)',
                  padding: '24px',
                  marginBottom: 32,
                }}
              >
                <span style={{ fontSize: 12, fontWeight: 700, color: 'var(--muted-foreground)', textTransform: 'uppercase', letterSpacing: '0.06em', display: 'block', marginBottom: 12 }}>
                  Your Core Interest Themes:
                </span>
                <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(260px, 1fr))', gap: 16 }}>
                  {assessmentResults.topTraits.map((t) => {
                    const desc = RIASEC_DESCRIPTIONS[t];
                    if (!desc) return null;
                    return (
                      <div key={t} style={{ background: '#FAF9F6', border: '1px solid var(--border)', borderRadius: 'var(--radius)', padding: '14px 16px' }}>
                        <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 4 }}>
                          <span style={{ fontWeight: 700, fontSize: 14, color: 'var(--navy)' }}>
                            {t} · {desc.title}
                          </span>
                          <span style={{ fontSize: 11, color: 'var(--muted-foreground)' }}>({desc.subtitle})</span>
                        </div>
                        <p style={{ fontSize: 13, color: 'var(--muted-foreground)', lineHeight: 1.5, margin: 0 }}>
                          {desc.description}
                        </p>
                      </div>
                    );
                  })}
                </div>
              </div>
            )}

            {/* Tier Filter Tabs */}
            <div style={{ display: 'flex', gap: 8, marginBottom: 24, overflowX: 'auto', paddingBottom: 4 }}>
              {(['all', 'Strong alignment', 'Worth exploring', 'Possible fit'] as const).map((tab) => {
                const isCurrent = activeTierTab === tab;
                const count = tab === 'all' ? matchedList.length : matchedList.filter((c) => c.alignmentTier === tab).length;
                return (
                  <button
                    key={tab}
                    onClick={() => setActiveTierTab(tab)}
                    style={{
                      padding: '8px 16px',
                      borderRadius: 20,
                      border: isCurrent ? '1px solid var(--navy)' : '1px solid var(--border)',
                      background: isCurrent ? 'var(--navy)' : 'var(--card)',
                      color: isCurrent ? 'white' : 'var(--foreground)',
                      fontSize: 13,
                      fontWeight: 600,
                      cursor: 'pointer',
                      whiteSpace: 'nowrap',
                      display: 'flex',
                      alignItems: 'center',
                      gap: 6,
                    }}
                  >
                    <span>{tab === 'all' ? 'All Roles' : tab}</span>
                    <span style={{ fontSize: 11, opacity: 0.8 }}>({count})</span>
                  </button>
                );
              })}
            </div>

            {/* Matched Careers List */}
            <div style={{ display: 'flex', flexDirection: 'column', gap: 20 }}>
              {filteredCareers.map((career) => {
                const tierStyles: Record<string, { badgeBg: string; badgeColor: string; borderColor: string }> = {
                  'Strong alignment': { badgeBg: '#ECFDF5', badgeColor: '#065F46', borderColor: '#A7F3D0' },
                  'Worth exploring': { badgeBg: '#EFF6FF', badgeColor: '#1E40AF', borderColor: '#BFDBFE' },
                  'Possible fit': { badgeBg: '#F8FAFC', badgeColor: '#475569', borderColor: '#E2E8F0' },
                };
                const style = tierStyles[career.alignmentTier] || tierStyles['Possible fit'];

                return (
                  <div
                    key={career.id}
                    style={{
                      background: 'var(--card)',
                      border: '1px solid var(--border)',
                      borderRadius: 'calc(var(--radius) * 2)',
                      padding: '26px',
                      transition: 'all 0.2s ease',
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
                    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: 12, gap: 16, flexWrap: 'wrap' }}>
                      <div>
                        <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 4, flexWrap: 'wrap' }}>
                          <span
                            style={{
                              fontSize: 12,
                              fontWeight: 700,
                              padding: '3px 10px',
                              borderRadius: 12,
                              background: style.badgeBg,
                              color: style.badgeColor,
                              border: `1px solid ${style.borderColor}`,
                            }}
                          >
                            ● {career.alignmentTier}
                          </span>
                          <span style={{ fontSize: 12, color: 'var(--muted-foreground)' }}>
                            {career.category_name}
                          </span>
                        </div>
                        <h3 style={{ fontFamily: 'var(--font-display)', fontSize: 24, fontWeight: 500, color: 'var(--foreground)', margin: '4px 0' }}>
                          {career.title}
                        </h3>
                      </div>
                    </div>

                    <p style={{ fontSize: 14, color: 'var(--muted-foreground)', lineHeight: 1.6, marginBottom: 16 }}>
                      {career.tagline}
                    </p>

                    {/* Explainable Reasons */}
                    {career.reasons && career.reasons.length > 0 && (
                      <div style={{ background: '#FAF9F6', border: '1px solid var(--border)', borderRadius: 'var(--radius)', padding: '12px 16px', marginBottom: 18 }}>
                        <span style={{ fontSize: 11, fontWeight: 700, textTransform: 'uppercase', color: 'var(--navy)', letterSpacing: '0.05em', display: 'block', marginBottom: 6 }}>
                          Why this matches your profile:
                        </span>
                        <ul style={{ margin: 0, paddingLeft: 18, fontSize: 13, color: 'var(--foreground)', lineHeight: 1.5 }}>
                          {career.reasons.map((r, idx) => (
                            <li key={idx} style={{ marginBottom: 4 }}>{r}</li>
                          ))}
                        </ul>
                      </div>
                    )}

                    {/* Skill Gap Analysis summary */}
                    <div style={{ display: 'flex', gap: 16, flexWrap: 'wrap', marginBottom: 20, fontSize: 13 }}>
                      {career.knownSkills && career.knownSkills.length > 0 && (
                        <div>
                          <span style={{ color: 'var(--muted-foreground)' }}>Existing Strengths: </span>
                          <span style={{ fontWeight: 600, color: '#065F46' }}>{career.knownSkills.slice(0, 3).join(', ')}</span>
                        </div>
                      )}
                      {career.skillsToDevelop && career.skillsToDevelop.length > 0 && (
                        <div>
                          <span style={{ color: 'var(--muted-foreground)' }}>Skills to Develop in Pathway: </span>
                          <span style={{ fontWeight: 600, color: 'var(--navy)' }}>{career.skillsToDevelop.slice(0, 3).join(', ')}</span>
                        </div>
                      )}
                    </div>

                    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', paddingTop: 16, borderTop: '1px solid var(--border)', flexWrap: 'wrap', gap: 12 }}>
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
                            navigate(`/career/${career.id}`);
                          }}
                          style={{
                            background: 'transparent',
                            border: '1px solid var(--border)',
                            borderRadius: 'var(--radius)',
                            padding: '8px 16px',
                            fontSize: 13,
                            fontWeight: 500,
                            cursor: 'pointer',
                            color: 'var(--foreground)',
                          }}
                        >
                          Explore Details
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
                          }}
                        >
                          Start My Path →
                        </button>
                      </div>
                    </div>
                  </div>
                );
              })}
            </div>
          </div>
        )}
      </div>
      <TOBEWidget />
    </AppShell>
  );
}
