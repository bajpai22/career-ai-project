"""
career_knowledge.py
===================
Central knowledge base: required skills per career + learning roadmaps.
Import this in any service that needs career metadata.
"""

# ── Required skills per career (skill → minimum proficiency 1-10) ─────────────
CAREER_SKILLS = {
    "Data Scientist": {
        "Python Programming": 8,
        "Machine Learning": 8,
        "Statistics": 8,
        "Data Analysis": 7,
        "SQL / Databases": 6,
        "Data Visualization": 6,
        "Deep Learning": 5,
        "Cloud Platforms": 5,
    },
    "Web Developer": {
        "HTML/CSS": 8,
        "JavaScript": 8,
        "React / Vue / Angular": 7,
        "Node.js / Backend": 6,
        "REST APIs": 7,
        "SQL / Databases": 6,
        "Version Control (Git)": 7,
        "Responsive Design": 7,
    },
    "Data Analyst": {
        "SQL / Databases": 8,
        "Excel / Spreadsheets": 7,
        "Data Visualization": 8,
        "Python / R": 6,
        "Statistics": 7,
        "Business Intelligence Tools": 6,
        "Data Cleaning": 7,
        "Communication": 7,
    },
    "DevOps Engineer": {
        "Linux / Shell Scripting": 8,
        "CI/CD Pipelines": 8,
        "Docker / Kubernetes": 8,
        "Cloud Platforms": 9,
        "Infrastructure as Code": 7,
        "Monitoring & Logging": 7,
        "Networking": 6,
        "Version Control (Git)": 8,
    },
    "Product Manager": {
        "Communication": 9,
        "Project Management": 9,
        "Product Strategy": 8,
        "User Research": 7,
        "Agile / Scrum": 8,
        "Data Analysis": 6,
        "Stakeholder Management": 8,
        "Road-mapping Tools": 7,
    },
    "Cybersecurity Analyst": {
        "Network Security": 9,
        "Penetration Testing": 7,
        "Security Protocols": 8,
        "Risk Assessment": 8,
        "SIEM Tools": 7,
        "Linux / Shell Scripting": 7,
        "Incident Response": 8,
        "Cloud Security": 6,
    },
    "UX/UI Designer": {
        "Figma / Sketch": 9,
        "User Research": 8,
        "Prototyping": 8,
        "Visual Design": 8,
        "Usability Testing": 7,
        "HTML/CSS Basics": 5,
        "Design Systems": 7,
        "Communication": 7,
    },
    "Software Project Manager": {
        "Project Management": 9,
        "Agile / Scrum": 9,
        "Communication": 8,
        "Risk Management": 7,
        "Budgeting": 7,
        "Technical Understanding": 6,
        "Team Leadership": 8,
        "Road-mapping Tools": 7,
    },
    "Network Engineer": {
        "Networking Protocols": 9,
        "Cisco / Network Hardware": 8,
        "Network Security": 7,
        "Linux / Shell Scripting": 6,
        "Cloud Networking": 6,
        "Troubleshooting": 8,
        "Firewall Configuration": 7,
        "VPN / VoIP": 6,
    },
    "ML Engineer": {
        "Python Programming": 9,
        "Machine Learning": 9,
        "Deep Learning": 8,
        "MLOps / Model Deployment": 8,
        "Cloud Platforms": 7,
        "SQL / Databases": 6,
        "Statistics": 8,
        "Software Engineering": 7,
    },
}

