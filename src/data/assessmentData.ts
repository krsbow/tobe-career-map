// Multi-Domain RIASEC & Skills Assessment Bank for TO BE Career Discovery Platform
// Career-neutral assessment across 5 structured sections:
// Section 1: Standardized RIASEC Interest Profiler (O*NET based)
// Section 2: 11 Multi-Domain Skill Categories
// Section 3: Work Style & Environmental Preferences
// Section 4: Career Priorities & Core Values
// Section 5: Background & Education Level

export interface QuestionOption {
  id: string;
  text: string;
  scores?: Record<string, number>;
  preference?: string;
  impact?: string;
}

export interface AssessmentQuestion {
  id: string;
  category: 'interests' | 'work_preferences' | 'priorities' | 'impact' | 'background';
  dimension: string;
  title: string;
  subtitle: string;
  type: 'single_choice' | 'multi_select';
  max_select?: number;
  options: QuestionOption[];
}

export const SKILL_CATEGORIES: Record<string, string[]> = {
  "Technology & Software": [
    "Python", "JavaScript", "TypeScript", "React", "Node.js", "SQL", "Git & GitHub",
    "HTML/CSS", "Cloud & AWS", "Linux & Docker", "Cybersecurity Basics", "API Development"
  ],
  "Design & Creative Arts": [
    "Figma & UI Design", "UX Research", "Wireframing & Prototyping", "Graphic Design",
    "Brand Identity", "Design Systems", "Adobe Photoshop/Illustrator", "Visual Storytelling"
  ],
  "Data & Analytics": [
    "Data Analysis", "Excel / Advanced Spreadsheets", "SQL & Database Queries",
    "Power BI / Tableau", "Statistics & Probability", "Machine Learning Concepts",
    "Data Cleaning & Wrangling", "Dashboard Creation"
  ],
  "Business, Strategy & Marketing": [
    "Digital Marketing", "SEO & Content Strategy", "Social Media Management",
    "Market Research", "Project Management", "Agile & Scrum", "Business Planning",
    "Client Relationship Management", "Sales & Negotiation"
  ],
  "Healthcare & Life Sciences": [
    "Patient Care & Assessment", "Clinical Documentation", "Health Informatics & EHR",
    "Medical Terminology", "Infection Control & Safety", "Pharmacology Basics",
    "Public Health & Health Promotion", "Triage & Emergency Care"
  ],
  "Engineering, Construction & Architecture": [
    "AutoCAD & 2D Drafting", "Structural Analysis Basics", "Building Information Modeling (BIM)",
    "Circuit Design & Electronics", "Cost Estimation & Quantity Surveying",
    "Project Scheduling", "Site Inspection & Quality Control", "Engineering Mathematics"
  ],
  "Finance, Accounting & Economics": [
    "Financial Accounting", "Bookkeeping & General Ledger", "Tax Compliance (BIR/Local)",
    "Financial Statement Analysis", "Budgeting & Forecasting", "Auditing Principles",
    "QuickBooks / Xero", "Risk Assessment"
  ],
  "Education, Teaching & Training": [
    "Curriculum & Lesson Planning", "Classroom Management", "Instructional Design",
    "Educational Technology / LMS", "Student Assessment & Evaluation",
    "Workshop Facilitation", "Special Needs / Inclusive Education", "Mentorship"
  ],
  "Skilled Trades & Practical Technical": [
    "Electrical Wiring & Installation", "HVAC / Refrigeration Systems",
    "Schematic & Blueprint Reading", "Power & Hand Tools Mastery",
    "Preventive Maintenance & Troubleshooting", "Occupational Health & Safety (OSHA)",
    "Plumbing & Piping", "Welding & Metal Fabrication"
  ],
  "Writing, Media & Communications": [
    "Technical Writing & Documentation", "Copywriting & Editing", "Public Relations",
    "Journalism & Reporting", "Video Production & Editing", "Speech & Presentation",
    "Content Strategy", "Internal Communications"
  ],
  "Social Impact, Law & Public Service": [
    "Community Organizing", "Policy Research & Analysis", "Legal Research & Ethics",
    "Conflict Resolution & Mediation", "Counseling & Social Welfare", "Volunteer Management",
    "Civic Engagement", "Non-Profit Operations"
  ]
};

