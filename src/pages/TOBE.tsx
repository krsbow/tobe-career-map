import { useState, useRef, useEffect } from 'react';
import { useSearchParams } from 'react-router-dom';
import AppShell from '../components/AppShell';
import { useAuth } from '../context/AuthContext';
import { useCareer } from '../context/CareerContext';
import { Career } from '../data/careersData';
import {
  guidedMentorEngine,
  QuestionIntentDef,
  GuidedTurn,
} from '../services/guidedMentorService';
import { mentorService } from '../services/mentorService';

export default function TOBE() {
  const { user } = useAuth();
  const { activeRoadmap, assessmentResults, careers } = useCareer();
  const [searchParams, setSearchParams] = useSearchParams();
  const careerParam = searchParams.get('career');

  const selectedCareer: Career | undefined = careerParam
    ? careers.find((c) => c.id === careerParam)
    : activeRoadmap
    ? careers.find((c) => c.id === activeRoadmap.careerId)
    : careers[0]; // fallback default to first career if nothing specified

  const activeCareerObj: Career | undefined = selectedCareer || careers[0];

  const [sessionId, setSessionId] = useState<string>('guided-session');
  const [exploredIntents, setExploredIntents] = useState<string[]>([]);
  const [turns, setTurns] = useState<GuidedTurn[]>([]);
  const [availableQuestions, setAvailableQuestions] = useState<QuestionIntentDef[]>([]);
  const [isChangingCareer, setIsChangingCareer] = useState<boolean>(false);

  const bottomRef = useRef<HTMLDivElement>(null);

  // Initialize session in Supabase if authenticated
  useEffect(() => {
    if (user?.id) {
      mentorService.getOrCreateSession(user.id).then((id) => setSessionId(id));
    }
  }, [user?.id]);

  // Reset/Initialize guided flow whenever active career changes
  useEffect(() => {
    if (!activeCareerObj) return;

    const initialQuestions = guidedMentorEngine.getInitialQuestions(activeCareerObj);
    const greeting = user?.name
      ? `Hi ${user.name}. I'm TOBE, your career mentor.`
      : "Hi there. I'm TOBE, your career mentor.";

    let intro = `Let's explore the ${activeCareerObj.title} path together.`;
    if (assessmentResults?.topTraits?.length) {
      intro += ` Your assessment highlighted interests in ${assessmentResults.topTraits.slice(0, 2).join(' and ')}, making this a relevant pathway to inspect.`;
    }

    const firstTurn: GuidedTurn = {
      id: `turn-intro-${Date.now()}`,
      from: 'tobe',
      text: `${greeting}\n\n${intro}`,
      timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
    };

    setTurns([firstTurn]);
    setExploredIntents([]);
    setAvailableQuestions(initialQuestions);
    setIsChangingCareer(false);
  }, [activeCareerObj?.id]);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [turns, availableQuestions]);

  const handleSelectQuestion = (qDef: QuestionIntentDef) => {
    if (!activeCareerObj) return;

    const questionText = qDef.getQuestionText(activeCareerObj);
    const userTurn: GuidedTurn = {
      id: `user-${Date.now()}`,
      from: 'user',
      intent: qDef.intent,
      category: qDef.category,
      text: questionText,
      timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
    };

    const userCtx = {
      preferredName: user?.name,
      topTraits: assessmentResults?.topTraits,
      selectedSkills: assessmentResults?.selectedSkills,
      activeCareerId: activeCareerObj.id,
      activeRoadmapProgress: activeRoadmap
        ? {
            completedCount: activeRoadmap.milestones.reduce(
              (acc, m) => acc + m.tasks.filter((t) => t.completed).length,
              0
            ),
            totalCount: activeRoadmap.milestones.reduce((acc, m) => acc + m.tasks.length, 0),
            percentage: Math.round(
              (activeRoadmap.milestones.reduce(
                (acc, m) => acc + m.tasks.filter((t) => t.completed).length,
                0
              ) /
                Math.max(
                  1,
                  activeRoadmap.milestones.reduce((acc, m) => acc + m.tasks.length, 0)
                )) *
                100
            ),
          }
        : undefined,
    };

    const answerText = guidedMentorEngine.generateAnswer(qDef.intent, activeCareerObj, userCtx);
    const tobeTurn: GuidedTurn = {
      id: `tobe-${Date.now()}`,
      from: 'tobe',
      intent: qDef.intent,
      category: qDef.category,
      text: answerText,
      timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
    };

    const updatedExplored = [...exploredIntents, qDef.intent];
    setExploredIntents(updatedExplored);
    setTurns((prev) => [...prev, userTurn, tobeTurn]);

    if (user?.id) {
      mentorService.saveMessageToSupabase(user.id, sessionId, 'user', questionText);
      mentorService.saveMessageToSupabase(user.id, sessionId, 'assistant', answerText);
    }

    const nextQs = guidedMentorEngine.getNextQuestions(activeCareerObj, updatedExplored);
    setAvailableQuestions(nextQs);
  };

  const handleSwitchCareer = (newCareerId: string) => {
    setSearchParams({ career: newCareerId });
    setIsChangingCareer(false);
  };

  return (
    <AppShell>
      <div
        style={{
          maxWidth: 860,
          margin: '0 auto',
          padding: '0 24px',
          display: 'flex',
          flexDirection: 'column',
          height: 'calc(100vh - 65px)',
        }}
      >
        {/* Top Header & Career Switcher */}
        <div
          style={{
            padding: '16px 0',
            borderBottom: '1px solid var(--border)',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'space-between',
            flexShrink: 0,
          }}
        >
          <div style={{ display: 'flex', alignItems: 'center', gap: 14 }}>
            <div
              style={{
                width: 42,
                height: 42,
                borderRadius: 'var(--radius)',
                background: 'var(--primary)',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                color: 'var(--sage)',
              }}
            >
              <svg width="22" height="22" viewBox="0 0 20 20" fill="none">
                <circle cx="10" cy="10" r="8" stroke="rgba(255,255,255,0.35)" strokeWidth="1.5" />
                <circle cx="10" cy="10" r="4.5" stroke="white" strokeWidth="1.5" />
                <circle cx="10" cy="10" r="2" fill="var(--sage)" />
              </svg>
            </div>
            <div>
              <div style={{ fontSize: 17, fontWeight: 600, color: 'var(--foreground)' }}>
                TOBE Career Mentor
              </div>
              <div style={{ fontSize: 12, color: 'var(--muted-foreground)' }}>
                {activeCareerObj ? `Focusing on ${activeCareerObj.title}` : 'Career Guidance'}
              </div>
            </div>
          </div>

          {/* Active Career Control */}
          {activeCareerObj && (
            <div style={{ display: 'flex', alignItems: 'center', gap: 10 }}>
              <div
                style={{
                  fontSize: 12,
                  fontWeight: 600,
                  color: 'var(--navy)',
                  background: 'var(--secondary)',
                  padding: '5px 12px',
                  borderRadius: 6,
                }}
              >
                {activeCareerObj.title}
              </div>
              <button
                onClick={() => setIsChangingCareer(!isChangingCareer)}
                style={{
                  background: 'transparent',
                  border: '1px solid var(--border)',
                  color: 'var(--muted-foreground)',
                  padding: '5px 10px',
                  borderRadius: 6,
                  fontSize: 12,
                  fontWeight: 500,
                  cursor: 'pointer',
                  fontFamily: 'var(--font-body)',
                }}
              >
                {isChangingCareer ? 'Cancel' : 'Change Career'}
              </button>
            </div>
          )}
        </div>

        {/* Quick Career Selector Dropdown */}
        {isChangingCareer && (
          <div
            style={{
              padding: '14px 18px',
              background: 'var(--card)',
              borderBottom: '1px solid var(--border)',
              display: 'flex',
              alignItems: 'center',
              gap: 12,
              flexWrap: 'wrap',
            }}
          >
            <span style={{ fontSize: 13, fontWeight: 600, color: 'var(--foreground)' }}>
              Select Career:
            </span>
            <select
              value={activeCareerObj?.id || ''}
              onChange={(e) => handleSwitchCareer(e.target.value)}
              style={{
                padding: '6px 12px',
                borderRadius: 6,
                border: '1px solid var(--border)',
                background: 'var(--background)',
                color: 'var(--foreground)',
                fontSize: 13,
                fontFamily: 'var(--font-body)',
                cursor: 'pointer',
              }}
            >
              {careers.map((c) => (
                <option key={c.id} value={c.id}>
                  {c.title} ({c.field})
                </option>
              ))}
            </select>
          </div>
        )}

        {/* Conversation Flow */}
        <div
          style={{
            flex: 1,
            overflowY: 'auto',
            padding: '24px 0',
            display: 'flex',
            flexDirection: 'column',
            gap: 20,
          }}
        >
          {turns.map((t) => (
            <div
              key={t.id}
              style={{
                display: 'flex',
                flexDirection: 'column',
                alignItems: t.from === 'user' ? 'flex-end' : 'flex-start',
                maxWidth: '100%',
              }}
            >
              <div
                style={{
                  display: 'flex',
                  gap: 12,
                  justifyContent: t.from === 'user' ? 'flex-end' : 'flex-start',
                  maxWidth: '100%',
                }}
              >
                {t.from === 'tobe' && (
                  <div
                    style={{
                      width: 32,
                      height: 32,
                      borderRadius: 'var(--radius)',
                      background: 'var(--secondary)',
                      color: 'var(--navy)',
                      display: 'flex',
                      alignItems: 'center',
                      justifyContent: 'center',
                      fontSize: 13,
                      fontWeight: 700,
                      flexShrink: 0,
                    }}
                  >
                    T
                  </div>
                )}
                <div
                  style={{
                    maxWidth: '82%',
                    background: t.from === 'user' ? 'var(--navy)' : 'var(--card)',
                    color: t.from === 'user' ? 'white' : 'var(--foreground)',
                    border: t.from === 'user' ? 'none' : '1px solid var(--border)',
                    borderRadius: 'calc(var(--radius) * 1.5)',
                    padding: '16px 20px',
                    fontSize: 15,
                    lineHeight: 1.65,
                    fontFamily: 'var(--font-body)',
                    whiteSpace: 'pre-line',
                    boxShadow: '0 2px 8px rgba(0,0,0,0.02)',
                  }}
                >
                  <div>{t.text}</div>
                </div>
              </div>
            </div>
          ))}

          <div ref={bottomRef} />
        </div>

        {/* Natural Question Choices (Chips) */}
        {availableQuestions.length > 0 && (
          <div
            style={{
              padding: '16px 0 24px',
              borderTop: '1px solid var(--border)',
              flexShrink: 0,
              display: 'flex',
              flexDirection: 'column',
              gap: 10,
            }}
          >
            <div
              style={{
                display: 'flex',
                gap: 10,
                flexWrap: 'wrap',
              }}
            >
              {availableQuestions.map((qDef) => {
                const questionText = activeCareerObj ? qDef.getQuestionText(activeCareerObj) : '';
                return (
                  <button
                    key={qDef.intent}
                    onClick={() => handleSelectQuestion(qDef)}
                    style={{
                      background: 'var(--card)',
                      border: '1px solid var(--border)',
                      borderRadius: 'calc(var(--radius) * 1.5)',
                      padding: '11px 18px',
                      fontSize: 13.5,
                      fontWeight: 500,
                      color: 'var(--foreground)',
                      cursor: 'pointer',
                      fontFamily: 'var(--font-body)',
                      display: 'flex',
                      alignItems: 'center',
                      transition: 'all 0.15s ease',
                      boxShadow: '0 1px 3px rgba(0,0,0,0.02)',
                      textAlign: 'left',
                    }}
                    onMouseEnter={(e) => {
                      e.currentTarget.style.borderColor = 'var(--navy)';
                      e.currentTarget.style.color = 'var(--navy)';
                      e.currentTarget.style.transform = 'translateY(-1px)';
                      e.currentTarget.style.boxShadow = '0 4px 12px rgba(26,31,46,0.06)';
                    }}
                    onMouseLeave={(e) => {
                      e.currentTarget.style.borderColor = 'var(--border)';
                      e.currentTarget.style.color = 'var(--foreground)';
                      e.currentTarget.style.transform = 'translateY(0)';
                      e.currentTarget.style.boxShadow = '0 1px 3px rgba(0,0,0,0.02)';
                    }}
                  >
                    <span>{questionText}</span>
                  </button>
                );
              })}
            </div>
          </div>
        )}
      </div>
    </AppShell>
  );
}
