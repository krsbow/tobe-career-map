/**
 * Guided Career Mentor Service & Question Catalog for TO BE
 * 
 * Provides structured question intents across WHAT / WHY / HOW / PRACTICAL,
 * priority-based question progression, career-adaptive wording, and
 * deterministic, intent-specific answer generation.
 */

import { CAREERS, Career } from '../data/careersData';

export type IntentCategory = 'WHAT' | 'WHY' | 'HOW' | 'PRACTICAL';

export interface QuestionIntentDef {
  intent: string;
  category: IntentCategory;
  priority: 'HIGH' | 'MEDIUM' | 'LOW';
  getQuestionText: (career: Career) => string;
  getAnswer: (career: Career, userContext?: UserAssessmentContext) => string;
}

export interface UserAssessmentContext {
  preferredName?: string;
  topTraits?: string[];
  selectedSkills?: string[];
  activeCareerId?: string;
  activeRoadmapProgress?: {
    completedCount: number;
    totalCount: number;
    percentage: number;
  };
}

export interface GuidedTurn {
  id: string;
  from: 'tobe' | 'user';
  intent?: string;
  category?: IntentCategory;
  text: string;
  timestamp: string;
}

export interface GuidedMentorState {
  careerId: string;
  exploredIntents: string[];
  turns: GuidedTurn[];
  isComplete: boolean;
}

/**
 * Career-specific prerequisite concern mapping
 */
function getPrerequisiteQuestion(career: Career): string {
  const id = career.id.toLowerCase();
  const title = career.title.toLowerCase();

  if (id.includes('ai-ml') || title.includes('machine learning') || title.includes('ai')) {
    return 'Do I need to be good at math and algorithms?';
  }
  if (id.includes('ui-ux') || title.includes('design') || title.includes('ui/ux')) {
    return 'Do I need to be good at drawing or visual art?';
  }
  if (id.includes('cybersecurity') || title.includes('security')) {
    return 'Do I need strong programming experience to start?';
  }
  if (id.includes('data-analyst') || title.includes('data')) {
    return 'How much statistics and math do I need to know?';
  }
  if (id.includes('project-manager') || title.includes('manager') || title.includes('scrum')) {
    return 'Do I need deep technical skills to be a project manager?';
  }
  if (id.includes('frontend') || title.includes('front-end')) {
    return 'Do I need to be a graphic designer to do front-end?';
  }
  if (id.includes('nurse') || title.includes('nursing')) {
    return 'What is the emotional and physical demand of bedside nursing?';
  }
  if (id.includes('civil') || title.includes('engineer')) {
    return 'How much physics and advanced calculus is required?';
  }
  if (id.includes('electrician') || title.includes('electrical')) {
    return 'Is commercial electrical work dangerous or physically heavy?';
  }
  if (id.includes('accountant') || title.includes('cpa')) {
    return 'Is the CPA board exam necessary to get hired?';
  }
  if (id.includes('marketing')) {
    return 'Do I need coding or technical skills for digital marketing?';
  }
  return `What background or prerequisites are needed for ${career.title}?`;
}