# ── Learning roadmaps ─────────────────────────────────────────────────────────
ROADMAPS = {
    "Data Scientist": [
        {"phase": "Phase 1 – Foundations", "duration": "2 months", "topics": [
            "Python basics (variables, loops, functions, OOP)",
            "NumPy & Pandas for data manipulation",
            "Matplotlib & Seaborn for visualization",
            "Statistics & Probability fundamentals",
        ]},
        {"phase": "Phase 2 – Core ML", "duration": "3 months", "topics": [
            "Scikit-learn (regression, classification, clustering)",
            "Feature engineering & data preprocessing",
            "Model evaluation & cross-validation",
            "SQL for data retrieval",
        ]},
        {"phase": "Phase 3 – Advanced", "duration": "3 months", "topics": [
            "Deep Learning with TensorFlow / PyTorch",
            "NLP & Computer Vision basics",
            "Big Data tools (Spark)",
            "Cloud ML platforms (AWS SageMaker / GCP Vertex AI)",
        ]},
        {"phase": "Phase 4 – Projects & Portfolio", "duration": "2 months", "topics": [
            "Kaggle competitions",
            "End-to-end ML project on GitHub",
            "Technical blog posts",
            "Interview prep (case studies, LeetCode)",
        ]},
    ],
    "Web Developer": [
        {"phase": "Phase 1 – Foundations", "duration": "2 months", "topics": [
            "HTML5 semantics & accessibility",
            "CSS3, Flexbox, Grid, animations",
            "JavaScript ES6+ (DOM, events, async/await)",
            "Git & GitHub",
        ]},
        {"phase": "Phase 2 – Frontend Framework", "duration": "2 months", "topics": [
            "React.js (components, hooks, state management)",
            "REST API consumption with Fetch/Axios",
            "Responsive design & CSS frameworks (Tailwind)",
            "Testing basics (Jest)",
        ]},
        {"phase": "Phase 3 – Backend", "duration": "2 months", "topics": [
            "Node.js & Express.js",
            "SQL (PostgreSQL) & NoSQL (MongoDB)",
            "Authentication (JWT, OAuth)",
            "Docker basics",
        ]},
        {"phase": "Phase 4 – Deploy & Portfolio", "duration": "2 months", "topics": [
            "Deploy on Vercel / Render / AWS",
            "CI/CD with GitHub Actions",
            "Build 3 full-stack projects",
            "Portfolio website",
        ]},
    ],
    "Data Analyst": [
        {"phase": "Phase 1 – Spreadsheets & SQL", "duration": "1.5 months", "topics": [
            "Excel / Google Sheets (pivot tables, formulas, charts)",
            "SQL (SELECT, JOINs, aggregations, subqueries)",
            "Database concepts (RDBMS)",
            "Data cleaning techniques",
        ]},
        {"phase": "Phase 2 – Python for Analysis", "duration": "2 months", "topics": [
            "Python basics",
            "Pandas for data manipulation",
            "Matplotlib, Seaborn, Plotly",
            "Statistics & descriptive analytics",
        ]},
        {"phase": "Phase 3 – BI Tools", "duration": "1.5 months", "topics": [
            "Tableau or Power BI (dashboards, calculated fields)",
            "Google Data Studio",
            "Storytelling with data",
            "Presentation skills",
        ]},
        {"phase": "Phase 4 – Projects", "duration": "2 months", "topics": [
            "3 end-to-end analysis projects",
            "Kaggle datasets exploration",
            "Business case analysis",
            "GitHub portfolio",
        ]},
    ],
    "DevOps Engineer": [
        {"phase": "Phase 1 – Linux & Scripting", "duration": "2 months", "topics": [
            "Linux command line (Bash, file system, permissions)",
            "Shell scripting",
            "Git & version control workflows",
            "Networking fundamentals (TCP/IP, DNS, HTTP)",
        ]},
        {"phase": "Phase 2 – Containers & CI/CD", "duration": "2 months", "topics": [
            "Docker (images, containers, compose)",
            "Kubernetes basics (pods, deployments, services)",
            "CI/CD with Jenkins / GitHub Actions",
            "YAML configuration files",
        ]},
        {"phase": "Phase 3 – Cloud & IaC", "duration": "3 months", "topics": [
            "AWS / Azure / GCP fundamentals (get certified)",
            "Terraform for Infrastructure as Code",
            "Ansible for configuration management",
            "Cloud monitoring (CloudWatch, Prometheus, Grafana)",
        ]},
        {"phase": "Phase 4 – Security & Projects", "duration": "2 months", "topics": [
            "DevSecOps basics",
            "SRE principles",
            "Build a complete CI/CD pipeline project",
            "AWS / CKA certification",
        ]},
    ],
    "Cybersecurity Analyst": [
        {"phase": "Phase 1 – Foundations", "duration": "2 months", "topics": [
            "Networking (TCP/IP, OSI model, DNS, HTTP/S)",
            "Linux command line",
            "Security fundamentals (CIA triad, cryptography basics)",
            "CompTIA Security+ certification prep",
        ]},
        {"phase": "Phase 2 – Defensive Security", "duration": "2 months", "topics": [
            "SIEM tools (Splunk, IBM QRadar)",
            "Incident response lifecycle",
            "Log analysis & threat hunting",
            "Vulnerability management",
        ]},
        {"phase": "Phase 3 – Offensive Security", "duration": "3 months", "topics": [
            "Penetration testing fundamentals",
            "Kali Linux & common tools (Nmap, Metasploit, Burp Suite)",
            "Web application security (OWASP Top 10)",
            "CTF challenges (HackTheBox, TryHackMe)",
        ]},
        {"phase": "Phase 4 – Certifications & Career", "duration": "2 months", "topics": [
            "CEH or OSCP certification",
            "Cloud security (AWS Security Specialty)",
            "Build a home lab",
            "Bug bounty programs",
        ]},
    ],
    "UX/UI Designer": [
        {"phase": "Phase 1 – Design Foundations", "duration": "1.5 months", "topics": [
            "Design principles (typography, color theory, layout)",
            "Figma fundamentals (frames, components, auto-layout)",
            "User-centered design thinking",
            "Accessibility standards (WCAG)",
        ]},
        {"phase": "Phase 2 – UX Research & IA", "duration": "2 months", "topics": [
            "User interviews & surveys",
            "Personas & user journey maps",
            "Information architecture & card sorting",
            "Wireframing (low & high fidelity)",
        ]},
        {"phase": "Phase 3 – UI & Prototyping", "duration": "2 months", "topics": [
            "UI design patterns & design systems",
            "Interactive prototyping in Figma",
            "Usability testing & iteration",
            "Motion design basics",
        ]},
        {"phase": "Phase 4 – Portfolio", "duration": "2 months", "topics": [
            "3 complete case studies",
            "Portfolio website (Behance / personal site)",
            "HTML/CSS basics for designer-developer handoff",
            "Interview prep & community networking",
        ]},
    ],
    "Product Manager": [
        {"phase": "Phase 1 – Foundations", "duration": "1.5 months", "topics": [
            "Product thinking & strategy",
            "Agile & Scrum methodology",
            "User research techniques",
            "Competitive analysis",
        ]},
        {"phase": "Phase 2 – Execution Skills", "duration": "2 months", "topics": [
            "Writing PRDs (Product Requirements Documents)",
            "Prioritization frameworks (RICE, MoSCoW)",
            "Roadmapping tools (Jira, Asana, Notion)",
            "Data-driven decision making (SQL basics)",
        ]},
        {"phase": "Phase 3 – Stakeholder & Metrics", "duration": "2 months", "topics": [
            "Stakeholder communication & alignment",
            "OKRs & KPI setting",
            "A/B testing basics",
            "Go-to-market strategy",
        ]},
        {"phase": "Phase 4 – Portfolio & Interview", "duration": "2 months", "topics": [
            "Build a product case study",
            "Mock product critique practice",
            "PM interview prep (Amazon, Google style)",
            "Networking & LinkedIn optimization",
        ]},
    ],
    "Software Project Manager": [
        {"phase": "Phase 1 – PM Fundamentals", "duration": "2 months", "topics": [
            "PMBOK / PMP certification basics",
            "Project lifecycle (initiation, planning, execution, closure)",
            "Scope, time & cost management",
            "Risk management",
        ]},
        {"phase": "Phase 2 – Agile & Tools", "duration": "2 months", "topics": [
            "Scrum Master role & ceremonies",
            "Jira, Trello, MS Project",
            "Sprint planning & retrospectives",
            "Kanban methodology",
        ]},
        {"phase": "Phase 3 – Leadership", "duration": "2 months", "topics": [
            "Team communication & conflict resolution",
            "Vendor & contract management",
            "Budget tracking & reporting",
            "Technical literacy (APIs, databases, SDLC)",
        ]},
        {"phase": "Phase 4 – Certification & Career", "duration": "2 months", "topics": [
            "PMP or CAPM certification",
            "Agile certifications (CSM, PMI-ACP)",
            "Portfolio of projects managed",
            "Interview & salary negotiation",
        ]},
    ],
    "Network Engineer": [
        {"phase": "Phase 1 – Networking Fundamentals", "duration": "2 months", "topics": [
            "OSI & TCP/IP models",
            "IP addressing, subnetting, CIDR",
            "Routing protocols (OSPF, BGP, EIGRP)",
            "Cisco CCNA certification prep",
        ]},
        {"phase": "Phase 2 – Infrastructure", "duration": "2 months", "topics": [
            "Switching (VLANs, STP, EtherChannel)",
            "Firewalls & ACLs",
            "VPN & WAN technologies",
            "Network monitoring tools (Wireshark, SolarWinds)",
        ]},
        {"phase": "Phase 3 – Advanced & Cloud", "duration": "2 months", "topics": [
            "Software-Defined Networking (SDN)",
            "Cloud networking (AWS VPC, Azure VNet)",
            "Network automation with Python / Ansible",
            "IPv6 deployment",
        ]},
        {"phase": "Phase 4 – Certifications", "duration": "2 months", "topics": [
            "CCNP or CompTIA Network+",
            "Cloud networking certifications",
            "Build home lab (GNS3 / Cisco Packet Tracer)",
            "Interview prep",
        ]},
    ],
    "ML Engineer": [
        {"phase": "Phase 1 – Software Engineering + ML Basics", "duration": "2 months", "topics": [
            "Python OOP & software design patterns",
            "Git, testing, code quality",
            "Scikit-learn & core ML algorithms",
            "SQL & data pipelines",
        ]},
        {"phase": "Phase 2 – Deep Learning", "duration": "3 months", "topics": [
            "TensorFlow 2 / PyTorch",
            "CNNs, RNNs, Transformers",
            "Transfer learning & fine-tuning",
            "Experiment tracking (MLflow, W&B)",
        ]},
        {"phase": "Phase 3 – MLOps", "duration": "2 months", "topics": [
            "Model serving (FastAPI, TorchServe, TF Serving)",
            "Docker & Kubernetes for ML",
            "Feature stores & data versioning (DVC)",
            "Cloud ML platforms (SageMaker, Vertex AI)",
        ]},
        {"phase": "Phase 4 – Specialization & Portfolio", "duration": "2 months", "topics": [
            "Choose NLP / Vision / Recommendation specialty",
            "Contribute to open-source ML projects",
            "End-to-end deployed ML system on GitHub",
            "Interview prep (system design + coding)",
        ]},
    ],
}