export const ONET_INTEREST_QUESTIONS = [
  // Realistic (R)
  { id: "onet_r1", dimension: "R", text: "Build kitchen cabinets or custom wooden furniture" },
  { id: "onet_r2", dimension: "R", text: "Lay brick or tile for a building project" },
  { id: "onet_r3", dimension: "R", text: "Repair household appliances, electronic circuits, or engines" },
  { id: "onet_r4", dimension: "R", text: "Assemble electronic parts or computer hardware components" },
  { id: "onet_r5", dimension: "R", text: "Operate heavy machinery, power tools, or industrial equipment" },

  // Investigative (I)
  { id: "onet_i1", dimension: "I", text: "Study how biological organisms develop and reproduce" },
  { id: "onet_i2", dimension: "I", text: "Conduct laboratory research to develop new medicines or materials" },
  { id: "onet_i3", dimension: "I", text: "Analyze complex numerical data sets to discover hidden trends" },
  { id: "onet_i4", dimension: "I", text: "Examine why software systems fail and engineer algorithmic solutions" },
  { id: "onet_i5", dimension: "I", text: "Investigate financial records to detect discrepancies or anomalies" },

  // Artistic (A)
  { id: "onet_a1", dimension: "A", text: "Write scripts, articles, stories, or creative editorial pieces" },
  { id: "onet_a2", dimension: "A", text: "Design graphic layouts, branding, or interactive digital interfaces" },
  { id: "onet_a3", dimension: "A", text: "Compose music, edit film and video footage, or produce multimedia" },
  { id: "onet_a4", dimension: "A", text: "Create architectural concepts, interior layouts, or product sketches" },
  { id: "onet_a5", dimension: "A", text: "Direct or participate in theatrical, artistic, or creative productions" },

  // Social (S)
  { id: "onet_s1", dimension: "S", text: "Teach high school students or facilitate adult learning workshops" },
  { id: "onet_s2", dimension: "S", text: "Care for patients in a healthcare clinic, hospital, or wellness setting" },
  { id: "onet_s3", dimension: "S", text: "Counsel individuals experiencing personal, career, or family challenges" },
  { id: "onet_s4", dimension: "S", text: "Help people rehabilitate after physical injuries or medical procedures" },
  { id: "onet_s5", dimension: "S", text: "Organize community welfare programs or volunteer support initiatives" },

  // Enterprising (E)
  { id: "onet_e1", dimension: "E", text: "Pitch an innovative business idea to investors or stakeholders" },
  { id: "onet_e2", dimension: "E", text: "Manage a department, lead a project team, and allocate resources" },
  { id: "onet_e3", dimension: "E", text: "Negotiate contracts, supplier agreements, or commercial terms" },
  { id: "onet_e4", dimension: "E", text: "Create and execute marketing campaigns to launch new products" },
  { id: "onet_e5", dimension: "E", text: "Direct company operations and make high-stakes strategic decisions" },

  // Conventional (C)
  { id: "onet_c1", dimension: "C", text: "Maintain systematic financial accounts, general ledgers, and budgets" },
  { id: "onet_c2", dimension: "C", text: "Inspect operational workflows or documentation for regulatory compliance" },
  { id: "onet_c3", dimension: "C", text: "Organize and verify database records, inventory lists, or official registries" },
  { id: "onet_c4", dimension: "C", text: "Calculate tax returns and ensure statutory compliance with financial standards" },
  { id: "onet_c5", dimension: "C", text: "Develop structured standard operating procedures and documentation systems" }
];