function getPrerequisiteAnswer(career: Career): string {
  const id = career.id.toLowerCase();
  const title = career.title;

  if (id.includes('ai-ml') || id.includes('machine-learning')) {
    return `For AI & Machine Learning Engineering, you need a comfortable working foundation in linear algebra (matrices, vectors), calculus (gradients, partial derivatives), and probability.\n\nYou do not need to be a pure mathematical theorist to start; applied machine learning relies heavily on using established libraries (PyTorch, TensorFlow, Scikit-learn) and understanding how algorithms optimize weights.\n\nSolid Python programming and data manipulation skills are just as important as mathematical foundations.`;
  }
  if (id.includes('ui-ux') || id.includes('design')) {
    return `You do not need fine-art drawing or sketching talent for UI/UX design.\n\nUI/UX design is about digital usability, layout hierarchy, spacing systems, and user flows inside tools like Figma. These rely on structured geometric components, typographic scales, and design heuristics rather than freehand illustration.\n\nEmpathy for user friction and curiosity about how people interact with software matter far more than drawing ability.`;
  }
  if (id.includes('cybersecurity')) {
    return `You do not need to be a master programmer to begin in Cybersecurity, but foundational scripting (Python or Bash) and a solid grasp of computer networking (TCP/IP, DNS, routing) and operating system internals (Linux and Windows admin) are essential.\n\nMany entry-level analysts start with network defense, log analysis in SIEM tools, and vulnerability scanning before learning advanced exploit analysis or reverse engineering.`;
  }
  if (id.includes('data-analyst') || id.includes('data')) {
    return `Junior Data Analysts do not need advanced mathematical statistics or multivariable calculus.\n\nYou need solid working comfort with descriptive statistics (mean, median, standard deviation, percentiles, correlation) and clean arithmetic logic.\n\nThe majority of everyday data analysis centers on SQL querying, data cleaning in Excel or Python, and communicating visual trends effectively through dashboards.`;
  }
  if (id.includes('project-manager')) {
    return `Project Managers do not write production code or create Figma components daily, but having high 'technical literacy' is extremely valuable.\n\nUnderstanding software development cycles (Agile, Scrum), sprint planning, API dependencies, and how engineers estimate effort helps you communicate with credibility, protect project timelines, and eliminate blockers.`;
  }
  if (id.includes('frontend')) {
    return `You do not need graphic design skills to be a successful Front-End Developer.\n\nFront-end development is about translating Figma designs into clean, semantic, responsive code (HTML, CSS, JavaScript, React), managing component state, and integrating backend REST APIs. Professional designers provide the mockups; your focus is interactive architecture, performance, and accessibility.`;
  }
  if (id.includes('nurse')) {
    return `Bedside nursing is physically active and emotionally demanding. You spend long shifts on your feet, administering medications, monitoring patient vitals, and coordinating with physicians.\n\nStrong emotional resilience, attention to detail under pressure, and genuine empathy are core strengths that sustain nurses in clinical environments.`;
  }
  if (id.includes('civil')) {
    return `Civil Engineering involves applied algebra, geometry, and structural mechanics, supported heavily by specialized calculation and CAD software.\n\nWhile structural engineering requires rigorous calculation, modern practice emphasizes building codes, project management, material specifications, and quality control on site.`;
  }
  if (id.includes('accountant') || id.includes('cpa')) {
    return `In the Philippines, the Certified Public Accountant (CPA) title requires passing the official CPALE board exam and is legally required for public auditing and signing financial statements.\n\nHowever, many corporate accounting, bookkeeping, and financial analyst roles hire Bachelor of Science in Accountancy (BSA) or Finance graduates without immediate CPA licensure.`;
  }
  if (id.includes('electrician')) {
    return `Commercial electrical work requires safety discipline and physical stamina, but following established electrical codes and wearing proper PPE makes it a very safe and respected trade.\n\nIn the Philippines, obtaining TESDA NC II and working toward the Registered Master Electrician (RME) license provides legal authorization and opens high-demand opportunities.`;
  }
  return `For ${title}, core prerequisites center on practical problem solving and foundational tool literacy. Proof of hands-on capability is prioritized over rigid academic hurdles.`;
}

/**
 * Question Intent Catalog
 */
