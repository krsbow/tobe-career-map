"""
Seed Knowledge Base for TO BE Career Platform.
Contains structured data for 26 multi-domain careers across Technology, Design, Healthcare,
Engineering, Finance, Education, Trades, and Communications with authentic PSOC and O*NET classifications.
"""

from typing import List, Dict, Any

CAREER_CATEGORIES = [
    {
        "id": "development",
        "name": "Software & Web Development",
        "icon": "\ud83d\udcbb"
    },
    {
        "id": "design",
        "name": "UI/UX & Creative Design",
        "icon": "\ud83c\udfa8"
    },
    {
        "id": "data_ai",
        "name": "Data, Analytics & AI",
        "icon": "\ud83d\udcca"
    },
    {
        "id": "cloud_security",
        "name": "Cloud, DevOps & Cybersecurity",
        "icon": "\ud83d\udee1\ufe0f"
    },
    {
        "id": "product_management",
        "name": "Product & Tech Strategy",
        "icon": "\ud83d\ude80"
    },
    {
        "id": "business_marketing",
        "name": "Business & Digital Marketing",
        "icon": "\ud83d\udcc8"
    },
    {
        "id": "healthcare",
        "name": "Healthcare & Life Sciences",
        "icon": "\ud83e\ude7a"
    },
    {
        "id": "engineering",
        "name": "Engineering & Architecture",
        "icon": "\u2699\ufe0f"
    },
    {
        "id": "finance_accounting",
        "name": "Finance & Accounting",
        "icon": "\ud83d\udcb0"
    },
    {
        "id": "education",
        "name": "Education & Training",
        "icon": "\ud83c\udf93"
    },
    {
        "id": "skilled_trades",
        "name": "Skilled Trades & Technical Services",
        "icon": "\ud83d\udd27"
    },
    {
        "id": "communications",
        "name": "Writing & Communications",
        "icon": "\u270d\ufe0f"
    }
]