export const ASSESSMENT_QUESTIONS: AssessmentQuestion[] = [
  // 1. RIASEC & Interests
  {
    id: "interest_1",
    category: "interests",
    dimension: "RIASEC",
    title: "What kind of work challenge sparks your greatest engagement?",
    subtitle: "Think about what naturally commands your attention and flow state.",
    type: "single_choice",
    options: [
      {
        id: "i1_artistic",
        text: "Designing creative visuals, aesthetic concepts, or engaging human experiences",
        scores: { A: 3, S: 1 }
      },
      {
        id: "i1_investigative",
        text: "Investigating complex problems, discovering data patterns, or analyzing scientific systems",
        scores: { I: 3, R: 1 }
      },
      {
        id: "i1_enterprising",
        text: "Pitching new initiatives, leading strategic direction, and growing an organization",
        scores: { E: 3, S: 1 }
      },
      {
        id: "i1_realistic",
        text: "Building physical/technical structures, troubleshooting equipment, or hands-on engineering",
        scores: { R: 3, C: 1 }
      },
      {
        id: "i1_social",
        text: "Guiding people, teaching new skills, or providing essential healthcare and wellness support",
        scores: { S: 3, A: 1 }
      },
      {
        id: "i1_conventional",
        text: "Structuring orderly processes, managing accurate financial records, or quality auditing",
        scores: { C: 3, I: 1 }
      }
    ]
  },
  {
    id: "interest_2",
    category: "interests",
    dimension: "RIASEC",
    title: "If you had a free weekend to dive into a personal project, what would you pick?",
    subtitle: "There are no wrong answers — select what feels most natural to you.",
    type: "single_choice",
    options: [
      {
        id: "i2_creative_media",
        text: "Creating visual art, writing content, redesigning a brand, or editing media",
        scores: { A: 3, I: 1 }
      },
      {
        id: "i2_analytical_data",
        text: "Researching an intriguing question, analyzing data, or building a coding/logic tool",
        scores: { I: 3, R: 2 }
      },
      {
        id: "i2_community_service",
        text: "Organizing a mentoring session, community workshop, or helping someone solve a life challenge",
        scores: { S: 3, E: 1 }
      },
      {
        id: "i2_business_venture",
        text: "Developing a startup business plan, marketing campaign, or sales strategy",
        scores: { E: 3, C: 1 }
      },
      {
        id: "i2_practical_craft",
        text: "Assembling hardware, electrical wiring, repairing mechanics, or constructing physical models",
        scores: { R: 3, C: 2 }
      }
    ]
  },
  {
    id: "interest_3",
    category: "interests",
    dimension: "RIASEC",
    title: "Which environment feels most aligned with your cognitive strengths?",
    subtitle: "Reflect on how your mind prefers to process and solve problems.",
    type: "single_choice",
    options: [
      {
        id: "i3_visual_human",
        text: "Visual & Expressive: Crafting human-centered experiences, aesthetic harmony, and emotional resonance",
        scores: { A: 3, S: 2 }
      },
      {
        id: "i3_logical_scientific",
        text: "Scientific & Analytical: Breaking down intricate systems, mathematical reasoning, and finding root causes",
        scores: { I: 3, R: 2 }
      },
      {
        id: "i3_relational_empowering",
        text: "Relational & Empathetic: Connecting with people, counseling, healing, and empowering growth",
        scores: { S: 3, E: 1 }
      },
      {
        id: "i3_strategic_commercial",
        text: "Strategic & Commercial: Driving outcomes, negotiating partnerships, and positioning products for growth",
        scores: { E: 3, C: 1 }
      },
      {
        id: "i3_structured_precision",
        "text": "Systematic & Methodical: Ensuring compliance, financial precision, and bulletproof standards",
        scores: { C: 3, R: 1, I: 1 }
      }
    ]
  },

  // 2. Work Environment & Working Style Preferences
  {
    id: "work_preference_1",
    category: "work_preferences",
    dimension: "Work Environment",
    title: "What kind of daily work rhythm brings out your best performance?",
    subtitle: "Select the working style that aligns best with your natural rhythm.",
    type: "single_choice",
    options: [
      {
        id: "wp1_independent_deep",
        text: "Deep Independent Focus: Long uninterrupted blocks of concentration, problem-solving, and building",
        preference: "Deep Focus / Independent",
        scores: { I: 2, R: 1 }
      },
      {
        id: "wp1_collaborative_team",
        text: "Team Collaboration: Brainstorming ideas, coordinating cross-functional projects, and shared goals",
        preference: "High Collaboration / Cross-Functional",
        scores: { S: 2, E: 1 }
      },
      {
        id: "wp1_people_facing",
        text: "Client & People-Facing: Direct interpersonal engagement, patient/client consultation, and active listening",
        preference: "People-Facing & Consultative",
        scores: { S: 3, E: 2 }
      },
      {
        id: "wp1_practical_site",
        text: "Hands-On & Field/Site Work: Active physical engagement, site visits, workshops, or clinical settings",
        preference: "Hands-On / Field / Practical",
        scores: { R: 3, C: 1 }
      }
    ]
  },

  // 3. Career Priorities & Values
  {
    id: "career_priorities",
    category: "priorities",
    dimension: "Values & Motivation",
    title: "What matters most to you in your next career step?",
    subtitle: "Select up to 3 core priorities.",
    type: "multi_select",
    max_select: 3,
    options: [
      { id: "p_earning", text: "High earning potential & rapid financial growth" },
      { id: "p_stability", text: "Long-term job stability, security & steady demand" },
      { id: "p_meaning", text: "Direct social impact, public service & helping others" },
      { id: "p_learning", text: "Intellectual challenge & continuous learning" },
      { id: "p_creativity", text: "Creative freedom, craft mastery & self-expression" },
      { id: "p_flexibility", text: "Work flexibility, autonomy & remote/hybrid options" },
      { id: "p_leadership", text: "Strategic influence, team leadership & executive impact" }
    ]
  },

  // 4. Background & Education Level (Optional)
  {
    id: "background_education",
    category: "background",
    dimension: "Education & Background",
    title: "What is your current educational background or career stage? (Optional)",
    subtitle: "This helps tailor roadmap starting points and certification pathways.",
    type: "single_choice",
    options: [
      { id: "edu_senior_high", text: "Senior High School Student / Recent Graduate" },
      { id: "edu_vocational", text: "TVET / Vocational Student / TESDA National Certificate (NC) Holder" },
      { id: "edu_undergraduate", text: "College / University Student (Undergraduate)" },
      { id: "edu_graduate", text: "Bachelor's Degree Graduate (Any Field)" },
      { id: "edu_professional_shifter", text: "Working Professional exploring a Career Shift" },
      { id: "edu_self_taught", text: "Self-Taught / Independent Learner" }
    ]
  }
];