export const QUESTION_CATALOG: QuestionIntentDef[] = [
  // ==========================================
  // WHAT TO BE
  // ==========================================
  {
    intent: 'overview',
    category: 'WHAT',
    priority: 'HIGH',
    getQuestionText: (c) => `What does a ${c.title} actually do?`,
    getAnswer: (c) => {
      const tagline = c.tagline ? `${c.tagline}\n\n` : '';
      const desc = c.description || `${c.title}s specialize in delivering practical solutions within the ${c.field} sector.`;
      return `${tagline}${desc}\n\nTheir primary focus is translating domain objectives into dependable, high-quality outcomes.`;
    },
  },
  {
    intent: 'daily_work',
    category: 'WHAT',
    priority: 'HIGH',
    getQuestionText: (c) => `What does a typical day look like for a ${c.title}?`,
    getAnswer: (c) => {
      const workStyle = c.work_style || 'Focused individual building combined with team coordination';
      return `A typical workday for a ${c.title} balances focused execution and collaborative review:\n\n• Morning (30–45 mins): A quick team sync or standup to review priorities, unblock tasks, and plan the day.\n• Core Focus Block (2–4 hours): Deep, uninterrupted work time dedicated to primary deliverables.\n• Afternoon (1–2 hours): Cross-functional reviews with teammates, testing, and refining deliverables.\n\nWork Style: ${workStyle}.`;
    },
  },
  {
    intent: 'responsibilities',
    category: 'WHAT',
    priority: 'MEDIUM',
    getQuestionText: (c) => `What are the core responsibilities of this role?`,
    getAnswer: (c) => {
      if (c.core_skills && c.core_skills.length > 0) {
        return `As a ${c.title}, key responsibilities center on:\n\n` +
          c.core_skills.slice(0, 4).map((s) => `• Executing and maintaining high standards in ${s}.`).join('\n') +
          `\n\nYou are responsible for delivering reliable outcomes, documenting your work clearly, and collaborating smoothly with project stakeholders.`;
      }
      return `The primary responsibilities of a ${c.title} involve planning, building, and maintaining core deliverables while adhering to industry safety, quality, and performance standards.`;
    },
  },
  {
    intent: 'tools',
    category: 'WHAT',
    priority: 'MEDIUM',
    getQuestionText: (c) => `What tools and technologies are commonly used?`,
    getAnswer: (c) => {
      const tools = c.common_tools || [];
      if (tools.length > 0) {
        return `Standard industry tools used by ${c.title}s include:\n\n` +
          tools.slice(0, 6).map((t) => `• ${t}`).join('\n') +
          `\n\nBecoming comfortable with these tools builds the foundation for everyday workflow efficiency.`;
      }
      return `Tools vary based on the specific specialization, but typically include industry-standard planning, production, and testing software.`;
    },
  },
  {
    intent: 'environment',
    category: 'WHAT',
    priority: 'LOW',
    getQuestionText: (c) => `Where do ${c.title}s usually work?`,
    getAnswer: (c) => {
      const style = c.work_style || 'Office / Hybrid environment';
      return `${c.title}s typically operate in ${style}.\n\nDepending on the employer, roles range from co-located office teams to fully distributed remote setups and on-site field locations.`;
    },
  },

  // ==========================================
  // WHY TO BE
  // ==========================================
  {
    intent: 'required_skills',
    category: 'WHY',
    priority: 'HIGH',
    getQuestionText: (c) => `What skills should I have for this career?`,
    getAnswer: (c) => {
      const core = c.core_skills || [];
      const optional = c.optional_skills || [];
      return `To thrive as a ${c.title}, you want to develop both core functional capabilities and supportive strengths:\n\nCore Foundations:\n` +
        core.slice(0, 4).map((s) => `• ${s}`).join('\n') +
        (optional.length > 0
          ? `\n\nValuable Differentiators:\n` + optional.slice(0, 3).map((s) => `• ${s}`).join('\n')
          : '');
    },
  },
  {
    intent: 'prerequisite_concern',
    category: 'WHY',
    priority: 'HIGH',
    getQuestionText: (c) => getPrerequisiteQuestion(c),
    getAnswer: (c) => getPrerequisiteAnswer(c),
  },
  {
    intent: 'challenges',
    category: 'WHY',
    priority: 'MEDIUM',
    getQuestionText: (c) => `What are the most challenging parts of this career?`,
    getAnswer: (c) => {
      return `Every career has real tradeoffs. For a ${c.title}, the primary challenges often include:\n\n• Continuous Evolution: Tools and best practices advance quickly, requiring ongoing self-learning.\n• Problem Complexity: Troubleshooting unexpected bugs or bottlenecks requires patience and structured thinking.\n• Scope Balancing: Balancing quality polish with deadlines and stakeholder requirements.\n\nKnowing these upfront helps you build healthy pacing and steady problem-solving habits.`;
    },
  },
  {
    intent: 'career_fit',
    category: 'WHY',
    priority: 'MEDIUM',
    getQuestionText: (c) => `Why might this career fit someone with my profile?`,
    getAnswer: (c, userCtx) => {
      const name = userCtx?.preferredName || 'Explorer';
      const traits = userCtx?.topTraits;
      const skills = userCtx?.selectedSkills;

      let fitReason = `Based on the nature of ${c.title}, this career is an engaging fit for people who enjoy structured problem solving, clear tangible results, and ongoing skill growth.`;

      if (traits && traits.length > 0) {
        fitReason = `Based on your profile highlights in ${traits.join(', ')}, ${c.title} connects naturally with your curiosity and work style.`;
      }

      if (skills && skills.length > 0) {
        fitReason += `\n\nYour existing familiarity with ${skills.slice(0, 3).join(', ')} gives you an encouraging starting point to build upon.`;
      }

      return fitReason;
    },
  },
  {
    intent: 'related_careers',
    category: 'WHY',
    priority: 'LOW',
    getQuestionText: (c) => `What careers are closely related to this one?`,
    getAnswer: (c) => {
      const relatedIds = c.related_careers || [];
      const relatedNames = relatedIds
        .map((rId) => CAREERS.find((x) => x.id === rId)?.title || rId.replace(/-/g, ' '))
        .filter(Boolean);

      if (relatedNames.length > 0) {
        return `If you find ${c.title} interesting, you may also want to explore these related pathways:\n\n` +
          relatedNames.map((r) => `• ${r}`).join('\n') +
          `\n\nThese roles share foundational competencies and offer flexible pivot opportunities as your interests develop.`;
      }
      return `Related roles span adjacent areas in ${c.field}, allowing you to transfer core problem-solving and communication skills across specializations.`;
    },
  },

  // ==========================================
  // HOW TO BE
  // ==========================================
  {
    intent: 'learn_first',
    category: 'HOW',
    priority: 'HIGH',
    getQuestionText: (c) => `What should I learn first?`,
    getAnswer: (c) => {
      const tools = c.common_tools || [];
      const skills = c.core_skills || [];
      return `When starting out in ${c.title}, focus on one clean foundation before trying to learn advanced specializations:\n\n` +
        `• Step 1 (Weeks 1–3): Master the fundamental concepts of ${skills[0] || 'core theory'}.\n` +
        `• Step 2 (Weeks 4–6): Get hands-on with essential industry tools like ${tools[0] || 'standard workflow tools'}.\n` +
        `• Step 3 (Weeks 7–8): Build your first small, end-to-end beginner project to cement the workflow.\n\n` +
        `Protecting 1 to 2 focused hours a day will give you noticeable momentum within a couple of months.`;
    },
  },
  {
    intent: 'projects',
    category: 'HOW',
    priority: 'HIGH',
    getQuestionText: (c) => `What kind of projects can I build for my portfolio?`,
    getAnswer: (c) => {
      const projects = c.portfolio_projects || [];
      if (projects.length > 0) {
        return `Here are realistic portfolio projects suitable for a ${c.title}:\n\n` +
          projects.slice(0, 3).map((p) => `• ${p.title} (${p.difficulty}): ${p.description}`).join('\n\n') +
          `\n\nFocus on finishing 2 to 3 polished projects that solve real problems rather than starting dozens of half-finished demos.`;
      }
      return `Build 2 or 3 small, working projects that solve clear practical problems. Document your thought process, challenges faced, and how you verified your solution.`;
    },
  },
  {
    intent: 'education',
    category: 'HOW',
    priority: 'MEDIUM',
    getQuestionText: (c) => `What education or training is recommended?`,
    getAnswer: (c) => {
      const paths = c.education_paths || [];
      if (['registered-nurse', 'civil-engineer', 'cpa-accountant'].includes(c.id)) {
        return `In the Philippines, ${c.title} is a legally regulated profession requiring an accredited 4-year Bachelor's degree and passing the official PRC Board Examination.\n\nFormal clinical or engineering units are required by law before professional practice.`;
      }
      if (paths.length > 0) {
        return `Common pathways to enter ${c.title} include:\n\n` +
          paths.map((p) => `• ${p}`).join('\n') +
          `\n\nIn technology, design, and digital operations, hiring managers prioritize tangible proof of capability (working portfolio projects, GitHub code repositories, and problem-solving ability) over formal pedigree alone.`;
      }
      return `Both formal degree programs and dedicated self-directed project portfolios are respected pathways to enter this field.`;
    },
  },
  {
    intent: 'certifications',
    category: 'HOW',
    priority: 'LOW',
    getQuestionText: (c) => `Are there certifications worth considering?`,
    getAnswer: (c) => {
      const certs = c.certifications || [];
      if (certs.length > 0) {
        return `Industry certifications that carry recognized weight for ${c.title} include:\n\n` +
          certs.slice(0, 3).map((crt) => `• ${crt.name} (${crt.provider || 'Accredited'}) — ${crt.cost || 'Standard fee'}`).join('\n') +
          `\n\nCertifications validate structured competence, but pairing them with real project proof gives you the strongest advantage.`;
      }
      return `Certifications can be helpful for resume validation, but building 2 to 3 real-world portfolio projects is almost always the highest-ROI investment of your study time.`;
    },
  },
  {
    intent: 'next_step',
    category: 'HOW',
    priority: 'HIGH',
    getQuestionText: (c) => `What should I do next to get started?`,
    getAnswer: (c) => {
      return `Here are the 3 most practical next steps you can take today for ${c.title}:\n\n` +
        `1. Build Your Personalized Roadmap: Add ${c.title} to your TO BE pathway to get milestone-by-milestone guided tasks.\n` +
        `2. Test in One Afternoon: Build one mini-exercise with ${c.common_tools?.[0] || 'core tools'} to see how the problem-solving feels to you.\n` +
        `3. Bookmark Curated Free Resources: Check the Learning Resources section on this career page for free, high-quality learning materials.`;
    },
  },

  // ==========================================
  // PRACTICAL MARKET
  // ==========================================
  {
    intent: 'salary',
    category: 'PRACTICAL',
    priority: 'MEDIUM',
    getQuestionText: (c) => `What is the entry-level salary benchmark in the Philippines?`,
    getAnswer: (c) => {
      const sal = c.salary_data?.philippines;
      if (sal) {
        return `Verified compensation benchmarks in the Philippines for ${c.title}:\n\n` +
          `• Entry-Level: ${sal.entry_level} (${sal.currency})\n` +
          `• Mid-Level: ${sal.mid_level} (${sal.currency})\n` +
          `• Senior-Level: ${sal.senior_level} (${sal.currency})\n\n` +
          `Source: ${sal.source} (Updated: ${sal.updated_at}). Compensation grows significantly with practical portfolio execution and domain mastery.`;
      }
      return `Salary data is currently being benchmarked for this specific role. Entry-level digital roles in the Philippines typically start between ₱25,000 and ₱45,000 monthly.`;
    },
  },
  {
    intent: 'remote_work',
    category: 'PRACTICAL',
    priority: 'LOW',
    getQuestionText: (c) => `Can this career be done remotely or freelance?`,
    getAnswer: (c) => {
      const id = c.id.toLowerCase();
      if (['commercial-electrician', 'registered-nurse', 'civil-engineer'].includes(id)) {
        return `This role is primarily an on-site, in-person profession requiring hands-on physical presence in clinical, construction, or maintenance environments.\n\nHowever, experienced professionals in this domain often expand into consultative, project planning, or administrative compliance roles that offer greater scheduling flexibility.`;
      }
      return `Yes. ${c.title} is among the most remote-friendly careers in the modern job market.\n\nBecause work deliverables are digital and team communication happens asynchronously, many professionals work for distributed international companies or maintain independent freelance clients from the Philippines.`;
    },
  },
];

