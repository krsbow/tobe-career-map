import { useState, useEffect, useRef } from 'react';
import { createPortal } from 'react-dom';
import { useNavigate } from 'react-router-dom';
import AppShell from '../components/AppShell';
import TOBEWidget from '../components/TOBEWidget';
import { useAuth } from '../context/AuthContext';
import { useCareer } from '../context/CareerContext';

export default function MyPath() {
  const { user } = useAuth();
  const navigate = useNavigate();
  const {
    careers,
    roadmaps,
    activeRoadmap,
    savedCareerIds,
    careerNotes,
    toggleRoadmapTask,
    addCareerNote,
    deleteCareerNote,
    createOrSetRoadmap,
    switchActiveRoadmap,
    deleteRoadmap,
  } = useCareer();

  const containerRef = useRef<HTMLDivElement>(null);
  const [noteTitle, setNoteTitle] = useState('');
  const [noteContent, setNoteContent] = useState('');
  const [savedNotesToast, setSavedNotesToast] = useState(false);

  // Multi-pathway modal states
  const [showAddModal, setShowAddModal] = useState(false);
  const [showDeleteConfirm, setShowDeleteConfirm] = useState(false);
  const [searchCareerQuery, setSearchCareerQuery] = useState('');

  useEffect(() => {
    if (!containerRef.current) return;
    const observer = new IntersectionObserver(
      (entries) => entries.forEach((e) => e.isIntersecting && e.target.classList.add('visible')),
      { threshold: 0.08 }
    );
    containerRef.current.querySelectorAll('.reveal').forEach((el) => observer.observe(el));
    return () => observer.disconnect();
  }, [activeRoadmap, careerNotes]);

  const handleSaveNote = () => {
    if (!noteContent.trim()) return;
    addCareerNote(
      noteContent,
      noteTitle.trim() || undefined,
      activeRoadmap?.careerId,
      activeRoadmap?.careerTitle
    );
    setNoteTitle('');
    setNoteContent('');
    setSavedNotesToast(true);
    setTimeout(() => setSavedNotesToast(false), 2500);
  };

  // Saved careers resolution
  const savedCareersList = savedCareerIds
    .map((id) => careers.find((c) => c.id === id))
    .filter(Boolean);

  // Compute live progress
  const totalTasks = activeRoadmap
    ? activeRoadmap.milestones.reduce((sum, m) => sum + m.tasks.length, 0)
    : 0;
  const completedTasks = activeRoadmap
    ? activeRoadmap.milestones.reduce(
        (sum, m) => sum + m.tasks.filter((t) => t.completed).length,
        0
      )
    : 0;
  const progressPercent = totalTasks > 0 ? Math.round((completedTasks / totalTasks) * 100) : 0;
  const completedMilestones = activeRoadmap
    ? activeRoadmap.milestones.filter((m) => m.status === 'done' || m.tasks.every((t) => t.completed)).length
    : 0;

  // Filter available careers for modal
  const filteredCareers = careers.filter((c) => {
    const matchesSearch =
      c.title.toLowerCase().includes(searchCareerQuery.toLowerCase()) ||
      c.category_name.toLowerCase().includes(searchCareerQuery.toLowerCase()) ||
      c.core_skills.some((s) => s.toLowerCase().includes(searchCareerQuery.toLowerCase()));
    return matchesSearch;
  });

  return (
    <AppShell>
      <div ref={containerRef} style={{ maxWidth: 1040, margin: '0 auto', padding: '56px 32px 80px' }}>
        {/* Header */}
        <div className="reveal" style={{ marginBottom: 32 }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 8, flexWrap: 'wrap', gap: 12 }}>
            <p style={{ fontSize: 13, fontWeight: 600, letterSpacing: '0.08em', textTransform: 'uppercase', color: 'var(--muted-foreground)', margin: 0 }}>
              My Pathways ({roadmaps.length})
            </p>
            {activeRoadmap && (
              <div style={{ display: 'flex', gap: 10 }}>
                <button
                  onClick={() => setShowAddModal(true)}
                  style={{
                    background: 'var(--navy)',
                    color: 'white',
                    border: 'none',
                    borderRadius: 'var(--radius)',
                    padding: '8px 16px',
                    fontSize: 13,
                    fontWeight: 500,
                    cursor: 'pointer',
                    fontFamily: 'var(--font-body)',
                    display: 'flex',
                    alignItems: 'center',
                    gap: 6,
                    transition: 'all 0.18s ease',
                  }}
                >
                  <span style={{ fontSize: 16, lineHeight: 1 }}>+</span> Add Another Pathway
                </button>
                <button
                  onClick={() => setShowDeleteConfirm(true)}
                  style={{
                    background: 'transparent',
                    border: '1px solid var(--border)',
                    borderRadius: 'var(--radius)',
                    padding: '8px 14px',
                    fontSize: 13,
                    fontWeight: 500,
                    cursor: 'pointer',
                    fontFamily: 'var(--font-body)',
                    color: 'var(--muted-foreground)',
                    transition: 'all 0.18s ease',
                  }}
                  onMouseEnter={(e) => { e.currentTarget.style.color = '#c53030'; e.currentTarget.style.borderColor = '#c53030'; }}
                  onMouseLeave={(e) => { e.currentTarget.style.color = 'var(--muted-foreground)'; e.currentTarget.style.borderColor = 'var(--border)'; }}
                  title="Remove this active pathway"
                >
                  Remove Pathway
                </button>
              </div>
            )}
          </div>

          <div>
            <h1 style={{ fontFamily: 'var(--font-display)', fontSize: 'clamp(28px, 5vw, 42px)', fontWeight: 400, letterSpacing: '-0.025em', color: 'var(--foreground)', marginBottom: 8 }}>
              {activeRoadmap
                ? `${user?.name || 'Explorer'}'s Pathway: ${activeRoadmap.careerTitle}`
                : `${user?.name || 'Explorer'}'s Career Journey`}
            </h1>
            <p style={{ fontSize: 15, color: 'var(--muted-foreground)' }}>
              {activeRoadmap
                ? `Active pathway initiated on ${activeRoadmap.createdAt}. You can switch between multiple concurrent career roadmaps at any time without losing your progress.`
                : 'Track your career goals, step-by-step milestones, and skills mastery.'}
            </p>
          </div>
        </div>

        {/* Multi-Pathway Segmented Switcher */}
        {roadmaps.length > 0 && (
          <div className="reveal" style={{ marginBottom: 32 }}>
            <div
              style={{
                display: 'flex',
                alignItems: 'center',
                gap: 8,
                overflowX: 'auto',
                paddingBottom: 6,
                scrollbarWidth: 'thin',
              }}
            >
              {roadmaps.map((rm) => {
                const isActive = activeRoadmap?.careerId === rm.careerId;
                const rTotal = rm.milestones.reduce((s, m) => s + m.tasks.length, 0);
                const rDone = rm.milestones.reduce((s, m) => s + m.tasks.filter((t) => t.completed).length, 0);
                const rPercent = rTotal > 0 ? Math.round((rDone / rTotal) * 100) : 0;

                return (
                  <button
                    key={rm.careerId}
                    onClick={() => switchActiveRoadmap(rm.careerId)}
                    style={{
                      display: 'flex',
                      alignItems: 'center',
                      gap: 8,
                      padding: '8px 16px',
                      borderRadius: 100,
                      border: isActive ? '1px solid var(--navy)' : '1px solid var(--border)',
                      background: isActive ? 'var(--navy)' : 'var(--card)',
                      color: isActive ? '#FFFFFF' : 'var(--foreground)',
                      fontSize: 13,
                      fontWeight: 500,
                      cursor: 'pointer',
                      fontFamily: 'var(--font-body)',
                      whiteSpace: 'nowrap',
                      transition: 'all 0.18s ease',
                      boxShadow: isActive ? '0 2px 8px rgba(36,55,96,0.18)' : 'none',
                    }}
                  >
                    <span>{rm.careerTitle}</span>
                    <span
                      style={{
                        fontSize: 11,
                        fontWeight: 600,
                        padding: '2px 8px',
                        borderRadius: 10,
                        background: isActive ? 'rgba(255,255,255,0.2)' : 'var(--secondary)',
                        color: isActive ? '#FFFFFF' : 'var(--navy)',
                      }}
                    >
                      {rPercent}%
                    </span>
                  </button>
                );
              })}

              <button
                onClick={() => setShowAddModal(true)}
                style={{
                  display: 'flex',
                  alignItems: 'center',
                  gap: 6,
                  padding: '8px 14px',
                  borderRadius: 100,
                  border: '1px dashed var(--border)',
                  background: 'transparent',
                  color: 'var(--muted-foreground)',
                  fontSize: 13,
                  fontWeight: 500,
                  cursor: 'pointer',
                  fontFamily: 'var(--font-body)',
                  whiteSpace: 'nowrap',
                  transition: 'all 0.18s ease',
                }}
                onMouseEnter={(e) => {
                  e.currentTarget.style.borderColor = 'var(--navy)';
                  e.currentTarget.style.color = 'var(--navy)';
                }}
                onMouseLeave={(e) => {
                  e.currentTarget.style.borderColor = 'var(--border)';
                  e.currentTarget.style.color = 'var(--muted-foreground)';
                }}
              >
                <span>+ Add Pathway</span>
              </button>
            </div>
          </div>
        )}

        {/* Clean Zero-State for First-Time Users */}
        {!activeRoadmap ? (
          <div className="reveal">
            <div
              style={{
                background: 'var(--card)',
                border: '1px solid var(--border)',
                borderRadius: 'calc(var(--radius) * 2)',
                padding: '48px 36px',
                textAlign: 'center',
                marginBottom: 48,
              }}
            >
              <div
                style={{
                  width: 56,
                  height: 56,
                  borderRadius: '50%',
                  background: 'var(--secondary)',
                  color: 'var(--navy)',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  margin: '0 auto 20px',
                }}
              >
                <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.75">
                  <path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6" />
                </svg>
              </div>

              <h2 style={{ fontFamily: 'var(--font-display)', fontSize: 26, fontWeight: 500, color: 'var(--foreground)', marginBottom: 12 }}>
                No active pathway yet.
              </h2>
              <p style={{ fontSize: 15, color: 'var(--muted-foreground)', maxWidth: 540, margin: '0 auto 32px', lineHeight: 1.6 }}>
                Select a target career from our knowledge base or complete the Discovery Assessment to generate your custom 4-phase milestone roadmap.
              </p>

              <div style={{ display: 'flex', gap: 16, justifyContent: 'center', flexWrap: 'wrap' }}>
                <button
                  onClick={() => navigate('/discover')}
                  style={{
                    background: 'var(--primary)',
                    color: 'white',
                    border: 'none',
                    borderRadius: 'var(--radius)',
                    padding: '12px 28px',
                    fontSize: 14,
                    fontWeight: 600,
                    cursor: 'pointer',
                    fontFamily: 'var(--font-body)',
                  }}
                >
                  Take Discovery Assessment
                </button>
                <button
                  onClick={() => navigate('/explore')}
                  style={{
                    background: 'transparent',
                    border: '1px solid var(--border)',
                    borderRadius: 'var(--radius)',
                    padding: '12px 28px',
                    fontSize: 14,
                    fontWeight: 500,
                    cursor: 'pointer',
                    fontFamily: 'var(--font-body)',
                    color: 'var(--foreground)',
                  }}
                >
                  Browse 25+ Multi-Domain Careers
                </button>

              </div>
            </div>

            {/* Quick 1-click popular pathways */}
            <div>
              <h3 style={{ fontFamily: 'var(--font-display)', fontSize: 20, fontWeight: 500, color: 'var(--foreground)', marginBottom: 16 }}>
                Or select a popular pathway to start immediately:
              </h3>
              <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))', gap: 14 }}>
                {careers.slice(0, 4).map((c) => (
                  <button
                    key={c.id}
                    onClick={() => createOrSetRoadmap(c.id)}
                    style={{
                      background: 'var(--card)',
                      border: '1px solid var(--border)',
                      borderRadius: 'var(--radius)',
                      padding: '20px',
                      textAlign: 'left',
                      cursor: 'pointer',
                      fontFamily: 'var(--font-body)',
                      transition: 'all 0.18s ease',
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
                    <div style={{ fontSize: 11, color: 'var(--sage)', fontWeight: 700, textTransform: 'uppercase', marginBottom: 4 }}>
                      {c.category_name}
                    </div>
                    <div style={{ fontSize: 16, fontWeight: 600, color: 'var(--foreground)', marginBottom: 6 }}>
                      {c.title}
                    </div>
                    <div style={{ fontSize: 12, color: 'var(--navy)', fontWeight: 500 }}>
                      Start this Pathway →
                    </div>
                  </button>
                ))}
              </div>
            </div>
          </div>
        ) : (
          /* Active Roadmap View */
          <div>
            {/* Overview Stats */}
            <div
              className="reveal"
              style={{
                background: 'var(--card)',
                border: '1px solid var(--border)',
                borderRadius: 'calc(var(--radius) * 2)',
                padding: '32px',
                marginBottom: 40,
                display: 'grid',
                gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))',
                gap: 28,
              }}
            >
              <div>
                <div style={{ fontSize: 48, fontWeight: 400, fontFamily: 'var(--font-display)', color: 'var(--navy)', lineHeight: 1 }}>
                  {progressPercent}%
                </div>
                <div style={{ fontSize: 14, color: 'var(--muted-foreground)', marginTop: 4 }}>Overall pathway progress</div>
                <div style={{ height: 4, background: 'var(--border)', borderRadius: 2, overflow: 'hidden', marginTop: 16 }}>
                  <div
                    style={{
                      height: '100%',
                      width: `${progressPercent}%`,
                      background: 'var(--navy)',
                      borderRadius: 2,
                      transition: 'width 0.6s cubic-bezier(0.4, 0, 0.2, 1)',
                    }}
                  />
                </div>
              </div>
              <div style={{ borderLeft: '1px solid var(--border)', paddingLeft: 28 }}>
                <div style={{ fontSize: 48, fontWeight: 400, fontFamily: 'var(--font-display)', color: 'var(--foreground)', lineHeight: 1 }}>
                  {completedTasks} / {totalTasks}
                </div>
                <div style={{ fontSize: 14, color: 'var(--muted-foreground)', marginTop: 4 }}>Action items completed</div>
                <div style={{ fontSize: 13, color: 'var(--muted-foreground)', marginTop: 8 }}>
                  {totalTasks - completedTasks} remaining
                </div>
              </div>
              <div style={{ borderLeft: '1px solid var(--border)', paddingLeft: 28 }}>
                <div style={{ fontSize: 48, fontWeight: 400, fontFamily: 'var(--font-display)', color: 'var(--foreground)', lineHeight: 1 }}>
                  {completedMilestones} / {activeRoadmap.milestones.length}
                </div>
                <div style={{ fontSize: 14, color: 'var(--muted-foreground)', marginTop: 4 }}>Milestone phases completed</div>
                <div style={{ fontSize: 13, color: 'var(--muted-foreground)', marginTop: 8 }}>
                  {activeRoadmap.careerTitle}
                </div>
              </div>
            </div>

            {/* Step-by-Step Milestones */}
            <div className="reveal" style={{ marginBottom: 48 }}>
              <h2 style={{ fontFamily: 'var(--font-display)', fontSize: 24, fontWeight: 400, color: 'var(--foreground)', marginBottom: 24 }}>
                Roadmap Milestones & Tasks
              </h2>

              <div style={{ display: 'flex', flexDirection: 'column', gap: 20 }}>
                {activeRoadmap.milestones.map((m) => {
                  const allDone = m.tasks.every((t) => t.completed);
                  return (
                    <div
                      key={m.id}
                      style={{
                        background: 'var(--card)',
                        border: allDone ? '1px solid rgba(122, 158, 142, 0.4)' : '1px solid var(--border)',
                        borderRadius: 'calc(var(--radius) * 1.5)',
                        padding: '24px',
                        transition: 'all 0.2s ease',
                      }}
                    >
                      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: 12, flexWrap: 'wrap', gap: 8 }}>
                        <div>
                          <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                            <span style={{ fontSize: 11, fontWeight: 700, color: 'var(--sage)', textTransform: 'uppercase', letterSpacing: '0.06em' }}>
                              {m.phase}
                            </span>
                            <span style={{ fontSize: 12, color: 'var(--muted-foreground)' }}>· {m.estimatedWeeks}</span>
                          </div>
                          <h3 style={{ fontFamily: 'var(--font-display)', fontSize: 20, fontWeight: 500, color: 'var(--foreground)', margin: '4px 0 2px' }}>
                            {m.title}
                          </h3>
                        </div>
                        <span
                          style={{
                            fontSize: 12,
                            fontWeight: 600,
                            padding: '3px 10px',
                            borderRadius: 12,
                            background: allDone ? 'rgba(122, 158, 142, 0.15)' : 'var(--secondary)',
                            color: allDone ? 'var(--sage)' : 'var(--navy)',
                          }}
                        >
                          {allDone ? '✓ Phase Complete' : m.status === 'active' ? 'In Progress' : 'Upcoming'}
                        </span>
                      </div>

                      <p style={{ fontSize: 14, color: 'var(--muted-foreground)', marginBottom: 16 }}>
                        {m.description}
                      </p>

                      {/* Interactive Task Checkboxes */}
                      <div style={{ display: 'flex', flexDirection: 'column', gap: 10 }}>
                        {m.tasks.map((task) => (
                          <label
                            key={task.id}
                            style={{
                              display: 'flex',
                              alignItems: 'flex-start',
                              gap: 12,
                              padding: '10px 14px',
                              background: task.completed ? 'rgba(235, 240, 236, 0.5)' : '#FAF9F6',
                              border: '1px solid var(--border)',
                              borderRadius: 'var(--radius)',
                              cursor: 'pointer',
                              transition: 'all 0.15s ease',
                            }}
                          >
                            <input
                              type="checkbox"
                              checked={task.completed}
                              onChange={() => toggleRoadmapTask(m.id, task.id)}
                              style={{
                                width: 16,
                                height: 16,
                                marginTop: 3,
                                accentColor: 'var(--navy)',
                                cursor: 'pointer',
                              }}
                            />
                            <span
                              style={{
                                fontSize: 14,
                                color: task.completed ? 'var(--muted-foreground)' : 'var(--foreground)',
                                textDecoration: task.completed ? 'line-through' : 'none',
                                lineHeight: 1.5,
                              }}
                            >
                              {task.text}
                            </span>
                          </label>
                        ))}
                      </div>
                    </div>
                  );
                })}
              </div>
            </div>

            {/* Notes & Reflections Section */}
            <div className="reveal" style={{ marginBottom: 48 }}>
              <div style={{ background: 'var(--card)', border: '1px solid var(--border)', borderRadius: 'calc(var(--radius) * 1.5)', padding: '28px' }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: 10, marginBottom: 8 }}>
                  <div
                    style={{
                      width: 28,
                      height: 28,
                      borderRadius: 6,
                      background: 'var(--secondary)',
                      color: 'var(--navy)',
                      display: 'flex',
                      alignItems: 'center',
                      justifyContent: 'center',
                    }}
                  >
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                      <path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7" />
                      <path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z" />
                    </svg>
                  </div>
                  <h3 style={{ fontFamily: 'var(--font-display)', fontSize: 22, fontWeight: 500, color: 'var(--foreground)', margin: 0 }}>
                    Personal Career Notes & Reflections
                  </h3>
                </div>
                <p style={{ fontSize: 14, color: 'var(--muted-foreground)', marginBottom: 20 }}>
                  Document your takeaways, projects you want to build, or mentor insights from TOBE. Every note you save appears in your list below.
                </p>

                {/* Input Form */}
                <div style={{ display: 'flex', flexDirection: 'column', gap: 12, marginBottom: 28 }}>
                  <input
                    type="text"
                    value={noteTitle}
                    onChange={(e) => setNoteTitle(e.target.value)}
                    placeholder="Note Subject (e.g. Portfolio Project Ideas, Figma Shortcuts, Interview Checklist)..."
                    style={{
                      width: '100%',
                      padding: '10px 14px',
                      border: '1px solid var(--border)',
                      borderRadius: 'var(--radius)',
                      fontSize: 14,
                      fontFamily: 'var(--font-body)',
                      background: 'white',
                      color: 'var(--foreground)',
                      boxSizing: 'border-box',
                      outline: 'none',
                    }}
                    onFocus={(e) => { e.target.style.borderColor = 'var(--navy)'; }}
                    onBlur={(e) => { e.target.style.borderColor = 'var(--border)'; }}
                  />
                  <textarea
                    value={noteContent}
                    onChange={(e) => setNoteContent(e.target.value)}
                    placeholder="Write your reflection, key learnings, or next action items here..."
                    rows={3}
                    style={{
                      width: '100%',
                      padding: '12px 14px',
                      border: '1px solid var(--border)',
                      borderRadius: 'var(--radius)',
                      fontSize: 14,
                      fontFamily: 'var(--font-body)',
                      background: 'white',
                      color: 'var(--foreground)',
                      boxSizing: 'border-box',
                      outline: 'none',
                      resize: 'vertical',
                    }}
                    onFocus={(e) => { e.target.style.borderColor = 'var(--navy)'; }}
                    onBlur={(e) => { e.target.style.borderColor = 'var(--border)'; }}
                  />
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                    <div>
                      {savedNotesToast && (
                        <span style={{ fontSize: 13, color: 'var(--sage)', fontWeight: 600 }}>
                          ✓ Note saved to your journey below!
                        </span>
                      )}
                    </div>
                    <button
                      onClick={handleSaveNote}
                      disabled={!noteContent.trim()}
                      style={{
                        background: noteContent.trim() ? 'var(--primary)' : 'var(--border)',
                        color: 'white',
                        border: 'none',
                        borderRadius: 'var(--radius)',
                        padding: '10px 24px',
                        fontSize: 14,
                        fontWeight: 600,
                        cursor: noteContent.trim() ? 'pointer' : 'not-allowed',
                        fontFamily: 'var(--font-body)',
                        display: 'flex',
                        alignItems: 'center',
                        gap: 6,
                        transition: 'all 0.18s ease',
                      }}
                    >
                      <span>Save Note</span>
                      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                        <line x1="12" y1="5" x2="12" y2="19" />
                        <line x1="5" y1="12" x2="19" y2="12" />
                      </svg>
                    </button>
                  </div>
                </div>

                {/* Display list of Saved Notes */}
                <div style={{ borderTop: '1px solid var(--border)', paddingTop: 20 }}>
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 16 }}>
                    <h4 style={{ fontSize: 15, fontWeight: 700, color: 'var(--navy)', margin: 0, letterSpacing: '0.02em' }}>
                      Saved Notes & History ({careerNotes.length})
                    </h4>
                  </div>

                  {careerNotes.length > 0 ? (
                    <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
                      {careerNotes.map((note) => (
                        <div
                          key={note.id}
                          style={{
                            background: '#FAF9F6',
                            border: '1px solid var(--border)',
                            borderRadius: 'var(--radius)',
                            padding: '16px 20px',
                            display: 'flex',
                            flexDirection: 'column',
                            gap: 8,
                            position: 'relative',
                          }}
                        >
                          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
                            <div style={{ display: 'flex', alignItems: 'center', gap: 8, flexWrap: 'wrap' }}>
                              {note.title && (
                                <strong style={{ fontSize: 15, color: 'var(--foreground)' }}>
                                  {note.title}
                                </strong>
                              )}
                              {note.careerTitle && (
                                <span
                                  style={{
                                    fontSize: 11,
                                    fontWeight: 700,
                                    background: 'rgba(122, 158, 142, 0.15)',
                                    color: 'var(--sage)',
                                    padding: '2px 8px',
                                    borderRadius: 4,
                                    textTransform: 'uppercase',
                                  }}
                                >
                                  {note.careerTitle}
                                </span>
                              )}
                            </div>
                            <div style={{ display: 'flex', alignItems: 'center', gap: 12 }}>
                              <span style={{ fontSize: 12, color: 'var(--muted-foreground)' }}>
                                {note.createdAt}
                              </span>
                              <button
                                onClick={() => deleteCareerNote(note.id)}
                                title="Delete note"
                                style={{
                                  background: 'none',
                                  border: 'none',
                                  cursor: 'pointer',
                                  color: 'var(--muted-foreground)',
                                  padding: 4,
                                  display: 'flex',
                                  alignItems: 'center',
                                }}
                                onMouseEnter={(e) => { e.currentTarget.style.color = '#c53030'; }}
                                onMouseLeave={(e) => { e.currentTarget.style.color = 'var(--muted-foreground)'; }}
                              >
                                <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                                  <polyline points="3 6 5 6 21 6" />
                                  <path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2" />
                                </svg>
                              </button>
                            </div>
                          </div>
                          <p style={{ fontSize: 14, color: 'var(--foreground)', lineHeight: 1.6, margin: 0, whiteSpace: 'pre-wrap' }}>
                            {note.content}
                          </p>
                        </div>
                      ))}
                    </div>
                  ) : (
                    <div style={{ padding: '20px', textAlign: 'center', background: '#FAF9F6', borderRadius: 'var(--radius)', border: '1px dashed var(--border)' }}>
                      <p style={{ fontSize: 13, color: 'var(--muted-foreground)', margin: 0 }}>
                        No saved reflections yet. Use the form above to capture your thoughts and study milestones.
                      </p>
                    </div>
                  )}
                </div>
              </div>
            </div>

            {/* Saved Bookmarks */}
            {savedCareersList.length > 0 && (
              <div className="reveal">
                <h3 style={{ fontFamily: 'var(--font-display)', fontSize: 20, fontWeight: 500, color: 'var(--foreground)', marginBottom: 16 }}>
                  Saved & Bookmarked Careers ({savedCareersList.length})
                </h3>
                <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(240px, 1fr))', gap: 14 }}>
                  {savedCareersList.map((c: any) => (
                    <div
                      key={c.id}
                      style={{
                        background: 'var(--card)',
                        border: '1px solid var(--border)',
                        borderRadius: 'var(--radius)',
                        padding: '18px',
                        display: 'flex',
                        flexDirection: 'column',
                        justifyContent: 'space-between',
                      }}
                    >
                      <div>
                        <div style={{ fontSize: 11, color: 'var(--sage)', fontWeight: 700, textTransform: 'uppercase' }}>
                          {c.category_name}
                        </div>
                        <div style={{ fontSize: 16, fontWeight: 600, color: 'var(--foreground)', margin: '4px 0' }}>
                          {c.title}
                        </div>
                        <div style={{ fontSize: 12, color: 'var(--muted-foreground)' }}>
                          {c.salary_data.philippines.entry_level.split('(')[0]}
                        </div>
                      </div>
                      <div style={{ display: 'flex', gap: 8, marginTop: 16 }}>
                        <button
                          onClick={() => createOrSetRoadmap(c.id)}
                          style={{
                            flex: 1,
                            background: 'var(--secondary)',
                            color: 'var(--navy)',
                            border: '1px solid var(--border)',
                            borderRadius: 'var(--radius)',
                            padding: '6px 10px',
                            fontSize: 12,
                            fontWeight: 600,
                            cursor: 'pointer',
                            fontFamily: 'var(--font-body)',
                          }}
                        >
                          {roadmaps.some((r) => r.careerId === c.id) ? 'Switch to this Pathway' : '+ Add as Pathway'}
                        </button>
                      </div>
                    </div>
                  ))}
                </div>
              </div>
            )}
          </div>
        )}
      </div>

      {/* MODAL 1: ADD NEW PATHWAY */}
      {showAddModal &&
        createPortal(
          <div
            style={{
              position: 'fixed',
              top: 0,
              left: 0,
              right: 0,
              bottom: 0,
              zIndex: 9999,
              background: 'rgba(20,25,35,0.65)',
              backdropFilter: 'blur(8px)',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              padding: 20,
            }}
            onClick={() => setShowAddModal(false)}
          >
            <div
              style={{
                background: 'var(--card)',
                borderRadius: 'calc(var(--radius) * 2)',
                border: '1px solid var(--border)',
                width: '100%',
                maxWidth: 620,
                maxHeight: '85vh',
                overflow: 'hidden',
                display: 'flex',
                flexDirection: 'column',
                boxShadow: '0 24px 60px rgba(0,0,0,0.25)',
              }}
              onClick={(e) => e.stopPropagation()}
            >
              {/* Modal Header */}
              <div style={{ padding: '24px 28px', borderBottom: '1px solid var(--border)', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                <div>
                  <h3 style={{ fontFamily: 'var(--font-display)', fontSize: 22, fontWeight: 500, color: 'var(--foreground)', margin: '0 0 4px' }}>
                    Add Another Career Pathway
                  </h3>
                  <p style={{ fontSize: 13, color: 'var(--muted-foreground)', margin: 0 }}>
                    Track multiple careers simultaneously. Your previous progress will remain safely saved.
                  </p>
                </div>
                <button
                  onClick={() => setShowAddModal(false)}
                  style={{ background: 'none', border: 'none', fontSize: 20, cursor: 'pointer', color: 'var(--muted-foreground)' }}
                >
                  ✕
                </button>
              </div>

              {/* Search input */}
              <div style={{ padding: '16px 28px', borderBottom: '1px solid var(--border)' }}>
                <input
                  type="text"
                  placeholder="Search by career title, category, or skill..."
                  value={searchCareerQuery}
                  onChange={(e) => setSearchCareerQuery(e.target.value)}
                  style={{
                    width: '100%',
                    padding: '10px 14px',
                    borderRadius: 'var(--radius)',
                    border: '1px solid var(--border)',
                    fontFamily: 'var(--font-body)',
                    fontSize: 14,
                    outline: 'none',
                    background: '#FAF9F6',
                    boxSizing: 'border-box',
                  }}
                  autoFocus
                />
              </div>

              {/* Career List */}
              <div style={{ padding: '16px 28px', overflowY: 'auto', flex: 1, display: 'flex', flexDirection: 'column', gap: 10 }}>
                {filteredCareers.length === 0 ? (
                  <p style={{ textAlign: 'center', color: 'var(--muted-foreground)', padding: 24, fontSize: 14 }}>
                    No careers found matching "{searchCareerQuery}".
                  </p>
                ) : (
                  filteredCareers.map((c) => {
                    const alreadyExists = roadmaps.some((r) => r.careerId === c.id);
                    return (
                      <div
                        key={c.id}
                        style={{
                          display: 'flex',
                          alignItems: 'center',
                          justifyContent: 'space-between',
                          padding: '14px 18px',
                          borderRadius: 'var(--radius)',
                          border: '1px solid var(--border)',
                          background: alreadyExists ? 'rgba(122,158,142,0.06)' : '#FAF9F6',
                        }}
                      >
                        <div>
                          <div style={{ fontSize: 11, color: 'var(--sage)', fontWeight: 700, textTransform: 'uppercase' }}>
                            {c.category_name}
                          </div>
                          <div style={{ fontSize: 15, fontWeight: 600, color: 'var(--foreground)', marginTop: 2 }}>
                            {c.title}
                          </div>
                          <div style={{ fontSize: 12, color: 'var(--muted-foreground)', marginTop: 2 }}>
                            {c.salary_data.philippines.entry_level.split('(')[0]} • {c.core_skills.slice(0, 3).join(', ')}
                          </div>
                        </div>

                        <button
                          onClick={() => {
                            createOrSetRoadmap(c.id);
                            setShowAddModal(false);
                            setSearchCareerQuery('');
                          }}
                          style={{
                            background: alreadyExists ? 'var(--secondary)' : 'var(--navy)',
                            color: alreadyExists ? 'var(--navy)' : '#FFFFFF',
                            border: '1px solid var(--border)',
                            borderRadius: 'var(--radius)',
                            padding: '8px 16px',
                            fontSize: 13,
                            fontWeight: 600,
                            cursor: 'pointer',
                            fontFamily: 'var(--font-body)',
                            whiteSpace: 'nowrap',
                          }}
                        >
                          {alreadyExists ? 'Switch to this' : '+ Start Pathway'}
                        </button>
                      </div>
                    );
                  })
                )}
              </div>
            </div>
          </div>,
          document.body
        )}

      {/* MODAL 2: CONFIRM DELETE PATHWAY */}
      {showDeleteConfirm &&
        activeRoadmap &&
        createPortal(
          <div
            style={{
              position: 'fixed',
              top: 0,
              left: 0,
              right: 0,
              bottom: 0,
              zIndex: 9999,
              background: 'rgba(20,25,35,0.65)',
              backdropFilter: 'blur(8px)',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              padding: 20,
            }}
            onClick={() => setShowDeleteConfirm(false)}
          >
            <div
              style={{
                background: 'var(--card)',
                borderRadius: 'calc(var(--radius) * 2)',
                border: '1px solid var(--border)',
                width: '100%',
                maxWidth: 440,
                padding: '28px',
                boxShadow: '0 24px 60px rgba(0,0,0,0.25)',
              }}
              onClick={(e) => e.stopPropagation()}
            >
              <h3 style={{ fontFamily: 'var(--font-display)', fontSize: 20, fontWeight: 500, color: 'var(--foreground)', margin: '0 0 8px' }}>
                Remove Pathway?
              </h3>
              <p style={{ fontSize: 14, color: 'var(--muted-foreground)', lineHeight: 1.5, margin: '0 0 24px' }}>
                Are you sure you want to remove the <strong>{activeRoadmap.careerTitle}</strong> pathway? Your other pathways and saved bookmarks will not be affected.
              </p>

              <div style={{ display: 'flex', gap: 12, justifyContent: 'flex-end' }}>
                <button
                  onClick={() => setShowDeleteConfirm(false)}
                  style={{
                    background: 'transparent',
                    border: '1px solid var(--border)',
                    borderRadius: 'var(--radius)',
                    padding: '8px 18px',
                    fontSize: 13,
                    fontWeight: 500,
                    cursor: 'pointer',
                    color: 'var(--foreground)',
                  }}
                >
                  Cancel
                </button>
                <button
                  onClick={() => {
                    deleteRoadmap(activeRoadmap.careerId);
                    setShowDeleteConfirm(false);
                  }}
                  style={{
                    background: '#c53030',
                    color: '#FFFFFF',
                    border: 'none',
                    borderRadius: 'var(--radius)',
                    padding: '8px 18px',
                    fontSize: 13,
                    fontWeight: 600,
                    cursor: 'pointer',
                  }}
                >
                  Remove
                </button>
              </div>
            </div>
          </div>,
          document.body
        )}

      <TOBEWidget />
    </AppShell>
  );
}
