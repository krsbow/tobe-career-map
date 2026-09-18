-- Seed Data for TO BE Career Platform Categories & Initial Careers

-- 1. Categories
insert into public.career_categories (id, name, icon) values
('development', 'Software & Web Development', '💻'),
('design', 'UI/UX & Product Design', '🎨'),
('data_ai', 'Data, Analytics & AI', '📊'),
('cloud_security', 'Cloud, DevOps & Cybersecurity', '🛡️'),
('product_management', 'Product & Tech Strategy', '🚀')
on conflict (id) do update set name = excluded.name, icon = excluded.icon;

-- 2. Careers (Sample SQL insertion)
insert into public.careers (
    id, title, field, category_id, tagline, description,
    responsibilities, riasec_traits, work_style, core_skills, optional_skills,
    common_tools, education_paths, certifications, portfolio_projects,
    salary_data, learning_resources, related_careers, sources, last_updated
) values
(
    'frontend-developer',
    'Front-End Developer',
    'Technology',
    'development',
    'Build responsive, accessible, interactive web experiences that users see and interact with daily.',
    'Front-End Developers build the client-facing side of web applications. They translate design wireframes and user interface specifications into clean, performant, and accessible code using HTML, CSS, JavaScript, and modern frameworks.',
    '["Translate UI/UX design mockups and wireframes into pixel-perfect, responsive web pages", "Develop interactive user interfaces using modern JavaScript/TypeScript frameworks (e.g., React, Vue, or Next.js)", "Optimize web applications for maximum speed, mobile responsiveness, and cross-browser compatibility", "Implement web accessibility standards (WCAG 2.1) to ensure inclusivity for all users", "Integrate front-end views with back-end RESTful APIs and GraphQL endpoints"]'::jsonb,
    '["A", "I", "R"]'::jsonb,
    'Project-based, collaborative with designers, balanced with independent coding flow.',
    '["HTML5", "CSS3", "JavaScript", "React", "TypeScript", "Responsive Design", "Git & GitHub", "REST APIs"]'::jsonb,
    '["Next.js", "Tailwind CSS", "Web Accessibility (a11y)", "GraphQL", "Performance Optimization", "Unit Testing (Jest/Vitest)"]'::jsonb,
    '["VS Code", "Figma", "Chrome DevTools", "GitHub", "Vercel / Netlify", "npm/pnpm"]'::jsonb,
    '["Self-taught through structured open-source curricula and interactive platforms (very common)", "Coding bootcamps focusing on modern full-stack / front-end workflows", "Bachelor''s degree in Computer Science, Information Technology, or related discipline"]'::jsonb,
    '[{"name": "freeCodeCamp Responsive Web Design Certification", "cost": "Free", "provider": "freeCodeCamp", "url": "https://www.freecodecamp.org/learn/2022/responsive-web-design/"}, {"name": "freeCodeCamp JavaScript Algorithms and Data Structures", "cost": "Free", "provider": "freeCodeCamp", "url": "https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures-v8/"}, {"name": "Meta Front-End Developer Professional Certificate", "cost": "Low-cost (Coursera FinAid Available)", "provider": "Coursera / Meta", "url": "https://www.coursera.org/professional-certificates/meta-front-end-developer"}]'::jsonb,
    '[{"title": "Accessible Portfolio Website", "description": "High-performance personal website featuring light/dark mode, semantic HTML, keyboard navigation, and WCAG AA contrast.", "difficulty": "Foundational"}, {"title": "Real-time Weather & Geo Dashboard", "description": "Interactive dashboard fetching live weather data, forecasts, and air quality using OpenWeather API with responsive chart visualizations.", "difficulty": "Intermediate"}, {"title": "Full-Featured E-Commerce / SaaS UI with Cart & State Management", "description": "Production-ready store frontend featuring product filtering, checkout flow, custom state hooks, and optimistic UI updates.", "difficulty": "Advanced"}]'::jsonb,
    '{"philippines": {"currency": "PHP", "entry_level": "₱300,000 – ₱540,000 / year (₱25k - ₱45k/mo)", "mid_level": "₱600,000 – ₱1,200,000 / year (₱50k - ₱100k/mo)", "senior_level": "₱1,200,000 – ₱2,400,000+ / year (₱100k - ₱200k+/mo)", "source": "Payscale PH, JobStreet Philippines Tech Salary Benchmarks", "updated_at": "2026-Q1"}, "global_usd": {"currency": "USD", "entry_level": "$65,000 – $85,000 / year", "mid_level": "$90,000 – $130,000 / year", "senior_level": "$140,000 – $190,000+ / year", "source": "Levels.fyi, US Bureau of Labor Statistics (Web Developers)", "updated_at": "2026-Q1"}}'::jsonb,
    '[{"title": "MDN Web Docs (Mozilla)", "type": "Documentation & Guides", "cost": "Free", "provider": "Mozilla", "url": "https://developer.mozilla.org/"}, {"title": "The Odin Project (Full Stack JavaScript)", "type": "Structured Curriculum", "cost": "Free", "provider": "The Odin Project", "url": "https://www.theodinproject.com/"}, {"title": "React Official Documentation", "type": "Interactive Tutorial", "cost": "Free", "provider": "React Team", "url": "https://react.dev/"}]'::jsonb,
    '["fullstack-developer", "ux-engineer", "ui-designer", "mobile-app-developer"]'::jsonb,
    '["MDN Developer Network", "U.S. Bureau of Labor Statistics", "Payscale", "Levels.fyi"]'::jsonb,
    '2026-09-01'
)
on conflict (id) do update set
    title = excluded.title,
    field = excluded.field,
    category_id = excluded.category_id,
    tagline = excluded.tagline,
    description = excluded.description,
    responsibilities = excluded.responsibilities,
    riasec_traits = excluded.riasec_traits,
    work_style = excluded.work_style,
    core_skills = excluded.core_skills,
    optional_skills = excluded.optional_skills,
    common_tools = excluded.common_tools,
    education_paths = excluded.education_paths,
    certifications = excluded.certifications,
    portfolio_projects = excluded.portfolio_projects,
    salary_data = excluded.salary_data,
    learning_resources = excluded.learning_resources,
    related_careers = excluded.related_careers,
    sources = excluded.sources,
    last_updated = excluded.last_updated;
