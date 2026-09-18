"""
Seed Knowledge Base for TO BE Career Platform.
Contains structured data for 20+ technology and related careers with realistic salary benchmarks (PH & Global),
curated free and low-cost learning resources, portfolio projects, and certifications.
"""

from typing import List, Dict, Any

CAREER_CATEGORIES = [
    {"id": "development", "name": "Software & Web Development", "icon": "💻"},
    {"id": "design", "name": "UI/UX & Product Design", "icon": "🎨"},
    {"id": "data_ai", "name": "Data, Analytics & AI", "icon": "📊"},
    {"id": "cloud_security", "name": "Cloud, DevOps & Cybersecurity", "icon": "🛡️"},
    {"id": "product_management", "name": "Product & Tech Strategy", "icon": "🚀"}
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
        "riasec_traits": ["A", "I", "R"],
        "work_style": "Project-based, collaborative with designers, balanced with independent coding flow.",
        "core_skills": ["HTML5", "CSS3", "JavaScript", "React", "TypeScript", "Responsive Design", "Git & GitHub", "REST APIs"],
        "optional_skills": ["Next.js", "Tailwind CSS", "Web Accessibility (a11y)", "GraphQL", "Performance Optimization", "Unit Testing (Jest/Vitest)"],
        "common_tools": ["VS Code", "Figma", "Chrome DevTools", "GitHub", "Vercel / Netlify", "npm/pnpm"],
        "education_paths": [
            "Self-taught through structured open-source curricula and interactive platforms (very common)",
            "Coding bootcamps focusing on modern full-stack / front-end workflows",
            "Bachelor's degree in Computer Science, Information Technology, or related discipline"
        ],
        "certifications": [
            {"name": "freeCodeCamp Responsive Web Design Certification", "cost": "Free", "provider": "freeCodeCamp", "url": "https://www.freecodecamp.org/learn/2022/responsive-web-design/"},
            {"name": "freeCodeCamp JavaScript Algorithms and Data Structures", "cost": "Free", "provider": "freeCodeCamp", "url": "https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures-v8/"},
            {"name": "Meta Front-End Developer Professional Certificate", "cost": "Low-cost (Coursera FinAid Available)", "provider": "Coursera / Meta", "url": "https://www.coursera.org/professional-certificates/meta-front-end-developer"}
        ],
        "portfolio_projects": [
            {"title": "Accessible Portfolio Website", "description": "High-performance personal website featuring light/dark mode, semantic HTML, keyboard navigation, and WCAG AA contrast.", "difficulty": "Foundational"},
            {"title": "Real-time Weather & Geo Dashboard", "description": "Interactive dashboard fetching live weather data, forecasts, and air quality using OpenWeather API with responsive chart visualizations.", "difficulty": "Intermediate"},
            {"title": "Full-Featured E-Commerce / SaaS UI with Cart & State Management", "description": "Production-ready store frontend featuring product filtering, checkout flow, custom state hooks, and optimistic UI updates.", "difficulty": "Advanced"}
        ],
        "salary_data": {
            "philippines": {
                "currency": "PHP",
                "entry_level": "₱300,000 – ₱540,000 / year (₱25k - ₱45k/mo)",
                "mid_level": "₱600,000 – ₱1,200,000 / year (₱50k - ₱100k/mo)",
                "senior_level": "₱1,200,000 – ₱2,400,000+ / year (₱100k - ₱200k+/mo)",
                "source": "Payscale PH, JobStreet Philippines Tech Salary Benchmarks",
                "updated_at": "2026-Q1"
            },
            "global_usd": {
                "currency": "USD",
                "entry_level": "$65,000 – $85,000 / year",
                "mid_level": "$90,000 – $130,000 / year",
                "senior_level": "$140,000 – $190,000+ / year",
                "source": "Levels.fyi, US Bureau of Labor Statistics (Web Developers)",
                "updated_at": "2026-Q1"
            }
        },
        "learning_resources": [
            {"title": "MDN Web Docs (Mozilla)", "type": "Documentation & Guides", "cost": "Free", "provider": "Mozilla", "url": "https://developer.mozilla.org/"},
            {"title": "The Odin Project (Full Stack JavaScript)", "type": "Structured Curriculum", "cost": "Free", "provider": "The Odin Project", "url": "https://www.theodinproject.com/"},
            {"title": "React Official Documentation", "type": "Interactive Tutorial", "cost": "Free", "provider": "React Team", "url": "https://react.dev/"}
        ],
        "related_careers": ["fullstack-developer", "ux-engineer", "ui-designer", "mobile-app-developer"],
        "sources": ["MDN Developer Network", "U.S. Bureau of Labor Statistics", "Payscale", "Levels.fyi"],
        "last_updated": "2026-09-01"
    },
    {
        "id": "ux-designer",
        "title": "UX Designer",
        "field": "Design & User Experience",
        "category_id": "design",
        "category_name": "UI/UX & Product Design",
        "tagline": "Understand human behavior to design intuitive, seamless digital product experiences.",
        "description": "User Experience (UX) Designers research how people interact with products, uncover pain points, and craft intuitive workflows, information architecture, wireframes, and prototypes that make digital tools effortless and enjoyable.",
        "responsibilities": [
            "Conduct qualitative user interviews, usability testing, and surveys to identify pain points",
            "Create user personas, journey maps, user flows, and site architectures",
            "Produce low-fidelity wireframes and interactive clickable prototypes in Figma",
            "Collaborate closely with product managers and engineers to ensure design feasibility",
            "Iterate designs based on quantitative product analytics and qualitative user feedback"
        ],
        "riasec_traits": ["A", "I", "S"],
        "work_style": "Human-centered, investigative research, creative problem-solving, and cross-team communication.",
        "core_skills": ["UX Research", "Figma", "Wireframing", "Prototyping", "Information Architecture", "Usability Testing", "User Empathy"],
        "optional_skills": ["Design Systems", "Interaction Design", "UI Design", "HTML/CSS Basics", "Product Analytics", "Workshop Facilitation"],
        "common_tools": ["Figma", "FigJam", "Miro", "Maze", "Notion", "Hotjar"],
        "education_paths": [
            "Degrees in Human-Computer Interaction (HCI), Psychology, Graphic Design, Multimedia Arts, or Computer Science",
            "Self-directed portfolio learning and apprenticeship",
            "UX/UI design bootcamps with hands-on client case studies"
        ],
        "certifications": [
            {"name": "Google UX Design Professional Certificate", "cost": "Low-cost (Coursera FinAid Available)", "provider": "Coursera / Google", "url": "https://www.coursera.org/professional-certificates/google-ux-design"},
            {"name": "Interaction Design Foundation (IxDF) Courses", "cost": "Low-cost Student Membership", "provider": "IxDF", "url": "https://www.interaction-design.org/"}
        ],
        "portfolio_projects": [
            {"title": "Mobile App Redesign Case Study", "description": "End-to-end UX case study identifying usability friction in a transit or banking app, complete with user interviews, journey maps, and tested prototypes.", "difficulty": "Foundational"},
            {"title": "Accessible Healthcare / Telehealth Booking Flow", "description": "Designing an accessible appointment booking flow for seniors and diverse ability groups, focusing on WCAG contrast and cognitive load reduction.", "difficulty": "Intermediate"},
            {"title": "Multi-Platform B2B SaaS Workflow & Design System", "description": "Comprehensive design system with reusable components, documentation tokens, and complex multi-step data table workflows.", "difficulty": "Advanced"}
        ],
        "salary_data": {
            "philippines": {
                "currency": "PHP",
                "entry_level": "₱360,000 – ₱600,000 / year (₱30k - ₱50k/mo)",
                "mid_level": "₱720,000 – ₱1,320,000 / year (₱60k - ₱110k/mo)",
                "senior_level": "₱1,440,000 – ₱2,600,000+ / year (₱120k - ₱215k+/mo)",
                "source": "Payscale PH, UX Philippines Industry Compensation Survey",
                "updated_at": "2026-Q1"
            },
            "global_usd": {
                "currency": "USD",
                "entry_level": "$70,000 – $92,000 / year",
                "mid_level": "$98,000 – $140,000 / year",
                "senior_level": "$145,000 – $205,000+ / year",
                "source": "Levels.fyi, Nielsen Norman Group Salary Reports",
                "updated_at": "2026-Q1"
            }
        },
        "learning_resources": [
            {"title": "Nielsen Norman Group Free UX Articles & Videos", "type": "Research & Best Practices", "cost": "Free", "provider": "NN/g", "url": "https://www.nngroup.com/articles/"},
            {"title": "Figma Learn and Design Fundamentals", "type": "Interactive Guides", "cost": "Free", "provider": "Figma", "url": "https://help.figma.com/hc/en-us/categories/360002051613"},
            {"title": "LawsofUX.com (Psychological UX Principles)", "type": "Reference Guide", "cost": "Free", "provider": "Jon Yablonski", "url": "https://lawsofux.com/"}
        ],
        "related_careers": ["product-designer", "ui-designer", "ux-engineer", "product-manager"],
        "sources": ["Nielsen Norman Group", "Interaction Design Foundation", "Levels.fyi", "UXPH"],
        "last_updated": "2026-09-01"
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
        "riasec_traits": ["I", "R", "A"],
        "work_style": "Holistic system builder, deep problem solver, adaptable across different tech stack tiers.",
        "core_skills": ["JavaScript/TypeScript", "Python or Node.js", "React or Vue", "SQL & Database Design", "REST APIs", "Git", "HTML/CSS"],
        "optional_skills": ["PostgreSQL", "Docker", "Next.js", "Tailwind CSS", "Redis", "Cloud Deployment (AWS/Vercel/Supabase)", "CI/CD"],
        "common_tools": ["VS Code", "Postman", "Docker Desktop", "Supabase / DBeaver", "GitHub", "Linux CLI"],
        "education_paths": [
            "Bachelor's in Computer Science, Software Engineering, or Information Systems",
            "Full-Stack coding bootcamps with portfolio capstones",
            "Self-taught via open-source curricula (Odin Project, Full Stack Open)"
        ],
        "certifications": [
            {"name": "Full Stack Open (University of Helsinki)", "cost": "Free", "provider": "University of Helsinki", "url": "https://fullstackopen.com/en/"},
            {"name": "AWS Certified Cloud Practitioner", "cost": "$100 (Exam fee)", "provider": "Amazon Web Services", "url": "https://aws.amazon.com/certification/certified-cloud-practitioner/"}
        ],
        "portfolio_projects": [
            {"title": "Full-Stack Collaborative Workspace / Task Management App", "description": "Interactive web app with user authentication, real-time board updates, PostgreSQL persistence, and role-based permissions.", "difficulty": "Intermediate"},
            {"title": "Community Market Platform with Payments & Media Uploads", "description": "Multi-vendor platform featuring item search, filter, cloud image uploads, Stripe/PayMongo sandbox checkout, and transactional emails.", "difficulty": "Advanced"},
            {"title": "AI-Enhanced Knowledge Base & Note Taking SaaS", "description": "Full-stack SaaS application with markdown editor, semantic tagging, Supabase PostgreSQL with RLS, and Stripe subscription tiering.", "difficulty": "Advanced"}
        ],
        "salary_data": {
            "philippines": {
                "currency": "PHP",
                "entry_level": "₱360,000 – ₱600,000 / year (₱30k - ₱50k/mo)",
                "mid_level": "₱720,000 – ₱1,500,000 / year (₱60k - ₱125k/mo)",
                "senior_level": "₱1,500,000 – ₱3,000,000+ / year (₱125k - ₱250k+/mo)",
                "source": "Payscale PH, NodeFlair SEA Tech Salary Report",
                "updated_at": "2026-Q1"
            },
            "global_usd": {
                "currency": "USD",
                "entry_level": "$75,000 – $95,000 / year",
                "mid_level": "$105,000 – $145,000 / year",
                "senior_level": "$150,000 – $215,000+ / year",
                "source": "Levels.fyi, Stack Overflow Developer Survey",
                "updated_at": "2026-Q1"
            }
        },
        "learning_resources": [
            {"title": "Full Stack Open (React, Redux, Node.js, MongoDB, GraphQL, TypeScript)", "type": "Comprehensive Course", "cost": "Free", "provider": "University of Helsinki", "url": "https://fullstackopen.com/en/"},
            {"title": "CS50's Web Programming with Python and JavaScript", "type": "University Course", "cost": "Free", "provider": "Harvard University (edX)", "url": "https://cs50.harvard.edu/web/"},
            {"title": "Supabase Documentation & PostgreSQL Guides", "type": "Database Guides", "cost": "Free", "provider": "Supabase", "url": "https://supabase.com/docs"}
        ],
        "related_careers": ["frontend-developer", "backend-developer", "devops-engineer", "cloud-engineer"],
        "sources": ["Stack Overflow Developer Survey", "Levels.fyi", "NodeFlair", "Payscale"],
        "last_updated": "2026-09-01"
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
        "riasec_traits": ["I", "C", "S"],
        "work_style": "Analytical investigation, structured data modeling, and consultative storytelling.",
        "core_skills": ["SQL", "Data Analysis", "Tableau or Power BI", "Excel / Spreadsheets", "Data Visualization", "Critical Thinking"],
        "optional_skills": ["Python (Pandas/Matplotlib)", "Statistics", "Data Cleaning", "Business Intelligence", "ETL Basics", "A/B Testing"],
        "common_tools": ["SQL Server / PostgreSQL", "Power BI", "Tableau", "Excel", "Jupyter Notebooks", "Google Sheets"],
        "education_paths": [
            "Degree in Statistics, Mathematics, Economics, Information Systems, Business, or Computer Science",
            "Professional data analytics certificates and guided portfolio projects",
            "Transition from finance, operations, or marketing analytics"
        ],
        "certifications": [
            {"name": "Google Data Analytics Professional Certificate", "cost": "Low-cost (Coursera FinAid Available)", "provider": "Coursera / Google", "url": "https://www.coursera.org/professional-certificates/google-data-analytics"},
            {"name": "Microsoft Certified: Power BI Data Analyst Associate (PL-300)", "cost": "$165 (Exam fee)", "provider": "Microsoft", "url": "https://learn.microsoft.com/en-us/credentials/certifications/data-analyst-associate/"}
        ],
        "portfolio_projects": [
            {"title": "Public Health or Economic Trend Dashboard", "description": "Cleaned open government/WHO datasets analyzed with SQL and displayed via an interactive Power BI / Tableau public dashboard.", "difficulty": "Foundational"},
            {"title": "E-Commerce Customer Retention & Cohort Analysis", "description": "SQL-driven exploratory analysis calculating churn rates, customer lifetime value (LTV), and seasonal purchase patterns.", "difficulty": "Intermediate"},
            {"title": "Real-World Business KPI Pipeline with Automated Reporting", "description": "End-to-end analytics workflow combining raw CSV/API ingestion, automated Python data transformation, and scheduled KPI visualizations.", "difficulty": "Advanced"}
        ],
        "salary_data": {
            "philippines": {
                "currency": "PHP",
                "entry_level": "₱300,000 – ₱480,000 / year (₱25k - ₱40k/mo)",
                "mid_level": "₱540,000 – ₱1,080,000 / year (₱45k - ₱90k/mo)",
                "senior_level": "₱1,200,000 – ₱2,100,000+ / year (₱100k - ₱175k+/mo)",
                "source": "Payscale PH, Analytics Association of the Philippines",
                "updated_at": "2026-Q1"
            },
            "global_usd": {
                "currency": "USD",
                "entry_level": "$62,000 – $80,000 / year",
                "mid_level": "$85,000 – $115,000 / year",
                "senior_level": "$120,000 – $160,000+ / year",
                "source": "Levels.fyi, US BLS (Operations & Data Analysts)",
                "updated_at": "2026-Q1"
            }
        },
        "learning_resources": [
            {"title": "Kaggle Micro-Courses (Python, Pandas, SQL, Data Visualization)", "type": "Interactive Coding", "cost": "Free", "provider": "Kaggle", "url": "https://www.kaggle.com/learn"},
            {"title": "SQLBolt - Learn SQL with simple, interactive exercises", "type": "Interactive Tutorial", "cost": "Free", "provider": "SQLBolt", "url": "https://sqlbolt.com/"},
            {"title": "Microsoft Learn Power BI Learning Path", "type": "Official Guides", "cost": "Free", "provider": "Microsoft", "url": "https://learn.microsoft.com/en-us/training/powerplatform/power-bi"}
        ],
        "related_careers": ["data-scientist", "business-analyst", "product-manager", "database-administrator"],
        "sources": ["U.S. Bureau of Labor Statistics", "Payscale", "Analytics Association of the Philippines", "Levels.fyi"],
        "last_updated": "2026-09-01"
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
        "riasec_traits": ["I", "R", "C"],
        "work_style": "Vigilant, systematic, investigative problem-solving with high attention to detail.",
        "core_skills": ["Networking Fundamentals (TCP/IP, DNS)", "Linux/Unix Commands", "Security Principles", "Vulnerability Scanning", "Incident Response"],
        "optional_skills": ["Python / Bash Scripting", "SIEM Tools (Splunk/Wazuh)", "Wireshark", "Cloud Security (AWS/Azure)", "Ethical Hacking", "Threat Hunting"],
        "common_tools": ["Wireshark", "Nmap", "Splunk", "Burp Suite", "Kali Linux", "Wazuh / Elastic SIEM"],
        "education_paths": [
            "Degree in Cybersecurity, Information Technology, Computer Engineering, or Computer Science",
            "Industry standard vendor-neutral certifications and hands-on capture-the-flag (CTF) labs",
            "Transition from IT Helpdesk, Network Administration, or Systems Administration"
        ],
        "certifications": [
            {"name": "CompTIA Security+ (SY0-701)", "cost": "$392 (Exam fee, student discounts available)", "provider": "CompTIA", "url": "https://www.comptia.org/certifications/security"},
            {"name": "Google Cybersecurity Professional Certificate", "cost": "Low-cost (Coursera FinAid Available)", "provider": "Coursera / Google", "url": "https://www.coursera.org/professional-certificates/google-cybersecurity"},
            {"name": "ISC2 Certified in Cybersecurity (CC)", "cost": "Free Exam via One Million Certified in Cybersecurity campaign", "provider": "ISC2", "url": "https://www.isc2.org/landing/1mcc"}
        ],
        "portfolio_projects": [
            {"title": "Home Lab Virtual Network & SIEM Setup", "description": "Configuring a dedicated virtual home lab with pfSense firewall, Linux/Windows endpoints, and an open-source SIEM (Wazuh/Splunk) to analyze attack logs.", "difficulty": "Foundational"},
            {"title": "Network Traffic Analysis & Malware Packet Triage", "description": "Documented packet capture (pcap) investigation using Wireshark to identify C2 beaconing, port scans, and credential exfiltration.", "difficulty": "Intermediate"},
            {"title": "Comprehensive Vulnerability Assessment & Hardening Report", "description": "Conducting an authorized vulnerability assessment against a test environment (e.g. Metasploitable) and writing an executive remediation report.", "difficulty": "Advanced"}
        ],
        "salary_data": {
            "philippines": {
                "currency": "PHP",
                "entry_level": "₱360,000 – ₱540,000 / year (₱30k - ₱45k/mo)",
                "mid_level": "₱660,000 – ₱1,320,000 / year (₱55k - ₱110k/mo)",
                "senior_level": "₱1,440,000 – ₱2,800,000+ / year (₱120k - ₱230k+/mo)",
                "source": "Payscale PH, Philippine Information Security Association",
                "updated_at": "2026-Q1"
            },
            "global_usd": {
                "currency": "USD",
                "entry_level": "$72,000 – $90,000 / year",
                "mid_level": "$95,000 – $135,000 / year",
                "senior_level": "$145,000 – $195,000+ / year",
                "source": "Levels.fyi, US BLS (Information Security Analysts)",
                "updated_at": "2026-Q1"
            }
        },
        "learning_resources": [
            {"title": "TryHackMe (Pre-Security & Cyber Defense Paths)", "type": "Hands-on Gamified Labs", "cost": "Free Tier & Low-cost Student Plan", "provider": "TryHackMe", "url": "https://tryhackme.com/"},
            {"title": "OverTheWire Wargames (Bandit Linux Basics)", "type": "Terminal Practice", "cost": "Free", "provider": "OverTheWire", "url": "https://overthewire.org/wargames/"},
            {"title": "Professor Messer CompTIA Security+ Training Course", "type": "Video Lecture Series", "cost": "Free", "provider": "Professor Messer", "url": "https://www.professormesser.com/security-plus/sy0-701/sy0-701-video/sy0-701-training-course/"}
        ],
        "related_careers": ["cloud-engineer", "devops-engineer", "software-engineer", "database-administrator"],
        "sources": ["U.S. Bureau of Labor Statistics", "CompTIA", "ISC2 Cybersecurity Workforce Study", "Payscale"],
        "last_updated": "2026-09-01"
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
        "riasec_traits": ["R", "I", "C"],
        "work_style": "Systematic, architecture-focused, automated problem-solving with high autonomy.",
        "core_skills": ["Cloud Platforms (AWS/GCP/Azure)", "Linux Administration", "Networking Fundamentals", "Infrastructure as Code (Terraform)", "Git & GitHub"],
        "optional_skills": ["Docker", "Kubernetes", "Python / Bash Scripting", "CI/CD Pipelines", "Serverless Architecture", "Cloud Security"],
        "common_tools": ["AWS Console / CLI", "Terraform", "Docker", "Linux Terminal", "Datadog / CloudWatch", "GitHub Actions"],
        "education_paths": [
            "Bachelor's degree in Computer Science, IT, Computer Engineering, or related technical fields",
            "Industry cloud certifications combined with verifiable GitHub infrastructure projects",
            "Transition from Systems Administrator or Network Engineer roles"
        ],
        "certifications": [
            {"name": "AWS Certified Solutions Architect – Associate", "cost": "$150 (Exam fee)", "provider": "Amazon Web Services", "url": "https://aws.amazon.com/certification/certified-solutions-architect-associate/"},
            {"name": "Google Cloud Associate Cloud Engineer", "cost": "$125 (Exam fee)", "provider": "Google Cloud", "url": "https://cloud.google.com/learn/certification/cloud-engineer"},
            {"name": "HashiCorp Certified: Terraform Associate", "cost": "$70 (Exam fee)", "provider": "HashiCorp", "url": "https://www.hashicorp.com/certification/terraform-associate"}
        ],
        "portfolio_projects": [
            {"title": "High-Availability Multi-Tier Web Architecture on AWS", "description": "Deploying a resilient VPC with public/private subnets, Auto Scaling EC2 instances, Application Load Balancer, and RDS PostgreSQL.", "difficulty": "Foundational"},
            {"title": "Infrastructure as Code (Terraform) Cloud Deployment", "description": "Writing modular Terraform scripts to provision an entire cloud environment with automated state management in an S3 bucket.", "difficulty": "Intermediate"},
            {"title": "Serverless Event-Driven Processing Pipeline", "description": "Building an automated pipeline using AWS Lambda / Google Cloud Functions, SQS/PubSub queues, and DynamoDB/Firestore to process incoming files.", "difficulty": "Advanced"}
        ],
        "salary_data": {
            "philippines": {
                "currency": "PHP",
                "entry_level": "₱420,000 – ₱660,000 / year (₱35k - ₱55k/mo)",
                "mid_level": "₱780,000 – ₱1,560,000 / year (₱65k - ₱130k/mo)",
                "senior_level": "₱1,680,000 – ₱3,200,000+ / year (₱140k - ₱265k+/mo)",
                "source": "Payscale PH, JobStreet Tech Compensation Reports",
                "updated_at": "2026-Q1"
            },
            "global_usd": {
                "currency": "USD",
                "entry_level": "$80,000 – $100,000 / year",
                "mid_level": "$110,000 – $155,000 / year",
                "senior_level": "$160,000 – $220,000+ / year",
                "source": "Levels.fyi, Robert Half Technology Salary Guide",
                "updated_at": "2026-Q1"
            }
        },
        "learning_resources": [
            {"title": "AWS Skill Builder Free Digital Training", "type": "Official Self-Paced Courses", "cost": "Free", "provider": "Amazon Web Services", "url": "https://explore.skillbuilder.aws/"},
            {"title": "Google Cloud Free Tier & Architecture Center", "type": "Cloud Sandbox & Best Practices", "cost": "Free Sandbox Allowance", "provider": "Google Cloud", "url": "https://cloud.google.com/architecture"},
            {"title": "Terraform Official Tutorials (HashiCorp Learn)", "type": "Interactive Guides", "cost": "Free", "provider": "HashiCorp", "url": "https://developer.hashicorp.com/terraform/tutorials"}
        ],
        "related_careers": ["devops-engineer", "cybersecurity-analyst", "fullstack-developer", "database-administrator"],
        "sources": ["Amazon Web Services", "Google Cloud", "Levels.fyi", "Payscale"],
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
        "riasec_traits": ["E", "S", "I"],
        "work_style": "Strategic leadership, high cross-functional collaboration, empathetic problem-solving.",
        "core_skills": ["Product Strategy", "User Research & Empathy", "Agile / Scrum", "Roadmapping", "Communication", "Data-Driven Decision Making"],
        "optional_skills": ["Technical Fluency (APIs/Databases)", "SQL Basics", "A/B Testing", "Financial Modeling", "Figma Basics", "Go-to-Market (GTM)"],
        "common_tools": ["Jira / Linear", "Notion", "Mixpanel / Amplitude", "Figma", "Slack", "Productboard"],
        "education_paths": [
            "Diverse backgrounds: Business Administration, Computer Science, Engineering, Economics, or Communications",
            "Product management certificates and case study teardowns",
            "Transition from software engineering, UX design, data analysis, or project management"
        ],
        "certifications": [
            {"name": "University of Virginia: Digital Product Management Specialization", "cost": "Low-cost (Coursera FinAid Available)", "provider": "Coursera / Darden School of Business", "url": "https://www.coursera.org/specializations/uva-darden-digital-product-management"},
            {"name": "Scrum Alliance Certified Scrum Product Owner (CSPO)", "cost": "$400 – $600 (Course fee)", "provider": "Scrum Alliance", "url": "https://www.scrumalliance.org/get-certified/product-owner-track/certified-scrum-product-owner"}
        ],
        "portfolio_projects": [
            {"title": "Product Teardown & Redesign Proposal", "description": "Thorough analysis of an existing consumer or B2B product, evaluating its user friction, metrics, unit economics, and proposing a feature teardown.", "difficulty": "Foundational"},
            {"title": "Comprehensive Product Requirement Document (PRD)", "description": "End-to-end PRD for a new digital product concept featuring user personas, edge cases, system flowcharts, launch milestones, and risk matrix.", "difficulty": "Intermediate"},
            {"title": "0-to-1 Product Launch Strategy & Metrics Framework", "description": "Complete product discovery artifact including user interview synthesis, wireframes, North Star metric definition, and Go-To-Market plan.", "difficulty": "Advanced"}
        ],
        "salary_data": {
            "philippines": {
                "currency": "PHP",
                "entry_level": "₱480,000 – ₱720,000 / year (₱40k - ₱60k/mo)",
                "mid_level": "₱840,000 – ₱1,800,000 / year (₱70k - ₱150k/mo)",
                "senior_level": "₱1,920,000 – ₱3,600,000+ / year (₱160k - ₱300k+/mo)",
                "source": "Payscale PH, Product Leaders PH Salary Benchmarks",
                "updated_at": "2026-Q1"
            },
            "global_usd": {
                "currency": "USD",
                "entry_level": "$85,000 – $110,000 / year",
                "mid_level": "$120,000 – $165,000 / year",
                "senior_level": "$175,000 – $240,000+ / year",
                "source": "Levels.fyi, Product Management Salary Survey",
                "updated_at": "2026-Q1"
            }
        },
        "learning_resources": [
            {"title": "Reforge Product Briefs & Thought Leadership", "type": "Industry Essays", "cost": "Free Articles Available", "provider": "Reforge", "url": "https://www.reforge.com/blog"},
            {"title": "Lenny's Newsletter & Podcast (Product & Growth)", "type": "Practitioner Guides", "cost": "Free & Paid Substack", "provider": "Lenny Rachitsky", "url": "https://www.lennysnewsletter.com/"},
            {"title": "Mind the Product Free Content Library", "type": "Community Talks & Articles", "cost": "Free", "provider": "Mind the Product", "url": "https://www.mindtheproduct.com/"}
        ],
        "related_careers": ["ux-designer", "data-analyst", "product-designer", "business-analyst"],
        "sources": ["Levels.fyi", "Mind the Product", "Product School", "Payscale"],
        "last_updated": "2026-09-01"
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
        "riasec_traits": ["I", "R", "C"],
        "work_style": "Mathematical rigor, experimental research, deep coding, and continuous learning.",
        "core_skills": ["Python", "Machine Learning Fundamentals", "PyTorch or TensorFlow", "Data Preprocessing", "Git", "Math & Linear Algebra"],
        "optional_skills": ["LLM Engineering / RAG", "Docker", "Hugging Face", "MLOps (MLflow/Kubeflow)", "FastAPI", "Vector Databases", "Cloud ML Platforms"],
        "common_tools": ["Jupyter Lab", "PyTorch", "Hugging Face Hub", "FastAPI", "Docker", "Weights & Biases"],
        "education_paths": [
            "Bachelor's or Master's in Computer Science, AI, Data Science, Electrical Engineering, or Physics",
            "Applied machine learning self-study paths and competitive Kaggle portfolios",
            "Software engineers transitioning into AI engineering through applied projects"
        ],
        "certifications": [
            {"name": "DeepLearning.AI Deep Learning Specialization", "cost": "Low-cost (Coursera FinAid Available)", "provider": "Coursera / DeepLearning.AI", "url": "https://www.coursera.org/specializations/deep-learning"},
            {"name": "DeepLearning.AI Generative AI with Large Language Models", "cost": "Low-cost (Coursera FinAid Available)", "provider": "Coursera / AWS", "url": "https://www.coursera.org/learn/generative-ai-with-llms"},
            {"name": "TensorFlow Developer Certificate (or AWS ML Specialty)", "cost": "$100 – $300 (Exam fee)", "provider": "Google / AWS", "url": "https://www.tensorflow.org/certificate"}
        ],
        "portfolio_projects": [
            {"title": "Predictive Classification / Regression Model on Tabular Data", "description": "End-to-end exploratory analysis, feature engineering, model tuning with XGBoost, and performance metrics evaluation on a real-world dataset.", "difficulty": "Foundational"},
            {"title": "Computer Vision or NLP Classification API with FastAPI & Docker", "description": "Trained PyTorch image classifier or sentiment analysis model wrapped in a high-performance REST API containerized with Docker.", "difficulty": "Intermediate"},
            {"title": "Production RAG System with Vector Search & Evaluation Suite", "description": "Production retrieval-augmented generation system parsing domain documents, generating embeddings, querying PostgreSQL pgvector, and benchmarking accuracy.", "difficulty": "Advanced"}
        ],
        "salary_data": {
            "philippines": {
                "currency": "PHP",
                "entry_level": "₱480,000 – ₱780,000 / year (₱40k - ₱65k/mo)",
                "mid_level": "₱900,000 – ₱1,800,000 / year (₱75k - ₱150k/mo)",
                "senior_level": "₱1,920,000 – ₱3,600,000+ / year (₱160k - ₱300k+/mo)",
                "source": "Payscale PH, SEA AI Talent Compensation Benchmark",
                "updated_at": "2026-Q1"
            },
            "global_usd": {
                "currency": "USD",
                "entry_level": "$90,000 – $120,000 / year",
                "mid_level": "$130,000 – $180,000 / year",
                "senior_level": "$190,000 – $275,000+ / year",
                "source": "Levels.fyi, O'Reilly AI/ML Salary Survey",
                "updated_at": "2026-Q1"
            }
        },
        "learning_resources": [
            {"title": "fast.ai: Practical Deep Learning for Coders", "type": "Top-Down AI Course", "cost": "Free", "provider": "fast.ai", "url": "https://course.fast.ai/"},
            {"title": "Hugging Face NLP & Deep Learning Course", "type": "Interactive Transformers Guide", "cost": "Free", "provider": "Hugging Face", "url": "https://huggingface.co/learn/nlp-course/chapter1/1"},
            {"title": "Google AI for Developers Documentation", "type": "Official Guides & SDKs", "cost": "Free", "provider": "Google", "url": "https://ai.google.dev/"}
        ],
        "related_careers": ["data-scientist", "data-analyst", "software-engineer", "backend-developer"],
        "sources": ["DeepLearning.AI", "Levels.fyi", "O'Reilly", "Payscale"],
        "last_updated": "2026-09-01"
    },
    {
        "id": "ui-designer",
        "title": "UI Designer",
        "field": "Design",
        "category_id": "design",
        "category_name": "UI/UX & Product Design",
        "tagline": "Craft visual aesthetics, typography, color palettes, and component design systems for digital interfaces.",
        "description": "User Interface (UI) Designers focus on the visual, interactive, and graphic aspects of digital products. They create cohesive visual languages, icons, typography scales, layout grids, and interactive states.",
        "responsibilities": [
            "Create high-fidelity screen designs, UI elements, illustrations, and iconography",
            "Build and maintain scalable design systems with reusable components and tokens",
            "Design responsive layouts across desktop, tablet, and mobile breakpoints",
            "Establish consistent visual guidelines for color, typography, spacing, and micro-interactions",
            "Prepare detailed design handoff specifications and assets for front-end developers"
        ],
        "riasec_traits": ["A", "R", "C"],
        "work_style": "Visual craft, artistic intuition, attention to detail, and creative collaboration.",
        "core_skills": ["UI Design", "Figma", "Design Systems", "Typography & Color Theory", "Responsive Layouts", "Visual Hierarchy"],
        "optional_skills": ["Prototyping (Figma/Protopie)", "HTML/CSS Basics", "Iconography", "Micro-animations", "Adobe Creative Suite"],
        "common_tools": ["Figma", "Adobe Illustrator / Photoshop", "Protopie", "Zeplin", "FigJam"],
        "education_paths": [
            "Degrees in Graphic Design, Fine Arts, Multimedia Arts, Visual Communication, or HCI",
            "Self-taught visual designers building public Dribbble/Behance portfolios",
            "Design bootcamps focusing on UI kits and modern responsive design"
        ],
        "certifications": [
            {"name": "CalArts UI / UX Design Specialization", "cost": "Low-cost (Coursera FinAid Available)", "provider": "Coursera / CalArts", "url": "https://www.coursera.org/specializations/ui-ux-design"},
            {"name": "Figma for UI/UX Design Masterclass", "cost": "Free Tutorials on YouTube / Figma Community", "provider": "Figma Community", "url": "https://www.figma.com/community"}
        ],
        "portfolio_projects": [
            {"title": "Multi-Theme UI Component Kit & Style Guide", "description": "Complete Figma design system with auto-layout components, color tokens, typography scales, and dark/light mode variants.", "difficulty": "Foundational"},
            {"title": "Mobile Banking / Fintech App UI Concept", "description": "High-fidelity 15+ screen mobile app interface with micro-interactions, transaction feeds, and card management.", "difficulty": "Intermediate"},
            {"title": "Editorial Web Publication & Tablet Reader Interface", "description": "Sophisticated typographic design for an online magazine with custom responsive grid layouts and animated reading progress.", "difficulty": "Advanced"}
        ],
        "salary_data": {
            "philippines": {
                "currency": "PHP",
                "entry_level": "₱300,000 – ₱500,000 / year (₱25k - ₱42k/mo)",
                "mid_level": "₱600,000 – ₱1,140,000 / year (₱50k - ₱95k/mo)",
                "senior_level": "₱1,200,000 – ₱2,200,000+ / year (₱100k - ₱180k+/mo)",
                "source": "Payscale PH, UXPH Survey",
                "updated_at": "2026-Q1"
            },
            "global_usd": {
                "currency": "USD",
                "entry_level": "$65,000 – $85,000 / year",
                "mid_level": "$90,000 – $125,000 / year",
                "senior_level": "$135,000 – $185,000+ / year",
                "source": "Levels.fyi, Dribbble Design Salary Survey",
                "updated_at": "2026-Q1"
            }
        },
        "learning_resources": [
            {"title": "Refactoring UI (Design Tips for Developers & Designers)", "type": "Design Tips & Articles", "cost": "Free Articles & Paid Book", "provider": "Adam Wathan & Steve Schoger", "url": "https://www.refactoringui.com/"},
            {"title": "Figma YouTube Channel Tutorials", "type": "Video Tutorials", "cost": "Free", "provider": "Figma", "url": "https://www.youtube.com/@Figma"},
            {"title": "Typewolf (Typography Guides & Inspiration)", "type": "Typography Resource", "cost": "Free", "provider": "Typewolf", "url": "https://www.typewolf.com/"}
        ],
        "related_careers": ["ux-designer", "product-designer", "frontend-developer", "ux-engineer"],
        "sources": ["Dribbble", "Figma", "Levels.fyi", "Payscale"],
        "last_updated": "2026-09-01"
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
        "riasec_traits": ["R", "I", "C"],
        "work_style": "Process automation, systems reliability, proactive troubleshooting, and cross-team collaboration.",
        "core_skills": ["Linux", "Git & GitHub Actions", "Docker", "CI/CD Pipelines", "Bash / Python Scripting", "Cloud Basics (AWS/GCP)"],
        "optional_skills": ["Kubernetes", "Terraform", "Prometheus & Grafana", "Ansible", "DevSecOps", "Helm"],
        "common_tools": ["Docker", "Kubernetes", "GitHub Actions / GitLab CI", "Grafana", "Prometheus", "Terraform"],
        "education_paths": [
            "Bachelor's degree in Computer Science, IT, Computer Engineering, or related technical disciplines",
            "Self-taught through containerization projects, hands-on Linux administration, and CI/CD pipelines",
            "Transition from Systems Administration or Software Development"
        ],
        "certifications": [
            {"name": "Certified Kubernetes Administrator (CKA)", "cost": "$395 (Exam fee)", "provider": "Linux Foundation / CNCF", "url": "https://www.cncf.io/certification/cka/"},
            {"name": "GitHub Actions Certification", "cost": "$99 (Exam fee)", "provider": "GitHub", "url": "https://examregistration.github.com/"},
            {"name": "AWS Certified DevOps Engineer – Professional", "cost": "$300 (Exam fee)", "provider": "AWS", "url": "https://aws.amazon.com/certification/certified-devops-engineer-professional/"}
        ],
        "portfolio_projects": [
            {"title": "Automated Multi-Stage CI/CD Pipeline with GitHub Actions", "description": "Complete CI/CD pipeline that runs linter checks, automated unit tests, builds a Docker image, and deploys to a test server on push.", "difficulty": "Foundational"},
            {"title": "Production Monitoring Stack with Prometheus & Grafana", "description": "Deploying containerized Prometheus and Grafana dashboards monitoring CPU, memory, HTTP request rates, and error rate alerting.", "difficulty": "Intermediate"},
            {"title": "Production Kubernetes Cluster Deployment with Helm & GitOps", "description": "Zero-downtime rolling update deployment of a microservice application on Kubernetes utilizing ArgoCD and Helm charts.", "difficulty": "Advanced"}
        ],
        "salary_data": {
            "philippines": {
                "currency": "PHP",
                "entry_level": "₱420,000 – ₱720,000 / year (₱35k - ₱60k/mo)",
                "mid_level": "₱840,000 – ₱1,680,000 / year (₱70k - ₱140k/mo)",
                "senior_level": "₱1,800,000 – ₱3,400,000+ / year (₱150k - ₱280k+/mo)",
                "source": "Payscale PH, NodeFlair SEA Report",
                "updated_at": "2026-Q1"
            },
            "global_usd": {
                "currency": "USD",
                "entry_level": "$85,000 – $105,000 / year",
                "mid_level": "$115,000 – $160,000 / year",
                "senior_level": "$165,000 – $230,000+ / year",
                "source": "Levels.fyi, Puppet State of DevOps Report",
                "updated_at": "2026-Q1"
            }
        },
        "learning_resources": [
            {"title": "DevOps Roadmap (roadmap.sh/devops)", "type": "Community Visual Guide", "cost": "Free", "provider": "roadmap.sh", "url": "https://roadmap.sh/devops"},
            {"title": "Docker Official Getting Started Guide", "type": "Documentation & Hands-on", "cost": "Free", "provider": "Docker", "url": "https://docs.docker.com/get-started/"},
            {"title": "Kubernetes Official Interactive Tutorials", "type": "Interactive Sandbox", "cost": "Free", "provider": "Kubernetes.io", "url": "https://kubernetes.io/docs/tutorials/"}
        ],
        "related_careers": ["cloud-engineer", "fullstack-developer", "cybersecurity-analyst", "software-engineer"],
        "sources": ["CNCF", "Puppet", "Levels.fyi", "Payscale"],
        "last_updated": "2026-09-01"
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
        "riasec_traits": ["I", "A", "C"],
        "work_style": "Deep intellectual investigation, hypothesis testing, data exploration, and statistical reasoning.",
        "core_skills": ["Python / R", "Statistics & Probability", "SQL", "Pandas & NumPy", "Machine Learning Algorithms", "Data Storytelling"],
        "optional_skills": ["A/B Testing Methodology", "Deep Learning", "Big Data (PySpark)", "Cloud Warehouses (Snowflake/BigQuery)", "Data Visualization"],
        "common_tools": ["Jupyter / Google Colab", "Python", "scikit-learn", "SQL", "Tableau", "Git"],
        "education_paths": [
            "Degree in Statistics, Mathematics, Computer Science, Data Science, Physics, or Quantitative Economics",
            "Self-taught through competitive Kaggle datasets, published Jupyter case studies, and open-source contributions",
            "Transition from Data Analytics with deepened mathematical training"
        ],
        "certifications": [
            {"name": "IBM Data Science Professional Certificate", "cost": "Low-cost (Coursera FinAid Available)", "provider": "Coursera / IBM", "url": "https://www.coursera.org/professional-certificates/ibm-data-science"},
            {"name": "Kaggle Competitions Master / Notebooks Master", "cost": "Free", "provider": "Kaggle", "url": "https://www.kaggle.com/"}
        ],
        "portfolio_projects": [
            {"title": "Customer Churn Predictive Model with Interpretability", "description": "Predicting customer subscription churn with Random Forest / XGBoost, featuring SHAP value explanations for feature importance.", "difficulty": "Foundational"},
            {"title": "A/B Experimentation Analysis & Statistical Significance Report", "description": "Comprehensive statistical notebook assessing sample size, p-value calculations, bootstrap intervals, and bias avoidance.", "difficulty": "Intermediate"},
            {"title": "End-to-End Time Series Demand Forecasting Model", "description": "Forecasting multi-category retail inventory demand utilizing ARIMA/Prophet models with backtesting evaluation.", "difficulty": "Advanced"}
        ],
        "salary_data": {
            "philippines": {
                "currency": "PHP",
                "entry_level": "₱420,000 – ₱720,000 / year (₱35k - ₱60k/mo)",
                "mid_level": "₱840,000 – ₱1,680,000 / year (₱70k - ₱140k/mo)",
                "senior_level": "₱1,800,000 – ₱3,200,000+ / year (₱150k - ₱265k+/mo)",
                "source": "Payscale PH, Analytics Association of the Philippines",
                "updated_at": "2026-Q1"
            },
            "global_usd": {
                "currency": "USD",
                "entry_level": "$80,000 – $105,000 / year",
                "mid_level": "$115,000 – $160,000 / year",
                "senior_level": "$165,000 – $235,000+ / year",
                "source": "Levels.fyi, US BLS (Data Scientists)",
                "updated_at": "2026-Q1"
            }
        },
        "learning_resources": [
            {"title": "StatQuest with Josh Starmer (Machine Learning & Stats)", "type": "Visual Educational Videos", "cost": "Free", "provider": "StatQuest", "url": "https://statquest.org/"},
            {"title": "Python Data Science Handbook (Jake VanderPlas)", "type": "Open Access Book", "cost": "Free", "provider": "GitHub / O'Reilly", "url": "https://jakevdp.github.io/PythonDataScienceHandbook/"},
            {"title": "Kaggle Learn Micro-Courses", "type": "Interactive Tutorials", "cost": "Free", "provider": "Kaggle", "url": "https://www.kaggle.com/learn"}
        ],
        "related_careers": ["data-analyst", "ai-ml-engineer", "product-manager", "database-administrator"],
        "sources": ["U.S. Bureau of Labor Statistics", "Kaggle", "Levels.fyi", "Payscale"],
        "last_updated": "2026-09-01"
    },
    {
        "id": "technical-writer",
        "title": "Technical Writer",
        "field": "Documentation & Communications",
        "category_id": "product_management",
        "category_name": "Product & Tech Strategy",
        "tagline": "Translate intricate code, APIs, and systems into crystal-clear developer documentation and user guides.",
        "description": "Technical Writers create comprehensive documentation, API references, tutorials, and developer guides. They make complex technologies easy to understand, adopt, and integrate.",
        "responsibilities": [
            "Write and maintain developer documentation, API references, code samples, and tutorials",
            "Collaborate with software engineers to test APIs and document endpoint parameters",
            "Maintain documentation-as-code repositories using Markdown, Git, and static site generators",
            "Create architectural diagrams, onboarding guides, and troubleshooting workflows",
            "Review documentation analytics and gather user feedback to clarify confusing topics"
        ],
        "riasec_traits": ["A", "I", "C"],
        "work_style": "Editorial clarity, meticulous organization, independent research, and developer empathy.",
        "core_skills": ["Technical Writing", "Clear Communication", "Markdown & Docs-as-Code", "API Basics", "Git & GitHub", "Information Architecture"],
        "optional_skills": ["HTML/CSS", "Python Basics", "Static Site Generators (Docusaurus/MkDocs)", "API Testing (Postman)", "Diagramming (Mermaid/Draw.io)"],
        "common_tools": ["Markdown", "VS Code", "Git / GitHub", "Postman", "Docusaurus / Readme.com", "Notion"],
        "education_paths": [
            "Degrees in English, Communications, Journalism, Technical Communication, Computer Science, or IT",
            "Developers or QA specialists with strong writing and communication strengths",
            "Self-taught technical writers with published open-source documentation portfolios"
        ],
        "certifications": [
            {"name": "Google Technical Writing Courses (I & II)", "cost": "Free", "provider": "Google Developers", "url": "https://developers.google.com/tech-writing"},
            {"name": "Society for Technical Communication (STC) Certifications", "cost": "$250 – $400", "provider": "STC", "url": "https://www.stc.org/"}
        ],
        "portfolio_projects": [
            {"title": "Open-Source Library API Reference & Getting Started Guide", "description": "Authored complete Getting Started guide, quickstart code samples, and comprehensive API parameter tables for an open-source project.", "difficulty": "Foundational"},
            {"title": "Interactive REST API Tutorial & Postman Collection", "description": "Step-by-step developer tutorial guiding users through authentication, webhook setup, and error handling with clear curl examples.", "difficulty": "Intermediate"},
            {"title": "Full Documentation-as-Code Site with Docusaurus", "description": "Custom deployed documentation website with versioning, search integration, code tabs, and automated GitHub Actions deployment.", "difficulty": "Advanced"}
        ],
        "salary_data": {
            "philippines": {
                "currency": "PHP",
                "entry_level": "₱300,000 – ₱480,000 / year (₱25k - ₱40k/mo)",
                "mid_level": "₱540,000 – ₱1,020,000 / year (₱45k - ₱85k/mo)",
                "senior_level": "₱1,080,000 – ₱2,000,000+ / year (₱90k - ₱165k+/mo)",
                "source": "Payscale PH, Write the Docs Salary Benchmarks",
                "updated_at": "2026-Q1"
            },
            "global_usd": {
                "currency": "USD",
                "entry_level": "$60,000 – $78,000 / year",
                "mid_level": "$82,000 – $112,000 / year",
                "senior_level": "$120,000 – $165,000+ / year",
                "source": "Levels.fyi, US BLS (Technical Writers)",
                "updated_at": "2026-Q1"
            }
        },
        "learning_resources": [
            {"title": "Google Technical Writing Free Courses", "type": "Official Interactive Modules", "cost": "Free", "provider": "Google", "url": "https://developers.google.com/tech-writing"},
            {"title": "Write the Docs Community Guide", "type": "Community Documentation Resources", "cost": "Free", "provider": "Write the Docs", "url": "https://www.writethedocs.org/"},
            {"title": "Diátaxis Documentation Framework", "type": "Documentation Architecture Model", "cost": "Free", "provider": "Diátaxis", "url": "https://diataxis.fr/"}
        ],
        "related_careers": ["frontend-developer", "product-manager", "qa-engineer", "ux-designer"],
        "sources": ["Google Developers", "Write the Docs", "U.S. BLS", "Payscale"],
        "last_updated": "2026-09-01"
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
        "riasec_traits": ["C", "I", "R"],
        "work_style": "Detail-oriented investigation, methodical verification, and quality craftsmanship.",
        "core_skills": ["Software Testing Principles", "Bug Tracking & Reporting", "API Testing (Postman)", "Test Case Design", "Git Basics"],
        "optional_skills": ["Playwright or Cypress", "Python / JavaScript Basics", "CI/CD Test Automation", "Performance Testing (JMeter)", "Accessibility Testing"],
        "common_tools": ["Postman", "Playwright / Cypress", "Jira", "Chrome DevTools", "GitHub Actions", "Selenium"],
        "education_paths": [
            "Degree in Computer Science, Information Technology, or Engineering",
            "Entry-level manual testing transitioning to test automation engineering",
            "Self-taught QA practitioners with hands-on test portfolio automation repositories"
        ],
        "certifications": [
            {"name": "ISTQB Certified Tester Foundation Level (CTFL)", "cost": "$229 (Exam fee)", "provider": "ISTQB / ASTQB", "url": "https://www.istqb.org/certifications/certified-tester-foundation-level"},
            {"name": "Postman API Fundamentals Student Expert", "cost": "Free", "provider": "Postman", "url": "https://www.postman.com/student-program/student-expert/"}
        ],
        "portfolio_projects": [
            {"title": "Comprehensive Test Plan & Bug Tracking Portfolio", "description": "Structured test matrix, equivalence partitioning test cases, and documented GitHub issue bug reports for a live open-source web application.", "difficulty": "Foundational"},
            {"title": "Automated End-to-End (E2E) Test Suite with Playwright", "description": "Automated cross-browser test suite covering user authentication, shopping cart edge cases, and form validation with screenshot failure artifacts.", "difficulty": "Intermediate"},
            {"title": "Automated API & Performance Testing Pipeline in GitHub Actions", "description": "Scheduled CI/CD pipeline executing automated Newman (Postman) API contract tests and k6 load testing against staging endpoints.", "difficulty": "Advanced"}
        ],
        "salary_data": {
            "philippines": {
                "currency": "PHP",
                "entry_level": "₱280,000 – ₱480,000 / year (₱23k - ₱40k/mo)",
                "mid_level": "₱540,000 – ₱1,100,000 / year (₱45k - ₱90k/mo)",
                "senior_level": "₱1,200,000 – ₱2,300,000+ / year (₱100k - ₱190k+/mo)",
                "source": "Payscale PH, JobStreet Tech Salaries",
                "updated_at": "2026-Q1"
            },
            "global_usd": {
                "currency": "USD",
                "entry_level": "$62,000 – $82,000 / year",
                "mid_level": "$88,000 – $120,000 / year",
                "senior_level": "$130,000 – $175,000+ / year",
                "source": "Levels.fyi, Glassdoor QA Salary Benchmarks",
                "updated_at": "2026-Q1"
            }
        },
        "learning_resources": [
            {"title": "Playwright Official Guides & Tutorial", "type": "Modern E2E Testing Docs", "cost": "Free", "provider": "Microsoft Playwright", "url": "https://playwright.dev/"},
            {"title": "Ministry of Testing Community Guides", "type": "Testing Articles & Forums", "cost": "Free Articles Available", "provider": "Ministry of Testing", "url": "https://www.ministryoftesting.com/"},
            {"title": "Postman Learning Center", "type": "Interactive API Testing Guide", "cost": "Free", "provider": "Postman", "url": "https://learning.postman.com/"}
        ],
        "related_careers": ["frontend-developer", "fullstack-developer", "devops-engineer", "technical-writer"],
        "sources": ["ISTQB", "Ministry of Testing", "Levels.fyi", "Payscale"],
        "last_updated": "2026-09-01"
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
        "riasec_traits": ["R", "A", "I"],
        "work_style": "Hands-on coding, creative tactile problem-solving, and device-focused polish.",
        "core_skills": ["Flutter (Dart) or React Native", "Mobile UI Patterns", "REST APIs", "State Management", "Git & GitHub"],
        "optional_skills": ["Swift / SwiftUI (iOS)", "Kotlin / Jetpack Compose (Android)", "SQLite / Hive Local Storage", "App Store Publishing", "Push Notifications"],
        "common_tools": ["Android Studio", "Xcode", "VS Code", "Figma", "Firebase", "Postman"],
        "education_paths": [
            "Bachelor's in Computer Science, Information Technology, or Software Engineering",
            "Mobile development bootcamps and guided app store publishing projects",
            "Self-taught engineers with live published apps on Google Play or Apple App Store"
        ],
        "certifications": [
            {"name": "Google Associate Android Developer (Kotlin)", "cost": "$149 (Exam fee)", "provider": "Google", "url": "https://developers.google.com/certification/associate-android-developer"},
            {"name": "Meta iOS / Android Developer Professional Certificate", "cost": "Low-cost (Coursera FinAid Available)", "provider": "Coursera / Meta", "url": "https://www.coursera.org/professional-certificates/meta-android-developer"}
        ],
        "portfolio_projects": [
            {"title": "Habit Tracker & Daily Journal with Offline Sync", "description": "Mobile app featuring smooth animations, offline local SQLite storage, dark mode, and scheduled local notifications.", "difficulty": "Foundational"},
            {"title": "Location-Aware Food Delivery or Cafe Discovery App", "description": "Cross-platform app integrating Google Maps API, live geolocation tracking, search filtering, and mock payment checkout.", "difficulty": "Intermediate"},
            {"title": "Real-Time Audio / Chat Messaging Mobile Client", "description": "Production mobile app utilizing WebSockets / Supabase real-time, optimistic message sending, media caching, and biometric login.", "difficulty": "Advanced"}
        ],
        "salary_data": {
            "philippines": {
                "currency": "PHP",
                "entry_level": "₱360,000 – ₱600,000 / year (₱30k - ₱50k/mo)",
                "mid_level": "₱720,000 – ₱1,440,000 / year (₱60k - ₱120k/mo)",
                "senior_level": "₱1,500,000 – ₱2,800,000+ / year (₱125k - ₱230k+/mo)",
                "source": "Payscale PH, NodeFlair SEA",
                "updated_at": "2026-Q1"
            },
            "global_usd": {
                "currency": "USD",
                "entry_level": "$75,000 – $95,000 / year",
                "mid_level": "$105,000 – $145,000 / year",
                "senior_level": "$150,000 – $210,000+ / year",
                "source": "Levels.fyi, Indeed Tech Salary Indices",
                "updated_at": "2026-Q1"
            }
        },
        "learning_resources": [
            {"title": "Flutter Official Documentation & Codelabs", "type": "Interactive Guides", "cost": "Free", "provider": "Flutter Team", "url": "https://docs.flutter.dev/"},
            {"title": "Android Basics with Compose (Official Google Course)", "type": "Guided Course", "cost": "Free", "provider": "Google Developers", "url": "https://developer.android.com/courses/android-basics-compose/course"},
            {"title": "React Native Official Getting Started", "type": "Documentation", "cost": "Free", "provider": "Meta", "url": "https://reactnative.dev/docs/getting-started"}
        ],
        "related_careers": ["frontend-developer", "fullstack-developer", "ui-designer", "ux-engineer"],
        "sources": ["Google Developers", "Apple Developer", "Levels.fyi", "Payscale"],
        "last_updated": "2026-09-01"
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
        "riasec_traits": ["A", "E", "I"],
        "work_style": "Holistic product thinking, creative craft, cross-functional leadership, and user empathy.",
        "core_skills": ["End-to-End Product Design", "Figma", "UX Research", "UI Design", "Design Systems", "Prototyping", "Strategic Thinking"],
        "optional_skills": ["Interaction Design", "Product Metrics & Analytics", "Basic Front-End Code (HTML/CSS)", "Design Sprint Facilitation"],
        "common_tools": ["Figma", "FigJam", "Miro", "Notion", "Maze", "Loom"],
        "education_paths": [
            "Degrees in Design, Human-Computer Interaction, Industrial Design, Fine Arts, or Computer Science",
            "Designers transitioning from graphic, UI, or UX design through complex product case studies",
            "Self-taught product designers with published case studies detailing metrics and business outcomes"
        ],
        "certifications": [
            {"name": "Google UX Design Professional Certificate", "cost": "Low-cost (Coursera FinAid Available)", "provider": "Coursera / Google", "url": "https://www.coursera.org/professional-certificates/google-ux-design"},
            {"name": "Interaction Design Foundation (IxDF) Master Classes", "cost": "Low-cost Membership", "provider": "IxDF", "url": "https://www.interaction-design.org/"}
        ],
        "portfolio_projects": [
            {"title": "0-to-1 B2C App Product Discovery & Design Case Study", "description": "Documented 0-to-1 design journey including competitor benchmarking, user problem statements, wireframe iterations, and tested high-fi Figma prototypes.", "difficulty": "Intermediate"},
            {"title": "Enterprise B2B Workflow Optimization & Design System", "description": "Designing complex data filtering, permissions management, and scalable design token architecture for a cloud platform.", "difficulty": "Advanced"}
        ],
        "salary_data": {
            "philippines": {
                "currency": "PHP",
                "entry_level": "₱420,000 – ₱660,000 / year (₱35k - ₱55k/mo)",
                "mid_level": "₱780,000 – ₱1,500,000 / year (₱65k - ₱125k/mo)",
                "senior_level": "₱1,560,000 – ₱2,900,000+ / year (₱130k - ₱240k+/mo)",
                "source": "Payscale PH, UXPH Compensation Survey",
                "updated_at": "2026-Q1"
            },
            "global_usd": {
                "currency": "USD",
                "entry_level": "$78,000 – $102,000 / year",
                "mid_level": "$110,000 – $155,000 / year",
                "senior_level": "$160,000 – $225,000+ / year",
                "source": "Levels.fyi, Dribbble Design Salary Index",
                "updated_at": "2026-Q1"
            }
        },
        "learning_resources": [
            {"title": "Design Systems Handbook (DesignBetter.Co)", "type": "Comprehensive Guide", "cost": "Free", "provider": "InVision / DesignBetter", "url": "https://www.designbetter.co/design-systems-handbook"},
            {"title": "Figma Best Practices Guide", "type": "Official Workflows", "cost": "Free", "provider": "Figma", "url": "https://www.figma.com/best-practices/"},
            {"title": "Growth.Design Case Studies", "type": "Interactive Comic UX Teardowns", "cost": "Free", "provider": "Growth.Design", "url": "https://growth.design/case-studies"}
        ],
        "related_careers": ["ux-designer", "ui-designer", "product-manager", "ux-engineer"],
        "sources": ["DesignBetter", "Growth.Design", "Levels.fyi", "Payscale"],
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
        "riasec_traits": ["C", "I", "R"],
        "work_style": "Methodical, meticulous data stewardship, deep systems troubleshooting, and high reliability.",
        "core_skills": ["SQL & Relational Modeling", "PostgreSQL or MySQL Administration", "Performance Tuning & Indexing", "Backup & Recovery", "Linux Basics"],
        "optional_skills": ["NoSQL (MongoDB/Redis)", "Database Replication & Clustering", "Cloud DBs (AWS RDS/Aurora)", "Python / Bash Scripting", "Data Warehousing"],
        "common_tools": ["PostgreSQL / pgAdmin", "DBeaver", "Linux Terminal", "AWS RDS", "Explain Plan Tools", "Prometheus / Datadog"],
        "education_paths": [
            "Degree in Computer Science, Information Technology, Information Systems, or Database Management",
            "Transition from Systems Administration or Data Engineering",
            "Vendor database certifications combined with enterprise database administration experience"
        ],
        "certifications": [
            {"name": "PostgreSQL Professional Certification (EDB / Linux Foundation)", "cost": "$200 – $300", "provider": "EnterpriseDB", "url": "https://www.enterprisedb.com/training-certification"},
            {"name": "AWS Certified Database – Specialty (or AWS Cloud Solutions)", "cost": "$300 (Exam fee)", "provider": "AWS", "url": "https://aws.amazon.com/certification/certified-database-specialty/"},
            {"name": "Oracle Certified Professional MySQL Database Administrator", "cost": "$245 (Exam fee)", "provider": "Oracle", "url": "https://education.oracle.com/mysql-database-administrator-certified-professional"}
        ],
        "portfolio_projects": [
            {"title": "PostgreSQL High-Availability Master-Replica Lab", "description": "Configuring PostgreSQL streaming replication with automated failover using pgpool and monitoring replication lag.", "difficulty": "Foundational"},
            {"title": "Query Optimization & Indexing Benchmark Case Study", "description": "Diagnosing a slow 10-million row database table, analyzing EXPLAIN ANALYZE execution plans, and reducing query latency by 95% with composite indexing.", "difficulty": "Intermediate"}
        ],
        "salary_data": {
            "philippines": {
                "currency": "PHP",
                "entry_level": "₱360,000 – ₱540,000 / year (₱30k - ₱45k/mo)",
                "mid_level": "₱660,000 – ₱1,320,000 / year (₱55k - ₱110k/mo)",
                "senior_level": "₱1,440,000 – ₱2,700,000+ / year (₱120k - ₱225k+/mo)",
                "source": "Payscale PH, JobStreet Database Benchmarks",
                "updated_at": "2026-Q1"
            },
            "global_usd": {
                "currency": "USD",
                "entry_level": "$70,000 – $90,000 / year",
                "mid_level": "$98,000 – $135,000 / year",
                "senior_level": "$140,000 – $190,000+ / year",
                "source": "Levels.fyi, US BLS (Database Administrators)",
                "updated_at": "2026-Q1"
            }
        },
        "learning_resources": [
            {"title": "PostgreSQL Official Documentation & Manual", "type": "Comprehensive Reference", "cost": "Free", "provider": "PostgreSQL Global Development Group", "url": "https://www.postgresql.org/docs/"},
            {"title": "Use The Index, Luke! (SQL Indexing Guide)", "type": "Database Indexing Guide", "cost": "Free", "provider": "Markus Winand", "url": "https://use-the-index-luke.com/"},
            {"title": "SQL Tutorial for Beginners (Mode Analytics)", "type": "Interactive SQL Guide", "cost": "Free", "provider": "Mode Analytics", "url": "https://mode.com/sql-tutorial/"}
        ],
        "related_careers": ["data-analyst", "cloud-engineer", "fullstack-developer", "devops-engineer"],
        "sources": ["PostgreSQL.org", "U.S. BLS", "Levels.fyi", "Payscale"],
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
        "riasec_traits": ["I", "R", "C"],
        "work_style": "Systematic backend logic, deep algorithmic focus, and architectural problem solving.",
        "core_skills": ["Python, Node.js, or Go", "SQL & Database Design", "REST APIs", "Git & GitHub", "Data Structures & Algorithms"],
        "optional_skills": ["PostgreSQL", "Docker", "Redis Caching", "Microservices", "System Design", "Message Queues (RabbitMQ/Kafka)"],
        "common_tools": ["VS Code / PyCharm", "Postman", "PostgreSQL / DBeaver", "Docker", "Linux CLI", "Git"],
        "education_paths": [
            "Bachelor's in Computer Science, Software Engineering, or Information Systems",
            "Back-End intensive bootcamps and open-source contributions",
            "Self-taught engineers building complex API projects"
        ],
        "certifications": [
            {"name": "freeCodeCamp Back End Development and APIs", "cost": "Free", "provider": "freeCodeCamp", "url": "https://www.freecodecamp.org/learn/back-end-development-and-apis/"},
            {"name": "Meta Back-End Developer Professional Certificate", "cost": "Low-cost (Coursera FinAid Available)", "provider": "Coursera / Meta", "url": "https://www.coursera.org/professional-certificates/meta-back-end-developer"}
        ],
        "portfolio_projects": [
            {"title": "High-Concurrency REST API with Authentication & Rate Limiting", "description": "Production-grade API featuring JWT auth, Redis rate-limiting, and PostgreSQL CRUD operations with 100% test coverage.", "difficulty": "Foundational"},
            {"title": "Distributed Event-Driven Order Processing System", "description": "Microservices architecture utilizing message queues (RabbitMQ), idempotency checks, and asynchronous webhook dispatching.", "difficulty": "Intermediate"},
            {"title": "Custom Search Engine Indexer & Caching Pipeline", "description": "High-speed inverted index search API with Redis cache invalidation and database connection pooling.", "difficulty": "Advanced"}
        ],
        "salary_data": {
            "philippines": {
                "currency": "PHP",
                "entry_level": "₱360,000 – ₱600,000 / year (₱30k - ₱50k/mo)",
                "mid_level": "₱720,000 – ₱1,500,000 / year (₱60k - ₱125k/mo)",
                "senior_level": "₱1,500,000 – ₱3,000,000+ / year (₱125k - ₱250k+/mo)",
                "source": "Payscale PH, NodeFlair SEA",
                "updated_at": "2026-Q1"
            },
            "global_usd": {
                "currency": "USD",
                "entry_level": "$75,000 – $98,000 / year",
                "mid_level": "$105,000 – $150,000 / year",
                "senior_level": "$155,000 – $220,000+ / year",
                "source": "Levels.fyi, Stack Overflow Developer Survey",
                "updated_at": "2026-Q1"
            }
        },
        "learning_resources": [
            {"title": "Backend Development Roadmap (roadmap.sh/backend)", "type": "Visual Guide", "cost": "Free", "provider": "roadmap.sh", "url": "https://roadmap.sh/backend"},
            {"title": "CS50's Introduction to Computer Science", "type": "University Course", "cost": "Free", "provider": "Harvard University (edX)", "url": "https://cs50.harvard.edu/x/"},
            {"title": "FastAPI / Node.js Official Documentation", "type": "Documentation", "cost": "Free", "provider": "FastAPI", "url": "https://fastapi.tiangolo.com/"}
        ],
        "related_careers": ["fullstack-developer", "devops-engineer", "cloud-engineer", "database-administrator"],
        "sources": ["Stack Overflow", "Levels.fyi", "Payscale", "NodeFlair"],
        "last_updated": "2026-09-01"
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
        "riasec_traits": ["A", "I", "R"],
        "work_style": "Hybrid creative-technical craft, rapid prototyping, and cross-discipline collaboration.",
        "core_skills": ["HTML5/CSS3/JavaScript", "React & TypeScript", "Figma", "Design Systems", "Web Accessibility (a11y)", "Git"],
        "optional_skills": ["Storybook", "Framer Motion / CSS Animations", "Tailwind CSS", "UX Research Basics", "Component Unit Testing"],
        "common_tools": ["VS Code", "Figma", "Storybook", "Chrome DevTools", "GitHub", "Vercel"],
        "education_paths": [
            "Degree in Computer Science, HCI, Interactive Media, or Graphic Design",
            "Front-End developers who developed deep design expertise",
            "UI/UX designers who learned modern JavaScript component development"
        ],
        "certifications": [
            {"name": "Interaction Design Foundation: UI & Front-End Design", "cost": "Low-cost Membership", "provider": "IxDF", "url": "https://www.interaction-design.org/"},
            {"name": "Frontend Masters Design Systems Path", "cost": "Subscription", "provider": "Frontend Masters", "url": "https://frontendmasters.com/courses/design-systems/"}
        ],
        "portfolio_projects": [
            {"title": "Accessible Design System in Storybook", "description": "Interactive component library with automated a11y tests, keyboard navigation, and theme tokens.", "difficulty": "Foundational"},
            {"title": "High-Fidelity Interactive App Prototype in Code", "description": "Fully interactive code prototype demonstrating complex multi-step drag-and-drop or canvas interactions.", "difficulty": "Intermediate"}
        ],
        "salary_data": {
            "philippines": {
                "currency": "PHP",
                "entry_level": "₱380,000 – ₱620,000 / year (₱32k - ₱52k/mo)",
                "mid_level": "₱750,000 – ₱1,400,000 / year (₱62k - ₱116k/mo)",
                "senior_level": "₱1,500,000 – ₱2,800,000+ / year (₱125k - ₱230k+/mo)",
                "source": "Payscale PH, UXPH",
                "updated_at": "2026-Q1"
            },
            "global_usd": {
                "currency": "USD",
                "entry_level": "$75,000 – $98,000 / year",
                "mid_level": "$105,000 – $148,000 / year",
                "senior_level": "$155,000 – $215,000+ / year",
                "source": "Levels.fyi, Google UXE Salary Data",
                "updated_at": "2026-Q1"
            }
        },
        "learning_resources": [
            {"title": "Storybook Official Tutorials", "type": "Interactive Guides", "cost": "Free", "provider": "Storybook", "url": "https://storybook.js.org/tutorials/"},
            {"title": "Inclusive Components by Heydon Pickering", "type": "Accessible Patterns", "cost": "Free", "provider": "Inclusive Components", "url": "https://inclusive-components.design/"}
        ],
        "related_careers": ["frontend-developer", "ux-designer", "ui-designer", "product-designer"],
        "sources": ["Storybook", "Google Careers", "Levels.fyi", "Payscale"],
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
        "riasec_traits": ["E", "C", "S"],
        "work_style": "Consultative communication, structured requirements analysis, and business alignment.",
        "core_skills": ["Business Process Modeling", "Requirements Gathering", "Agile / User Stories", "Stakeholder Communication", "Data Analysis Basics"],
        "optional_skills": ["SQL Basics", "Tableau / Power BI", "UML Diagramming", "Financial Modeling", "Jira / Confluence"],
        "common_tools": ["Jira / Confluence", "Lucidchart / Miro", "Excel", "Power BI", "Notion"],
        "education_paths": [
            "Degrees in Business Administration, Information Systems, Management Engineering, or Economics",
            "Transition from operations, project management, or quality assurance",
            "Professional Business Analysis certifications (IIBA ECBA/CBAP)"
        ],
        "certifications": [
            {"name": "IIBA Entry Certificate in Business Analysis (ECBA)", "cost": "$225 (Exam fee)", "provider": "IIBA", "url": "https://www.iiba.org/business-analysis-certifications/ecba/"},
            {"name": "Coursera / IBM IT Scrum Master & Business Analyst Specialization", "cost": "Low-cost (Coursera FinAid Available)", "provider": "IBM / Coursera", "url": "https://www.coursera.org/specializations/ibm-scrum-master"}
        ],
        "portfolio_projects": [
            {"title": "Business Process Model & Gap Analysis Report", "description": "End-to-end BPMN workflow mapping for an e-commerce or customer onboarding flow, detailing 40% reduction in processing time.", "difficulty": "Foundational"},
            {"title": "Software Functional Specification Document & UAT Matrix", "description": "Comprehensive requirement package with traceability matrix, acceptance criteria, and edge-case testing plans.", "difficulty": "Intermediate"}
        ],
        "salary_data": {
            "philippines": {
                "currency": "PHP",
                "entry_level": "₱300,000 – ₱500,000 / year (₱25k - ₱42k/mo)",
                "mid_level": "₱600,000 – ₱1,200,000 / year (₱50k - ₱100k/mo)",
                "senior_level": "₱1,200,000 – ₱2,400,000+ / year (₱100k - ₱200k+/mo)",
                "source": "Payscale PH, IIBA Philippines",
                "updated_at": "2026-Q1"
            },
            "global_usd": {
                "currency": "USD",
                "entry_level": "$65,000 – $85,000 / year",
                "mid_level": "$90,000 – $125,000 / year",
                "senior_level": "$130,000 – $175,000+ / year",
                "source": "Levels.fyi, US BLS (Management & IT Analysts)",
                "updated_at": "2026-Q1"
            }
        },
        "learning_resources": [
            {"title": "IIBA Guide to the Business Analysis Body of Knowledge (BABOK)", "type": "Industry Standard", "cost": "Free Overview Available", "provider": "IIBA", "url": "https://www.iiba.org/career-resources/a-guide-to-the-business-analysis-body-of-knowledge-babok-guide/"},
            {"title": "Modern Business Analysis by Bridging the Gap", "type": "Articles & Guides", "cost": "Free", "provider": "Bridging the Gap", "url": "https://www.bridging-the-gap.com/"}
        ],
        "related_careers": ["product-manager", "data-analyst", "technical-writer", "database-administrator"],
        "sources": ["IIBA", "U.S. BLS", "Levels.fyi", "Payscale"],
        "last_updated": "2026-09-01"
    }
]
