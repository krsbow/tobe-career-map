import { useEffect, useRef, useState } from 'react';
import { useNavigate } from 'react-router-dom';

const careers = [
  { title: 'Product Designer', field: 'Design', match: 94 },
  { title: 'UX Researcher', field: 'Research', match: 88 },
  { title: 'Brand Strategist', field: 'Marketing', match: 82 },
  { title: 'Data Analyst', field: 'Analytics', match: 76 },
  { title: 'Innovation Lead', field: 'Strategy', match: 71 },
];

const steps = [
  {
    number: '01',
    title: 'Reflect',
    body: 'Answer thoughtful questions about your interests, values, and working style. No tests. No scores.',
  },
  {
    number: '02',
    title: 'Discover',
    body: 'Explore careers curated to you — with real salary data, day-in-the-life stories, and growth trajectories.',
  },
  {
    number: '03',
    title: 'Chart your path',
    body: 'Build a step-by-step plan. Track progress. Get guidance from TOBE, your AI career mentor.',
  },
];

function useRevealOnScroll(selector = '.reveal') {
  const containerRef = useRef<HTMLDivElement>(null);
  useEffect(() => {
    const container = containerRef.current;
    if (!container) return;
    const observer = new IntersectionObserver(
      (entries) => entries.forEach((e) => e.isIntersecting && e.target.classList.add('visible')),
      { threshold: 0.1, rootMargin: '0px 0px -40px 0px' }
    );
    container.querySelectorAll(selector).forEach((el) => observer.observe(el));
    return () => observer.disconnect();
  }, [selector]);
  return containerRef;
}