# ── Common skill keywords for resume parsing ──────────────────────────────────
SKILL_KEYWORDS = [
    # Programming
    "python", "java", "javascript", "typescript", "c++", "c#", "ruby", "go", "rust", "scala",
    "kotlin", "swift", "php", "r programming",
    # Web
    "html", "css", "react", "angular", "vue", "node.js", "express", "django", "flask",
    "fastapi", "spring boot", "laravel", "jquery", "bootstrap", "tailwind",
    # Data & ML
    "machine learning", "deep learning", "tensorflow", "pytorch", "scikit-learn", "keras",
    "pandas", "numpy", "matplotlib", "seaborn", "nltk", "spacy", "computer vision",
    "nlp", "data analysis", "data science", "statistics",
    # Databases
    "sql", "mysql", "postgresql", "mongodb", "redis", "sqlite", "oracle", "nosql",
    "elasticsearch", "cassandra",
    # Cloud & DevOps
    "aws", "azure", "gcp", "docker", "kubernetes", "ci/cd", "jenkins", "terraform",
    "ansible", "linux", "bash", "git", "github", "gitlab",
    # Tools
    "tableau", "power bi", "excel", "jira", "agile", "scrum", "figma", "sketch",
    # Security
    "cybersecurity", "penetration testing", "kali linux", "network security",
    "ethical hacking", "siem", "vulnerability assessment",
    # Soft
    "communication", "leadership", "project management", "team management",
]