export const RIASEC_DESCRIPTIONS: Record<string, { title: string; subtitle: string; description: string; color: string }> = {
  R: {
    title: "Realistic",
    subtitle: "The Practical Doer",
    description: "Hands-on problem solver who thrives working with physical tools, machinery, electronics, and tangible crafts.",
    color: "from-amber-500 to-orange-600"
  },
  I: {
    title: "Investigative",
    subtitle: "The Analytical Thinker",
    description: "Inquisitive mind driven by scientific inquiry, data analysis, deep problem-solving, and systematic research.",
    color: "from-blue-500 to-cyan-600"
  },
  A: {
    title: "Artistic",
    subtitle: "The Creative Innovator",
    description: "Original thinker who excels at visual design, user experience, creative writing, aesthetics, and human expression.",
    color: "from-purple-500 to-pink-600"
  },
  S: {
    title: "Social",
    subtitle: "The Empathetic Helper",
    description: "People-centered advocate driven by teaching, mentoring, patient care, healthcare, counseling, and community service.",
    color: "from-emerald-500 to-teal-600"
  },
  E: {
    title: "Enterprising",
    subtitle: "The Strategic Leader",
    description: "Ambitious strategist who thrives on leading teams, pitching innovative ideas, negotiating, and driving business growth.",
    color: "from-rose-500 to-red-600"
  },
  C: {
    title: "Conventional",
    subtitle: "The Methodical Organizer",
    description: "Detail-oriented specialist who ensures operational precision, compliance, financial accuracy, and structured systems.",
    color: "from-indigo-500 to-blue-700"
  }
};
