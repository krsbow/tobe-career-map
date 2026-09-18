import { useState, useRef, useEffect } from 'react';
import AppShell from '../components/AppShell';
import { useAuth } from '../context/AuthContext';
import { useCareer } from '../context/CareerContext';

type Message = {
  id: number;
  from: 'user' | 'tobe';
  text: string;
};

type ConversationTopic =
  | 'coding'
  | 'design'
  | 'data'
  | 'security'
  | 'cloud'
  | 'product'
  | 'salary'
  | 'general';

const starterPrompts = [
  "How can I learn coding from scratch?",
  "Give me real portfolio project ideas to build",
  "How do I choose between Front-End and UX Design?",
  "What salary can I expect as a junior developer or designer in the Philippines?",
];

export default function TOBE() {
  const { user } = useAuth();
  const { activeRoadmap, assessmentResults } = useCareer();
  const [topicContext, setTopicContext] = useState<ConversationTopic>(() => {
    if (activeRoadmap?.careerId.includes('developer')) return 'coding';
    if (activeRoadmap?.careerId.includes('design')) return 'design';
    if (activeRoadmap?.careerId.includes('data')) return 'data';
    if (activeRoadmap?.careerId.includes('security')) return 'security';
    if (activeRoadmap?.careerId.includes('cloud')) return 'cloud';
    return 'general';
  });

  const [messages, setMessages] = useState<Message[]>([
    {
      id: 0,
      from: 'tobe',
      text: `Hi ${user?.name || 'there'}. I'm TOBE — your AI career mentor. ${
        activeRoadmap
          ? `I see you're currently working toward becoming a ${activeRoadmap.careerTitle}.`
          : assessmentResults
          ? `I see your assessment highlighted strengths in ${assessmentResults.topTraits.join(', ')}.`
          : `I'm here to help you learn skills, build portfolio projects, explore salaries, and plan your career transition.`
      } What would you like to explore today?`,
    },
  ]);
  const [input, setInput] = useState('');
  const [isTyping, setIsTyping] = useState(false);
  const bottomRef = useRef<HTMLDivElement>(null);
  const nextId = useRef(1);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages, isTyping]);

  const generateAIResponse = (userQuery: string): string => {
    const q = userQuery.toLowerCase().trim();

    // 1. PROJECT IDEAS (Direct intent or follow-up e.g. "give me projects", "what should i build", "portfolio ideas")
    if (
      q.includes('project') ||
      q.includes('portfolio idea') ||
      q.includes('what should i build') ||
      q.includes('what to build') ||
      q.includes('give me ideas') ||
      q.includes('capstone')
    ) {
      if (topicContext === 'design' || q.includes('design') || q.includes('ux') || q.includes('ui')) {
        setTopicContext('design');
        return `Here are 3 standout UX / Product Design case study projects that will impress hiring managers:

1. **Foundational: Mobile App Usability Redesign**
   • *Brief*: Identify friction in a real public transit, banking, or local delivery app.
   • *Deliverables*: User interview findings, heuristic evaluation, interactive Figma prototype, and before/after usability test metrics.

2. **Intermediate: Accessible Telehealth / Clinic Booking Flow**
   • *Brief*: Design a friction-free healthcare appointment flow tailored for seniors and low-contrast visibility needs.
   • *Focus*: WCAG 2.1 AA accessibility, clear error handling, and cognitive load reduction.

3. **Advanced: Multi-Platform B2B SaaS Design System**
   • *Brief*: Build a complete design system in Figma with color/spacing tokens, Auto-layout components, interactive states, and data table filtering patterns.

Which project would you like to start first? I can help you outline the problem statement!`;
      }

      if (topicContext === 'data' || q.includes('data') || q.includes('python') || q.includes('sql')) {
        setTopicContext('data');
        return `Here are 3 data analytics projects that prove practical business value:

1. **Foundational: Public Health or Economic Trend Dashboard**
   • *Stack*: SQL + Power BI / Tableau + Open government/WHO dataset.
   • *Deliverable*: Interactive dashboard uncovering hidden seasonal trends with clear executive takeaway KPIs.

2. **Intermediate: E-Commerce Customer Retention & Churn Cohort Analysis**
   • *Stack*: PostgreSQL + Python (Pandas/Seaborn) + Jupyter Notebook.
   • *Deliverable*: Cohort retention heatmaps, customer lifetime value (LTV) calculation, and churn risk scoring.

3. **Advanced: Automated KPI Pipeline & Anomaly Detector**
   • *Stack*: Python API script + automated PostgreSQL transformation + scheduled Slack/Email metric alert.`;
      }

      if (topicContext === 'security' || topicContext === 'cloud' || q.includes('security') || q.includes('cloud') || q.includes('aws')) {
        setTopicContext('security');
        return `Here are 3 real-world Cloud & Cybersecurity portfolio projects:

1. **Home Lab Virtual Network & SIEM Setup**
   • *Stack*: pfSense firewall + Linux/Windows virtual machines + Wazuh/Splunk SIEM.
   • *Deliverable*: Documented attack simulation (brute-force/port scan) and how your SIEM detected and alerted on it.

2. **Terraform Multi-Tier Cloud Infrastructure on AWS**
   • *Stack*: Terraform + AWS (VPC, Public/Private Subnets, ALB, Auto-scaling EC2, RDS).
   • *Deliverable*: Clean GitHub repository with modular Infrastructure-as-Code scripts and architecture diagram.

3. **Network Packet Forensics & Malware Triage Report**
   • *Stack*: Wireshark + NetworkMiner + open-source PCAP capture.
   • *Deliverable*: Executive incident response report detailing C2 traffic identification and IOC extractions.`;
      }

      // Default to coding / web dev projects
      setTopicContext('coding');
      return `Here are 3 high-impact coding projects that avoid the "generic tutorial clone" trap:

1. **Foundational: Interactive Habit & Goal Tracker with Local Storage**
   • *Stack*: HTML5, Tailwind CSS, TypeScript / React.
   • *Key Features*: Light/dark theme toggle, drag-and-drop ordering, localStorage state persistence, and responsive mobile layout.

2. **Intermediate: Live API Data & Analytics Dashboard**
   • *Stack*: React, TypeScript, Chart.js / Recharts, OpenWeather or GitHub API.
   • *Key Features*: Real-time search, interactive charts, debounced inputs, error boundaries, and skeleton loading states.

3. **Advanced: Full-Stack SaaS / Collaborative Workspace with Auth & DB**
   • *Stack*: Next.js / React + Tailwind + Supabase (PostgreSQL with Row Level Security) + Vercel deployment.
   • *Key Features*: User sign-up/login, real-time board updates, database persistence, and clean optimistic UI.

Would you like help breaking down the implementation steps for any of these?`;
    }

    // 2. LEARNING TO CODE / WEB DEVELOPMENT
    if (
      q.includes('learn code') ||
      q.includes('learn coding') ||
      q.includes('learn to code') ||
      q.includes('start coding') ||
      q.includes('how to code') ||
      q.includes('how can i learn coding') ||
      q.includes('learn web development') ||
      q.includes('learn programming') ||
      q.includes('beginner programmer') ||
      q.includes('learn javascript')
    ) {
      setTopicContext('coding');
      return `Learning to code is a clear, step-by-step progression:

1. **Phase 1: Web Fundamentals (Weeks 1–4)**
   • **HTML5 & Modern CSS**: Master semantic tags, Flexbox, CSS Grid, and responsive styling.
   • **JavaScript Essentials**: Variables, arrays, objects, functions, async/await, and DOM manipulation.
   • **Best Free Resource**: Start with **freeCodeCamp's Responsive Web Design** and **The Odin Project Foundations**.

2. **Phase 2: Modern Tooling & Git (Weeks 5–6)**
   • Install **VS Code** with Prettier and ESLint.
   • Learn **Git version control** and push every project to GitHub to build your portfolio trail.

3. **Phase 3: Modern Front-End Framework (Weeks 7–12)**
   • Learn **React with TypeScript and Tailwind CSS** — the standard stack for modern tech companies.
   • Build 2 interactive web applications.

4. **Phase 4: Backend & APIs (Weeks 13–16)**
   • Learn REST API design with **Node.js** or **Python**, connecting to **PostgreSQL** or **Supabase**.

Would you like me to give you a week-by-week study plan or project ideas?`;
    }

    // 3. LEARNING UX / DESIGN
    if (
      q.includes('learn ux') ||
      q.includes('learn ui') ||
      q.includes('learn design') ||
      q.includes('how to design') ||
      q.includes('become a designer') ||
      q.includes('figma')
    ) {
      setTopicContext('design');
      return `Here is the practical roadmap to becoming a UI/UX or Product Designer:

1. **Figma Proficiency**:
   • Master Auto-layout, component variants, interactive prototyping, and design tokens.
   • Practice by deconstructing and recreating your favorite mobile apps.

2. **UX Psychology & Research**:
   • Study fundamental design heuristics on **LawsofUX.com**.
   • Learn how to write interview scripts, run usability tests, and create journey maps.

3. **Build Real Case Studies**:
   • Complete 2 end-to-end case studies detailing the problem, user research, wireframes, and tested solutions.
   • The **Google UX Design Certificate** is a great structured guide.

Would you like me to suggest project ideas or review case study structures?`;
    }

    // 4. TIMELINE / DURATION / "HOW LONG DOES IT TAKE?"
    if (
      q.includes('how long') ||
      q.includes('timeline') ||
      q.includes('how many months') ||
      q.includes('duration') ||
      q.includes('how much time')
    ) {
      return `Here is a realistic timeline based on dedication:

• **Full-Time (20–30 hours/week)**: ~3 to 4 months to reach junior/entry-level job readiness.
• **Part-Time (10–15 hours/week)**: ~5 to 7 months of consistent study.

**Key Milestone Breakdown**:
• Month 1: Core Fundamentals & Tools (Syntax, Git, Figma/CLI).
• Month 2–3: Frameworks & Building Real Small Projects.
• Month 4–5: Full-featured Capstone Projects & Portfolio creation.
• Month 6: Resume polish, interview practice, and active job applications.

Consistency (e.g. 1 hour every single day) beats cramming once a week!`;
    }

    // 5. DEGREE / SELF-TAUGHT / "CAN I DO IT WITHOUT A DEGREE?"
    if (
      q.includes('degree') ||
      q.includes('college') ||
      q.includes('without degree') ||
      q.includes('self taught') ||
      q.includes('no experience') ||
      q.includes('hard to learn') ||
      q.includes('is it hard')
    ) {
      return `**Yes, absolutely.** In modern tech, software development, and UI/UX design:

1. **Proof of Work > Degrees**: Hiring managers look at your live deployed websites, GitHub repositories, and Figma case studies first. If your work solves real problems and is clean, you will get interviews.
2. **Transferable Skills**: If you have a background in business, education, arts, or support, those communication and analytical skills make you a stronger developer/designer.
3. **What Matters Most**:
   • Clear, readable code / thoughtful design rationale.
   • Knowing how to use modern tools (Git, React, Figma, Postman, SQL).
   • A humble, proactive problem-solving mindset.`;
    }

    // 6. FREE RESOURCES / COURSES / CERTIFICATIONS
    if (
      q.includes('free resource') ||
      q.includes('free course') ||
      q.includes('certification') ||
      q.includes('where to study') ||
      q.includes('recommend courses') ||
      q.includes('website to learn')
    ) {
      return `Here are the top, 100% free and high-quality learning resources:

• **Coding & Web Development**:
  - **The Odin Project** (*theodinproject.com*) — full-stack curriculum with real projects.
  - **freeCodeCamp** (*freecodecamp.org*) — interactive certifications.
  - **CS50 by Harvard** (*cs50.harvard.edu*) — world-class computer science fundamentals.
  - **Full Stack Open** (*fullstackopen.com*) — modern React, Node, and TypeScript.

• **UX & Product Design**:
  - **Figma Learn** (*help.figma.com*) — official interactive Figma tutorials.
  - **Laws of UX** (*lawsofux.com*) — psychological UX principles.
  - **Nielsen Norman Group Articles** (*nngroup.com/articles*).

• **Data & Cybersecurity**:
  - **SQLBolt** (*sqlbolt.com*) — interactive SQL in browser.
  - **Kaggle Learn** (*kaggle.com/learn*) — Python, Pandas, and ML micro-courses.
  - **TryHackMe** (*tryhackme.com*) — hands-on security and Linux labs.`;
    }

    // 7. SALARY & COMPENSATION
    const isSalary = /\b(salary|salaries|pay|paid|compensation|earnings|income|rate|rates|pesos|php|usd|how much)\b/i.test(
      q
    );
    if (isSalary) {
      setTopicContext('salary');
      return `Here are verified compensation benchmarks based on Payscale, Levels.fyi, and JobStreet tech surveys:

🇵🇭 **Philippines Benchmarks**:
• **Front-End & Full-Stack Developers**: ₱25k–₱45k/mo (Entry) | ₱60k–₱125k/mo (Mid) | ₱125k–₱250k+/mo (Senior)
• **UI/UX Designers & Product Managers**: ₱30k–₱55k/mo (Entry) | ₱70k–₱140k/mo (Mid) | ₱150k–₱300k+/mo (Senior)
• **Cloud & Cybersecurity Engineers**: ₱35k–₱55k/mo (Entry) | ₱65k–₱130k/mo (Mid) | ₱140k–₱265k+/mo (Senior)
• **Data & AI Engineers**: ₱30k–₱60k/mo (Entry) | ₱70k–₱150k/mo (Mid) | ₱150k–₱280k+/mo (Senior)

🌎 **Global Remote Benchmarks (USD)**:
• **Junior / Entry**: $65,000 – $95,000 / year
• **Mid-Level**: $95,000 – $145,000 / year
• **Senior / Lead**: $150,000 – $220,000+ / year

Which field would you like to explore in more detail?`;
    }

    // 8. FOLLOW-UPS & MULTI-TURN QUESTIONS (e.g. "what next?", "how do i start?", "more details", "tell me more")
    if (
      q.includes('what next') ||
      q.includes('what else') ||
      q.includes('how to start') ||
      q.includes('where do i start') ||
      q.includes('tell me more') ||
      q.includes('more info') ||
      q.includes('step 1')
    ) {
      if (topicContext === 'coding') {
        return `To take action on coding right now:

1. **Today**: Open **The Odin Project** (*theodinproject.com*) or **freeCodeCamp** and complete the first HTML lesson.
2. **This Week**: Download **VS Code**, create an \`index.html\` file, and build a single-page tribute or recipe card.
3. **Next Week**: Add CSS styling with colors, fonts, and Flexbox centering.

Would you like me to guide you through setting up your coding environment or building your first HTML page?`;
      }
      if (topicContext === 'design') {
        return `To start with UX design right away:

1. **Today**: Create a free account on **Figma.com**.
2. **This Week**: Follow Figma's beginner tutorial to learn frames, shapes, text styles, and Auto-layout.
3. **Next Week**: Pick your favorite app (e.g. Spotify) and replicate 2 screens pixel-for-pixel to build muscle memory.

Would you like to start on a design exercise together?`;
      }
    }

    // 9. GENERAL / EMPATHETIC FALLBACK WITH CONTEXT
    return `I understand! Career exploration is all about finding the right balance of curiosity, practical skills, and proof of work.

To help give you the most specific guidance:
• Are you looking to learn **Coding / Development**, **UI/UX Design**, **Data & AI**, or **Cloud/Security**?
• Would you like **project briefs**, **learning roadmaps**, **free resource links**, or **salary benchmarks**?

Tell me what you'd like to dive into next!`;
  };

  const sendMessage = (text: string) => {
    if (!text.trim()) return;

    const userMsg: Message = { id: nextId.current++, from: 'user', text: text.trim() };
    setMessages((prev) => [...prev, userMsg]);
    setInput('');
    setIsTyping(true);

    const delay = 500 + Math.random() * 400;
    setTimeout(() => {
      setIsTyping(false);
      const reply = generateAIResponse(text);
      setMessages((prev) => [...prev, { id: nextId.current++, from: 'tobe', text: reply }]);
    }, delay);
  };

  const handleKey = (e: React.KeyboardEvent<HTMLTextAreaElement>) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      sendMessage(input);
    }
  };

  return (
    <AppShell>
      <div
        style={{
          maxWidth: 820,
          margin: '0 auto',
          padding: '0 24px',
          display: 'flex',
          flexDirection: 'column',
          height: 'calc(100vh - 60px)',
        }}
      >
        {/* Header */}
        <div
          style={{
            padding: '24px 0 16px',
            borderBottom: '1px solid var(--border)',
            display: 'flex',
            alignItems: 'center',
            gap: 14,
            flexShrink: 0,
          }}
        >
          <div
            style={{
              width: 40,
              height: 40,
              borderRadius: 'var(--radius)',
              background: 'var(--primary)',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
            }}
          >
            <svg width="20" height="20" viewBox="0 0 16 16" fill="none">
              <circle cx="8" cy="8" r="6" stroke="var(--sage)" strokeWidth="1.5" />
              <path d="M8 5v3l2 2" stroke="var(--sage)" strokeWidth="1.5" strokeLinecap="round" />
            </svg>
          </div>
          <div>
            <div style={{ fontSize: 16, fontWeight: 600, color: 'var(--foreground)' }}>TOBE</div>
            <div style={{ fontSize: 12, color: 'var(--muted-foreground)' }}>AI Career Mentor · Multi-turn intelligent guidance</div>
          </div>
        </div>

        {/* Message area */}
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
          {messages.map((m) => (
            <div
              key={m.id}
              style={{
                display: 'flex',
                gap: 12,
                justifyContent: m.from === 'user' ? 'flex-end' : 'flex-start',
                maxWidth: '100%',
              }}
            >
              {m.from === 'tobe' && (
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
                    fontSize: 12,
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
                  background: m.from === 'user' ? 'var(--navy)' : 'var(--card)',
                  color: m.from === 'user' ? 'white' : 'var(--foreground)',
                  border: m.from === 'user' ? 'none' : '1px solid var(--border)',
                  borderRadius: 'calc(var(--radius) * 1.5)',
                  padding: '16px 20px',
                  fontSize: 15,
                  lineHeight: 1.65,
                  fontFamily: 'var(--font-body)',
                  whiteSpace: 'pre-line',
                }}
              >
                {m.text}
              </div>
            </div>
          ))}

          {isTyping && (
            <div style={{ display: 'flex', gap: 12, alignItems: 'center' }}>
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
                  fontSize: 12,
                  fontWeight: 700,
                  flexShrink: 0,
                }}
              >
                T
              </div>
              <div
                style={{
                  background: 'var(--card)',
                  border: '1px solid var(--border)',
                  borderRadius: 'calc(var(--radius) * 1.5)',
                  padding: '12px 18px',
                  display: 'flex',
                  gap: 6,
                  alignItems: 'center',
                }}
              >
                <div style={{ width: 6, height: 6, borderRadius: '50%', background: 'var(--muted-foreground)', animation: 'pulse 1s infinite' }} />
                <div style={{ width: 6, height: 6, borderRadius: '50%', background: 'var(--muted-foreground)', animation: 'pulse 1s infinite 0.2s' }} />
                <div style={{ width: 6, height: 6, borderRadius: '50%', background: 'var(--muted-foreground)', animation: 'pulse 1s infinite 0.4s' }} />
              </div>
            </div>
          )}
          <div ref={bottomRef} />
        </div>

        {/* Starter prompts */}
        {messages.length <= 2 && (
          <div style={{ paddingBottom: 16 }}>
            <div style={{ fontSize: 12, color: 'var(--muted-foreground)', marginBottom: 8, fontWeight: 500 }}>
              Suggested topics:
            </div>
            <div style={{ display: 'flex', gap: 8, flexWrap: 'wrap' }}>
              {starterPrompts.map((p) => (
                <button
                  key={p}
                  onClick={() => sendMessage(p)}
                  style={{
                    background: 'var(--card)',
                    border: '1px solid var(--border)',
                    borderRadius: 20,
                    padding: '6px 14px',
                    fontSize: 12,
                    fontWeight: 500,
                    color: 'var(--foreground)',
                    cursor: 'pointer',
                    fontFamily: 'var(--font-body)',
                    transition: 'all 0.15s ease',
                  }}
                  onMouseEnter={(e) => { e.currentTarget.style.borderColor = 'var(--navy)'; }}
                  onMouseLeave={(e) => { e.currentTarget.style.borderColor = 'var(--border)'; }}
                >
                  {p}
                </button>
              ))}
            </div>
          </div>
        )}

        {/* Input box */}
        <div style={{ padding: '16px 0 24px', borderTop: '1px solid var(--border)', flexShrink: 0 }}>
          <div style={{ display: 'flex', gap: 10, alignItems: 'flex-end' }}>
            <textarea
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyDown={handleKey}
              placeholder="Ask TOBE anything (e.g. 'Give me projects', 'How to learn coding', 'What is the salary?')..."
              rows={2}
              style={{
                flex: 1,
                padding: '12px 16px',
                border: '1px solid var(--border)',
                borderRadius: 'var(--radius)',
                fontSize: 14,
                fontFamily: 'var(--font-body)',
                background: 'var(--card)',
                color: 'var(--foreground)',
                outline: 'none',
                resize: 'none',
                boxSizing: 'border-box',
              }}
              onFocus={(e) => { e.target.style.borderColor = 'var(--navy)'; }}
              onBlur={(e) => { e.target.style.borderColor = 'var(--border)'; }}
            />
            <button
              onClick={() => sendMessage(input)}
              disabled={!input.trim()}
              style={{
                background: input.trim() ? 'var(--navy)' : 'var(--border)',
                color: 'white',
                border: 'none',
                borderRadius: 'var(--radius)',
                padding: '12px 20px',
                fontSize: 14,
                fontWeight: 600,
                cursor: input.trim() ? 'pointer' : 'not-allowed',
                fontFamily: 'var(--font-body)',
                height: 48,
              }}
            >
              Send
            </button>
          </div>
        </div>
      </div>
    </AppShell>
  );
}
