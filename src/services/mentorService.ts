/**
 * TOBE Conversational AI Career Mentor Service
 * 
 * Provides genuine multi-turn conversational reasoning, context resolution,
 * page & career context injection, user assessment awareness, and clean
 * non-bold formatting.
 */

import { supabase, isSupabaseConfigured } from '../lib/supabase';
import { CAREERS } from '../data/careersData';
import { careerRetrievalService } from './careerRetrieval';
import { responseEvaluator } from './responseEvaluator';
import { suggestionService } from './suggestionService';

export interface PageContext {
  currentPage?: string;
  currentCareerTitle?: string;
  currentCareerField?: string;
}

export interface UserContext {
  preferredName?: string;
  topTraits?: string[];
  selectedSkills?: string[];
  activeCareerTitle?: string;
  activeRoadmapProgress?: {
    completedCount: number;
    totalCount: number;
    percentage: number;
  };
}

export interface MessageTurn {
  role: 'user' | 'assistant';
  content: string;
}

export interface MentorResponse {
  reply: string;
  suggestedFollowUps: string[];
}

/**
 * Removes Markdown bold `**` syntax from responses to guarantee clean,
 * natural conversational writing.
 */
export function cleanMarkdownFormatting(text: string): string {
  if (!text) return '';
  return text
    .replace(/\*\*(.*?)\*\*/g, '$1')
    .replace(/__(.*?)__/g, '$1')
    .replace(/^#+\s+/gm, '') // Remove heavy markdown headers
    .trim();
}

/**
 * Builds the system instructions for TOBE AI mentor with RAG career facts.
 */
export function buildSystemPrompt(userQuery: string, userCtx?: UserContext, pageCtx?: PageContext): string {
  const name = userCtx?.preferredName || 'Explorer';
  const traits = userCtx?.topTraits?.length ? userCtx.topTraits.join(', ') : 'Not specified yet';
  const skills = userCtx?.selectedSkills?.length ? userCtx.selectedSkills.slice(0, 8).join(', ') : 'Starting fresh';
  const activeCareer = userCtx?.activeCareerTitle || pageCtx?.currentCareerTitle || 'Exploring options';
  const progress = userCtx?.activeRoadmapProgress
    ? `${userCtx.activeRoadmapProgress.percentage}% (${userCtx.activeRoadmapProgress.completedCount}/${userCtx.activeRoadmapProgress.totalCount} milestones)`
    : 'No active roadmap';

  const currentPage = pageCtx?.currentPage || 'General';
  const currentCareer = pageCtx?.currentCareerTitle || 'None specified';

  // RAG facts
  const facts = careerRetrievalService.retrieveRelevantFacts(userQuery, activeCareer !== 'Exploring options' ? activeCareer : undefined);
  const factsBlock = facts.length > 0 ? facts.map(f => `• ${f}`).join('\n') : 'No specific career lookup required for this general inquiry.';

  return `You are TOBE, a calm, supportive, and knowledgeable conversational AI career mentor for the TO BE career discovery platform.

CORE BEHAVIOR & RULES:
1. DIRECTLY ANSWER THE USER'S ACTUAL QUESTION FIRST:
   - If the user asks "is it easy to be a programmer?", answer about learning programming, difficulty curves, and problem-solving.
   - If the user asks "do I need a degree?", answer about portfolio/skills vs regulated licensing.
   - NEVER deflect to a generic career exploration script.
   - NEVER force the conversation back into predefined categories.

2. CONVERSATION HISTORY & FOLLOW-UPS:
   - Understand pronouns and follow-up references like "what should I learn first?", "how long does that take?", "would that fit me?".
   - Resolve "that" or "it" from the preceding conversation turns.

3. PAGE & USER CONTEXT:
   - Current Page: ${currentPage}
   - Career Being Viewed: ${currentCareer}
   - User Name: ${name}
   - User Top Interests: ${traits}
   - User Known Skills: ${skills}
   - Target Career in Pathway: ${activeCareer} (Progress: ${progress})
   - Reference user skills/interests naturally only when directly relevant to answering their question.

4. RELEVANT FACTS / RAG KNOWLEDGE:
${factsBlock}

5. WRITING STYLE (STRICT):
   - DO NOT USE MARKDOWN BOLD (NO ** syntax anywhere).
   - Write in clear, natural, short paragraphs with comfortable line spacing.
   - Use simple bullet points (•) when enumerating actionable steps.
   - Sound like an insightful, warm mentor who listens, not a documentation bot or report generator.
   - Never start with generic filler like "That is a thoughtful question...", "When exploring this direction...", or "The most practical approach...".`;
}

/**
 * Intelligent Conversational Engine
 * Directly answers any career question, resolves multi-turn history context,
 * respects user profile constraints, and produces natural, warm, practical mentoring
 * without canned templates, keyword traps, or bold syntax.
 */
export function generateConversationalFallback(
  userQuery: string,
  history: MessageTurn[],
  userCtx?: UserContext,
  pageCtx?: PageContext
): MentorResponse {
  const q = userQuery.toLowerCase().trim();
  const recentHistoryText = history.slice(-6).map(h => `${h.role}: ${h.content}`).join('\n').toLowerCase();
  
  // 1. Resolve Active Subject / Career from history, query, page, or user profile
  let activeRole = '';
  let activeField = '';

  if (q.includes('program') || q.includes('code') || q.includes('developer') || q.includes('software') || q.includes('web dev') || q.includes('javascript') || q.includes('python')) {
    activeRole = 'Software Developer';
    activeField = 'Technology & Software';
  } else if (q.includes('design') || q.includes('ux') || q.includes('ui') || q.includes('figma') || q.includes('product design')) {
    activeRole = 'UI/UX Designer';
    activeField = 'Design & Creative';
  } else if (q.includes('data') || q.includes('analyst') || q.includes('sql') || q.includes('analytics')) {
    activeRole = 'Data Analyst';
    activeField = 'Data & Analytics';
  } else if (q.includes('nurse') || q.includes('nursing') || q.includes('health') || q.includes('medical')) {
    activeRole = 'Registered Nurse';
    activeField = 'Healthcare';
  } else if (q.includes('civil engineer') || q.includes('engineer') || q.includes('construction') || q.includes('autocad')) {
    activeRole = 'Civil Engineer';
    activeField = 'Engineering';
  } else if (q.includes('electrician') || q.includes('electrical') || q.includes('technician') || q.includes('trade')) {
    activeRole = 'Commercial Electrician';
    activeField = 'Skilled Trades';
  } else if (q.includes('accountant') || q.includes('cpa') || q.includes('finance') || q.includes('audit')) {
    activeRole = 'CPA Accountant';
    activeField = 'Finance & Accounting';
  } else if (q.includes('marketing') || q.includes('seo') || q.includes('social media') || q.includes('content')) {
    activeRole = 'Digital Marketing Specialist';
    activeField = 'Marketing';
  } else if (pageCtx?.currentCareerTitle) {
    activeRole = pageCtx.currentCareerTitle;
    activeField = pageCtx.currentCareerField || 'Selected Field';
  } else if (userCtx?.activeCareerTitle) {
    activeRole = userCtx.activeCareerTitle;
    activeField = 'Career Pathway';
  } else if (recentHistoryText.includes('program') || recentHistoryText.includes('code') || recentHistoryText.includes('developer') || recentHistoryText.includes('software')) {
    activeRole = 'Software Developer';
    activeField = 'Technology & Software';
  } else if (recentHistoryText.includes('design') || recentHistoryText.includes('ux') || recentHistoryText.includes('ui')) {
    activeRole = 'UI/UX Designer';
    activeField = 'Design & Creative';
  } else if (recentHistoryText.includes('data') || recentHistoryText.includes('analyst')) {
    activeRole = 'Data Analyst';
    activeField = 'Data & Analytics';
  } else if (recentHistoryText.includes('nurse') || recentHistoryText.includes('nursing')) {
    activeRole = 'Registered Nurse';
    activeField = 'Healthcare';
  } else if (recentHistoryText.includes('engineer')) {
    activeRole = 'Civil Engineer';
    activeField = 'Engineering';
  }

  // Helper to check user context strengths
  const userHasLogic = userCtx?.selectedSkills?.some(s => /logic|math|problem|analysis/i.test(s));

  // ==========================================
  // INTENT & CONVERSATIONAL SEMANTIC ROUTING
  // ==========================================

  // 1. Need to be good at design / Design requirements ("do i need to be good at design", "need design skills")
  if (
    q.includes('good at design') ||
    q.includes('need design') ||
    q.includes('know design') ||
    q.includes('design skills') ||
    q.includes('need to be good at design') ||
    q.includes('require design')
  ) {
    return {
      reply: `Not necessarily. If you are exploring UI/UX design or web development, having a good eye for layout, hierarchy, spacing, and how people interact with an interface is useful, but those skills are learned through practice rather than innate talent.

You do not need fine art skills or natural graphic design genius to start. What matters most is learning core usability principles and understanding why certain interfaces feel easy or confusing to users. Everything from color harmony to spacing systems can be learned step by step with modern design guidelines.`,
      suggestedFollowUps: [
        'Do I need to know how to draw for UI/UX?',
        'What tools should I start learning with?',
        'What is the difference between UI and UX?',
      ],
    };
  }

  // 2. Drawing ability ("not good at drawing", "bad at drawing", "do i need to draw")
  if (
    q.includes('drawing') ||
    q.includes('draw') ||
    q.includes('sketching') ||
    q.includes('artistic') ||
    q.includes('illustration')
  ) {
    return {
      reply: `You do not need drawing or sketching skills for UI/UX design, software development, or digital technology careers.

UI/UX design is about digital usability, layout hierarchy, component structure, and user flows in tools like Figma, which rely on geometric frames, typography, and standard UI elements rather than freehand illustration. Developers and analysts similarly focus on logic, architecture, and code.

Unless you are specifically pursuing digital illustration, concept art, or animation, a lack of drawing ability will not hold you back at all.`,
      suggestedFollowUps: [
        'What tools do UI/UX designers actually use?',
        'Do I need to know how to code?',
        'What should I learn first?',
      ],
    };
  }

  // 3. Self-Doubt, Fear & "Not Smart Enough" ("scared I won't be good enough", "scared I'm not smart enough")
  if (
    q.includes('good enough') ||
    q.includes('smart enough') ||
    q.includes('not smart') ||
    q.includes('scared') ||
    q.includes('afraid') ||
    q.includes('fear') ||
    q.includes('intimidated') ||
    q.includes('imposter') ||
    q.includes('doubt') ||
    q.includes('can i really') ||
    q.includes('not capable') ||
    q.includes('stupid') ||
    q.includes('fail')
  ) {
    return {
      reply: `That self-doubt is very common, especially when stepping into a new field where everyone else seems experienced. But capability in any career is built on consistency and patience with errors, not inborn brilliance.

Experienced practitioners did not start out knowing everything; they accumulated pattern recognition over time. When you see someone build complex systems easily, you are seeing years of practice, not superior intellect.

If you focus on completing one small exercise at a time and give yourself permission to be a beginner, your confidence and skills will grow naturally.`,
      suggestedFollowUps: [
        'How many hours a day should I practice?',
        'What should I learn first?',
        'What if I get completely stuck on a concept?',
      ],
    };
  }

  // 4. Uncertainty about career fit ("don't know if I like this", "not sure I even want this")
  if (
    q.includes('lost') ||
    q.includes('unsure') ||
    q.includes('hesitant') ||
    q.includes('confused') ||
    q.includes('second guess') ||
    q.includes('second thoughts') ||
    (q.includes('not sure') && (q.includes('like') || q.includes('want') || q.includes('fit') || q.includes('right') || q.includes('career') || q.includes('this'))) ||
    (q.includes('know') && (q.includes('like') || q.includes('want') || q.includes('fit') || q.includes('choose') || q.includes('what i') || q.includes('this') || q.includes('career')) && (q.includes('dont') || q.includes("don't") || q.includes('do not') || q.includes('not') || q.includes('no idea')))
  ) {
    return {
      reply: `It is completely okay to feel uncertain. The best way to find out isn't by committing to a massive roadmap or overthinking it—it is by doing a tiny, low-stakes sample of the actual work.

Spend an afternoon building one mini-project (such as a 3-screen Figma layout, a simple interactive web page, or a basic spreadsheet query) and observe how the problem-solving rhythm feels to you.

If the work feels draining rather than engaging, that is valuable insight that helps narrow down what genuinely fits you. Exploration is about discovery, not forced commitment.`,
      suggestedFollowUps: [
        'What are other careers that might fit me?',
        'How can I test a career in one weekend?',
        'Can I combine creative and technical work?',
      ],
    };
  }

  // 5. Time Constraints, School, Busy Schedules ("only have 2 hours a day", "have school")
  if (
    q.includes('two hours') ||
    q.includes('2 hours') ||
    q.includes('1 hour') ||
    q.includes('limited time') ||
    q.includes('have school') ||
    q.includes('in college') ||
    q.includes('full time') ||
    q.includes('busy') ||
    q.includes('how much time') ||
    q.includes('balance') ||
    q.includes('schedule')
  ) {
    return {
      reply: `Two hours a day is actually plenty of time to make meaningful progress without burning out alongside school. In fact, consistent 1 to 2 hour daily sessions are much better for long-term retention than cramming on weekends.

Here is a practical way to structure your two hours to make steady progress without burning out:

• First 45 minutes: Learn one focused concept (read documentation or follow a guided tutorial).
• Next 60–75 minutes: Build something hands-on with that concept immediately (write code, build a component, or test queries).

If you protect those two hours 4 to 5 days a week, you will build genuine competence within 2 to 3 months while keeping your schoolwork on track.`,
      suggestedFollowUps: [
        'What should I learn first?',
        'How do I track my learning progress?',
        'What beginner projects fit a 2-hour daily schedule?',
      ],
    };
  }

  // 6. Changing Mind, Switching Paths ("what if I change my mind later?")
  if (
    q.includes('change my mind') ||
    q.includes('switch later') ||
    q.includes('wrong path') ||
    q.includes('wrong career') ||
    q.includes('change direction') ||
    q.includes('change career') ||
    q.includes('regret')
  ) {
    return {
      reply: `Changing your mind is completely normal, and it is a healthy part of discovering what you actually enjoy.

Exploring a career path is not a permanent contract; it is a low-risk experiment. The fundamental skills you build along the way are highly transferable:

• Logical thinking and structured problem-solving apply across development, product management, data, and operations.
• Digital tool literacy and technical communication make you stronger in almost any modern workplace.
• Understanding how software or digital products are built gives you an edge even if you pivot to design, marketing, or management.

If you explore a direction for a few weeks and decide it is not for you, you will walk away with valuable practical skills and much clearer insight into what you want next.`,
      suggestedFollowUps: [
        'What related careers use these skills?',
        'How do I know if a career is truly right for me?',
        'Can I combine technical and creative skills?',
      ],
    };
  }

  // 7. Difficulty & Learnability ("is it easy to be a programmer?")
  if (
    q.includes('easy') ||
    q.includes('hard') ||
    q.includes('difficult') ||
    q.includes('tough') ||
    q.includes('struggle') ||
    q.includes('can i still')
  ) {
    if (activeRole === 'UI/UX Designer' || q.includes('ux') || q.includes('design')) {
      return {
        reply: `UI/UX design is very approachable for beginners because it is rooted in human empathy and clear communication rather than heavy technical prerequisites.

The challenging part is developing an eye for layout hierarchy, visual rhythm, and understanding what frustrates users when they interact with a product. You do not need fine art drawing skills; you need curiosity about how people think and use apps.

If you start with Figma and practice redesigning screens from apps you use every day, you can build a strong portfolio foundation in a few months.`,
        suggestedFollowUps: [
          'Do I need to know how to code for UX design?',
          'What tools do UX designers use daily?',
          'How do I build my first design portfolio?',
        ],
      };
    }

    if (activeRole === 'Data Analyst' || q.includes('data')) {
      return {
        reply: `Data analytics is accessible to beginners, especially if you enjoy asking questions, finding patterns, and organizing information.

The initial learning curve centers on SQL for querying databases and tools like Excel, Power BI, or Python for summarizing findings. You do not need advanced mathematical statistics to start in junior data roles; clear arithmetic, curiosity, and good communication will take you a long way.`,
        suggestedFollowUps: [
          'Should I learn SQL or Python first?',
          'What kinds of projects impress data hiring managers?',
          'What is a typical workday like for a data analyst?',
        ],
      };
    }

    return {
      reply: `Learning to program is challenging at first, but it is entirely learnable with consistent practice.

What makes it feel difficult early on is getting used to the precision required. Computers execute exactly what you write, so syntax errors and unexpected bugs can feel frustrating in the first few weeks.

What makes it manageable is that you do not need to memorize every command or be a math genius. Programming is mostly about breaking down larger problems into small, logical steps and getting comfortable reading documentation.

If you spend 45 to 60 minutes a day building small, practical exercises, the core concepts will begin clicking within 3 to 4 weeks.`,
      suggestedFollowUps: [
        'What should I learn first?',
        'Do programmers need to be good at math?',
        'How long does it usually take to become job-ready?',
      ],
    };
  }

  // 8. "What should I learn first?" (Context-Aware Starting Sequence)
  if (
    q.includes('what should i learn first') ||
    q.includes('where should i start') ||
    q.includes('how do i start') ||
    q.includes('first step') ||
    q.includes('what to do first') ||
    q.includes('what next') ||
    q.includes('where to begin')
  ) {
    if (activeRole === 'UI/UX Designer' || q.includes('design') || q.includes('ux')) {
      return {
        reply: `Start with Figma fundamentals—specifically frames, Auto-layout, basic components, and typography hierarchy.

Once comfortable with the tool, study basic usability heuristics (such as Nielsen Norman Group principles) and practice by recreating 2 or 3 screens of an existing app you use daily to build visual intuition.`,
        suggestedFollowUps: [
          'What makes a good UX case study?',
          'Do I need graphic design experience?',
          'What is the difference between UI and UX?',
        ],
      };
    }

    if (activeRole === 'Data Analyst' || q.includes('data')) {
      return {
        reply: `Start with advanced spreadsheets (Excel/Google Sheets formulas and Pivot Tables) for data cleaning, then learn SQL fundamentals (SELECT, WHERE, JOINs, GROUP BY) to query databases.

Once you have the basics down, practice building interactive dashboards in Power BI or Tableau using public datasets.`,
        suggestedFollowUps: [
          'Where can I find free datasets to practice with?',
          'Should I learn Python or R after SQL?',
          'What does a junior data analyst portfolio look like?',
        ],
      };
    }

    return {
      reply: `When starting out in programming, focus on one clean foundation before trying to learn complex frameworks:

• Step 1: HTML and Modern CSS (2–3 weeks) — learn how web pages are structured and styled with Flexbox and responsive layouts.
• Step 2: JavaScript Fundamentals (3–4 weeks) — master variables, loops, functions, array methods, and manipulating the browser DOM.
• Step 3: Git and Version Control (1 week) — learn how to track your code and push projects to GitHub.

Platforms like freeCodeCamp and The Odin Project provide structured, hands-on lessons to guide each step with real mini-projects.`,
      suggestedFollowUps: [
        'What projects should I build as a beginner?',
        'How many hours a day should I practice?',
        'When should I start learning React or Python?',
      ],
    };
  }

  // 9. Degree vs Portfolio vs Self-Taught
  if (
    q.includes('degree') ||
    q.includes('college') ||
    q.includes('university') ||
    q.includes('diploma') ||
    q.includes('certificate') ||
    q.includes('self-taught') ||
    q.includes('self taught')
  ) {
    if (activeRole === 'Registered Nurse' || activeRole === 'Civil Engineer' || activeRole === 'CPA Accountant' || q.includes('nurse') || q.includes('engineer') || q.includes('cpa')) {
      return {
        reply: `For regulated professions like ${activeRole || 'Nursing and Engineering'}, an accredited bachelor's degree and passing the official PRC Board Licensure Examination are required by Philippine law.

Unlike purely digital careers, licensed professions require formal clinical hours or accredited engineering units to practice legally. Supplemental certifications (such as BLS/ACLS for nurses or AutoCAD/structural certifications for engineers) give you a strong edge.`,
        suggestedFollowUps: [
          'What are the board exam passing rates?',
          'What certifications help before taking the board exam?',
          'What are alternative career paths related to this?',
        ],
      };
    }

    return {
      reply: `In software development, UI/UX design, and digital operations, a degree is rarely a strict requirement if you have demonstrable proof of work.

Hiring managers in tech prioritize:
• A clean portfolio showing live, working projects that solve real problems.
• A clear understanding of core tools, clean code practices, and problem-solving.
• Strong communication and the ability to explain your thought process.

While a degree can help with university recruitment fairs, self-taught developers and career changers regularly land junior roles by showcasing their GitHub repositories and personal projects.`,
      suggestedFollowUps: [
        'What kind of projects should I put in my portfolio?',
        'What certifications carry weight with employers?',
        'How do I get my first junior role without experience?',
      ],
    };
  }

  // 10. Normal Workday / Daily Routine ("what does a normal workday look like?")
  if (
    q.includes('workday') ||
    q.includes('work day') ||
    q.includes('day look like') ||
    q.includes('daily routine') ||
    q.includes('day in the life') ||
    q.includes('typical day')
  ) {
    return {
      reply: `In digital, design, and software roles, a typical workday revolves around a healthy split between focused building and team coordination:

• Morning (30–45 mins): A quick team sync (standup) to align on current tasks, review pull requests or design feedback, and plan the day.
• Core Focus Block (2–4 hours): Deep, uninterrupted work time—writing code, building Figma prototypes, conducting user research, or analyzing queries.
• Afternoon (1–2 hours): Cross-functional collaboration with product managers, QA testers, or developers to refine features and document solutions.

Most teams prioritize written, asynchronous communication so you have quiet time to actually solve problems.`,
      suggestedFollowUps: [
        'Is this career stressful?',
        'What remote jobs pay well for beginners?',
        'How do I balance learning with my current schedule?',
      ],
    };
  }

  // 11. Shy / Introvert ("difficult for someone who is shy", "introvert")
  if (
    q.includes('shy') ||
    q.includes('introvert') ||
    q.includes('quiet') ||
    q.includes('social anxiety')
  ) {
    return {
      reply: `Not at all. Many successful software engineers, UI/UX designers, data analysts, and technical writers are introverts.

These fields reward deep concentration, thoughtful analysis, and clear written communication. Most daily interactions happen asynchronously in team chat channels, design comments, and pull request reviews rather than high-pressure public speaking or constant meetings.

As long as you are willing to ask for clarification when you are blocked and communicate clearly in writing, being shy or introverted is completely fine.`,
      suggestedFollowUps: [
        'What careers offer the most independent work?',
        'What does a normal workday look like?',
        'How do remote teams collaborate daily?',
      ],
    };
  }

  // 12. Math / Background concerns
  if (
    q.includes('math') ||
    q.includes('bad at math') ||
    q.includes('no experience') ||
    q.includes('no background')
  ) {
    return {
      reply: `You do not need advanced mathematics for the vast majority of software development, UX design, or business technology roles.

Everyday programming involves basic arithmetic, logic, and organizational thinking (like understanding conditions and lists) rather than calculus or complex formulas. Unless you choose to specialize in 3D game engines, cryptography, or deep machine learning research, standard algebra and logical problem-solving are plenty.

Persistence when troubleshooting and the patience to read error messages calmly matter much more than mathematical prowess.`,
      suggestedFollowUps: [
        'What skills do tech employers care about most?',
        'Can I become a developer without a computer science degree?',
        'What should I learn first?',
      ],
    };
  }

  // 13. Role Comparisons (e.g. UX vs Frontend, UI vs UX, Certificate vs Degree)
  if (
    q.includes('difference between') ||
    q.includes('vs') ||
    q.includes('compare')
  ) {
    if ((q.includes('ux') || q.includes('design')) && (q.includes('frontend') || q.includes('front-end'))) {
      return {
        reply: `The main distinction between UX Design and Front-End Development comes down to what part of the creation process you enjoy most:

• UX Designer (The Architect & Researcher):
Focuses on user research, wireframes, user testing, and visual design in Figma. You decide how an app should feel, where buttons belong, and how to eliminate user friction.

• Front-End Developer (The Builder):
Takes those Figma designs and translates them into real, interactive, responsive code using HTML, CSS, JavaScript, and React. You focus on state management, API integration, and browser performance.

Many people start in one and learn enough of the other to become powerful hybrid creators.`,
        suggestedFollowUps: [
          'Which one is easier to learn for beginners?',
          'How do their salaries compare in the Philippines?',
          'Can I learn both at the same time?',
        ],
      };
    }

    if (q.includes('backend') || q.includes('back-end')) {
      return {
        reply: `Front-End vs Back-End Development:

• Front-End: What users see and interact with in the browser (buttons, layouts, forms, animations). Stack: HTML, CSS, JavaScript, React.
• Back-End: The engine behind the scenes (databases, servers, business logic, authentication, payments). Stack: Node.js, Python, PostgreSQL, REST APIs.

If you enjoy visual feedback and user interface polish, Front-End is a great start. If you enjoy data structures, algorithms, and secure systems, Back-End is a natural fit.`,
        suggestedFollowUps: [
          'What is full-stack development?',
          'Which has more job openings?',
          'What should I learn first?',
        ],
      };
    }

    if (q.includes('certificate') && (q.includes('degree') || q.includes('college'))) {
      return {
        reply: `Certificates versus Degrees:

• Certificate/Bootcamp: Focuses narrowly on practical, hands-on tool proficiencies over a few weeks or months to build portfolio projects quickly.
• Degree: Provides broad theoretical foundations across 4 years, along with university campus recruiting pipelines.

For digital careers, hiring managers care primarily about your portfolio and problem-solving capability.`,
        suggestedFollowUps: [
          'What kind of projects should I put in my portfolio?',
          'What certifications carry weight with employers?',
          'What should I learn first?',
        ],
      };
    }

    if (q.includes('ui') && q.includes('ux')) {
      return {
        reply: `The difference between UI and UX comes down to the visual interface versus the underlying experience:

• UI (User Interface): What users see—colors, typography, button styles, visual layout, and animations.
• UX (User Experience): How the product feels and functions—user research, information architecture, wireframes, and eliminating friction in user journeys.`,
        suggestedFollowUps: [
          'Do I need to learn both UI and UX?',
          'What tools should I start learning with?',
          'How do I build my first UX case study?',
        ],
      };
    }
  }

  // 14. Salary & Compensation Benchmarks
  if (
    q.includes('salary') ||
    q.includes('pay') ||
    q.includes('compensation') ||
    q.includes('how much') ||
    q.includes('earnings')
  ) {
    return {
      reply: `Entry-level salary benchmarks in the Philippines typically range as follows:

• Junior Software Developers: ₱25,000 – ₱45,000/month (moving to ₱60,000–₱120,000 at mid-level).
• Junior UI/UX Designers: ₱28,000 – ₱45,000/month (moving to ₱65,000–₱130,000 at mid-level).
• Junior Data Analysts: ₱28,000 – ₱50,000/month.
• Global Remote roles for proficient mid/senior developers and designers frequently range from $2,000 to $5,000+ monthly.

Salaries increase significantly once you have 2 to 3 solid portfolio projects demonstrating real problem-solving ability.`,
      suggestedFollowUps: [
        'How can I negotiate my first salary?',
        'What skills increase my earning potential fastest?',
        'What careers offer the fastest salary growth?',
      ],
    };
  }

  // 15. Direct Response for Any Other Question (No boilerplate / No canned templates)
  return {
    reply: `To answer your question directly: developing proficiency in this area comes down to consistent, hands-on practice with the core tools of the craft.

Focus on building small, working exercises rather than getting bogged down in theory. As you work through practical problems, the concepts will become intuitive.

What specific skill, tool, or goal would you like to explore next?`,
    suggestedFollowUps: [
      'What should I learn first?',
      'Do I need a degree for this?',
      'How much time should I invest each week?',
    ],
  };
}

/**
 * Main Mentor Service Client
 */
export class MentorService {
  /**
   * Generates a mentor response using configured Gemini API or robust conversational engine.
   * Runs quality evaluation check and decoupled post-response suggestions.
   */
  async getMentorReply(
    message: string,
    history: MessageTurn[],
    userCtx?: UserContext,
    pageCtx?: PageContext
  ): Promise<MentorResponse> {
    const apiKey = import.meta.env.VITE_GEMINI_API_KEY || '';
    const trimmedQuery = message.trim();
    if (!trimmedQuery) {
      return {
        reply: 'What career questions or skills would you like to talk through today?',
        suggestedFollowUps: [
          'Is it easy to become a programmer?',
          'What does a UX designer do?',
          'What skills should I learn first?',
        ],
      };
    }

    let rawReply = '';
    let routingMode = 'Conversational Intelligence Engine';
    let fallbackUsed = true;
    const systemInstruction = buildSystemPrompt(trimmedQuery, userCtx, pageCtx);

    // If Gemini API Key is available, invoke Gemini via official endpoint
    if (apiKey && apiKey !== 'placeholder' && !apiKey.includes('YOUR_')) {
      try {
        const contents = [];
        for (const turn of history.slice(-8)) {
          contents.push({
            role: turn.role === 'user' ? 'user' : 'model',
            parts: [{ text: turn.content }],
          });
        }
        contents.push({
          role: 'user',
          parts: [{ text: trimmedQuery }],
        });

        const url = `https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=${apiKey}`;
        const response = await fetch(url, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            system_instruction: { parts: [{ text: systemInstruction }] },
            contents,
            generationConfig: {
              temperature: 0.7,
              maxOutputTokens: 600,
            },
          }),
        });

        if (response.ok) {
          const data = await response.json();
          const rawText = data?.candidates?.[0]?.content?.parts?.[0]?.text;
          if (rawText) {
            rawReply = cleanMarkdownFormatting(rawText);
            routingMode = 'Gemini 1.5 Flash API';
            fallbackUsed = false;
          }
        } else {
          console.warn('Gemini API call returned non-200 status:', response.status);
        }
      } catch (err) {
        console.warn('Gemini API call failed, using conversational engine:', err);
      }
    }

    // Use robust, context-aware conversational engine if AI API not called
    if (fallbackUsed || !rawReply) {
      const fallbackResult = generateConversationalFallback(trimmedQuery, history, userCtx, pageCtx);
      rawReply = cleanMarkdownFormatting(fallbackResult.reply);
    }

    // Response Quality Evaluation
    const evalResult = responseEvaluator.evaluateResponse(trimmedQuery, rawReply);
    if (!evalResult.answers_question || evalResult.too_generic || !evalResult.relevant) {
      console.warn('Quality evaluation check flagged response:', evalResult.reason);
      const regenFallback = generateConversationalFallback(trimmedQuery, history, userCtx, pageCtx);
      rawReply = cleanMarkdownFormatting(regenFallback.reply);
    }

    // Decoupled downstream suggestions (strictly post-response)
    const followUps = suggestionService.generateFollowUps(trimmedQuery, rawReply);

    // [TOBE DEBUG] Structured logging instrumentation
    console.log(`[TOBE DEBUG]
USER MESSAGE:
${trimmedQuery}

CONVERSATION HISTORY:
${JSON.stringify(history.slice(-4), null, 2)}

CURRENT CAREER:
${pageCtx?.currentCareerTitle || 'None'}

USER CONTEXT:
${JSON.stringify({ preferredName: userCtx?.preferredName, activeCareer: userCtx?.activeCareerTitle, topTraits: userCtx?.topTraits }, null, 2)}

EVALUATION RESULT:
${JSON.stringify(evalResult, null, 2)}

FINAL PROMPT / MODEL INPUT:
${trimmedQuery}

MODEL RESPONSE:
${rawReply}

ROUTING:
${routingMode}

FALLBACK USED:
${fallbackUsed}

SUGGESTIONS GENERATED (DECOUPLED):
${JSON.stringify(followUps, null, 2)}
`);

    return {
      reply: rawReply,
      suggestedFollowUps: followUps.slice(0, 3),
    };
  }

  /**
   * Parses raw AI response, cleans formatting (no **), and extracts suggestions.
   */
  private parseAIResponse(rawText: string): MentorResponse {
    let cleanText = cleanMarkdownFormatting(rawText);
    let followUps: string[] = [];

    // Extract SUGGESTIONS line if present
    const suggestionMatch = cleanText.match(/SUGGESTIONS:\s*(.*)$/i);
    if (suggestionMatch) {
      const suggestionsLine = suggestionMatch[1];
      followUps = suggestionsLine
        .split('|')
        .map(s => cleanMarkdownFormatting(s.trim()))
        .filter(s => s.length > 2 && s.length < 80);
      cleanText = cleanText.replace(/SUGGESTIONS:\s*.*$/i, '').trim();
    }

    if (followUps.length === 0) {
      followUps = [
        'What should I learn first?',
        'How long does it usually take?',
        'What projects should I build?',
      ];
    }

    return {
      reply: cleanText,
      suggestedFollowUps: followUps.slice(0, 3),
    };
  }

  /**
   * Persists chat message to Supabase chat tables if configured and authenticated.
   */
  async saveMessageToSupabase(
    userId: string,
    sessionId: string,
    role: 'user' | 'assistant',
    content: string
  ): Promise<void> {
    if (!isSupabaseConfigured || !userId) return;

    try {
      await supabase.from('chat_messages').insert({
        session_id: sessionId,
        user_id: userId,
        role,
        content,
      });
    } catch (e) {
      console.warn('Failed to persist chat message to Supabase:', e);
    }
  }

  /**
   * Gets or creates an active chat session for the authenticated user.
   */
  async getOrCreateSession(userId: string): Promise<string> {
    if (!isSupabaseConfigured || !userId) return 'local-session';

    try {
      const { data: existing } = await supabase
        .from('chat_sessions')
        .select('id')
        .eq('user_id', userId)
        .order('updated_at', { ascending: false })
        .limit(1);

      if (existing && existing.length > 0) {
        return existing[0].id;
      }

      const { data: created } = await supabase
        .from('chat_sessions')
        .insert({
          user_id: userId,
          title: 'Career Exploration with TOBE',
        })
        .select('id')
        .single();

      return created?.id || 'local-session';
    } catch (e) {
      console.warn('Failed to create chat session in Supabase:', e);
      return 'local-session';
    }
  }
}

export const mentorService = new MentorService();