/**
 * Question Selection Engine
 * Selects up to 3 prioritized, unexplored question intents for the current career.
 */
export class GuidedMentorEngine {
  /**
   * Get dynamic initial questions for a career.
   */
  getInitialQuestions(career: Career): QuestionIntentDef[] {
    const highPriority = QUESTION_CATALOG.filter((q) => q.priority === 'HIGH');
    
    // Pick 1 WHAT, 1 WHY, 1 HOW
    const what = highPriority.find((q) => q.category === 'WHAT') || QUESTION_CATALOG.find((q) => q.category === 'WHAT');
    const why = highPriority.find((q) => q.category === 'WHY') || QUESTION_CATALOG.find((q) => q.category === 'WHY');
    const how = highPriority.find((q) => q.category === 'HOW') || QUESTION_CATALOG.find((q) => q.category === 'HOW');

    const selected = [what, why, how].filter(Boolean) as QuestionIntentDef[];
    return selected.slice(0, 3);
  }

  /**
   * Get next 3 questions based on what has been explored so far.
   */
  getNextQuestions(career: Career, exploredIntents: string[]): QuestionIntentDef[] {
    const unexplored = QUESTION_CATALOG.filter((q) => !exploredIntents.includes(q.intent));

    if (unexplored.length === 0) {
      return [];
    }

    // Sort by priority: HIGH > MEDIUM > LOW
    const priorityWeight: Record<string, number> = { HIGH: 3, MEDIUM: 2, LOW: 1 };
    const sorted = [...unexplored].sort((a, b) => priorityWeight[b.priority] - priorityWeight[a.priority]);

    // Ensure category variety where possible
    const selected: QuestionIntentDef[] = [];
    const usedCategories = new Set<string>();

    for (const item of sorted) {
      if (!usedCategories.has(item.category) && selected.length < 3) {
        selected.push(item);
        usedCategories.add(item.category);
      }
    }

    // Fill remaining slots if < 3
    for (const item of sorted) {
      if (selected.length < 3 && !selected.some((s) => s.intent === item.intent)) {
        selected.push(item);
      }
    }

    return selected.slice(0, 3);
  }

  /**
   * Generate specific grounded answer for an intent.
   */
  generateAnswer(intentName: string, career: Career, userCtx?: UserAssessmentContext): string {
    const intentDef = QUESTION_CATALOG.find((q) => q.intent === intentName);
    if (intentDef) {
      return intentDef.getAnswer(career, userCtx);
    }
    return `For ${career.title}, focusing on foundational fundamentals and building real projects is the most dependable path forward.`;
  }

  /**
   * Check if user has explored enough core topics to display completion actions.
   */
  checkCompletion(exploredIntents: string[]): boolean {
    const highPriorityIntents = QUESTION_CATALOG.filter((q) => q.priority === 'HIGH').map((q) => q.intent);
    const exploredHigh = highPriorityIntents.filter((h) => exploredIntents.includes(h));
    
    // Complete if >= 5 total intents or at least 4 high-priority intents explored
    return exploredIntents.length >= 5 || exploredHigh.length >= 4;
  }
}

export const guidedMentorEngine = new GuidedMentorEngine();