export default function Landing() {
  const navigate = useNavigate();
  const pageRef = useRevealOnScroll();
  const [activeCareer, setActiveCareer] = useState(0);

  useEffect(() => {
    const interval = setInterval(() => {
      setActiveCareer((prev) => (prev + 1) % careers.length);
    }, 2400);
    return () => clearInterval(interval);
  }, []);

  return (
    <div ref={pageRef} style={{ minHeight: '100vh', background: 'var(--background)' }}>
      {/* Header */}
      <header
        style={{
          position: 'fixed',
          top: 0,
          left: 0,
          right: 0,
          zIndex: 100,
          background: 'rgba(249,248,245,0.88)',
          backdropFilter: 'blur(14px)',
          borderBottom: '1px solid var(--border)',
        }}
      >
        <div style={{ maxWidth: 1280, margin: '0 auto', padding: '0 32px', height: 64, display: 'flex', alignItems: 'center' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 8, flex: 1 }}>
            <svg width="24" height="24" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg" style={{ flexShrink: 0 }}>
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
          </div>
          <nav style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
            {['Explore', 'How It Works', 'About'].map((item) => (
              <a
                key={item}
                href={`#${item.toLowerCase().replace(/ /g, '-')}`}
                style={{
                  textDecoration: 'none',
                  fontSize: 14,
                  fontWeight: 500,
                  color: 'var(--muted-foreground)',
                  padding: '6px 12px',
                  borderRadius: 'var(--radius)',
                  display: 'none',
                }}
                className="nav-link-desktop"
              >
                {item}
              </a>
            ))}
            <button
              onClick={() => navigate('/auth')}
              style={{
                background: 'none',
                border: 'none',
                fontSize: 14,
                fontWeight: 500,
                color: 'var(--foreground)',
                cursor: 'pointer',
                padding: '6px 12px',
                fontFamily: 'var(--font-body)',
              }}
            >
              Log In
            </button>
            <button
              onClick={() => navigate('/auth')}
              style={{
                background: 'var(--primary)',
                color: 'white',
                border: 'none',
                borderRadius: 'var(--radius)',
                padding: '8px 20px',
                fontSize: 14,
                fontWeight: 600,
                cursor: 'pointer',
                fontFamily: 'var(--font-body)',
                transition: 'all 0.2s ease',
              }}
              onMouseEnter={(e) => { (e.target as HTMLElement).style.opacity = '0.88'; }}
              onMouseLeave={(e) => { (e.target as HTMLElement).style.opacity = '1'; }}
            >
              Start Exploring
            </button>
          </nav>
        </div>
      </header>

      {/* Hero */}
      <section
        style={{
          minHeight: '100vh',
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          justifyContent: 'center',
          padding: '120px 32px 80px',
          textAlign: 'center',
          position: 'relative',
          overflow: 'hidden',
        }}
      >
        {/* Subtle background grid */}
        <div
          style={{
            position: 'absolute',
            inset: 0,
            backgroundImage: `
              linear-gradient(var(--border) 1px, transparent 1px),
              linear-gradient(90deg, var(--border) 1px, transparent 1px)
            `,
            backgroundSize: '64px 64px',
            opacity: 0.4,
            pointerEvents: 'none',
          }}
        />
        <div
          style={{
            position: 'absolute',
            top: '30%',
            left: '50%',
            transform: 'translate(-50%, -50%)',
            width: 600,
            height: 600,
            borderRadius: '50%',
            background: 'radial-gradient(circle, rgba(91,127,166,0.08) 0%, transparent 70%)',
            pointerEvents: 'none',
          }}
        />

        <div style={{ position: 'relative', maxWidth: 760 }}>
          <h1
            className="animate-slide-up"
            style={{
              fontFamily: 'var(--font-display)',
              fontSize: 'clamp(44px, 7vw, 88px)',
              fontWeight: 400,
              color: 'var(--foreground)',
              lineHeight: 1.05,
              letterSpacing: '-0.03em',
              marginBottom: 28,
            }}
          >
            Explore what could
            <br />
            <em style={{ color: 'var(--navy)' }}>be next.</em>
          </h1>

          <p
            className="animate-slide-up delay-100"
            style={{
              fontSize: 18,
              color: 'var(--muted-foreground)',
              maxWidth: 500,
              margin: '0 auto 48px',
              lineHeight: 1.7,
              fontWeight: 400,
            }}
          >
            Discover careers that connect with your interests, skills, and goals.
            Understand what they involve, then build a path toward the ones you want to explore.
          </p>

          <div className="animate-slide-up delay-200" style={{ display: 'flex', gap: 12, justifyContent: 'center', flexWrap: 'wrap' }}>
            <button
              onClick={() => navigate('/auth')}
              style={{
                background: 'var(--primary)',
                color: 'white',
                border: 'none',
                borderRadius: 'var(--radius)',
                padding: '14px 32px',
                fontSize: 16,
                fontWeight: 600,
                cursor: 'pointer',
                fontFamily: 'var(--font-body)',
                letterSpacing: '-0.01em',
                transition: 'all 0.25s ease',
              }}
              onMouseEnter={(e) => {
                (e.target as HTMLElement).style.transform = 'translateY(-1px)';
                (e.target as HTMLElement).style.boxShadow = '0 8px 24px rgba(36,55,96,0.25)';
              }}
              onMouseLeave={(e) => {
                (e.target as HTMLElement).style.transform = 'translateY(0)';
                (e.target as HTMLElement).style.boxShadow = 'none';
              }}
            >
              Start Exploring
            </button>
            <button
              onClick={() => document.getElementById('explore')?.scrollIntoView({ behavior: 'smooth' })}
              style={{
                background: 'transparent',
                color: 'var(--foreground)',
                border: '1px solid var(--border)',
                borderRadius: 'var(--radius)',
                padding: '14px 32px',
                fontSize: 16,
                fontWeight: 500,
                cursor: 'pointer',
                fontFamily: 'var(--font-body)',
                transition: 'all 0.25s ease',
              }}
              onMouseEnter={(e) => { (e.target as HTMLElement).style.borderColor = 'var(--foreground)'; }}
              onMouseLeave={(e) => { (e.target as HTMLElement).style.borderColor = 'var(--border)'; }}
            >
              Explore Careers
            </button>
          </div>
        </div>

        {/* Career path visual */}
        <div
          className="animate-fade-in delay-500"
          style={{
            marginTop: 80,
            maxWidth: 640,
            width: '100%',
            background: 'var(--card)',
            border: '1px solid var(--border)',
            borderRadius: 'calc(var(--radius) * 2)',
            padding: '24px 28px',
            boxShadow: '0 4px 32px rgba(26,31,46,0.06)',
            position: 'relative',
          }}
        >
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 20 }}>
            <span style={{ fontSize: 12, fontWeight: 600, letterSpacing: '0.08em', textTransform: 'uppercase', color: 'var(--muted-foreground)' }}>
              Career matches for you
            </span>
            <span style={{ fontSize: 12, color: 'var(--muted-foreground)' }}>Based on your profile</span>
          </div>
          <div style={{ display: 'flex', flexDirection: 'column', gap: 10 }}>
            {careers.map((career, i) => (
              <div
                key={career.title}
                style={{
                  display: 'flex',
                  alignItems: 'center',
                  gap: 14,
                  padding: '10px 14px',
                  borderRadius: 'var(--radius)',
                  background: i === activeCareer ? 'var(--secondary)' : 'transparent',
                  border: `1px solid ${i === activeCareer ? 'var(--border)' : 'transparent'}`,
                  transition: 'all 0.4s cubic-bezier(0.4, 0, 0.2, 1)',
                }}
              >
                <div
                  style={{
                    width: 36,
                    height: 36,
                    borderRadius: 'var(--radius)',
                    background: i === activeCareer ? 'var(--primary)' : 'var(--muted)',
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                    transition: 'all 0.4s ease',
                    flexShrink: 0,
                  }}
                >
                  <svg width="16" height="16" viewBox="0 0 16 16" fill="none">
                    <circle cx="8" cy="8" r="6" stroke={i === activeCareer ? 'white' : 'var(--muted-foreground)'} strokeWidth="1.5" />
                    <path d="M5 8l2 2 4-4" stroke={i === activeCareer ? 'white' : 'var(--muted-foreground)'} strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round" />
                  </svg>
                </div>
                <div style={{ flex: 1, minWidth: 0 }}>
                  <div style={{ fontSize: 14, fontWeight: 600, color: 'var(--foreground)' }}>{career.title}</div>
                  <div style={{ fontSize: 12, color: 'var(--muted-foreground)' }}>{career.field}</div>
                </div>
                <div style={{ textAlign: 'right', flexShrink: 0 }}>
                  <div style={{ fontSize: 16, fontWeight: 700, fontFamily: 'var(--font-display)', color: i === activeCareer ? 'var(--navy)' : 'var(--muted-foreground)' }}>
                    {career.match}%
                  </div>
                  <div style={{ fontSize: 11, color: 'var(--muted-foreground)' }}>match</div>
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Scroll indicator */}
        <div
          className="animate-fade-in delay-700"
          style={{ marginTop: 48, display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 8 }}
        >
          <span style={{ fontSize: 12, color: 'var(--muted-foreground)', letterSpacing: '0.06em', textTransform: 'uppercase' }}>Scroll</span>
          <div
            style={{
              width: 1,
              height: 40,
              background: 'linear-gradient(to bottom, var(--border), transparent)',
            }}
          />
        </div>
      </section>

      {/* What / Why / How TO BE */}
      <section
        style={{
          padding: '120px 32px',
          maxWidth: 1200,
          margin: '0 auto',
        }}
      >
        <div className="reveal" style={{ textAlign: 'center', marginBottom: 80 }}>
          <p style={{ fontSize: 13, fontWeight: 600, letterSpacing: '0.1em', textTransform: 'uppercase', color: 'var(--muted-foreground)', marginBottom: 16 }}>
            The platform
          </p>
          <h2 style={{ fontFamily: 'var(--font-display)', fontSize: 'clamp(32px, 5vw, 56px)', fontWeight: 400, letterSpacing: '-0.03em', color: 'var(--foreground)' }}>
            Why TO BE exists
          </h2>
        </div>

        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))', gap: 2 }}>
          {[
            {
              label: 'WHAT TO BE',
              headline: 'A space to explore, not decide.',
              body: 'Most career tools ask you to commit before you understand yourself. TO BE flips that. It\'s a space to wander, reflect, and gradually find what fits — without pressure.',
            },
            {
              label: 'WHY TO BE',
              headline: 'Because the path is personal.',
              body: 'Career decisions shaped by algorithms, job boards, or social pressure often miss the mark. TO BE is built around who you are — your values, curiosity, and potential.',
            },
            {
              label: 'HOW TO BE',
              headline: 'Reflect. Discover. Chart.',
              body: 'You reflect on what matters to you, discover careers that genuinely match, then build a step-by-step path with TOBE — your AI career mentor — by your side.',
            },
          ].map((item, i) => (
            <div
              key={item.label}
              className="reveal"
              style={{
                padding: '48px 40px',
                borderTop: '2px solid var(--border)',
                transitionDelay: `${i * 0.12}s`,
              }}
            >
              <div style={{ fontSize: 11, fontWeight: 700, letterSpacing: '0.12em', textTransform: 'uppercase', color: 'var(--sage)', marginBottom: 20 }}>
                {item.label}
              </div>
              <h3 style={{ fontFamily: 'var(--font-display)', fontSize: 26, fontWeight: 400, color: 'var(--foreground)', marginBottom: 16, lineHeight: 1.3 }}>
                {item.headline}
              </h3>
              <p style={{ fontSize: 15, color: 'var(--muted-foreground)', lineHeight: 1.7 }}>{item.body}</p>
            </div>
          ))}
        </div>
      </section>

      {/* How It Works */}
      <section
        id="how-it-works"
        style={{ padding: '120px 32px', background: 'var(--card)', borderTop: '1px solid var(--border)', borderBottom: '1px solid var(--border)' }}
      >
        <div style={{ maxWidth: 1000, margin: '0 auto' }}>
          <div className="reveal" style={{ marginBottom: 80 }}>
            <p style={{ fontSize: 13, fontWeight: 600, letterSpacing: '0.1em', textTransform: 'uppercase', color: 'var(--muted-foreground)', marginBottom: 16 }}>
              How it works
            </p>
            <h2 style={{ fontFamily: 'var(--font-display)', fontSize: 'clamp(32px, 5vw, 52px)', fontWeight: 400, letterSpacing: '-0.03em', maxWidth: 560 }}>
              Three steps to finding your path
            </h2>
          </div>

          <div style={{ display: 'flex', flexDirection: 'column', gap: 0 }}>
            {steps.map((step, i) => (
              <div
                key={step.number}
                className="reveal"
                style={{
                  display: 'grid',
                  gridTemplateColumns: '80px 1fr',
                  gap: 32,
                  padding: '40px 0',
                  borderBottom: i < steps.length - 1 ? '1px solid var(--border)' : 'none',
                  transitionDelay: `${i * 0.1}s`,
                }}
              >
                <div style={{ fontFamily: 'var(--font-display)', fontSize: 48, fontWeight: 300, color: 'var(--border)', lineHeight: 1 }}>
                  {step.number}
                </div>
                <div>
                  <h3 style={{ fontFamily: 'var(--font-display)', fontSize: 28, fontWeight: 400, color: 'var(--foreground)', marginBottom: 10 }}>
                    {step.title}
                  </h3>
                  <p style={{ fontSize: 16, color: 'var(--muted-foreground)', maxWidth: 500, lineHeight: 1.7 }}>{step.body}</p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Career Preview */}
      <section id="explore" style={{ padding: '120px 32px', maxWidth: 1200, margin: '0 auto' }}>
        <div className="reveal" style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-end', marginBottom: 60, flexWrap: 'wrap', gap: 24 }}>
          <div>
            <p style={{ fontSize: 13, fontWeight: 600, letterSpacing: '0.1em', textTransform: 'uppercase', color: 'var(--muted-foreground)', marginBottom: 16 }}>
              Career preview
            </p>
            <h2 style={{ fontFamily: 'var(--font-display)', fontSize: 'clamp(28px, 4vw, 48px)', fontWeight: 400, letterSpacing: '-0.03em' }}>
              Explore real careers
            </h2>
          </div>
          <button
            onClick={() => navigate('/auth')}
            style={{
              background: 'none',
              border: '1px solid var(--border)',
              borderRadius: 'var(--radius)',
              padding: '10px 22px',
              fontSize: 14,
              fontWeight: 500,
              cursor: 'pointer',
              fontFamily: 'var(--font-body)',
              color: 'var(--foreground)',
              whiteSpace: 'nowrap',
            }}
          >
            See all careers
          </button>
        </div>

        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(260px, 1fr))', gap: 16 }}>
          {[
            { title: 'UX Designer', salary: '₱70k – ₱120k', growth: '+18%', skills: ['Figma', 'Research', 'Prototyping'] },
            { title: 'Climate Scientist', salary: '₱55k – ₱95k', growth: '+24%', skills: ['Data Analysis', 'Fieldwork', 'Modeling'] },
            { title: 'Product Manager', salary: '₱90k – ₱160k', growth: '+21%', skills: ['Strategy', 'Agile', 'Communication'] },
            { title: 'Therapist', salary: '₱45k – ₱80k', growth: '+15%', skills: ['Empathy', 'CBT', 'Assessment'] },
          ].map((career, i) => (
            <div
              key={career.title}
              className="reveal"
              style={{
                padding: '28px',
                background: 'var(--card)',
                border: '1px solid var(--border)',
                borderRadius: 'calc(var(--radius) * 2)',
                cursor: 'pointer',
                transition: 'all 0.25s ease',
                transitionDelay: `${i * 0.08}s`,
              }}
              onMouseEnter={(e) => {
                (e.currentTarget as HTMLElement).style.transform = 'translateY(-2px)';
                (e.currentTarget as HTMLElement).style.boxShadow = '0 8px 32px rgba(26,31,46,0.08)';
              }}
              onMouseLeave={(e) => {
                (e.currentTarget as HTMLElement).style.transform = 'translateY(0)';
                (e.currentTarget as HTMLElement).style.boxShadow = 'none';
              }}
              onClick={() => navigate('/auth')}
            >
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: 20 }}>
                <h3 style={{ fontFamily: 'var(--font-display)', fontSize: 22, fontWeight: 400, color: 'var(--foreground)' }}>
                  {career.title}
                </h3>
                <span
                  style={{
                    background: 'rgba(122,158,142,0.12)',
                    color: 'var(--sage)',
                    fontSize: 11,
                    fontWeight: 700,
                    letterSpacing: '0.06em',
                    padding: '3px 9px',
                    borderRadius: 40,
                  }}
                >
                  {career.growth}
                </span>
              </div>
              <div style={{ fontSize: 14, fontWeight: 600, color: 'var(--navy)', marginBottom: 16 }}>{career.salary}</div>
              <div style={{ display: 'flex', gap: 6, flexWrap: 'wrap' }}>
                {career.skills.map((skill) => (
                  <span
                    key={skill}
                    style={{
                      background: 'var(--muted)',
                      color: 'var(--muted-foreground)',
                      fontSize: 12,
                      fontWeight: 500,
                      padding: '3px 10px',
                      borderRadius: 40,
                    }}
                  >
                    {skill}
                  </span>
                ))}
              </div>
            </div>
          ))}
        </div>
      </section>

      {/* TOBE Preview */}
      <section
        style={{
          padding: '120px 32px',
          background: 'var(--primary)',
          position: 'relative',
          overflow: 'hidden',
        }}
      >
        <div
          style={{
            position: 'absolute',
            top: -100,
            right: -100,
            width: 500,
            height: 500,
            borderRadius: '50%',
            background: 'rgba(91,127,166,0.15)',
            pointerEvents: 'none',
          }}
        />
        <div style={{ maxWidth: 900, margin: '0 auto', display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 80, alignItems: 'center' }}>
          <div className="reveal">
            <p style={{ fontSize: 12, fontWeight: 700, letterSpacing: '0.12em', textTransform: 'uppercase', color: 'rgba(255,255,255,0.5)', marginBottom: 20 }}>
              TOBE — Your AI Mentor
            </p>
            <h2
              style={{
                fontFamily: 'var(--font-display)',
                fontSize: 'clamp(28px, 4vw, 48px)',
                fontWeight: 400,
                color: 'white',
                lineHeight: 1.15,
                marginBottom: 24,
              }}
            >
              A mentor that knows where you want to go.
            </h2>
            <p style={{ fontSize: 16, color: 'rgba(255,255,255,0.65)', lineHeight: 1.7, marginBottom: 32 }}>
              TOBE is your AI career mentor. Ask anything. Get honest, personalized guidance — no generic advice.
            </p>
            <button
              onClick={() => navigate('/auth')}
              style={{
                background: 'white',
                color: 'var(--navy)',
                border: 'none',
                borderRadius: 'var(--radius)',
                padding: '13px 28px',
                fontSize: 15,
                fontWeight: 600,
                cursor: 'pointer',
                fontFamily: 'var(--font-body)',
                transition: 'all 0.2s ease',
              }}
            >
              Meet TOBE
            </button>
          </div>

          <div className="reveal reveal-delay-2">
            <div
              style={{
                background: 'rgba(255,255,255,0.07)',
                border: '1px solid rgba(255,255,255,0.12)',
                borderRadius: 'calc(var(--radius) * 2)',
                padding: '24px',
              }}
            >
              {[
                { from: 'user', text: 'I feel like I\'m good at listening to people but I don\'t know what careers use that.' },
                { from: 'tobe', text: 'That\'s a genuinely valuable skill. Careers like counseling, UX research, mediation, and organizational psychology all center on it. Want to explore any of those?' },
                { from: 'user', text: 'UX Research sounds interesting — what does a day actually look like?' },
              ].map((msg, i) => (
                <div
                  key={i}
                  style={{
                    display: 'flex',
                    justifyContent: msg.from === 'user' ? 'flex-end' : 'flex-start',
                    marginBottom: 12,
                  }}
                >
                  <div
                    style={{
                      background: msg.from === 'user' ? 'rgba(255,255,255,0.12)' : 'rgba(255,255,255,0.06)',
                      borderRadius: msg.from === 'user' ? '16px 16px 4px 16px' : '4px 16px 16px 16px',
                      padding: '10px 14px',
                      maxWidth: '80%',
                      fontSize: 13,
                      lineHeight: 1.55,
                      color: msg.from === 'user' ? 'rgba(255,255,255,0.9)' : 'rgba(255,255,255,0.75)',
                    }}
                  >
                    {msg.from === 'tobe' && (
                      <div style={{ fontSize: 10, fontWeight: 700, letterSpacing: '0.1em', color: 'var(--sage)', marginBottom: 4, textTransform: 'uppercase' }}>TOBE</div>
                    )}
                    {msg.text}
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
      </section>

      {/* Final CTA */}
      <section style={{ padding: '140px 32px', textAlign: 'center' }}>
        <div className="reveal" style={{ maxWidth: 600, margin: '0 auto' }}>
          <h2
            style={{
              fontFamily: 'var(--font-display)',
              fontSize: 'clamp(36px, 6vw, 68px)',
              fontWeight: 400,
              color: 'var(--foreground)',
              lineHeight: 1.1,
              letterSpacing: '-0.03em',
              marginBottom: 28,
            }}
          >
            Begin becoming
            <br />
            <em>who you want to be.</em>
          </h2>
          <p style={{ fontSize: 17, color: 'var(--muted-foreground)', marginBottom: 40, lineHeight: 1.65 }}>
            Join thousands of people who found their path through TO BE.
          </p>
          <button
            onClick={() => navigate('/auth')}
            style={{
              background: 'var(--primary)',
              color: 'white',
              border: 'none',
              borderRadius: 'var(--radius)',
              padding: '16px 40px',
              fontSize: 17,
              fontWeight: 600,
              cursor: 'pointer',
              fontFamily: 'var(--font-body)',
              letterSpacing: '-0.01em',
              transition: 'all 0.25s ease',
            }}
            onMouseEnter={(e) => {
              (e.target as HTMLElement).style.transform = 'translateY(-2px)';
              (e.target as HTMLElement).style.boxShadow = '0 12px 32px rgba(36,55,96,0.25)';
            }}
            onMouseLeave={(e) => {
              (e.target as HTMLElement).style.transform = 'translateY(0)';
              (e.target as HTMLElement).style.boxShadow = 'none';
            }}
          >
            Start Exploring — it's free
          </button>
        </div>
      </section>

      {/* Footer */}
      <footer
        style={{
          borderTop: '1px solid var(--border)',
          padding: '32px',
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          flexWrap: 'wrap',
          gap: 16,
        }}
      >
        <span style={{ fontFamily: 'var(--font-display)', fontSize: 18, fontWeight: 500, color: 'var(--navy)', letterSpacing: '-0.02em' }}>
          TO BE
        </span>
        <p style={{ fontSize: 13, color: 'var(--muted-foreground)' }}>
          &copy; 2026 TO BE. Career discovery for the curious.
        </p>
        <p style={{ fontSize: 13, color: 'var(--muted-foreground)' }}>
          Created by krsbow
        </p>
      </footer>

      <style>{`
        @media (max-width: 768px) {
          .nav-link-desktop { display: none !important; }
        }
        @media (min-width: 769px) {
          .nav-link-desktop { display: block !important; }
        }
        section > div[style*="grid-template-columns: 1fr 1fr"] {
          grid-template-columns: 1fr !important;
        }
        @media (min-width: 700px) {
          section > div[style*="grid-template-columns: 1fr 1fr"] {
            grid-template-columns: 1fr 1fr !important;
          }
        }
      `}</style>
    </div>
  );
}