CAREERS_SEED: List[Dict[str, Any]] = [
    {
        "id": "frontend-developer",
        "title": "Front-End Developer",
        "field": "Technology",
        "category_id": "development",
        "category_name": "Software & Web Development",
        "tagline": "Build responsive, accessible, interactive web experiences that users see and interact with daily.",
        "description": "Front-End Developers build the client-facing side of web applications. They translate design wireframes and user interface specifications into clean, performant, and accessible code using HTML, CSS, JavaScript, and modern frameworks.",
        "responsibilities": [
            "Translate UI/UX design mockups and wireframes into pixel-perfect, responsive web pages",
            "Develop interactive user interfaces using modern JavaScript/TypeScript frameworks (e.g., React, Vue, or Next.js)",
            "Optimize web applications for maximum speed, mobile responsiveness, and cross-browser compatibility",
            "Implement web accessibility standards (WCAG 2.1) to ensure inclusivity for all users",
            "Integrate front-end views with back-end RESTful APIs and GraphQL endpoints"
        ],
        "riasec_traits": [
            "A",
            "I",
            "R"
        ],
        "work_style": "Project-based, collaborative with designers, balanced with independent coding flow.",
        "core_skills": [
            "HTML5",
            "CSS3",
            "JavaScript",
            "React",
            "TypeScript",
            "Responsive Design",
            "Git & GitHub",
            "REST APIs"
        ],
        "optional_skills": [
            "Next.js",
            "Tailwind CSS",
            "Web Accessibility (a11y)",
            "GraphQL",
            "Performance Optimization",
            "Unit Testing (Jest/Vitest)"
        ],
        "common_tools": [
            "VS Code",
            "Figma",
            "Chrome DevTools",
            "GitHub",
            "Vercel / Netlify",
            "npm/pnpm"
        ],
        "education_paths": [
            "Self-taught through structured open-source curricula and interactive platforms (very common)",
            "Coding bootcamps focusing on modern full-stack / front-end workflows",
            "Bachelor's degree in Computer Science, Information Technology, or related discipline"
        ],
        "certifications": [
            {
                "name": "freeCodeCamp Responsive Web Design Certification",
                "cost": "Free",
                "provider": "freeCodeCamp",
                "url": "https://www.freecodecamp.org/learn/2022/responsive-web-design/"
            },
            {
                "name": "freeCodeCamp JavaScript Algorithms and Data Structures",
                "cost": "Free",
                "provider": "freeCodeCamp",
                "url": "https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures-v8/"
            },
            {
                "name": "Meta Front-End Developer Professional Certificate",
                "cost": "Low-cost (Coursera FinAid Available)",
                "provider": "Coursera / Meta",
                "url": "https://www.coursera.org/professional-certificates/meta-front-end-developer"
            }
        ],
        "portfolio_projects": [
            {
                "title": "Accessible Portfolio Website",
                "description": "High-performance personal website featuring light/dark mode, semantic HTML, keyboard navigation, and WCAG AA contrast.",
                "difficulty": "Foundational"
            },
            {
                "title": "Real-time Weather & Geo Dashboard",
                "description": "Interactive dashboard fetching live weather data, forecasts, and air quality using OpenWeather API with responsive chart visualizations.",
                "difficulty": "Intermediate"
            },
            {
                "title": "Full-Featured E-Commerce / SaaS UI with Cart & State Management",
                "description": "Production-ready store frontend featuring product filtering, checkout flow, custom state hooks, and optimistic UI updates.",
                "difficulty": "Advanced"
            }
        ],
        "salary_data": {
            "philippines": {
                "currency": "PHP",
                "entry_level": "\u20b1300,000 \u2013 \u20b1540,000 / year (\u20b125k - \u20b145k/mo)",
                "mid_level": "\u20b1600,000 \u2013 \u20b11,200,000 / year (\u20b150k - \u20b1100k/mo)",
                "senior_level": "\u20b11,200,000 \u2013 \u20b12,400,000+ / year (\u20b1100k - \u20b1200k+/mo)",
                "source": "Payscale PH, JobStreet Philippines Tech Salary Benchmarks",
                "updated_at": "2026-Q1"
            },
            "global_usd": {
                "currency": "USD",
                "entry_level": "$65,000 \u2013 $85,000 / year",
                "mid_level": "$90,000 \u2013 $130,000 / year",
                "senior_level": "$140,000 \u2013 $190,000+ / year",
                "source": "Levels.fyi, US Bureau of Labor Statistics (Web Developers)",
                "updated_at": "2026-Q1"
            }
        },
        "learning_resources": [
            {
                "title": "MDN Web Docs (Mozilla)",
                "type": "Documentation & Guides",
                "cost": "Free",
                "provider": "Mozilla",
                "url": "https://developer.mozilla.org/"
            },
            {
                "title": "The Odin Project (Full Stack JavaScript)",
                "type": "Structured Curriculum",
                "cost": "Free",
                "provider": "The Odin Project",
                "url": "https://www.theodinproject.com/"
            },
            {
                "title": "React Official Documentation",
                "type": "Interactive Tutorial",
                "cost": "Free",
                "provider": "React Team",
                "url": "https://react.dev/"
            }
        ],
        "related_careers": [
            "fullstack-developer",
            "ux-engineer",
            "ui-designer",
            "mobile-app-developer"
        ],
        "sources": [
            "MDN Developer Network",
            "U.S. Bureau of Labor Statistics",
            "Payscale",
            "Levels.fyi"
        ],
        "last_updated": "2026-09-01",
        "psoc_code": "2512",
        "soc_code": "15-1254.00",
        "job_zone": 4
    },
    {
        "id": "ux-designer",
        "title": "UX Designer",
        "field": "Design & User Experience",
        "category_id": "design",
        "category_name": "UI/UX & Creative Design",
        "tagline": "Understand human behavior to design intuitive, seamless digital product experiences.",
        "description": "User Experience (UX) Designers research how people interact with products, uncover pain points, and craft intuitive workflows, information architecture, wireframes, and prototypes that make digital tools effortless and enjoyable.",
        "responsibilities": [
            "Conduct qualitative user interviews, usability testing, and surveys to identify pain points",
            "Create user personas, journey maps, user flows, and site architectures",
            "Produce low-fidelity wireframes and interactive clickable prototypes in Figma",
            "Collaborate closely with product managers and engineers to ensure design feasibility",
            "Iterate designs based on quantitative product analytics and qualitative user feedback"
        ],
        "riasec_traits": [
            "A",
            "I",
            "S"
        ],
        "work_style": "Human-centered, investigative research, creative problem-solving, and cross-team communication.",
        "core_skills": [
            "UX Research",
            "Figma",
            "Wireframing",
            "Prototyping",
            "Information Architecture",
            "Usability Testing",
            "User Empathy"
        ],
        "optional_skills": [
            "Design Systems",
            "Interaction Design",
            "UI Design",
            "HTML/CSS Basics",
            "Product Analytics",
            "Workshop Facilitation"
        ],
        "common_tools": [
            "Figma",
            "FigJam",
            "Miro",
            "Maze",
            "Notion",
            "Hotjar"
        ],
        "education_paths": [
            "Degrees in Human-Computer Interaction (HCI), Psychology, Graphic Design, Multimedia Arts, or Computer Science",
            "Self-directed portfolio learning and apprenticeship",
            "UX/UI design bootcamps with hands-on client case studies"
        ],
        "certifications": [
            {
                "name": "Google UX Design Professional Certificate",
                "cost": "Low-cost (Coursera FinAid Available)",
                "provider": "Coursera / Google",
                "url": "https://www.coursera.org/professional-certificates/google-ux-design"
            },
            {
                "name": "Interaction Design Foundation (IxDF) Courses",
                "cost": "Low-cost Student Membership",
                "provider": "IxDF",
                "url": "https://www.interaction-design.org/"
            }
        ],
        "portfolio_projects": [
            {
                "title": "Mobile App Redesign Case Study",
                "description": "End-to-end UX case study identifying usability friction in a transit or banking app, complete with user interviews, journey maps, and tested prototypes.",
                "difficulty": "Foundational"
            },
            {
                "title": "Accessible Healthcare / Telehealth Booking Flow",
                "description": "Designing an accessible appointment booking flow for seniors and diverse ability groups, focusing on WCAG contrast and cognitive load reduction.",
                "difficulty": "Intermediate"
            },
            {
                "title": "Multi-Platform B2B SaaS Workflow & Design System",
                "description": "Comprehensive design system with reusable components, documentation tokens, and complex multi-step data table workflows.",
                "difficulty": "Advanced"
            }
        ],
        "salary_data": {
            "philippines": {
                "currency": "PHP",
                "entry_level": "\u20b1360,000 \u2013 \u20b1600,000 / year (\u20b130k - \u20b150k/mo)",
                "mid_level": "\u20b1720,000 \u2013 \u20b11,320,000 / year (\u20b160k - \u20b1110k/mo)",
                "senior_level": "\u20b11,440,000 \u2013 \u20b12,600,000+ / year (\u20b1120k - \u20b1215k+/mo)",
                "source": "Payscale PH, UX Philippines Industry Compensation Survey",
                "updated_at": "2026-Q1"
            },
            "global_usd": {
                "currency": "USD",
                "entry_level": "$70,000 \u2013 $92,000 / year",
                "mid_level": "$98,000 \u2013 $140,000 / year",
                "senior_level": "$145,000 \u2013 $205,000+ / year",
                "source": "Levels.fyi, Nielsen Norman Group Salary Reports",
                "updated_at": "2026-Q1"
            }
        },
        "learning_resources": [
            {
                "title": "Nielsen Norman Group Free UX Articles & Videos",
                "type": "Research & Best Practices",
                "cost": "Free",
                "provider": "NN/g",
                "url": "https://www.nngroup.com/articles/"
            },
            {
                "title": "Figma Learn and Design Fundamentals",
                "type": "Interactive Guides",
                "cost": "Free",
                "provider": "Figma",
                "url": "https://help.figma.com/hc/en-us/categories/360002051613"
            },
            {
                "title": "LawsofUX.com (Psychological UX Principles)",
                "type": "Reference Guide",
                "cost": "Free",
                "provider": "Jon Yablonski",
                "url": "https://lawsofux.com/"
            }
        ],
        "related_careers": [
            "product-designer",
            "ui-designer",
            "ux-engineer",
            "product-manager"
        ],
        "sources": [
            "Nielsen Norman Group",
            "Interaction Design Foundation",
            "Levels.fyi",
            "UXPH"
        ],
        "last_updated": "2026-09-01",
        "psoc_code": "2166",
        "soc_code": "27-1024.00",
        "job_zone": 4
    },
    {
        "id": "fullstack-developer",
        "title": "Full-Stack Developer",
        "field": "Technology",
        "category_id": "development",
        "category_name": "Software & Web Development",
        "tagline": "Architect end-to-end applications from database queries to intuitive front-end interfaces.",
        "description": "Full-Stack Developers build and connect the entire software pipeline: front-end user interfaces, back-end web servers, application programming interfaces (APIs), and relational or NoSQL database architectures.",
        "responsibilities": [
            "Design and build responsive web applications utilizing modern front-end frameworks and back-end runtimes",
            "Architect, query, and optimize relational databases (PostgreSQL, MySQL) and database migrations",
            "Develop secure REST and GraphQL APIs with authentication, authorization, and rate limiting",
            "Deploy and maintain scalable containerized applications to cloud platforms",
            "Write comprehensive automated tests (unit, integration, and end-to-end)"
        ],
        "riasec_traits": [
            "I",
            "R",
            "A"
        ],
        "work_style": "Holistic system builder, deep problem solver, adaptable across different tech stack tiers.",
        "core_skills": [
            "JavaScript/TypeScript",
            "Python or Node.js",
            "React or Vue",
            "SQL & Database Design",
            "REST APIs",
            "Git",
            "HTML/CSS"
        ],
        "optional_skills": [
            "PostgreSQL",
            "Docker",
            "Next.js",
            "Tailwind CSS",
            "Redis",
            "Cloud Deployment (AWS/Vercel/Supabase)",
            "CI/CD"
        ],
        "common_tools": [
            "VS Code",
            "Postman",
            "Docker Desktop",
            "Supabase / DBeaver",
            "GitHub",
            "Linux CLI"
        ],
        "education_paths": [
            "Bachelor's in Computer Science, Software Engineering, or Information Systems",
            "Full-Stack coding bootcamps with portfolio capstones",
            "Self-taught via open-source curricula (Odin Project, Full Stack Open)"
        ],
        "certifications": [
            {
                "name": "Full Stack Open (University of Helsinki)",
                "cost": "Free",
                "provider": "University of Helsinki",
                "url": "https://fullstackopen.com/en/"
            },
            {
                "name": "AWS Certified Cloud Practitioner",
                "cost": "$100 (Exam fee)",
                "provider": "Amazon Web Services",
                "url": "https://aws.amazon.com/certification/certified-cloud-practitioner/"
            }
        ],
        "portfolio_projects": [
            {
                "title": "Full-Stack Collaborative Workspace / Task Management App",
                "description": "Interactive web app with user authentication, real-time board updates, PostgreSQL persistence, and role-based permissions.",
                "difficulty": "Intermediate"
            },
            {
                "title": "Community Market Platform with Payments & Media Uploads",
                "description": "Multi-vendor platform featuring item search, filter, cloud image uploads, Stripe/PayMongo sandbox checkout, and transactional emails.",
                "difficulty": "Advanced"
            },
            {
                "title": "AI-Enhanced Knowledge Base & Note Taking SaaS",
                "description": "Full-stack SaaS application with markdown editor, semantic tagging, Supabase PostgreSQL with RLS, and Stripe subscription tiering.",
                "difficulty": "Advanced"
            }
        ],
        "salary_data": {
            "philippines": {
                "currency": "PHP",
                "entry_level": "\u20b1360,000 \u2013 \u20b1600,000 / year (\u20b130k - \u20b150k/mo)",
                "mid_level": "\u20b1720,000 \u2013 \u20b11,500,000 / year (\u20b160k - \u20b1125k/mo)",
                "senior_level": "\u20b11,500,000 \u2013 \u20b13,000,000+ / year (\u20b1125k - \u20b1250k+/mo)",
                "source": "Payscale PH, NodeFlair SEA Tech Salary Report",
                "updated_at": "2026-Q1"
            },
            "global_usd": {
                "currency": "USD",
                "entry_level": "$75,000 \u2013 $95,000 / year",
                "mid_level": "$105,000 \u2013 $145,000 / year",
                "senior_level": "$150,000 \u2013 $215,000+ / year",
                "source": "Levels.fyi, Stack Overflow Developer Survey",
                "updated_at": "2026-Q1"
            }
        },
        "learning_resources": [
            {
                "title": "Full Stack Open (React, Redux, Node.js, MongoDB, GraphQL, TypeScript)",
                "type": "Comprehensive Course",
                "cost": "Free",
                "provider": "University of Helsinki",
                "url": "https://fullstackopen.com/en/"
            },
            {
                "title": "CS50's Web Programming with Python and JavaScript",
                "type": "University Course",
                "cost": "Free",
                "provider": "Harvard University (edX)",
                "url": "https://cs50.harvard.edu/web/"
            },
            {
                "title": "Supabase Documentation & PostgreSQL Guides",
                "type": "Database Guides",
                "cost": "Free",
                "provider": "Supabase",
                "url": "https://supabase.com/docs"
            }
        ],
        "related_careers": [
            "frontend-developer",
            "backend-developer",
            "devops-engineer",
            "cloud-engineer"
        ],
        "sources": [
            "Stack Overflow Developer Survey",
            "Levels.fyi",
            "NodeFlair",
            "Payscale"
        ],
        "last_updated": "2026-09-01",
        "psoc_code": "2512",
        "soc_code": "15-1252.00",
        "job_zone": 4
    },
    {
        "id": "data-analyst",
        "title": "Data Analyst",
        "field": "Data & Analytics",
        "category_id": "data_ai",
        "category_name": "Data, Analytics & AI",
        "tagline": "Transform raw numbers and business data into clear, actionable visual insights.",
        "description": "Data Analysts collect, clean, and interpret data to help organizations make smarter strategic decisions. They craft intuitive dashboards, track business metrics, and communicate findings to non-technical stakeholders.",
        "responsibilities": [
            "Extract, clean, and validate data from SQL relational databases and cloud warehouses",
            "Build interactive dashboards and reports using Tableau, Power BI, or Looker Studio",
            "Perform exploratory data analysis using SQL and Python (Pandas) to uncover market trends",
            "Define key performance indicators (KPIs) and monitor business health metrics",
            "Present data-driven insights and recommendations to leadership and cross-functional teams"
        ],
        "riasec_traits": [
            "I",
            "C",
            "S"
        ],
        "work_style": "Analytical investigation, structured data modeling, and consultative storytelling.",
        "core_skills": [
            "SQL",
            "Data Analysis",
            "Tableau or Power BI",
            "Excel / Spreadsheets",
            "Data Visualization",
            "Critical Thinking"
        ],
        "optional_skills": [
            "Python (Pandas/Matplotlib)",
            "Statistics",
            "Data Cleaning",
            "Business Intelligence",
            "ETL Basics",
            "A/B Testing"
        ],
        "common_tools": [
            "SQL Server / PostgreSQL",
            "Power BI",
            "Tableau",
            "Excel",
            "Jupyter Notebooks",
            "Google Sheets"
        ],
        "education_paths": [
            "Degree in Statistics, Mathematics, Economics, Information Systems, Business, or Computer Science",
            "Professional data analytics certificates and guided portfolio projects",
            "Transition from finance, operations, or marketing analytics"
        ],
        "certifications": [
            {
                "name": "Google Data Analytics Professional Certificate",
                "cost": "Low-cost (Coursera FinAid Available)",
                "provider": "Coursera / Google",
                "url": "https://www.coursera.org/professional-certificates/google-data-analytics"
            },
            {
                "name": "Microsoft Certified: Power BI Data Analyst Associate (PL-300)",
                "cost": "$165 (Exam fee)",
                "provider": "Microsoft",
                "url": "https://learn.microsoft.com/en-us/credentials/certifications/data-analyst-associate/"
            }
        ],
        "portfolio_projects": [
            {
                "title": "Public Health or Economic Trend Dashboard",
                "description": "Cleaned open government/WHO datasets analyzed with SQL and displayed via an interactive Power BI / Tableau public dashboard.",
                "difficulty": "Foundational"
            },
            {
                "title": "E-Commerce Customer Retention & Cohort Analysis",
                "description": "SQL-driven exploratory analysis calculating churn rates, customer lifetime value (LTV), and seasonal purchase patterns.",
                "difficulty": "Intermediate"
            },
            {
                "title": "Real-World Business KPI Pipeline with Automated Reporting",
                "description": "End-to-end analytics workflow combining raw CSV/API ingestion, automated Python data transformation, and scheduled KPI visualizations.",
                "difficulty": "Advanced"
            }
        ],
        "salary_data": {
            "philippines": {
                "currency": "PHP",
                "entry_level": "\u20b1300,000 \u2013 \u20b1480,000 / year (\u20b125k - \u20b140k/mo)",
                "mid_level": "\u20b1540,000 \u2013 \u20b11,080,000 / year (\u20b145k - \u20b190k/mo)",
                "senior_level": "\u20b11,200,000 \u2013 \u20b12,100,000+ / year (\u20b1100k - \u20b1175k+/mo)",
                "source": "Payscale PH, Analytics Association of the Philippines",
                "updated_at": "2026-Q1"
            },
            "global_usd": {
                "currency": "USD",
                "entry_level": "$62,000 \u2013 $80,000 / year",
                "mid_level": "$85,000 \u2013 $115,000 / year",
                "senior_level": "$120,000 \u2013 $160,000+ / year",
                "source": "Levels.fyi, US BLS (Operations & Data Analysts)",
                "updated_at": "2026-Q1"
            }
        },
        "learning_resources": [
            {
                "title": "Kaggle Micro-Courses (Python, Pandas, SQL, Data Visualization)",
                "type": "Interactive Coding",
                "cost": "Free",
                "provider": "Kaggle",
                "url": "https://www.kaggle.com/learn"
            },
            {
                "title": "SQLBolt - Learn SQL with simple, interactive exercises",
                "type": "Interactive Tutorial",
                "cost": "Free",
                "provider": "SQLBolt",
                "url": "https://sqlbolt.com/"
            },
            {
                "title": "Microsoft Learn Power BI Learning Path",
                "type": "Official Guides",
                "cost": "Free",
                "provider": "Microsoft",
                "url": "https://learn.microsoft.com/en-us/training/powerplatform/power-bi"
            }
        ],
        "related_careers": [
            "data-scientist",
            "business-analyst",
            "product-manager",
            "database-administrator"
        ],
        "sources": [
            "U.S. Bureau of Labor Statistics",
            "Payscale",
            "Analytics Association of the Philippines",
            "Levels.fyi"
        ],
        "last_updated": "2026-09-01",
        "psoc_code": "2521",
        "soc_code": "15-2051.01",
        "job_zone": 4
    },
    {
        "id": "cybersecurity-analyst",
        "title": "Cybersecurity Analyst",
        "field": "Security & Systems",
        "category_id": "cloud_security",
        "category_name": "Cloud, DevOps & Cybersecurity",
        "tagline": "Protect digital infrastructure, data, and users from malicious threats and vulnerabilities.",
        "description": "Cybersecurity Analysts monitor, detect, and mitigate cyber threats across computer networks, cloud environments, and digital systems. They conduct vulnerability assessments, evaluate security posture, and respond to security incidents.",
        "responsibilities": [
            "Monitor network traffic, endpoint logs, and SIEM alerts for security anomalies and breaches",
            "Conduct vulnerability scans and coordinate patching across infrastructure",
            "Investigate and respond to security incidents, malware infections, and phishing attempts",
            "Perform security assessments and assist in compliance audits (ISO 27001, SOC 2, NIST)",
            "Educate internal staff on security best practices, password safety, and social engineering risks"
        ],
        "riasec_traits": [
            "I",
            "R",
            "C"
        ],
        "work_style": "Vigilant, systematic, investigative problem-solving with high attention to detail.",
        "core_skills": [
            "Networking Fundamentals (TCP/IP, DNS)",
            "Linux/Unix Commands",
            "Security Principles",
            "Vulnerability Scanning",
            "Incident Response"
        ],
        "optional_skills": [
            "Python / Bash Scripting",
            "SIEM Tools (Splunk/Wazuh)",
            "Wireshark",
            "Cloud Security (AWS/Azure)",
            "Ethical Hacking",
            "Threat Hunting"
        ],
        "common_tools": [
            "Wireshark",
            "Nmap",
            "Splunk",
            "Burp Suite",
            "Kali Linux",
            "Wazuh / Elastic SIEM"
        ],
        "education_paths": [
            "Degree in Cybersecurity, Information Technology, Computer Engineering, or Computer Science",
            "Industry standard vendor-neutral certifications and hands-on capture-the-flag (CTF) labs",
            "Transition from IT Helpdesk, Network Administration, or Systems Administration"
        ],
        "certifications": [
            {
                "name": "CompTIA Security+ (SY0-701)",
                "cost": "$392 (Exam fee, student discounts available)",
                "provider": "CompTIA",
                "url": "https://www.comptia.org/certifications/security"
            },
            {
                "name": "Google Cybersecurity Professional Certificate",
                "cost": "Low-cost (Coursera FinAid Available)",
                "provider": "Coursera / Google",
                "url": "https://www.coursera.org/professional-certificates/google-cybersecurity"
            },
            {
                "name": "ISC2 Certified in Cybersecurity (CC)",
                "cost": "Free Exam via One Million Certified in Cybersecurity campaign",
                "provider": "ISC2",
                "url": "https://www.isc2.org/landing/1mcc"
            }
        ],
        "portfolio_projects": [
            {
                "title": "Home Lab Virtual Network & SIEM Setup",
                "description": "Configuring a dedicated virtual home lab with pfSense firewall, Linux/Windows endpoints, and an open-source SIEM (Wazuh/Splunk) to analyze attack logs.",
                "difficulty": "Foundational"
            },
            {
                "title": "Network Traffic Analysis & Malware Packet Triage",
                "description": "Documented packet capture (pcap) investigation using Wireshark to identify C2 beaconing, port scans, and credential exfiltration.",
                "difficulty": "Intermediate"
            },
            {
                "title": "Comprehensive Vulnerability Assessment & Hardening Report",
                "description": "Conducting an authorized vulnerability assessment against a test environment (e.g. Metasploitable) and writing an executive remediation report.",
                "difficulty": "Advanced"
            }
        ],
        "salary_data": {
            "philippines": {
                "currency": "PHP",
                "entry_level": "\u20b1360,000 \u2013 \u20b1540,000 / year (\u20b130k - \u20b145k/mo)",
                "mid_level": "\u20b1660,000 \u2013 \u20b11,320,000 / year (\u20b155k - \u20b1110k/mo)",
                "senior_level": "\u20b11,440,000 \u2013 \u20b12,800,000+ / year (\u20b1120k - \u20b1230k+/mo)",
                "source": "Payscale PH, Philippine Information Security Association",
                "updated_at": "2026-Q1"
            },
            "global_usd": {
                "currency": "USD",
                "entry_level": "$72,000 \u2013 $90,000 / year",
                "mid_level": "$95,000 \u2013 $135,000 / year",
                "senior_level": "$145,000 \u2013 $195,000+ / year",
                "source": "Levels.fyi, US BLS (Information Security Analysts)",
                "updated_at": "2026-Q1"
            }
        },
        "learning_resources": [
            {
                "title": "TryHackMe (Pre-Security & Cyber Defense Paths)",
                "type": "Hands-on Gamified Labs",
                "cost": "Free Tier & Low-cost Student Plan",
                "provider": "TryHackMe",
                "url": "https://tryhackme.com/"
            },
            {
                "title": "OverTheWire Wargames (Bandit Linux Basics)",
                "type": "Terminal Practice",
                "cost": "Free",
                "provider": "OverTheWire",
                "url": "https://overthewire.org/wargames/"
            },
            {
                "title": "Professor Messer CompTIA Security+ Training Course",
                "type": "Video Lecture Series",
                "cost": "Free",
                "provider": "Professor Messer",
                "url": "https://www.professormesser.com/security-plus/sy0-701/sy0-701-video/sy0-701-training-course/"
            }
        ],
        "related_careers": [
            "cloud-engineer",
            "devops-engineer",
            "software-engineer",
            "database-administrator"
        ],
        "sources": [
            "U.S. Bureau of Labor Statistics",
            "CompTIA",
            "ISC2 Cybersecurity Workforce Study",
            "Payscale"
        ],
        "last_updated": "2026-09-01",
        "psoc_code": "2529",
        "soc_code": "15-1212.00",
        "job_zone": 4
    },
    {
        "id": "cloud-engineer",
        "title": "Cloud Engineer",
        "field": "Cloud & Infrastructure",
        "category_id": "cloud_security",
        "category_name": "Cloud, DevOps & Cybersecurity",
        "tagline": "Design, deploy, and scale resilient cloud architecture that powers global software.",
        "description": "Cloud Engineers architect, build, and maintain cloud computing environments (such as AWS, Google Cloud, or Azure). They ensure high availability, scalability, cost optimization, and automated resource provisioning.",
        "responsibilities": [
            "Architect and deploy scalable infrastructure on public cloud platforms (AWS, GCP, Azure)",
            "Automate infrastructure provisioning using Infrastructure as Code (Terraform, CloudFormation)",
            "Configure virtual networks, subnets, load balancers, and security groups",
            "Monitor system performance, implement auto-scaling policies, and manage cloud costs",
            "Collaborate with software engineers to optimize application deployment architectures"
        ],
        "riasec_traits": [
            "R",
            "I",
            "C"
        ],
        "work_style": "Systematic, architecture-focused, automated problem-solving with high autonomy.",
        "core_skills": [
            "Cloud Platforms (AWS/GCP/Azure)",
            "Linux Administration",
            "Networking Fundamentals",
            "Infrastructure as Code (Terraform)",
            "Git & GitHub"
        ],
        "optional_skills": [
            "Docker",
            "Kubernetes",
            "Python / Bash Scripting",
            "CI/CD Pipelines",
            "Serverless Architecture",
            "Cloud Security"
        ],
        "common_tools": [
            "AWS Console / CLI",
            "Terraform",
            "Docker",
            "Linux Terminal",
            "Datadog / CloudWatch",
            "GitHub Actions"
        ],
        "education_paths": [
            "Bachelor's degree in Computer Science, IT, Computer Engineering, or related technical fields",
            "Industry cloud certifications combined with verifiable GitHub infrastructure projects",
            "Transition from Systems Administrator or Network Engineer roles"
        ],
        "certifications": [
            {
                "name": "AWS Certified Solutions Architect \u2013 Associate",
                "cost": "$150 (Exam fee)",
                "provider": "Amazon Web Services",
                "url": "https://aws.amazon.com/certification/certified-solutions-architect-associate/"
            },
            {
                "name": "Google Cloud Associate Cloud Engineer",
                "cost": "$125 (Exam fee)",
                "provider": "Google Cloud",
                "url": "https://cloud.google.com/learn/certification/cloud-engineer"
            },
            {
                "name": "HashiCorp Certified: Terraform Associate",
                "cost": "$70 (Exam fee)",
                "provider": "HashiCorp",
                "url": "https://www.hashicorp.com/certification/terraform-associate"
            }
        ],
        "portfolio_projects": [
            {
                "title": "High-Availability Multi-Tier Web Architecture on AWS",
                "description": "Deploying a resilient VPC with public/private subnets, Auto Scaling EC2 instances, Application Load Balancer, and RDS PostgreSQL.",
                "difficulty": "Foundational"
            },
            {
                "title": "Infrastructure as Code (Terraform) Cloud Deployment",
                "description": "Writing modular Terraform scripts to provision an entire cloud environment with automated state management in an S3 bucket.",
                "difficulty": "Intermediate"
            },
            {
                "title": "Serverless Event-Driven Processing Pipeline",
                "description": "Building an automated pipeline using AWS Lambda / Google Cloud Functions, SQS/PubSub queues, and DynamoDB/Firestore to process incoming files.",
                "difficulty": "Advanced"
            }
        ],
        "salary_data": {
            "philippines": {
                "currency": "PHP",
                "entry_level": "\u20b1420,000 \u2013 \u20b1660,000 / year (\u20b135k - \u20b155k/mo)",
                "mid_level": "\u20b1780,000 \u2013 \u20b11,560,000 / year (\u20b165k - \u20b1130k/mo)",
                "senior_level": "\u20b11,680,000 \u2013 \u20b13,200,000+ / year (\u20b1140k - \u20b1265k+/mo)",
                "source": "Payscale PH, JobStreet Tech Compensation Reports",
                "updated_at": "2026-Q1"
            },
            "global_usd": {
                "currency": "USD",
                "entry_level": "$80,000 \u2013 $100,000 / year",
                "mid_level": "$110,000 \u2013 $155,000 / year",
                "senior_level": "$160,000 \u2013 $220,000+ / year",
                "source": "Levels.fyi, Robert Half Technology Salary Guide",
                "updated_at": "2026-Q1"
            }
        },
        "learning_resources": [
            {
                "title": "AWS Skill Builder Free Digital Training",
                "type": "Official Self-Paced Courses",
                "cost": "Free",
                "provider": "Amazon Web Services",
                "url": "https://explore.skillbuilder.aws/"
            },
            {
                "title": "Google Cloud Free Tier & Architecture Center",
                "type": "Cloud Sandbox & Best Practices",
                "cost": "Free Sandbox Allowance",
                "provider": "Google Cloud",
                "url": "https://cloud.google.com/architecture"
            },
            {
                "title": "Terraform Official Tutorials (HashiCorp Learn)",
                "type": "Interactive Guides",
                "cost": "Free",
                "provider": "HashiCorp",
                "url": "https://developer.hashicorp.com/terraform/tutorials"
            }
        ],
        "related_careers": [
            "devops-engineer",
            "cybersecurity-analyst",
            "fullstack-developer",
            "database-administrator"
        ],
        "sources": [
            "Amazon Web Services",
            "Google Cloud",
            "Levels.fyi",
            "Payscale"
        ],
        "last_updated": "2026-09-01"
    },
    {
        "id": "product-manager",
        "title": "Product Manager (Tech)",
        "field": "Product Strategy & Management",
        "category_id": "product_management",
        "category_name": "Product & Tech Strategy",
        "tagline": "Bridge engineering, design, and business to define what gets built and why.",
        "description": "Product Managers guide the strategy, roadmap, and feature definition for digital products. They act as the connective tissue between users, software engineers, UX designers, and business leaders to solve real problems and deliver value.",
        "responsibilities": [
            "Define product vision, quarterly roadmap priorities, and success metrics (OKRs / KPIs)",
            "Gather user feedback, conduct market research, and synthesize customer requirements",
            "Author detailed Product Requirement Documents (PRDs) and user story backlogs",
            "Lead sprint planning, grooming, and cross-functional alignment in agile ceremonies",
            "Analyze product performance data post-launch to continuously iterate on feature adoption"
        ],
        "riasec_traits": [
            "E",
            "S",
            "I"
        ],
        "work_style": "Strategic leadership, high cross-functional collaboration, empathetic problem-solving.",
        "core_skills": [
            "Product Strategy",
            "User Research & Empathy",
            "Agile / Scrum",
            "Roadmapping",
            "Communication",
            "Data-Driven Decision Making"
        ],
        "optional_skills": [
            "Technical Fluency (APIs/Databases)",
            "SQL Basics",
            "A/B Testing",
            "Financial Modeling",
            "Figma Basics",
            "Go-to-Market (GTM)"
        ],
        "common_tools": [
            "Jira / Linear",
            "Notion",
            "Mixpanel / Amplitude",
            "Figma",
            "Slack",
            "Productboard"
        ],
        "education_paths": [
            "Diverse backgrounds: Business Administration, Computer Science, Engineering, Economics, or Communications",
            "Product management certificates and case study teardowns",
            "Transition from software engineering, UX design, data analysis, or project management"
        ],
        "certifications": [
            {
                "name": "University of Virginia: Digital Product Management Specialization",
                "cost": "Low-cost (Coursera FinAid Available)",
                "provider": "Coursera / Darden School of Business",
                "url": "https://www.coursera.org/specializations/uva-darden-digital-product-management"
            },
            {
                "name": "Scrum Alliance Certified Scrum Product Owner (CSPO)",
                "cost": "$400 \u2013 $600 (Course fee)",
                "provider": "Scrum Alliance",
                "url": "https://www.scrumalliance.org/get-certified/product-owner-track/certified-scrum-product-owner"
            }
        ],
        "portfolio_projects": [
            {
                "title": "Product Teardown & Redesign Proposal",
                "description": "Thorough analysis of an existing consumer or B2B product, evaluating its user friction, metrics, unit economics, and proposing a feature teardown.",
                "difficulty": "Foundational"
            },
            {
                "title": "Comprehensive Product Requirement Document (PRD)",
                "description": "End-to-end PRD for a new digital product concept featuring user personas, edge cases, system flowcharts, launch milestones, and risk matrix.",
                "difficulty": "Intermediate"
            },
            {
                "title": "0-to-1 Product Launch Strategy & Metrics Framework",
                "description": "Complete product discovery artifact including user interview synthesis, wireframes, North Star metric definition, and Go-To-Market plan.",
                "difficulty": "Advanced"
            }
        ],
        "salary_data": {
            "philippines": {
                "currency": "PHP",
                "entry_level": "\u20b1480,000 \u2013 \u20b1720,000 / year (\u20b140k - \u20b160k/mo)",
                "mid_level": "\u20b1840,000 \u2013 \u20b11,800,000 / year (\u20b170k - \u20b1150k/mo)",
                "senior_level": "\u20b11,920,000 \u2013 \u20b13,600,000+ / year (\u20b1160k - \u20b1300k+/mo)",
                "source": "Payscale PH, Product Leaders PH Salary Benchmarks",
                "updated_at": "2026-Q1"
            },
            "global_usd": {
                "currency": "USD",
                "entry_level": "$85,000 \u2013 $110,000 / year",
                "mid_level": "$120,000 \u2013 $165,000 / year",
                "senior_level": "$175,000 \u2013 $240,000+ / year",
                "source": "Levels.fyi, Product Management Salary Survey",
                "updated_at": "2026-Q1"
            }
        },
        "learning_resources": [
            {
                "title": "Reforge Product Briefs & Thought Leadership",
                "type": "Industry Essays",
                "cost": "Free Articles Available",
                "provider": "Reforge",
                "url": "https://www.reforge.com/blog"
            },
            {
                "title": "Lenny's Newsletter & Podcast (Product & Growth)",
                "type": "Practitioner Guides",
                "cost": "Free & Paid Substack",
                "provider": "Lenny Rachitsky",
                "url": "https://www.lennysnewsletter.com/"
            },
            {
                "title": "Mind the Product Free Content Library",
                "type": "Community Talks & Articles",
                "cost": "Free",
                "provider": "Mind the Product",
                "url": "https://www.mindtheproduct.com/"
            }
        ],
        "related_careers": [
            "ux-designer",
            "data-analyst",
            "product-designer",
            "business-analyst"
        ],
        "sources": [
            "Levels.fyi",
            "Mind the Product",
            "Product School",
            "Payscale"
        ],
        "last_updated": "2026-09-01",
        "psoc_code": "1219",
        "soc_code": "11-9199.00",
        "job_zone": 4
    },
    {
        "id": "ai-ml-engineer",
        "title": "AI / Machine Learning Engineer",
        "field": "Artificial Intelligence & Data",
        "category_id": "data_ai",
        "category_name": "Data, Analytics & AI",
        "tagline": "Build, fine-tune, and deploy intelligent machine learning systems and AI models.",
        "description": "AI/ML Engineers bridge data science and software engineering to develop, evaluate, and productionize machine learning models, neural networks, and generative AI systems that solve complex automated reasoning tasks.",
        "responsibilities": [
            "Develop, train, evaluate, and fine-tune machine learning and deep learning models",
            "Engineer scalable data pipelines for model training, validation, and feature stores",
            "Deploy machine learning models as production REST/gRPC microservices with low latency",
            "Integrate Foundation Models (LLMs, vision models) with retrieval-augmented generation (RAG)",
            "Monitor deployed models for performance drift, hallucination, and data quality degradation"
        ],
        "riasec_traits": [
            "I",
            "R",
            "C"
        ],
        "work_style": "Mathematical rigor, experimental research, deep coding, and continuous learning.",
        "core_skills": [
            "Python",
            "Machine Learning Fundamentals",
            "PyTorch or TensorFlow",
            "Data Preprocessing",
            "Git",
            "Math & Linear Algebra"
        ],
        "optional_skills": [
            "LLM Engineering / RAG",
            "Docker",
            "Hugging Face",
            "MLOps (MLflow/Kubeflow)",
            "FastAPI",
            "Vector Databases",
            "Cloud ML Platforms"
        ],
        "common_tools": [
            "Jupyter Lab",
            "PyTorch",
            "Hugging Face Hub",
            "FastAPI",
            "Docker",
            "Weights & Biases"
        ],
        "education_paths": [
            "Bachelor's or Master's in Computer Science, AI, Data Science, Electrical Engineering, or Physics",
            "Applied machine learning self-study paths and competitive Kaggle portfolios",
            "Software engineers transitioning into AI engineering through applied projects"
        ],
        "certifications": [
            {
                "name": "DeepLearning.AI Deep Learning Specialization",
                "cost": "Low-cost (Coursera FinAid Available)",
                "provider": "Coursera / DeepLearning.AI",
                "url": "https://www.coursera.org/specializations/deep-learning"
            },
            {
                "name": "DeepLearning.AI Generative AI with Large Language Models",
                "cost": "Low-cost (Coursera FinAid Available)",
                "provider": "Coursera / AWS",
                "url": "https://www.coursera.org/learn/generative-ai-with-llms"
            },
            {
                "name": "TensorFlow Developer Certificate (or AWS ML Specialty)",
                "cost": "$100 \u2013 $300 (Exam fee)",
                "provider": "Google / AWS",
                "url": "https://www.tensorflow.org/certificate"
            }
        ],
        "portfolio_projects": [
            {
                "title": "Predictive Classification / Regression Model on Tabular Data",
                "description": "End-to-end exploratory analysis, feature engineering, model tuning with XGBoost, and performance metrics evaluation on a real-world dataset.",
                "difficulty": "Foundational"
            },
            {
                "title": "Computer Vision or NLP Classification API with FastAPI & Docker",
                "description": "Trained PyTorch image classifier or sentiment analysis model wrapped in a high-performance REST API containerized with Docker.",
                "difficulty": "Intermediate"
            },
            {
                "title": "Production RAG System with Vector Search & Evaluation Suite",
                "description": "Production retrieval-augmented generation system parsing domain documents, generating embeddings, querying PostgreSQL pgvector, and benchmarking accuracy.",
                "difficulty": "Advanced"
            }
        ],
        "salary_data": {
            "philippines": {
                "currency": "PHP",
                "entry_level": "\u20b1480,000 \u2013 \u20b1780,000 / year (\u20b140k - \u20b165k/mo)",
                "mid_level": "\u20b1900,000 \u2013 \u20b11,800,000 / year (\u20b175k - \u20b1150k/mo)",
                "senior_level": "\u20b11,920,000 \u2013 \u20b13,600,000+ / year (\u20b1160k - \u20b1300k+/mo)",
                "source": "Payscale PH, SEA AI Talent Compensation Benchmark",
                "updated_at": "2026-Q1"
            },
            "global_usd": {
                "currency": "USD",
                "entry_level": "$90,000 \u2013 $120,000 / year",
                "mid_level": "$130,000 \u2013 $180,000 / year",
                "senior_level": "$190,000 \u2013 $275,000+ / year",
                "source": "Levels.fyi, O'Reilly AI/ML Salary Survey",
                "updated_at": "2026-Q1"
            }
        },
        "learning_resources": [
            {
                "title": "fast.ai: Practical Deep Learning for Coders",
                "type": "Top-Down AI Course",
                "cost": "Free",
                "provider": "fast.ai",
                "url": "https://course.fast.ai/"
            },
            {
                "title": "Hugging Face NLP & Deep Learning Course",
                "type": "Interactive Transformers Guide",
                "cost": "Free",
                "provider": "Hugging Face",
                "url": "https://huggingface.co/learn/nlp-course/chapter1/1"
            },
            {
                "title": "Google AI for Developers Documentation",
                "type": "Official Guides & SDKs",
                "cost": "Free",
                "provider": "Google",
                "url": "https://ai.google.dev/"
            }
        ],
        "related_careers": [
            "data-scientist",
            "data-analyst",
            "software-engineer",
            "backend-developer"
        ],
        "sources": [
            "DeepLearning.AI",
            "Levels.fyi",
            "O'Reilly",
            "Payscale"
        ],
        "last_updated": "2026-09-01",
        "psoc_code": "2512",
        "soc_code": "15-1299.08",
        "job_zone": 5
    },
    {
        "id": "ui-designer",
        "title": "UI Designer",
        "field": "Design",
        "category_id": "design",
        "category_name": "UI/UX & Creative Design",
        "tagline": "Craft visual aesthetics, typography, color palettes, and component design systems for digital interfaces.",
        "description": "User Interface (UI) Designers focus on the visual, interactive, and graphic aspects of digital products. They create cohesive visual languages, icons, typography scales, layout grids, and interactive states.",
        "responsibilities": [
            "Create high-fidelity screen designs, UI elements, illustrations, and iconography",
            "Build and maintain scalable design systems with reusable components and tokens",
            "Design responsive layouts across desktop, tablet, and mobile breakpoints",
            "Establish consistent visual guidelines for color, typography, spacing, and micro-interactions",
            "Prepare detailed design handoff specifications and assets for front-end developers"
        ],
        "riasec_traits": [
            "A",
            "R",
            "C"
        ],
        "work_style": "Visual craft, artistic intuition, attention to detail, and creative collaboration.",
        "core_skills": [
            "UI Design",
            "Figma",
            "Design Systems",
            "Typography & Color Theory",
            "Responsive Layouts",
            "Visual Hierarchy"
        ],
        "optional_skills": [
            "Prototyping (Figma/Protopie)",
            "HTML/CSS Basics",
            "Iconography",
            "Micro-animations",
            "Adobe Creative Suite"
        ],
        "common_tools": [
            "Figma",
            "Adobe Illustrator / Photoshop",
            "Protopie",
            "Zeplin",
            "FigJam"
        ],
        "education_paths": [
            "Degrees in Graphic Design, Fine Arts, Multimedia Arts, Visual Communication, or HCI",
            "Self-taught visual designers building public Dribbble/Behance portfolios",
            "Design bootcamps focusing on UI kits and modern responsive design"
        ],
        "certifications": [
            {
                "name": "CalArts UI / UX Design Specialization",
                "cost": "Low-cost (Coursera FinAid Available)",
                "provider": "Coursera / CalArts",
                "url": "https://www.coursera.org/specializations/ui-ux-design"
            },
            {
                "name": "Figma for UI/UX Design Masterclass",
                "cost": "Free Tutorials on YouTube / Figma Community",
                "provider": "Figma Community",
                "url": "https://www.figma.com/community"
            }
        ],
        "portfolio_projects": [
            {
                "title": "Multi-Theme UI Component Kit & Style Guide",
                "description": "Complete Figma design system with auto-layout components, color tokens, typography scales, and dark/light mode variants.",
                "difficulty": "Foundational"
            },
            {
                "title": "Mobile Banking / Fintech App UI Concept",
                "description": "High-fidelity 15+ screen mobile app interface with micro-interactions, transaction feeds, and card management.",
                "difficulty": "Intermediate"
            },
            {
                "title": "Editorial Web Publication & Tablet Reader Interface",
                "description": "Sophisticated typographic design for an online magazine with custom responsive grid layouts and animated reading progress.",
                "difficulty": "Advanced"
            }
        ],
        "salary_data": {
            "philippines": {
                "currency": "PHP",
                "entry_level": "\u20b1300,000 \u2013 \u20b1500,000 / year (\u20b125k - \u20b142k/mo)",
                "mid_level": "\u20b1600,000 \u2013 \u20b11,140,000 / year (\u20b150k - \u20b195k/mo)",
                "senior_level": "\u20b11,200,000 \u2013 \u20b12,200,000+ / year (\u20b1100k - \u20b1180k+/mo)",
                "source": "Payscale PH, UXPH Survey",
                "updated_at": "2026-Q1"
            },
            "global_usd": {
                "currency": "USD",
                "entry_level": "$65,000 \u2013 $85,000 / year",
                "mid_level": "$90,000 \u2013 $125,000 / year",
                "senior_level": "$135,000 \u2013 $185,000+ / year",
                "source": "Levels.fyi, Dribbble Design Salary Survey",
                "updated_at": "2026-Q1"
            }
        },
        "learning_resources": [
            {
                "title": "Refactoring UI (Design Tips for Developers & Designers)",
                "type": "Design Tips & Articles",
                "cost": "Free Articles & Paid Book",
                "provider": "Adam Wathan & Steve Schoger",
                "url": "https://www.refactoringui.com/"
            },
            {
                "title": "Figma YouTube Channel Tutorials",
                "type": "Video Tutorials",
                "cost": "Free",
                "provider": "Figma",
                "url": "https://www.youtube.com/@Figma"
            },
            {
                "title": "Typewolf (Typography Guides & Inspiration)",
                "type": "Typography Resource",
                "cost": "Free",
                "provider": "Typewolf",
                "url": "https://www.typewolf.com/"
            }
        ],
        "related_careers": [
            "ux-designer",
            "product-designer",
            "frontend-developer",
            "ux-engineer"
        ],
        "sources": [
            "Dribbble",
            "Figma",
            "Levels.fyi",
            "Payscale"
        ],
        "last_updated": "2026-09-01",
        "psoc_code": "2166",
        "soc_code": "27-1024.00",
        "job_zone": 4
    },
    {
        "id": "devops-engineer",
        "title": "DevOps Engineer",
        "field": "Infrastructure & Operations",
        "category_id": "cloud_security",
        "category_name": "Cloud, DevOps & Cybersecurity",
        "tagline": "Automate software delivery, streamline CI/CD pipelines, and maintain high system reliability.",
        "description": "DevOps Engineers bridge software development and IT operations. They build automated continuous integration and continuous delivery (CI/CD) pipelines, orchestrate containers, and ensure systems are observable, secure, and resilient.",
        "responsibilities": [
            "Design, implement, and maintain automated CI/CD pipelines for fast, reliable software deployments",
            "Manage containerized environments using Docker and Kubernetes clusters",
            "Implement monitoring, logging, and alerting systems (Prometheus, Grafana, ELK Stack)",
            "Enforce security best practices within development workflows (DevSecOps)",
            "Collaborate with developers to improve build speeds, testing automation, and deployment safety"
        ],
        "riasec_traits": [
            "R",
            "I",
            "C"
        ],
        "work_style": "Process automation, systems reliability, proactive troubleshooting, and cross-team collaboration.",
        "core_skills": [
            "Linux",
            "Git & GitHub Actions",
            "Docker",
            "CI/CD Pipelines",
            "Bash / Python Scripting",
            "Cloud Basics (AWS/GCP)"
        ],
        "optional_skills": [
            "Kubernetes",
            "Terraform",
            "Prometheus & Grafana",
            "Ansible",
            "DevSecOps",
            "Helm"
        ],
        "common_tools": [
            "Docker",
            "Kubernetes",
            "GitHub Actions / GitLab CI",
            "Grafana",
            "Prometheus",
            "Terraform"
        ],
        "education_paths": [
            "Bachelor's degree in Computer Science, IT, Computer Engineering, or related technical disciplines",
            "Self-taught through containerization projects, hands-on Linux administration, and CI/CD pipelines",
            "Transition from Systems Administration or Software Development"
        ],
        "certifications": [
            {
                "name": "Certified Kubernetes Administrator (CKA)",
                "cost": "$395 (Exam fee)",
                "provider": "Linux Foundation / CNCF",
                "url": "https://www.cncf.io/certification/cka/"
            },
            {
                "name": "GitHub Actions Certification",
                "cost": "$99 (Exam fee)",
                "provider": "GitHub",
                "url": "https://examregistration.github.com/"
            },
            {
                "name": "AWS Certified DevOps Engineer \u2013 Professional",
                "cost": "$300 (Exam fee)",
                "provider": "AWS",
                "url": "https://aws.amazon.com/certification/certified-devops-engineer-professional/"
            }
        ],
        "portfolio_projects": [
            {
                "title": "Automated Multi-Stage CI/CD Pipeline with GitHub Actions",
                "description": "Complete CI/CD pipeline that runs linter checks, automated unit tests, builds a Docker image, and deploys to a test server on push.",
                "difficulty": "Foundational"
            },
            {
                "title": "Production Monitoring Stack with Prometheus & Grafana",
                "description": "Deploying containerized Prometheus and Grafana dashboards monitoring CPU, memory, HTTP request rates, and error rate alerting.",
                "difficulty": "Intermediate"
            },
            {
                "title": "Production Kubernetes Cluster Deployment with Helm & GitOps",
                "description": "Zero-downtime rolling update deployment of a microservice application on Kubernetes utilizing ArgoCD and Helm charts.",
                "difficulty": "Advanced"
            }
        ],
        "salary_data": {
            "philippines": {
                "currency": "PHP",
                "entry_level": "\u20b1420,000 \u2013 \u20b1720,000 / year (\u20b135k - \u20b160k/mo)",
                "mid_level": "\u20b1840,000 \u2013 \u20b11,680,000 / year (\u20b170k - \u20b1140k/mo)",
                "senior_level": "\u20b11,800,000 \u2013 \u20b13,400,000+ / year (\u20b1150k - \u20b1280k+/mo)",
                "source": "Payscale PH, NodeFlair SEA Report",
                "updated_at": "2026-Q1"
            },
            "global_usd": {
                "currency": "USD",
                "entry_level": "$85,000 \u2013 $105,000 / year",
                "mid_level": "$115,000 \u2013 $160,000 / year",
                "senior_level": "$165,000 \u2013 $230,000+ / year",
                "source": "Levels.fyi, Puppet State of DevOps Report",
                "updated_at": "2026-Q1"
            }
        },
        "learning_resources": [
            {
                "title": "DevOps Roadmap (roadmap.sh/devops)",
                "type": "Community Visual Guide",
                "cost": "Free",
                "provider": "roadmap.sh",
                "url": "https://roadmap.sh/devops"
            },
            {
                "title": "Docker Official Getting Started Guide",
                "type": "Documentation & Hands-on",
                "cost": "Free",
                "provider": "Docker",
                "url": "https://docs.docker.com/get-started/"
            },
            {
                "title": "Kubernetes Official Interactive Tutorials",
                "type": "Interactive Sandbox",
                "cost": "Free",
                "provider": "Kubernetes.io",
                "url": "https://kubernetes.io/docs/tutorials/"
            }
        ],
        "related_careers": [
            "cloud-engineer",
            "fullstack-developer",
            "cybersecurity-analyst",
            "software-engineer"
        ],
        "sources": [
            "CNCF",
            "Puppet",
            "Levels.fyi",
            "Payscale"
        ],
        "last_updated": "2026-09-01",
        "psoc_code": "2512",
        "soc_code": "15-1252.00",
        "job_zone": 4
    },
    {
        "id": "data-scientist",
        "title": "Data Scientist",
        "field": "Data Science & Mathematics",
        "category_id": "data_ai",
        "category_name": "Data, Analytics & AI",
        "tagline": "Harness statistics, algorithms, and predictive modeling to answer complex organizational questions.",
        "description": "Data Scientists combine domain expertise, statistics, and machine learning to extract deep knowledge from large datasets. They formulate hypotheses, engineer experimental models, and discover predictive signals.",
        "responsibilities": [
            "Formulate mathematical and statistical models to predict business outcomes and user trends",
            "Clean, impute, and transform complex unstructured and structured datasets",
            "Design, execute, and evaluate controlled experiments (A/B testing) for product features",
            "Train and validate predictive models using Python, scikit-learn, and statistical packages",
            "Communicate probabilistic insights and experimental results to stakeholders"
        ],
        "riasec_traits": [
            "I",
            "A",
            "C"
        ],
        "work_style": "Deep intellectual investigation, hypothesis testing, data exploration, and statistical reasoning.",
        "core_skills": [
            "Python / R",
            "Statistics & Probability",
            "SQL",
            "Pandas & NumPy",
            "Machine Learning Algorithms",
            "Data Storytelling"
        ],
        "optional_skills": [
            "A/B Testing Methodology",
            "Deep Learning",
            "Big Data (PySpark)",
            "Cloud Warehouses (Snowflake/BigQuery)",
            "Data Visualization"
        ],
        "common_tools": [
            "Jupyter / Google Colab",
            "Python",
            "scikit-learn",
            "SQL",
            "Tableau",
            "Git"
        ],
        "education_paths": [
            "Degree in Statistics, Mathematics, Computer Science, Data Science, Physics, or Quantitative Economics",
            "Self-taught through competitive Kaggle datasets, published Jupyter case studies, and open-source contributions",
            "Transition from Data Analytics with deepened mathematical training"
        ],
        "certifications": [
            {
                "name": "IBM Data Science Professional Certificate",
                "cost": "Low-cost (Coursera FinAid Available)",
                "provider": "Coursera / IBM",
                "url": "https://www.coursera.org/professional-certificates/ibm-data-science"
            },
            {
                "name": "Kaggle Competitions Master / Notebooks Master",
                "cost": "Free",
                "provider": "Kaggle",
                "url": "https://www.kaggle.com/"
            }
        ],
        "portfolio_projects": [
            {
                "title": "Customer Churn Predictive Model with Interpretability",
                "description": "Predicting customer subscription churn with Random Forest / XGBoost, featuring SHAP value explanations for feature importance.",
                "difficulty": "Foundational"
            },
            {
                "title": "A/B Experimentation Analysis & Statistical Significance Report",
                "description": "Comprehensive statistical notebook assessing sample size, p-value calculations, bootstrap intervals, and bias avoidance.",
                "difficulty": "Intermediate"
            },
            {
                "title": "End-to-End Time Series Demand Forecasting Model",
                "description": "Forecasting multi-category retail inventory demand utilizing ARIMA/Prophet models with backtesting evaluation.",
                "difficulty": "Advanced"
            }
        ],
        "salary_data": {
            "philippines": {
                "currency": "PHP",
                "entry_level": "\u20b1420,000 \u2013 \u20b1720,000 / year (\u20b135k - \u20b160k/mo)",
                "mid_level": "\u20b1840,000 \u2013 \u20b11,680,000 / year (\u20b170k - \u20b1140k/mo)",
                "senior_level": "\u20b11,800,000 \u2013 \u20b13,200,000+ / year (\u20b1150k - \u20b1265k+/mo)",
                "source": "Payscale PH, Analytics Association of the Philippines",
                "updated_at": "2026-Q1"
            },
            "global_usd": {
                "currency": "USD",
                "entry_level": "$80,000 \u2013 $105,000 / year",
                "mid_level": "$115,000 \u2013 $160,000 / year",
                "senior_level": "$165,000 \u2013 $235,000+ / year",
                "source": "Levels.fyi, US BLS (Data Scientists)",
                "updated_at": "2026-Q1"
            }
        },
        "learning_resources": [
            {
                "title": "StatQuest with Josh Starmer (Machine Learning & Stats)",
                "type": "Visual Educational Videos",
                "cost": "Free",
                "provider": "StatQuest",
                "url": "https://statquest.org/"
            },
            {
                "title": "Python Data Science Handbook (Jake VanderPlas)",
                "type": "Open Access Book",
                "cost": "Free",
                "provider": "GitHub / O'Reilly",
                "url": "https://jakevdp.github.io/PythonDataScienceHandbook/"
            },
            {
                "title": "Kaggle Learn Micro-Courses",
                "type": "Interactive Tutorials",
                "cost": "Free",
                "provider": "Kaggle",
                "url": "https://www.kaggle.com/learn"
            }
        ],
        "related_careers": [
            "data-analyst",
            "ai-ml-engineer",
            "product-manager",
            "database-administrator"
        ],
        "sources": [
            "U.S. Bureau of Labor Statistics",
            "Kaggle",
            "Levels.fyi",
            "Payscale"
        ],
        "last_updated": "2026-09-01",
        "psoc_code": "2521",
        "soc_code": "15-2051.00",
        "job_zone": 5
    },
    {
        "id": "technical-writer",
        "title": "Technical Writer & Content Strategist",
        "field": "Writing, Media & Communications",
        "category_id": "communications",
        "category_name": "Writing & Communications",
        "tagline": "Translate complex technical systems, APIs, and product architectures into crystal-clear documentation.",
        "description": "Technical Writers bridge the gap between engineering teams and end-users. They produce developer documentation, API references, user manuals, knowledge bases, and standard operating procedures.",
        "responsibilities": [
            "Author comprehensive developer documentation, tutorials, and API reference guides",
            "Collaborate with software engineers, product managers, and designers to extract technical specifications",
            "Maintain docs-as-code workflows using Markdown, Git, static site generators, and CI/CD pipelines",
            "Create diagrams, architecture flowcharts, and instructional screen captures",
            "Review and edit user interface microcopy and system error messages for clarity"
        ],
        "riasec_traits": [
            "A",
            "I",
            "C"
        ],
        "work_style": "In-depth technical research, structured writing flow, and cross-team collaboration.",
        "core_skills": [
            "Technical Writing & Documentation",
            "API Documentation",
            "Markdown & Docs-as-Code",
            "Git & GitHub",
            "Information Architecture",
            "Content Strategy",
            "Copy Editing"
        ],
        "optional_skills": [
            "Swagger / OpenAPI",
            "HTML/CSS Basics",
            "JavaScript / Python Basics",
            "Docusaurus / MkDocs",
            "UX Microcopy"
        ],
        "common_tools": [
            "Markdown / MDX",
            "Git / GitHub",
            "VS Code",
            "Postman",
            "Docusaurus",
            "Notion / Confluence"
        ],
        "education_paths": [
            "Bachelor's degree in Communications, English, Technical Writing, Computer Science, or related field",
            "Demonstrated portfolio of public documentation, technical articles, and open-source contributions"
        ],
        "certifications": [
            {
                "name": "Google Technical Writing Courses",
                "cost": "Free",
                "provider": "Google Developers",
                "url": "https://developers.google.com/tech-writing"
            },
            {
                "name": "Society for Technical Communication (STC) Certified Professional",
                "cost": "$260 \u2013 $515",
                "provider": "STC",
                "url": "https://www.stc.org/certification/"
            }
        ],
        "portfolio_projects": [
            {
                "title": "Open-Source REST API Documentation & Quickstart Guide",
                "description": "Interactive API reference documentation with curl examples, payload schemas, and error code breakdowns.",
                "difficulty": "Intermediate"
            },
            {
                "title": "End-to-End Developer Tutorial & Architectural Deep Dive",
                "description": "Step-by-step onboarding guide teaching developers how to deploy a full-stack application.",
                "difficulty": "Intermediate"
            },
            {
                "title": "Standard Operating Procedure (SOP) & Knowledge Base Architecture",
                "description": "Structured taxonomy and multi-article troubleshooting knowledge base for a SaaS product.",
                "difficulty": "Foundational"
            }
        ],
        "salary_data": {
            "philippines": {
                "currency": "PHP",
                "entry_level": "\u20b1300,000 \u2013 \u20b1540,000 / year (\u20b125k - \u20b145k/mo)",
                "mid_level": "\u20b1600,000 \u2013 \u20b11,100,000 / year (\u20b150k - \u20b192k/mo)",
                "senior_level": "\u20b11,200,000 \u2013 \u20b12,200,000+ / year (\u20b1100k - \u20b1183k+/mo)",
                "source": "JobStreet Philippines & Payscale Technical Writer Benchmarks",
                "updated_at": "2026-Q1"
            },
            "global_usd": {
                "currency": "USD",
                "entry_level": "$60,000 \u2013 $80,000 / year",
                "mid_level": "$85,000 \u2013 $115,000 / year",
                "senior_level": "$120,000 \u2013 $165,000+ / year",
                "source": "U.S. Bureau of Labor Statistics (Technical Writers)",
                "updated_at": "2026-Q1"
            }
        },
        "learning_resources": [
            {
                "title": "Google Developers Technical Writing Courses",
                "type": "Interactive Curriculum",
                "cost": "Free",
                "provider": "Google",
                "url": "https://developers.google.com/tech-writing"
            },
            {
                "title": "Write the Docs Community Guides",
                "type": "Open-Source Documentation Community",
                "cost": "Free",
                "provider": "Write the Docs",
                "url": "https://www.writethedocs.org/"
            },
            {
                "title": "Microsoft Style Guide for Technical Publications",
                "type": "Writing Standards Reference",
                "cost": "Free",
                "provider": "Microsoft Learn",
                "url": "https://learn.microsoft.com/en-us/style-guide/welcome/"
            }
        ],
        "related_careers": [
            "frontend-developer",
            "product-manager",
            "secondary-educator"
        ],
        "sources": [
            "Philippine Statistics Authority (PSOC 2641)",
            "Google Developers Tech Writing Guide",
            "U.S. BLS"
        ],
        "last_updated": "2026-09-01",
        "psoc_code": "2641",
        "soc_code": "27-3042.00",
        "job_zone": 4
    },
    {
        "id": "qa-engineer",
        "title": "QA Engineer (Quality Assurance)",
        "field": "Software Quality & Testing",
        "category_id": "development",
        "category_name": "Software & Web Development",
        "tagline": "Ensure software reliability, catch edge cases, and automate test suites before code reaches users.",
        "description": "Quality Assurance (QA) Engineers design testing strategies, execute manual exploratory tests, and write automated test scripts (E2E, integration, API) to ensure software meets the highest standards of reliability, performance, and accessibility.",
        "responsibilities": [
            "Develop comprehensive test plans, test cases, and test scenarios based on product specs",
            "Write and maintain automated testing scripts using Playwright, Cypress, or Selenium",
            "Perform manual exploratory testing to identify edge cases, UX glitches, and functional regressions",
            "Execute API testing using Postman or automated test suites to verify response payloads",
            "Document clear bug reports with reproducible steps and collaborate with developers on fixes"
        ],
        "riasec_traits": [
            "C",
            "I",
            "R"
        ],
        "work_style": "Detail-oriented investigation, methodical verification, and quality craftsmanship.",
        "core_skills": [
            "Software Testing Principles",
            "Bug Tracking & Reporting",
            "API Testing (Postman)",
            "Test Case Design",
            "Git Basics"
        ],
        "optional_skills": [
            "Playwright or Cypress",
            "Python / JavaScript Basics",
            "CI/CD Test Automation",
            "Performance Testing (JMeter)",
            "Accessibility Testing"
        ],
        "common_tools": [
            "Postman",
            "Playwright / Cypress",
            "Jira",
            "Chrome DevTools",
            "GitHub Actions",
            "Selenium"
        ],
        "education_paths": [
            "Degree in Computer Science, Information Technology, or Engineering",
            "Entry-level manual testing transitioning to test automation engineering",
            "Self-taught QA practitioners with hands-on test portfolio automation repositories"
        ],
        "certifications": [
            {
                "name": "ISTQB Certified Tester Foundation Level (CTFL)",
                "cost": "$229 (Exam fee)",
                "provider": "ISTQB / ASTQB",
                "url": "https://www.istqb.org/certifications/certified-tester-foundation-level"
            },
            {
                "name": "Postman API Fundamentals Student Expert",
                "cost": "Free",
                "provider": "Postman",
                "url": "https://www.postman.com/student-program/student-expert/"
            }
        ],
        "portfolio_projects": [
            {
                "title": "Comprehensive Test Plan & Bug Tracking Portfolio",
                "description": "Structured test matrix, equivalence partitioning test cases, and documented GitHub issue bug reports for a live open-source web application.",
                "difficulty": "Foundational"
            },
            {
                "title": "Automated End-to-End (E2E) Test Suite with Playwright",
                "description": "Automated cross-browser test suite covering user authentication, shopping cart edge cases, and form validation with screenshot failure artifacts.",
                "difficulty": "Intermediate"
            },
            {
                "title": "Automated API & Performance Testing Pipeline in GitHub Actions",
                "description": "Scheduled CI/CD pipeline executing automated Newman (Postman) API contract tests and k6 load testing against staging endpoints.",
                "difficulty": "Advanced"
            }
        ],
        "salary_data": {
            "philippines": {
                "currency": "PHP",
                "entry_level": "\u20b1280,000 \u2013 \u20b1480,000 / year (\u20b123k - \u20b140k/mo)",
                "mid_level": "\u20b1540,000 \u2013 \u20b11,100,000 / year (\u20b145k - \u20b190k/mo)",
                "senior_level": "\u20b11,200,000 \u2013 \u20b12,300,000+ / year (\u20b1100k - \u20b1190k+/mo)",
                "source": "Payscale PH, JobStreet Tech Salaries",
                "updated_at": "2026-Q1"
            },
            "global_usd": {
                "currency": "USD",
                "entry_level": "$62,000 \u2013 $82,000 / year",
                "mid_level": "$88,000 \u2013 $120,000 / year",
                "senior_level": "$130,000 \u2013 $175,000+ / year",
                "source": "Levels.fyi, Glassdoor QA Salary Benchmarks",
                "updated_at": "2026-Q1"
            }
        },
        "learning_resources": [
            {
                "title": "Playwright Official Guides & Tutorial",
                "type": "Modern E2E Testing Docs",
                "cost": "Free",
                "provider": "Microsoft Playwright",
                "url": "https://playwright.dev/"
            },
            {
                "title": "Ministry of Testing Community Guides",
                "type": "Testing Articles & Forums",
                "cost": "Free Articles Available",
                "provider": "Ministry of Testing",
                "url": "https://www.ministryoftesting.com/"
            },
            {
                "title": "Postman Learning Center",
                "type": "Interactive API Testing Guide",
                "cost": "Free",
                "provider": "Postman",
                "url": "https://learning.postman.com/"
            }
        ],
        "related_careers": [
            "frontend-developer",
            "fullstack-developer",
            "devops-engineer",
            "technical-writer"
        ],
        "sources": [
            "ISTQB",
            "Ministry of Testing",
            "Levels.fyi",
            "Payscale"
        ],
        "last_updated": "2026-09-01",
        "psoc_code": "2519",
        "soc_code": "15-1253.00",
        "job_zone": 4
    },
    {
        "id": "mobile-app-developer",
        "title": "Mobile App Developer",
        "field": "Technology",
        "category_id": "development",
        "category_name": "Software & Web Development",
        "tagline": "Craft smooth, native and cross-platform mobile experiences for smartphones and tablets.",
        "description": "Mobile App Developers design and build applications for iOS and Android devices. Utilizing modern frameworks like Flutter, React Native, Swift, or Kotlin, they deliver fast, intuitive, and responsive handheld applications.",
        "responsibilities": [
            "Develop cross-platform or native mobile applications for iOS and Android",
            "Implement responsive mobile UIs that adapt across varying screen sizes and orientations",
            "Integrate RESTful APIs, local SQLite storage, push notifications, and biometric authentication",
            "Optimize app performance, battery usage, memory footprint, and network consumption",
            "Manage app store release workflows (Apple App Store & Google Play Store)"
        ],
        "riasec_traits": [
            "R",
            "A",
            "I"
        ],
        "work_style": "Hands-on coding, creative tactile problem-solving, and device-focused polish.",
        "core_skills": [
            "Flutter (Dart) or React Native",
            "Mobile UI Patterns",
            "REST APIs",
            "State Management",
            "Git & GitHub"
        ],
        "optional_skills": [
            "Swift / SwiftUI (iOS)",
            "Kotlin / Jetpack Compose (Android)",
            "SQLite / Hive Local Storage",
            "App Store Publishing",
            "Push Notifications"
        ],
        "common_tools": [
            "Android Studio",
            "Xcode",
            "VS Code",
            "Figma",
            "Firebase",
            "Postman"
        ],
        "education_paths": [
            "Bachelor's in Computer Science, Information Technology, or Software Engineering",
            "Mobile development bootcamps and guided app store publishing projects",
            "Self-taught engineers with live published apps on Google Play or Apple App Store"
        ],
        "certifications": [
            {
                "name": "Google Associate Android Developer (Kotlin)",
                "cost": "$149 (Exam fee)",
                "provider": "Google",
                "url": "https://developers.google.com/certification/associate-android-developer"
            },
            {
                "name": "Meta iOS / Android Developer Professional Certificate",
                "cost": "Low-cost (Coursera FinAid Available)",
                "provider": "Coursera / Meta",
                "url": "https://www.coursera.org/professional-certificates/meta-android-developer"
            }
        ],
        "portfolio_projects": [
            {
                "title": "Habit Tracker & Daily Journal with Offline Sync",
                "description": "Mobile app featuring smooth animations, offline local SQLite storage, dark mode, and scheduled local notifications.",
                "difficulty": "Foundational"
            },
            {
                "title": "Location-Aware Food Delivery or Cafe Discovery App",
                "description": "Cross-platform app integrating Google Maps API, live geolocation tracking, search filtering, and mock payment checkout.",
                "difficulty": "Intermediate"
            },
            {
                "title": "Real-Time Audio / Chat Messaging Mobile Client",
                "description": "Production mobile app utilizing WebSockets / Supabase real-time, optimistic message sending, media caching, and biometric login.",
                "difficulty": "Advanced"
            }
        ],
        "salary_data": {
            "philippines": {
                "currency": "PHP",
                "entry_level": "\u20b1360,000 \u2013 \u20b1600,000 / year (\u20b130k - \u20b150k/mo)",
                "mid_level": "\u20b1720,000 \u2013 \u20b11,440,000 / year (\u20b160k - \u20b1120k/mo)",
                "senior_level": "\u20b11,500,000 \u2013 \u20b12,800,000+ / year (\u20b1125k - \u20b1230k+/mo)",
                "source": "Payscale PH, NodeFlair SEA",
                "updated_at": "2026-Q1"
            },
            "global_usd": {
                "currency": "USD",
                "entry_level": "$75,000 \u2013 $95,000 / year",
                "mid_level": "$105,000 \u2013 $145,000 / year",
                "senior_level": "$150,000 \u2013 $210,000+ / year",
                "source": "Levels.fyi, Indeed Tech Salary Indices",
                "updated_at": "2026-Q1"
            }
        },
        "learning_resources": [
            {
                "title": "Flutter Official Documentation & Codelabs",
                "type": "Interactive Guides",
                "cost": "Free",
                "provider": "Flutter Team",
                "url": "https://docs.flutter.dev/"
            },
            {
                "title": "Android Basics with Compose (Official Google Course)",
                "type": "Guided Course",
                "cost": "Free",
                "provider": "Google Developers",
                "url": "https://developer.android.com/courses/android-basics-compose/course"
            },
            {
                "title": "React Native Official Getting Started",
                "type": "Documentation",
                "cost": "Free",
                "provider": "Meta",
                "url": "https://reactnative.dev/docs/getting-started"
            }
        ],
        "related_careers": [
            "frontend-developer",
            "fullstack-developer",
            "ui-designer",
            "ux-engineer"
        ],
        "sources": [
            "Google Developers",
            "Apple Developer",
            "Levels.fyi",
            "Payscale"
        ],
        "last_updated": "2026-09-01",
        "psoc_code": "2512",
        "soc_code": "15-1252.00",
        "job_zone": 4
    },
    {
        "id": "product-designer",
        "title": "Product Designer",
        "field": "Design & Product Strategy",
        "category_id": "design",
        "category_name": "UI/UX & Product Design",
        "tagline": "Shape the complete end-to-end product experience, uniting user needs with business goals.",
        "description": "Product Designers take holistic ownership of a digital product's design. They conduct user research, design wireframes and high-fidelity interfaces, build scalable design systems, and partner with product managers to validate business metrics.",
        "responsibilities": [
            "Own end-to-end product design from user discovery to production-ready design assets",
            "Synthesize qualitative user research and product telemetry into actionable UX solutions",
            "Design polished, accessible user interfaces and interactive design systems in Figma",
            "Partner with engineering on component architecture, design tokens, and technical constraints",
            "Run usability tests, design sprints, and validate business hypotheses with iterative prototypes"
        ],
        "riasec_traits": [
            "A",
            "E",
            "I"
        ],
        "work_style": "Holistic product thinking, creative craft, cross-functional leadership, and user empathy.",
        "core_skills": [
            "End-to-End Product Design",
            "Figma",
            "UX Research",
            "UI Design",
            "Design Systems",
            "Prototyping",
            "Strategic Thinking"
        ],
        "optional_skills": [
            "Interaction Design",
            "Product Metrics & Analytics",
            "Basic Front-End Code (HTML/CSS)",
            "Design Sprint Facilitation"
        ],
        "common_tools": [
            "Figma",
            "FigJam",
            "Miro",
            "Notion",
            "Maze",
            "Loom"
        ],
        "education_paths": [
            "Degrees in Design, Human-Computer Interaction, Industrial Design, Fine Arts, or Computer Science",
            "Designers transitioning from graphic, UI, or UX design through complex product case studies",
            "Self-taught product designers with published case studies detailing metrics and business outcomes"
        ],
        "certifications": [
            {
                "name": "Google UX Design Professional Certificate",
                "cost": "Low-cost (Coursera FinAid Available)",
                "provider": "Coursera / Google",
                "url": "https://www.coursera.org/professional-certificates/google-ux-design"
            },
            {
                "name": "Interaction Design Foundation (IxDF) Master Classes",
                "cost": "Low-cost Membership",
                "provider": "IxDF",
                "url": "https://www.interaction-design.org/"
            }
        ],
        "portfolio_projects": [
            {
                "title": "0-to-1 B2C App Product Discovery & Design Case Study",
                "description": "Documented 0-to-1 design journey including competitor benchmarking, user problem statements, wireframe iterations, and tested high-fi Figma prototypes.",
                "difficulty": "Intermediate"
            },
            {
                "title": "Enterprise B2B Workflow Optimization & Design System",
                "description": "Designing complex data filtering, permissions management, and scalable design token architecture for a cloud platform.",
                "difficulty": "Advanced"
            }
        ],
        "salary_data": {
            "philippines": {
                "currency": "PHP",
                "entry_level": "\u20b1420,000 \u2013 \u20b1660,000 / year (\u20b135k - \u20b155k/mo)",
                "mid_level": "\u20b1780,000 \u2013 \u20b11,500,000 / year (\u20b165k - \u20b1125k/mo)",
                "senior_level": "\u20b11,560,000 \u2013 \u20b12,900,000+ / year (\u20b1130k - \u20b1240k+/mo)",
                "source": "Payscale PH, UXPH Compensation Survey",
                "updated_at": "2026-Q1"
            },
            "global_usd": {
                "currency": "USD",
                "entry_level": "$78,000 \u2013 $102,000 / year",
                "mid_level": "$110,000 \u2013 $155,000 / year",
                "senior_level": "$160,000 \u2013 $225,000+ / year",
                "source": "Levels.fyi, Dribbble Design Salary Index",
                "updated_at": "2026-Q1"
            }
        },
        "learning_resources": [
            {
                "title": "Design Systems Handbook (DesignBetter.Co)",
                "type": "Comprehensive Guide",
                "cost": "Free",
                "provider": "InVision / DesignBetter",
                "url": "https://www.designbetter.co/design-systems-handbook"
            },
            {
                "title": "Figma Best Practices Guide",
                "type": "Official Workflows",
                "cost": "Free",
                "provider": "Figma",
                "url": "https://www.figma.com/best-practices/"
            },
            {
                "title": "Growth.Design Case Studies",
                "type": "Interactive Comic UX Teardowns",
                "cost": "Free",
                "provider": "Growth.Design",
                "url": "https://growth.design/case-studies"
            }
        ],
        "related_careers": [
            "ux-designer",
            "ui-designer",
            "product-manager",
            "ux-engineer"
        ],
        "sources": [
            "DesignBetter",
            "Growth.Design",
            "Levels.fyi",
            "Payscale"
        ],
        "last_updated": "2026-09-01"
    },
    {
        "id": "database-administrator",
        "title": "Database Administrator (DBA)",
        "field": "Data & Infrastructure",
        "category_id": "cloud_security",
        "category_name": "Cloud, DevOps & Cybersecurity",
        "tagline": "Safeguard data integrity, optimize query performance, and ensure 24/7 database reliability.",
        "description": "Database Administrators (DBAs) design, maintain, and optimize mission-critical database systems. They manage backups, query execution plans, indexing strategies, user security permissions, and disaster recovery.",
        "responsibilities": [
            "Install, configure, patch, and maintain relational databases (PostgreSQL, MySQL, Oracle, SQL Server)",
            "Analyze and optimize slow-running SQL queries, indexing strategies, and database locks",
            "Establish and test automated backup routines, replication pipelines, and disaster recovery procedures",
            "Implement database security, role-based access control (RBAC), and encryption at rest and in transit",
            "Plan storage capacity, manage database partitioning, and support application schema migrations"
        ],
        "riasec_traits": [
            "C",
            "I",
            "R"
        ],
        "work_style": "Methodical, meticulous data stewardship, deep systems troubleshooting, and high reliability.",
        "core_skills": [
            "SQL & Relational Modeling",
            "PostgreSQL or MySQL Administration",
            "Performance Tuning & Indexing",
            "Backup & Recovery",
            "Linux Basics"
        ],
        "optional_skills": [
            "NoSQL (MongoDB/Redis)",
            "Database Replication & Clustering",
            "Cloud DBs (AWS RDS/Aurora)",
            "Python / Bash Scripting",
            "Data Warehousing"
        ],
        "common_tools": [
            "PostgreSQL / pgAdmin",
            "DBeaver",
            "Linux Terminal",
            "AWS RDS",
            "Explain Plan Tools",
            "Prometheus / Datadog"
        ],
        "education_paths": [
            "Degree in Computer Science, Information Technology, Information Systems, or Database Management",
            "Transition from Systems Administration or Data Engineering",
            "Vendor database certifications combined with enterprise database administration experience"
        ],
        "certifications": [
            {
                "name": "PostgreSQL Professional Certification (EDB / Linux Foundation)",
                "cost": "$200 \u2013 $300",
                "provider": "EnterpriseDB",
                "url": "https://www.enterprisedb.com/training-certification"
            },
            {
                "name": "AWS Certified Database \u2013 Specialty (or AWS Cloud Solutions)",
                "cost": "$300 (Exam fee)",
                "provider": "AWS",
                "url": "https://aws.amazon.com/certification/certified-database-specialty/"
            },
            {
                "name": "Oracle Certified Professional MySQL Database Administrator",
                "cost": "$245 (Exam fee)",
                "provider": "Oracle",
                "url": "https://education.oracle.com/mysql-database-administrator-certified-professional"
            }
        ],
        "portfolio_projects": [
            {
                "title": "PostgreSQL High-Availability Master-Replica Lab",
                "description": "Configuring PostgreSQL streaming replication with automated failover using pgpool and monitoring replication lag.",
                "difficulty": "Foundational"
            },
            {
                "title": "Query Optimization & Indexing Benchmark Case Study",
                "description": "Diagnosing a slow 10-million row database table, analyzing EXPLAIN ANALYZE execution plans, and reducing query latency by 95% with composite indexing.",
                "difficulty": "Intermediate"
            }
        ],
        "salary_data": {
            "philippines": {
                "currency": "PHP",
                "entry_level": "\u20b1360,000 \u2013 \u20b1540,000 / year (\u20b130k - \u20b145k/mo)",
                "mid_level": "\u20b1660,000 \u2013 \u20b11,320,000 / year (\u20b155k - \u20b1110k/mo)",
                "senior_level": "\u20b11,440,000 \u2013 \u20b12,700,000+ / year (\u20b1120k - \u20b1225k+/mo)",
                "source": "Payscale PH, JobStreet Database Benchmarks",
                "updated_at": "2026-Q1"
            },
            "global_usd": {
                "currency": "USD",
                "entry_level": "$70,000 \u2013 $90,000 / year",
                "mid_level": "$98,000 \u2013 $135,000 / year",
                "senior_level": "$140,000 \u2013 $190,000+ / year",
                "source": "Levels.fyi, US BLS (Database Administrators)",
                "updated_at": "2026-Q1"
            }
        },
        "learning_resources": [
            {
                "title": "PostgreSQL Official Documentation & Manual",
                "type": "Comprehensive Reference",
                "cost": "Free",
                "provider": "PostgreSQL Global Development Group",
                "url": "https://www.postgresql.org/docs/"
            },
            {
                "title": "Use The Index, Luke! (SQL Indexing Guide)",
                "type": "Database Indexing Guide",
                "cost": "Free",
                "provider": "Markus Winand",
                "url": "https://use-the-index-luke.com/"
            },
            {
                "title": "SQL Tutorial for Beginners (Mode Analytics)",
                "type": "Interactive SQL Guide",
                "cost": "Free",
                "provider": "Mode Analytics",
                "url": "https://mode.com/sql-tutorial/"
            }
        ],
        "related_careers": [
            "data-analyst",
            "cloud-engineer",
            "fullstack-developer",
            "devops-engineer"
        ],
        "sources": [
            "PostgreSQL.org",
            "U.S. BLS",
            "Levels.fyi",
            "Payscale"
        ],
        "last_updated": "2026-09-01"
    },
    {
        "id": "backend-developer",
        "title": "Back-End Developer",
        "field": "Technology",
        "category_id": "development",
        "category_name": "Software & Web Development",
        "tagline": "Build high-throughput APIs, business logic, microservices, and server architecture.",
        "description": "Back-End Developers architect and maintain server-side applications, data storage pipelines, and API integrations. They ensure high concurrency, low latency, database integrity, and authentication security.",
        "responsibilities": [
            "Design and build performant RESTful and gRPC APIs for web and mobile clients",
            "Develop server-side business logic using Python, Node.js, Go, or Java",
            "Optimize relational database queries, transactions, and caching with Redis",
            "Implement secure authentication protocols (OAuth2, JWT) and role-based access control",
            "Collaborate with DevOps on containerization, CI/CD pipelines, and cloud deployment"
        ],
        "riasec_traits": [
            "I",
            "R",
            "C"
        ],
        "work_style": "Systematic backend logic, deep algorithmic focus, and architectural problem solving.",
        "core_skills": [
            "Python, Node.js, or Go",
            "SQL & Database Design",
            "REST APIs",
            "Git & GitHub",
            "Data Structures & Algorithms"
        ],
        "optional_skills": [
            "PostgreSQL",
            "Docker",
            "Redis Caching",
            "Microservices",
            "System Design",
            "Message Queues (RabbitMQ/Kafka)"
        ],
        "common_tools": [
            "VS Code / PyCharm",
            "Postman",
            "PostgreSQL / DBeaver",
            "Docker",
            "Linux CLI",
            "Git"
        ],
        "education_paths": [
            "Bachelor's in Computer Science, Software Engineering, or Information Systems",
            "Back-End intensive bootcamps and open-source contributions",
            "Self-taught engineers building complex API projects"
        ],
        "certifications": [
            {
                "name": "freeCodeCamp Back End Development and APIs",
                "cost": "Free",
                "provider": "freeCodeCamp",
                "url": "https://www.freecodecamp.org/learn/back-end-development-and-apis/"
            },
            {
                "name": "Meta Back-End Developer Professional Certificate",
                "cost": "Low-cost (Coursera FinAid Available)",
                "provider": "Coursera / Meta",
                "url": "https://www.coursera.org/professional-certificates/meta-back-end-developer"
            }
        ],
        "portfolio_projects": [
            {
                "title": "High-Concurrency REST API with Authentication & Rate Limiting",
                "description": "Production-grade API featuring JWT auth, Redis rate-limiting, and PostgreSQL CRUD operations with 100% test coverage.",
                "difficulty": "Foundational"
            },
            {
                "title": "Distributed Event-Driven Order Processing System",
                "description": "Microservices architecture utilizing message queues (RabbitMQ), idempotency checks, and asynchronous webhook dispatching.",
                "difficulty": "Intermediate"
            },
            {
                "title": "Custom Search Engine Indexer & Caching Pipeline",
                "description": "High-speed inverted index search API with Redis cache invalidation and database connection pooling.",
                "difficulty": "Advanced"
            }
        ],
        "salary_data": {
            "philippines": {
                "currency": "PHP",
                "entry_level": "\u20b1360,000 \u2013 \u20b1600,000 / year (\u20b130k - \u20b150k/mo)",
                "mid_level": "\u20b1720,000 \u2013 \u20b11,500,000 / year (\u20b160k - \u20b1125k/mo)",
                "senior_level": "\u20b11,500,000 \u2013 \u20b13,000,000+ / year (\u20b1125k - \u20b1250k+/mo)",
                "source": "Payscale PH, NodeFlair SEA",
                "updated_at": "2026-Q1"
            },
            "global_usd": {
                "currency": "USD",
                "entry_level": "$75,000 \u2013 $98,000 / year",
                "mid_level": "$105,000 \u2013 $150,000 / year",
                "senior_level": "$155,000 \u2013 $220,000+ / year",
                "source": "Levels.fyi, Stack Overflow Developer Survey",
                "updated_at": "2026-Q1"
            }
        },
        "learning_resources": [
            {
                "title": "Backend Development Roadmap (roadmap.sh/backend)",
                "type": "Visual Guide",
                "cost": "Free",
                "provider": "roadmap.sh",
                "url": "https://roadmap.sh/backend"
            },
            {
                "title": "CS50's Introduction to Computer Science",
                "type": "University Course",
                "cost": "Free",
                "provider": "Harvard University (edX)",
                "url": "https://cs50.harvard.edu/x/"
            },
            {
                "title": "FastAPI / Node.js Official Documentation",
                "type": "Documentation",
                "cost": "Free",
                "provider": "FastAPI",
                "url": "https://fastapi.tiangolo.com/"
            }
        ],
        "related_careers": [
            "fullstack-developer",
            "devops-engineer",
            "cloud-engineer",
            "database-administrator"
        ],
        "sources": [
            "Stack Overflow",
            "Levels.fyi",
            "Payscale",
            "NodeFlair"
        ],
        "last_updated": "2026-09-01",
        "psoc_code": "2512",
        "soc_code": "15-1252.00",
        "job_zone": 4
    },
    {
        "id": "ux-engineer",
        "title": "UX Engineer",
        "field": "Design & Engineering",
        "category_id": "design",
        "category_name": "UI/UX & Product Design",
        "tagline": "Bridge the gap between UX design and front-end engineering through interactive prototypes and design systems.",
        "description": "UX Engineers are hybrid practitioners who combine design sensibilities with deep front-end engineering expertise. They build interactive design system components, explore micro-interactions, and ensure seamless handoffs.",
        "responsibilities": [
            "Build and maintain scalable design systems in React/TypeScript with Storybook",
            "Develop high-fidelity code prototypes to test complex interactions and animations",
            "Ensure digital accessibility (WCAG AA) compliance across all UI components",
            "Bridge the technical feasibility gap between designers and front-end developers",
            "Advocate for design tokens, motion guidelines, and reusable component architectures"
        ],
        "riasec_traits": [
            "A",
            "I",
            "R"
        ],
        "work_style": "Hybrid creative-technical craft, rapid prototyping, and cross-discipline collaboration.",
        "core_skills": [
            "HTML5/CSS3/JavaScript",
            "React & TypeScript",
            "Figma",
            "Design Systems",
            "Web Accessibility (a11y)",
            "Git"
        ],
        "optional_skills": [
            "Storybook",
            "Framer Motion / CSS Animations",
            "Tailwind CSS",
            "UX Research Basics",
            "Component Unit Testing"
        ],
        "common_tools": [
            "VS Code",
            "Figma",
            "Storybook",
            "Chrome DevTools",
            "GitHub",
            "Vercel"
        ],
        "education_paths": [
            "Degree in Computer Science, HCI, Interactive Media, or Graphic Design",
            "Front-End developers who developed deep design expertise",
            "UI/UX designers who learned modern JavaScript component development"
        ],
        "certifications": [
            {
                "name": "Interaction Design Foundation: UI & Front-End Design",
                "cost": "Low-cost Membership",
                "provider": "IxDF",
                "url": "https://www.interaction-design.org/"
            },
            {
                "name": "Frontend Masters Design Systems Path",
                "cost": "Subscription",
                "provider": "Frontend Masters",
                "url": "https://frontendmasters.com/courses/design-systems/"
            }
        ],
        "portfolio_projects": [
            {
                "title": "Accessible Design System in Storybook",
                "description": "Interactive component library with automated a11y tests, keyboard navigation, and theme tokens.",
                "difficulty": "Foundational"
            },
            {
                "title": "High-Fidelity Interactive App Prototype in Code",
                "description": "Fully interactive code prototype demonstrating complex multi-step drag-and-drop or canvas interactions.",
                "difficulty": "Intermediate"
            }
        ],
        "salary_data": {
            "philippines": {
                "currency": "PHP",
                "entry_level": "\u20b1380,000 \u2013 \u20b1620,000 / year (\u20b132k - \u20b152k/mo)",
                "mid_level": "\u20b1750,000 \u2013 \u20b11,400,000 / year (\u20b162k - \u20b1116k/mo)",
                "senior_level": "\u20b11,500,000 \u2013 \u20b12,800,000+ / year (\u20b1125k - \u20b1230k+/mo)",
                "source": "Payscale PH, UXPH",
                "updated_at": "2026-Q1"
            },
            "global_usd": {
                "currency": "USD",
                "entry_level": "$75,000 \u2013 $98,000 / year",
                "mid_level": "$105,000 \u2013 $148,000 / year",
                "senior_level": "$155,000 \u2013 $215,000+ / year",
                "source": "Levels.fyi, Google UXE Salary Data",
                "updated_at": "2026-Q1"
            }
        },
        "learning_resources": [
            {
                "title": "Storybook Official Tutorials",
                "type": "Interactive Guides",
                "cost": "Free",
                "provider": "Storybook",
                "url": "https://storybook.js.org/tutorials/"
            },
            {
                "title": "Inclusive Components by Heydon Pickering",
                "type": "Accessible Patterns",
                "cost": "Free",
                "provider": "Inclusive Components",
                "url": "https://inclusive-components.design/"
            }
        ],
        "related_careers": [
            "frontend-developer",
            "ux-designer",
            "ui-designer",
            "product-designer"
        ],
        "sources": [
            "Storybook",
            "Google Careers",
            "Levels.fyi",
            "Payscale"
        ],
        "last_updated": "2026-09-01"
    },
    {
        "id": "business-analyst",
        "title": "Business Analyst (IT & Tech)",
        "field": "Business Strategy & Technology",
        "category_id": "product_management",
        "category_name": "Product & Tech Strategy",
        "tagline": "Analyze organizational processes, uncover operational inefficiencies, and define technological solutions.",
        "description": "Business Analysts evaluate organizational workflows, identify business challenges, and translate stakeholder needs into precise functional specifications for technical teams.",
        "responsibilities": [
            "Elicit and document business requirements through stakeholder interviews and process modeling",
            "Map current-state vs future-state business workflows and gap analyses",
            "Create functional requirement specifications, user stories, and acceptance criteria",
            "Perform feasibility analysis and calculate return on investment (ROI) for tech projects",
            "Support user acceptance testing (UAT) and facilitate stakeholder change management"
        ],
        "riasec_traits": [
            "E",
            "C",
            "S"
        ],
        "work_style": "Consultative communication, structured requirements analysis, and business alignment.",
        "core_skills": [
            "Business Process Modeling",
            "Requirements Gathering",
            "Agile / User Stories",
            "Stakeholder Communication",
            "Data Analysis Basics"
        ],
        "optional_skills": [
            "SQL Basics",
            "Tableau / Power BI",
            "UML Diagramming",
            "Financial Modeling",
            "Jira / Confluence"
        ],
        "common_tools": [
            "Jira / Confluence",
            "Lucidchart / Miro",
            "Excel",
            "Power BI",
            "Notion"
        ],
        "education_paths": [
            "Degrees in Business Administration, Information Systems, Management Engineering, or Economics",
            "Transition from operations, project management, or quality assurance",
            "Professional Business Analysis certifications (IIBA ECBA/CBAP)"
        ],
        "certifications": [
            {
                "name": "IIBA Entry Certificate in Business Analysis (ECBA)",
                "cost": "$225 (Exam fee)",
                "provider": "IIBA",
                "url": "https://www.iiba.org/business-analysis-certifications/ecba/"
            },
            {
                "name": "Coursera / IBM IT Scrum Master & Business Analyst Specialization",
                "cost": "Low-cost (Coursera FinAid Available)",
                "provider": "IBM / Coursera",
                "url": "https://www.coursera.org/specializations/ibm-scrum-master"
            }
        ],
        "portfolio_projects": [
            {
                "title": "Business Process Model & Gap Analysis Report",
                "description": "End-to-end BPMN workflow mapping for an e-commerce or customer onboarding flow, detailing 40% reduction in processing time.",
                "difficulty": "Foundational"
            },
            {
                "title": "Software Functional Specification Document & UAT Matrix",
                "description": "Comprehensive requirement package with traceability matrix, acceptance criteria, and edge-case testing plans.",
                "difficulty": "Intermediate"
            }
        ],
        "salary_data": {
            "philippines": {
                "currency": "PHP",
                "entry_level": "\u20b1300,000 \u2013 \u20b1500,000 / year (\u20b125k - \u20b142k/mo)",
                "mid_level": "\u20b1600,000 \u2013 \u20b11,200,000 / year (\u20b150k - \u20b1100k/mo)",
                "senior_level": "\u20b11,200,000 \u2013 \u20b12,400,000+ / year (\u20b1100k - \u20b1200k+/mo)",
                "source": "Payscale PH, IIBA Philippines",
                "updated_at": "2026-Q1"
            },
            "global_usd": {
                "currency": "USD",
                "entry_level": "$65,000 \u2013 $85,000 / year",
                "mid_level": "$90,000 \u2013 $125,000 / year",
                "senior_level": "$130,000 \u2013 $175,000+ / year",
                "source": "Levels.fyi, US BLS (Management & IT Analysts)",
                "updated_at": "2026-Q1"
            }
        },
        "learning_resources": [
            {
                "title": "IIBA Guide to the Business Analysis Body of Knowledge (BABOK)",
                "type": "Industry Standard",
                "cost": "Free Overview Available",
                "provider": "IIBA",
                "url": "https://www.iiba.org/career-resources/a-guide-to-the-business-analysis-body-of-knowledge-babok-guide/"
            },
            {
                "title": "Modern Business Analysis by Bridging the Gap",
                "type": "Articles & Guides",
                "cost": "Free",
                "provider": "Bridging the Gap",
                "url": "https://www.bridging-the-gap.com/"
            }
        ],
        "related_careers": [
            "product-manager",
            "data-analyst",
            "technical-writer",
            "database-administrator"
        ],
        "sources": [
            "IIBA",
            "U.S. BLS",
            "Levels.fyi",
            "Payscale"
        ],
        "last_updated": "2026-09-01"
    },
    {
        "id": "graphic-designer",
        "title": "Visual Graphic & Brand Identity Designer",
        "field": "Design & Creative Arts",
        "category_id": "design",
        "category_name": "UI/UX & Creative Design",
        "psoc_code": "2166",
        "soc_code": "27-1024.00",
        "job_zone": 3,
        "tagline": "Craft visual identities, typography, branding assets, and marketing visuals that captivate audiences.",
        "description": "Graphic & Brand Designers develop visual concepts and brand identities using digital illustration and layout tools. They translate brand messaging into cohesive visual assets across digital media, packaging, and print.",
        "responsibilities": [
            "Create comprehensive brand identity systems including logos, color palettes, and typography guidelines",
            "Design marketing collateral, social media assets, and digital campaign visuals",
            "Prepare print-ready files and collaborate with commercial printing providers",
            "Collaborate with marketing teams to maintain visual brand consistency across channels",
            "Present design rationale and brand storytelling to clients and stakeholders"
        ],
        "riasec_traits": [
            "A",
            "E",
            "R"
        ],
        "work_style": "Creative studio rhythm, client-facing brand reviews, and focused vector/layout production.",
        "core_skills": [
            "Adobe Illustrator",
            "Adobe Photoshop",
            "Brand Identity",
            "Typography",
            "Visual Storytelling",
            "Color Theory",
            "Layout Design"
        ],
        "optional_skills": [
            "Motion Graphics (After Effects)",
            "Figma",
            "Packaging Design",
            "3D Modeling Basics (Blender)",
            "Print Production Standards"
        ],
        "common_tools": [
            "Adobe Creative Cloud",
            "Illustrator",
            "Photoshop",
            "InDesign",
            "Figma",
            "Canva Pro"
        ],
        "education_paths": [
            "TESDA National Certificate: Visual Graphic Design NC III",
            "Bachelor of Fine Arts (BFA) in Advertising Arts, Multimedia Arts, or Graphic Design",
            "Self-taught portfolio path with verified brand identity client work"
        ],
        "certifications": [
            {
                "name": "TESDA Visual Graphic Design NC III",
                "cost": "Free / Subsidized (TESDA Accredited Centers)",
                "provider": "TESDA Philippines",
                "url": "https://www.tesda.gov.ph"
            },
            {
                "name": "Adobe Certified Professional in Visual Design",
                "cost": "$150",
                "provider": "Certiport / Adobe",
                "url": "https://certiport.pearsonvue.com/Certifications/Adobe/ACP/Overview"
            },
            {
                "name": "CalArts Graphic Design Specialization",
                "cost": "Low-cost (Coursera FinAid Available)",
                "provider": "Coursera / CalArts",
                "url": "https://www.coursera.org/specializations/graphic-design"
            }
        ],
        "portfolio_projects": [
            {
                "title": "Full Brand Identity System & Brand Guidelines",
                "description": "Comprehensive corporate identity package including logo suite, typography hierarchy, collateral, and 20-page brand manual.",
                "difficulty": "Intermediate"
            },
            {
                "title": "Commercial Product Packaging & Label System",
                "description": "3D mockups and print-ready die-cut packaging designs for a consumer beverage or cosmetics line.",
                "difficulty": "Intermediate"
            },
            {
                "title": "Multi-Channel Social & Advertising Campaign",
                "description": "Integrated digital ad set across Instagram, LinkedIn, and print banners with motion graphics snippets.",
                "difficulty": "Foundational"
            }
        ],
        "salary_data": {
            "philippines": {
                "currency": "PHP",
                "entry_level": "\u20b1240,000 \u2013 \u20b1420,000 / year (\u20b120k - \u20b135k/mo)",
                "mid_level": "\u20b1480,000 \u2013 \u20b1840,000 / year (\u20b140k - \u20b170k/mo)",
                "senior_level": "\u20b1900,000 \u2013 \u20b11,800,000+ / year (\u20b175k - \u20b1150k+/mo)",
                "source": "JobStreet Philippines & DOLE Occupational Benchmark",
                "updated_at": "2026-Q1"
            },
            "global_usd": {
                "currency": "USD",
                "entry_level": "$45,000 \u2013 $60,000 / year",
                "mid_level": "$65,000 \u2013 $90,000 / year",
                "senior_level": "$95,000 \u2013 $140,000+ / year",
                "source": "U.S. Bureau of Labor Statistics (Graphic Designers)",
                "updated_at": "2026-Q1"
            }
        },
        "learning_resources": [
            {
                "title": "TESDA Visual Graphic Design Training Regulations",
                "type": "TVET Competency Guide",
                "cost": "Free",
                "provider": "TESDA",
                "url": "https://www.tesda.gov.ph"
            },
            {
                "title": "Creative Live Design Fundamentals",
                "type": "Video Tutorials",
                "cost": "Free/Freemium",
                "provider": "CreativeLive",
                "url": "https://www.creativelive.com"
            },
            {
                "title": "Adobe Illustrator Classroom in a Book",
                "type": "Official Tutorial Series",
                "cost": "Free Guides",
                "provider": "Adobe Help Center",
                "url": "https://helpx.adobe.com/illustrator.html"
            }
        ],
        "related_careers": [
            "ui-designer",
            "ux-designer",
            "technical-writer"
        ],
        "sources": [
            "Philippine Statistics Authority (PSOC 2166)",
            "TESDA Training Regulations",
            "U.S. Bureau of Labor Statistics"
        ],
        "last_updated": "2026-09-01"
    },
    {
        "id": "digital-marketing-strategist",
        "title": "Digital Marketing & Growth Strategist",
        "field": "Business, Marketing & Strategy",
        "category_id": "business_marketing",
        "category_name": "Business & Digital Marketing",
        "psoc_code": "2431",
        "soc_code": "13-1161.00",
        "job_zone": 4,
        "tagline": "Drive customer acquisition, brand reach, and revenue growth through data-backed multi-channel campaigns.",
        "description": "Digital Marketing Strategists architect and execute cross-channel customer acquisition campaigns using SEO, performance advertising, content strategy, and conversion rate optimization (CRO) to drive measurable business growth.",
        "responsibilities": [
            "Formulate omnichannel marketing strategies spanning search, social, email, and paid media",
            "Manage PPC advertising budgets across Google Ads, Meta Ads, and LinkedIn Ads with strict ROI targets",
            "Conduct keyword research, technical SEO audits, and content optimization workflows",
            "Analyze funnel analytics in Google Analytics 4 (GA4) to identify drop-offs and conversion opportunities",
            "A/B test landing pages and email automations to maximize customer retention and lifetime value (LTV)"
        ],
        "riasec_traits": [
            "E",
            "A",
            "I"
        ],
        "work_style": "Analytical yet creative, fast-paced campaign cycles, and executive growth reporting.",
        "core_skills": [
            "Digital Marketing",
            "SEO & Content Strategy",
            "Google Analytics 4 (GA4)",
            "Paid Media & PPC",
            "Conversion Rate Optimization (CRO)",
            "Copywriting",
            "A/B Testing"
        ],
        "optional_skills": [
            "Email Marketing Automation (HubSpot/Klaviyo)",
            "SQL Basics",
            "Marketing Psychology",
            "Social Media Advertising",
            "CRM Systems"
        ],
        "common_tools": [
            "Google Analytics 4",
            "Google Ads",
            "Meta Ads Manager",
            "SEMrush / Ahrefs",
            "HubSpot",
            "Looker Studio"
        ],
        "education_paths": [
            "Bachelor's degree in Marketing, Business Administration, Communications, or Information Systems",
            "Industry professional certifications with hands-on campaign portfolio"
        ],
        "certifications": [
            {
                "name": "Google Digital Marketing & E-commerce Professional Certificate",
                "cost": "Free / Low-cost",
                "provider": "Google / Coursera",
                "url": "https://grow.google/certificates/digital-marketing-ecommerce/"
            },
            {
                "name": "HubSpot Inbound Marketing & Content Marketing Certification",
                "cost": "Free",
                "provider": "HubSpot Academy",
                "url": "https://academy.hubspot.com/"
            },
            {
                "name": "Meta Certified Digital Marketing Associate",
                "cost": "$99",
                "provider": "Meta Blueprint",
                "url": "https://www.facebook.com/business/learn/certification"
            }
        ],
        "portfolio_projects": [
            {
                "title": "End-to-End Search Engine Optimization (SEO) Case Study",
                "description": "Keyword strategy, on-page optimization, and technical audit that grew organic impressions by 150%+ over 90 days.",
                "difficulty": "Intermediate"
            },
            {
                "title": "Multi-Channel Paid Acquisition Campaign Plan & ROAS Model",
                "description": "Complete media plan, audience segmentations, ad creative copies, and budget allocation model with target CAC/ROAS.",
                "difficulty": "Intermediate"
            },
            {
                "title": "Automated Email Lead Nurturing & Drip Sequence",
                "description": "5-stage behavioral trigger email workflow designed to convert freemium signups to paid subscribers.",
                "difficulty": "Foundational"
            }
        ],
        "salary_data": {
            "philippines": {
                "currency": "PHP",
                "entry_level": "\u20b1300,000 \u2013 \u20b1540,000 / year (\u20b125k - \u20b145k/mo)",
                "mid_level": "\u20b1600,000 \u2013 \u20b11,200,000 / year (\u20b150k - \u20b1100k/mo)",
                "senior_level": "\u20b11,200,000 \u2013 \u20b12,400,000+ / year (\u20b1100k - \u20b1200k+/mo)",
                "source": "JobStreet Philippines & Payscale Digital Marketing Benchmarks",
                "updated_at": "2026-Q1"
            },
            "global_usd": {
                "currency": "USD",
                "entry_level": "$55,000 \u2013 $75,000 / year",
                "mid_level": "$80,000 \u2013 $115,000 / year",
                "senior_level": "$120,000 \u2013 $170,000+ / year",
                "source": "U.S. Bureau of Labor Statistics (Market Research Analysts)",
                "updated_at": "2026-Q1"
            }
        },
        "learning_resources": [
            {
                "title": "Google Skillshop (Ads & Analytics Certification Courses)",
                "type": "Interactive Certification",
                "cost": "Free",
                "provider": "Google",
                "url": "https://skillshop.withgoogle.com/"
            },
            {
                "title": "HubSpot Academy Digital Marketing Courses",
                "type": "Comprehensive Guides",
                "cost": "Free",
                "provider": "HubSpot",
                "url": "https://academy.hubspot.com/"
            },
            {
                "title": "Moz Beginner's Guide to SEO",
                "type": "Open Documentation",
                "cost": "Free",
                "provider": "Moz",
                "url": "https://moz.com/beginners-guide-to-seo"
            }
        ],
        "related_careers": [
            "product-manager",
            "data-analyst",
            "technical-writer"
        ],
        "sources": [
            "Philippine Statistics Authority (PSOC 2431)",
            "Google Digital Growth Benchmarks",
            "U.S. BLS"
        ],
        "last_updated": "2026-09-01"
    },
    {
        "id": "registered-nurse",
        "title": "Registered Nurse & Clinical Specialist",
        "field": "Healthcare & Life Sciences",
        "category_id": "healthcare",
        "category_name": "Healthcare & Life Sciences",
        "psoc_code": "2221",
        "soc_code": "29-1141.00",
        "job_zone": 4,
        "tagline": "Deliver compassionate, life-saving patient care, clinical assessment, and health advocacy.",
        "description": "Registered Nurses provide direct patient care, administer medications, monitor clinical vital signs, collaborate with multidisciplinary medical teams, and educate patients and families on disease management and recovery.",
        "responsibilities": [
            "Perform comprehensive patient assessments, triage, and continuous vital sign monitoring",
            "Administer medications, IV therapies, and clinical treatments following strict medical protocols",
            "Maintain meticulous and confidential patient records in Electronic Health Record (EHR) systems",
            "Collaborate with physicians, pharmacists, and allied healthcare professionals to optimize care plans",
            "Educate patients and caregivers on post-discharge care, preventive health, and medication adherence"
        ],
        "riasec_traits": [
            "S",
            "I",
            "R"
        ],
        "work_style": "High-empathy, fast-paced clinical shifts, critical decision-making, and patient-first care.",
        "core_skills": [
            "Patient Care & Assessment",
            "Clinical Documentation",
            "Health Informatics & EHR",
            "Medication Administration",
            "Infection Control",
            "Emergency Triage",
            "Vital Signs Monitoring"
        ],
        "optional_skills": [
            "Critical Care (ICU) Nursing",
            "Pediatric Care",
            "Public Health Nursing",
            "Clinical Research Coordination",
            "BLS / ACLS Certification"
        ],
        "common_tools": [
            "Epic / Cerner EHR",
            "Vital Signs Monitors",
            "Infusion Pumps",
            "Glucometers",
            "Electronic Stethoscopes"
        ],
        "education_paths": [
            "Bachelor of Science in Nursing (BSN) \u2014 4-year accredited degree",
            "Passing the Philippine Nursing Licensure Examination (PNLE) administered by PRC",
            "NCLEX-RN certification for international / overseas clinical practice"
        ],
        "certifications": [
            {
                "name": "Philippine Registered Nurse License (PRC-RN)",
                "cost": "Official Board Exam",
                "provider": "Professional Regulation Commission (PRC)",
                "url": "https://www.prc.gov.ph"
            },
            {
                "name": "Basic Life Support (BLS) & Advanced Cardiac Life Support (ACLS)",
                "cost": "\u20b13,500 \u2013 \u20b16,000",
                "provider": "Philippine Heart Association / AHA",
                "url": "https://cpr.heart.org/"
            },
            {
                "name": "NCLEX-RN (US / International Licensure)",
                "cost": "$200 + International fee",
                "provider": "NCSBN",
                "url": "https://www.ncsbn.org/nclex.page"
            }
        ],
        "portfolio_projects": [
            {
                "title": "Evidence-Based Nursing Care Plan & Clinical Case Study",
                "description": "Detailed diagnosis, outcome identification, nursing interventions, and rationales for complex patient cases.",
                "difficulty": "Intermediate"
            },
            {
                "title": "Hospital Infection Prevention & Control Protocol Guide",
                "description": "Standardized hospital checklist and training deck adhering to WHO and DOH infection prevention guidelines.",
                "difficulty": "Foundational"
            },
            {
                "title": "Community Health Assessment & Family Wellness Program",
                "description": "Barangay health survey data analysis and actionable nutrition/vaccination educational outreach plan.",
                "difficulty": "Intermediate"
            }
        ],
        "salary_data": {
            "philippines": {
                "currency": "PHP",
                "entry_level": "\u20b1240,000 \u2013 \u20b1420,000 / year (\u20b120k - \u20b135k/mo)",
                "mid_level": "\u20b1450,000 \u2013 \u20b1720,000 / year (\u20b137k - \u20b160k/mo)",
                "senior_level": "\u20b1750,000 \u2013 \u20b11,400,000+ / year (\u20b162k - \u20b1115k+/mo)",
                "source": "DOH Salary Grade Tables & Private Hospital Benchmarks",
                "updated_at": "2026-Q1"
            },
            "global_usd": {
                "currency": "USD",
                "entry_level": "$60,000 \u2013 $75,000 / year",
                "mid_level": "$80,000 \u2013 $105,000 / year",
                "senior_level": "$110,000 \u2013 $145,000+ / year",
                "source": "U.S. Bureau of Labor Statistics (Registered Nurses)",
                "updated_at": "2026-Q1"
            }
        },
        "learning_resources": [
            {
                "title": "World Health Organization (WHO) Open Learning Channels",
                "type": "Clinical Open Courses",
                "cost": "Free",
                "provider": "WHO",
                "url": "https://openwho.org/"
            },
            {
                "title": "RegisteredNurseRN Clinical Guides & Video Lessons",
                "type": "Interactive Nursing Education",
                "cost": "Free",
                "provider": "RegisteredNurseRN",
                "url": "https://www.registerednursern.com/"
            },
            {
                "title": "Department of Health (DOH) Clinical Practice Guidelines",
                "type": "Statutory Healthcare Standards",
                "cost": "Free",
                "provider": "DOH Philippines",
                "url": "https://doh.gov.ph"
            }
        ],
        "related_careers": [
            "health-informatics-specialist",
            "secondary-educator"
        ],
        "sources": [
            "Philippine Statistics Authority (PSOC 2221)",
            "Professional Regulation Commission (PRC)",
            "U.S. BLS"
        ],
        "last_updated": "2026-09-01"
    },
    {
        "id": "civil-engineer",
        "title": "Civil Engineer & Infrastructure Project Lead",
        "field": "Engineering, Construction & Architecture",
        "category_id": "engineering",
        "category_name": "Engineering & Architecture",
        "psoc_code": "2142",
        "soc_code": "17-2051.00",
        "job_zone": 4,
        "tagline": "Design, inspect, and build resilient infrastructure, bridges, buildings, and transportation networks.",
        "description": "Civil Engineers plan, design, and supervise the construction and maintenance of building structures and public infrastructure including highways, water supply networks, bridges, and commercial complexes.",
        "responsibilities": [
            "Perform structural calculations, stress analyses, and geotechnical site evaluations",
            "Prepare detailed engineering drawings, architectural blueprints, and 3D BIM models",
            "Conduct quantity surveying, material cost estimations, and project procurement plans",
            "Supervise on-site construction activities ensuring compliance with National Building Code and safety standards",
            "Liaise with local government units (LGUs), environmental agencies, and project contractors"
        ],
        "riasec_traits": [
            "R",
            "I",
            "C"
        ],
        "work_style": "Rigorous engineering calculations, on-site field inspections, and multi-contractor coordination.",
        "core_skills": [
            "Structural Analysis",
            "AutoCAD",
            "Building Information Modeling (BIM)",
            "Quantity Surveying",
            "Project Scheduling",
            "Site Inspection & Quality Control",
            "National Building Code Compliance"
        ],
        "optional_skills": [
            "STAAD.Pro / ETABS",
            "Geotechnical Engineering",
            "Primavera P6 / MS Project",
            "Green Building Standards (LEED/BERDE)",
            "Hydrology & Drainage Design"
        ],
        "common_tools": [
            "AutoCAD",
            "ETABS",
            "STAAD.Pro",
            "Revit",
            "MS Project",
            "Total Station Surveying Tools"
        ],
        "education_paths": [
            "Bachelor of Science in Civil Engineering (BSCE) \u2014 4-year accredited degree",
            "Passing the Civil Engineering Licensure Examination administered by PRC",
            "Continuing Professional Development (CPD) accreditation through PICE"
        ],
        "certifications": [
            {
                "name": "Civil Engineer PRC Board License",
                "cost": "Official Board Exam",
                "provider": "Professional Regulation Commission (PRC)",
                "url": "https://www.prc.gov.ph"
            },
            {
                "name": "Autodesk Certified Professional in AutoCAD / Revit",
                "cost": "$150",
                "provider": "Autodesk / Certiport",
                "url": "https://www.autodesk.com/certification"
            },
            {
                "name": "DOLE Construction Occupational Safety & Health (COSH)",
                "cost": "\u20b14,000 \u2013 \u20b16,000",
                "provider": "DOLE-OSHC Accredited Centers",
                "url": "https://oshc.dole.gov.ph"
            }
        ],
        "portfolio_projects": [
            {
                "title": "Multi-Story Reinforced Concrete Building Structural Analysis",
                "description": "Full structural design report with seismic loads calculation, beam-column schedule, and ETABS model output.",
                "difficulty": "Advanced"
            },
            {
                "title": "Drainage System Master Plan & Flood Mitigation Model",
                "description": "Hydrological watershed calculations, pipe sizing, and retention basin design for a residential subdivision.",
                "difficulty": "Intermediate"
            },
            {
                "title": "Bill of Quantities (BOQ) & Detailed Cost Estimation",
                "description": "Comprehensive quantity take-off spreadsheet and material price analysis for a 2-story commercial structure.",
                "difficulty": "Foundational"
            }
        ],
        "salary_data": {
            "philippines": {
                "currency": "PHP",
                "entry_level": "\u20b1260,000 \u2013 \u20b1450,000 / year (\u20b122k - \u20b137k/mo)",
                "mid_level": "\u20b1500,000 \u2013 \u20b1960,000 / year (\u20b142k - \u20b180k/mo)",
                "senior_level": "\u20b11,000,000 \u2013 \u20b12,000,000+ / year (\u20b183k - \u20b1165k+/mo)",
                "source": "Philippine Institute of Civil Engineers (PICE) & JobStreet Benchmark",
                "updated_at": "2026-Q1"
            },
            "global_usd": {
                "currency": "USD",
                "entry_level": "$65,000 \u2013 $80,000 / year",
                "mid_level": "$88,000 \u2013 $120,000 / year",
                "senior_level": "$125,000 \u2013 $170,000+ / year",
                "source": "U.S. Bureau of Labor Statistics (Civil Engineers)",
                "updated_at": "2026-Q1"
            }
        },
        "learning_resources": [
            {
                "title": "MIT OpenCourseWare (Structural & Civil Engineering)",
                "type": "Open University Course",
                "cost": "Free",
                "provider": "MIT OCW",
                "url": "https://ocw.mit.edu/"
            },
            {
                "title": "Autodesk Design Academy (Revit & AutoCAD Tutorials)",
                "type": "Interactive 3D Tutorials",
                "cost": "Free",
                "provider": "Autodesk",
                "url": "https://www.autodesk.com/design-academy"
            },
            {
                "title": "National Building Code of the Philippines (PD 1096)",
                "type": "Statutory Standards Guide",
                "cost": "Free",
                "provider": "DPWH Philippines",
                "url": "https://www.dpwh.gov.ph"
            }
        ],
        "related_careers": [
            "commercial-electrician",
            "hvac-technician"
        ],
        "sources": [
            "Philippine Statistics Authority (PSOC 2142)",
            "Professional Regulation Commission (PRC)",
            "DPWH",
            "U.S. BLS"
        ],
        "last_updated": "2026-09-01"
    },
    {
        "id": "certified-public-accountant",
        "title": "Certified Public Accountant & Financial Auditor",
        "field": "Finance, Accounting & Economics",
        "category_id": "finance_accounting",
        "category_name": "Finance & Accounting",
        "psoc_code": "2411",
        "soc_code": "13-2011.00",
        "job_zone": 4,
        "tagline": "Ensure financial integrity, tax statutory compliance, auditing excellence, and corporate fiscal health.",
        "description": "Certified Public Accountants (CPAs) manage corporate financial records, prepare statutory financial statements, conduct internal/external audits, calculate corporate taxes, and provide strategic advisory to executives.",
        "responsibilities": [
            "Prepare monthly and year-end Balance Sheets, Income Statements, and Cash Flow Statements",
            "Ensure statutory tax compliance and filing with the Bureau of Internal Revenue (BIR)",
            "Perform rigorous financial auditing and test internal controls for risk mitigation",
            "Reconcile complex multi-currency bank accounts, general ledgers, and accounts payable/receivable",
            "Advise leadership on cost optimization, capital expenditure, and budgetary forecasting"
        ],
        "riasec_traits": [
            "C",
            "E",
            "I"
        ],
        "work_style": "High-precision financial compliance, systematic verification, and executive financial reporting.",
        "core_skills": [
            "Financial Accounting",
            "General Ledger Bookkeeping",
            "Tax Compliance (BIR)",
            "Financial Auditing",
            "Financial Statement Analysis",
            "Excel Financial Modeling",
            "Internal Controls"
        ],
        "optional_skills": [
            "QuickBooks / Xero / SAP",
            "IFRS / PFRS Standards",
            "Forensic Accounting",
            "Budgeting & Forecasting",
            "Corporate Finance"
        ],
        "common_tools": [
            "SAP ERP",
            "QuickBooks",
            "Xero",
            "Advanced MS Excel",
            "Taxumo / BIR eFPS",
            "AuditBoard"
        ],
        "education_paths": [
            "Bachelor of Science in Accountancy (BSA) \u2014 4-year accredited degree",
            "Passing the Certified Public Accountant Licensure Exam (CPALE) administered by PRC",
            "TESDA Bookkeeping NC III for foundational vocational bookkeeping track"
        ],
        "certifications": [
            {
                "name": "Certified Public Accountant (PRC-CPA License)",
                "cost": "Official Board Exam",
                "provider": "Professional Regulation Commission (PRC)",
                "url": "https://www.prc.gov.ph"
            },
            {
                "name": "TESDA Bookkeeping NC III",
                "cost": "Free / Subsidized",
                "provider": "TESDA Philippines",
                "url": "https://www.tesda.gov.ph"
            },
            {
                "name": "Certified Management Accountant (CMA)",
                "cost": "$400 \u2013 $800",
                "provider": "Institute of Management Accountants (IMA)",
                "url": "https://www.imanet.org"
            }
        ],
        "portfolio_projects": [
            {
                "title": "Complete 3-Statement Financial Model & Valuation Forecast",
                "description": "Integrated Income Statement, Balance Sheet, and DCF Valuation model in Excel with sensitivity analysis.",
                "difficulty": "Intermediate"
            },
            {
                "title": "Corporate BIR Tax Compliance & Audit Defense Documentation",
                "description": "Mock end-of-year tax return package with withholding tax schedules and deductible expense verification.",
                "difficulty": "Intermediate"
            },
            {
                "title": "Internal Controls Assessment & Risk Mitigation Matrix",
                "description": "Comprehensive audit checklist assessing procurement and payroll controls with remediation workflows.",
                "difficulty": "Foundational"
            }
        ],
        "salary_data": {
            "philippines": {
                "currency": "PHP",
                "entry_level": "\u20b1300,000 \u2013 \u20b1540,000 / year (\u20b125k - \u20b145k/mo)",
                "mid_level": "\u20b1600,000 \u2013 \u20b11,200,000 / year (\u20b150k - \u20b1100k/mo)",
                "senior_level": "\u20b11,300,000 \u2013 \u20b12,600,000+ / year (\u20b1108k - \u20b1215k+/mo)",
                "source": "Philippine Institute of Certified Public Accountants (PICPA) & JobStreet",
                "updated_at": "2026-Q1"
            },
            "global_usd": {
                "currency": "USD",
                "entry_level": "$60,000 \u2013 $78,000 / year",
                "mid_level": "$82,000 \u2013 $115,000 / year",
                "senior_level": "$125,000 \u2013 $180,000+ / year",
                "source": "U.S. Bureau of Labor Statistics (Accountants & Auditors)",
                "updated_at": "2026-Q1"
            }
        },
        "learning_resources": [
            {
                "title": "PICPA Professional Standards & CPD Webinars",
                "type": "Statutory Accounting Frameworks",
                "cost": "Free/Member",
                "provider": "PICPA",
                "url": "https://www.picpa.com.ph"
            },
            {
                "title": "AccountingCoach (Free Accounting & Bookkeeping Guides)",
                "type": "Interactive Explanations",
                "cost": "Free",
                "provider": "AccountingCoach",
                "url": "https://www.accountingcoach.com/"
            },
            {
                "title": "Corporate Finance Institute (CFI) Free Resources",
                "type": "Financial Modeling Templates",
                "cost": "Free",
                "provider": "CFI",
                "url": "https://corporatefinanceinstitute.com/"
            }
        ],
        "related_careers": [
            "data-analyst",
            "product-manager"
        ],
        "sources": [
            "Philippine Statistics Authority (PSOC 2411)",
            "PRC Board of Accountancy",
            "U.S. BLS"
        ],
        "last_updated": "2026-09-01"
    },
    {
        "id": "secondary-educator",
        "title": "High School STEM & Digital Skills Educator",
        "field": "Education, Teaching & Training",
        "category_id": "education",
        "category_name": "Education & Training",
        "psoc_code": "2330",
        "soc_code": "25-2031.00",
        "job_zone": 4,
        "tagline": "Inspire, teach, and equip the next generation of students with critical STEM and digital competencies.",
        "description": "Secondary Educators design and deliver engaging curricula in science, mathematics, technology, and humanities for junior and senior high school students, fostering critical thinking, student development, and digital literacy.",
        "responsibilities": [
            "Plan and execute daily lesson plans aligned with DepEd K-12 curriculum competencies",
            "Design formative and summative assessments, quizzes, and hands-on laboratory projects",
            "Manage classroom dynamics and facilitate collaborative learning environments",
            "Integrate Educational Technology (EdTech) and Learning Management Systems (LMS) into instruction",
            "Conduct parent-teacher conferences and provide individualized academic mentoring"
        ],
        "riasec_traits": [
            "S",
            "A",
            "I"
        ],
        "work_style": "Student-centered pedagogy, active classroom facilitation, mentorship, and creative lesson design.",
        "core_skills": [
            "Curriculum & Lesson Planning",
            "Classroom Management",
            "Educational Technology & LMS",
            "Student Assessment & Rubrics",
            "Pedagogical Content Knowledge",
            "Workshop Facilitation",
            "Public Speaking"
        ],
        "optional_skills": [
            "Differentiated Instruction",
            "Special Education Inclusivity",
            "STEM Project-Based Learning (PBL)",
            "Instructional Design",
            "Python for Education"
        ],
        "common_tools": [
            "Google Classroom",
            "Canvas LMS",
            "Canva for Education",
            "Kahoot / Quizizz",
            "MS Office 365",
            "Interactive Whiteboards"
        ],
        "education_paths": [
            "Bachelor of Secondary Education (BSEd) with major in Science, Math, or English",
            "Passing the Licensure Examination for Teachers (LET) administered by PRC",
            "Certificate in Professional Education (CPE) for non-education degree holders"
        ],
        "certifications": [
            {
                "name": "Professional Teacher PRC Board License (LET)",
                "cost": "Official Board Exam",
                "provider": "Professional Regulation Commission (PRC)",
                "url": "https://www.prc.gov.ph"
            },
            {
                "name": "Google Certified Educator (Level 1 & 2)",
                "cost": "$10 \u2013 $25",
                "provider": "Google for Education",
                "url": "https://edu.google.com/intl/ALL_us/for-educators/certification-programs/"
            },
            {
                "name": "Microsoft Certified Educator (MCE)",
                "cost": "$127",
                "provider": "Microsoft Education",
                "url": "https://learn.microsoft.com/en-us/credentials/certifications/microsoft-certified-educator/"
            }
        ],
        "portfolio_projects": [
            {
                "title": "10-Week Project-Based STEM Curriculum Module & Rubrics",
                "description": "Complete unit plan with inquiry-based learning activities, rubric criteria, and digital lab exercises.",
                "difficulty": "Intermediate"
            },
            {
                "title": "Interactive Digital Classroom & LMS Course Package",
                "description": "Structured Google Classroom / Canvas course shell containing modular quizzes, video guides, and peer reviews.",
                "difficulty": "Foundational"
            },
            {
                "title": "Student Learning Analytics & Remediation Intervention Plan",
                "description": "Data assessment tracking student performance metrics and tailored differentiated learning interventions.",
                "difficulty": "Intermediate"
            }
        ],
        "salary_data": {
            "philippines": {
                "currency": "PHP",
                "entry_level": "\u20b1324,000 \u2013 \u20b1480,000 / year (\u20b127k - \u20b140k/mo / DepEd Teacher I)",
                "mid_level": "\u20b1500,000 \u2013 \u20b1800,000 / year (\u20b141k - \u20b166k/mo)",
                "senior_level": "\u20b1850,000 \u2013 \u20b11,500,000+ / year (\u20b170k - \u20b1125k+/mo)",
                "source": "Department of Budget & Management (DBM) Salary Standardization Law & DepEd",
                "updated_at": "2026-Q1"
            },
            "global_usd": {
                "currency": "USD",
                "entry_level": "$48,000 \u2013 $62,000 / year",
                "mid_level": "$65,000 \u2013 $88,000 / year",
                "senior_level": "$92,000 \u2013 $120,000+ / year",
                "source": "U.S. Bureau of Labor Statistics (High School Teachers)",
                "updated_at": "2026-Q1"
            }
        },
        "learning_resources": [
            {
                "title": "DepEd Learning Resource Portal",
                "type": "Curriculum Standards & Modules",
                "cost": "Free",
                "provider": "Department of Education Philippines",
                "url": "https://lrmds.deped.gov.ph/"
            },
            {
                "title": "Khan Academy Teacher Toolkit",
                "type": "Interactive Learning Platform",
                "cost": "Free",
                "provider": "Khan Academy",
                "url": "https://www.khanacademy.org/resources/teacher-resources"
            },
            {
                "title": "Edutopia (George Lucas Educational Foundation)",
                "type": "Pedagogy & Classroom Strategies",
                "cost": "Free",
                "provider": "Edutopia",
                "url": "https://www.edutopia.org/"
            }
        ],
        "related_careers": [
            "technical-writer",
            "registered-nurse"
        ],
        "sources": [
            "Philippine Statistics Authority (PSOC 2330)",
            "Department of Education (DepEd)",
            "PRC Board of Professional Teachers",
            "U.S. BLS"
        ],
        "last_updated": "2026-09-01"
    },
    {
        "id": "commercial-electrician",
        "title": "Industrial & Commercial Electrician",
        "field": "Skilled Trades & Technical Services",
        "category_id": "skilled_trades",
        "category_name": "Skilled Trades & Technical Services",
        "psoc_code": "7411",
        "soc_code": "47-2111.00",
        "job_zone": 3,
        "tagline": "Install, maintain, and troubleshoot electrical power systems, industrial machinery, and smart grids.",
        "description": "Commercial & Industrial Electricians install, inspect, and repair electrical power, lighting, control systems, and machinery in commercial buildings, manufacturing plants, and industrial complexes following the Philippine Electrical Code.",
        "responsibilities": [
            "Read and interpret electrical blueprints, circuit schematics, and single-line diagrams",
            "Install electrical conduits, wiring harnesses, distribution panels, and switchgear equipment",
            "Perform preventive maintenance and electrical troubleshooting using digital multimeters and thermal scanners",
            "Ensure full compliance with the Philippine Electrical Code (PEC) and Occupational Safety standards",
            "Connect high-capacity electrical equipment, backup generators, and solar photovoltaic (PV) systems"
        ],
        "riasec_traits": [
            "R",
            "C",
            "I"
        ],
        "work_style": "Hands-on diagnostic precision, practical field safety protocols, and physical technical building.",
        "core_skills": [
            "Electrical Wiring & Installation",
            "Schematic & Blueprint Reading",
            "Preventive Maintenance",
            "Circuit Troubleshooting",
            "Multimeter & Diagnostic Testing",
            "Philippine Electrical Code (PEC)",
            "Lockout/Tagout Safety (LOTO)"
        ],
        "optional_skills": [
            "Solar PV System Installation",
            "Motor Controls & PLC Programming Basics",
            "Industrial Switchgear",
            "Thermal Imaging Inspection",
            "HVAC Electrical Systems"
        ],
        "common_tools": [
            "Digital Multimeter / Clamp Meter",
            "Conduit Bender",
            "Wire Strippers & Crimpers",
            "Megohmmeter (Megger)",
            "Thermal Imaging Camera",
            "Safety PPE"
        ],
        "education_paths": [
            "TESDA National Certificate: Electrical Installation & Maintenance NC II and NC III",
            "Registered Master Electrician (RME) Licensure Exam administered by PRC",
            "Associate degree in Electrical Engineering Technology"
        ],
        "certifications": [
            {
                "name": "TESDA Electrical Installation and Maintenance NC II & NC III",
                "cost": "Free / Subsidized",
                "provider": "TESDA Philippines",
                "url": "https://www.tesda.gov.ph"
            },
            {
                "name": "Registered Master Electrician (PRC-RME License)",
                "cost": "Official Board Exam",
                "provider": "Professional Regulation Commission (PRC)",
                "url": "https://www.prc.gov.ph"
            },
            {
                "name": "TESDA Solar PV Installation NC II",
                "cost": "Free / Subsidized",
                "provider": "TESDA Philippines",
                "url": "https://www.tesda.gov.ph"
            }
        ],
        "portfolio_projects": [
            {
                "title": "Commercial Panelboard Load Schedule & Single-Line Diagram",
                "description": "Complete electrical computation calculating total connected load, branch circuit breaker ratings, and main feeder sizing.",
                "difficulty": "Intermediate"
            },
            {
                "title": "Industrial Motor Control Circuit Wiring Prototype",
                "description": "Hands-on assembly of forward-reverse motor controller with overload protection and emergency stop switches.",
                "difficulty": "Intermediate"
            },
            {
                "title": "Grid-Tied Residential Solar Photovoltaic (PV) Layout Design",
                "description": "Solar panel string sizing, inverter matching, and AC/DC disconnect wiring schematic.",
                "difficulty": "Foundational"
            }
        ],
        "salary_data": {
            "philippines": {
                "currency": "PHP",
                "entry_level": "\u20b1220,000 \u2013 \u20b1360,000 / year (\u20b118k - \u20b130k/mo)",
                "mid_level": "\u20b1420,000 \u2013 \u20b1720,000 / year (\u20b135k - \u20b160k/mo)",
                "senior_level": "\u20b1780,000 \u2013 \u20b11,500,000+ / year (\u20b165k - \u20b1125k+/mo)",
                "source": "TESDA Placement Data & IIEE Industry Salary Benchmarks",
                "updated_at": "2026-Q1"
            },
            "global_usd": {
                "currency": "USD",
                "entry_level": "$50,000 \u2013 $65,000 / year",
                "mid_level": "$70,000 \u2013 $95,000 / year",
                "senior_level": "$100,000 \u2013 $135,000+ / year",
                "source": "U.S. Bureau of Labor Statistics (Electricians)",
                "updated_at": "2026-Q1"
            }
        },
        "learning_resources": [
            {
                "title": "TESDA EIM Online Training Modules",
                "type": "TVET Practical Modules",
                "cost": "Free",
                "provider": "e-TESDA Portal",
                "url": "https://e-tesda.gov.ph/"
            },
            {
                "title": "All About Circuits (Open Electrical Textbook)",
                "type": "Open Technical Reference",
                "cost": "Free",
                "provider": "All About Circuits",
                "url": "https://www.allaboutcircuits.com/"
            },
            {
                "title": "Institute of Integrated Electrical Engineers (IIEE) Standards",
                "type": "Professional Standards",
                "cost": "Free/Member",
                "provider": "IIEE Philippines",
                "url": "https://iiee.org.ph"
            }
        ],
        "related_careers": [
            "civil-engineer",
            "devops-engineer"
        ],
        "sources": [
            "Philippine Statistics Authority (PSOC 7411)",
            "TESDA Training Regulations",
            "PRC Board of Electrical Engineering",
            "U.S. BLS"
        ],
        "last_updated": "2026-09-01"
    }
]
