# AI-Powered Career Recommendation System
### Final Year Project — Flask + Scikit-learn + Vanilla JS

---

## 📁 Folder Structure

```
career_ai/
├── app.py                        ← Flask entry point (run this)
├── train_model.py                ← ML model training script (run once)
├── requirements.txt
│
├── dataset/
│   └── career_data.csv           ← Training dataset (50 samples, 13 features)
│
├── models/                       ← Auto-created after training
│   ├── career_model.pkl          ← Trained Random Forest model
│   └── label_encoder.pkl         ← Label encoder for career names
│
├── routes/
│   ├── __init__.py
│   └── api_routes.py             ← All Flask REST API endpoints
│
├── services/
│   ├── __init__.py
│   ├── career_predictor.py       ← Loads .pkl model, runs prediction
│   ├── resume_parser.py          ← PDF text extraction + skill detection
│   ├── skill_gap_service.py      ← Compares user skills vs career requirements
│   └── roadmap_service.py        ← Returns phase-by-phase learning roadmap
│
├── utils/
│   ├── __init__.py
│   └── career_knowledge.py       ← Central knowledge base (skills + roadmaps)
│
└── frontend/
    ├── shared.css                ← Global styles (dark theme)
    ├── index.html                ← Home page
    ├── questionnaire.html        ← Skill rating form (13 sliders)
    ├── results.html              ← Prediction + gap + roadmap results
    └── resume.html               ← PDF upload + skill extraction
```

---

## ⚡ Setup & Run Instructions

### Step 1 — Install Python dependencies

```bash
cd career_ai
pip install -r requirements.txt
```

> **Python 3.10+** recommended.

---

### Step 2 — Train the ML model (run ONCE)

```bash
python train_model.py
```

This will:
- Read `dataset/career_data.csv`
- Train a Random Forest classifier on 13 skill features
- Save `models/career_model.pkl` and `models/label_encoder.pkl`
- Print accuracy report in terminal

Expected output:
```
✅  Test Accuracy: 100.0%
💾  Model saved  → models/career_model.pkl
💾  Encoder saved → models/label_encoder.pkl
```

---

### Step 3 — Start the Flask server

```bash
python app.py
```

Server starts at: **http://localhost:5000**

---

### Step 4 — Open in browser

Visit: **http://localhost:5000**

All 4 pages are served automatically:
| Page | URL |
|------|-----|
| Home | http://localhost:5000 |
| Questionnaire | http://localhost:5000/questionnaire.html |
| Results | http://localhost:5000/results.html |
| Resume Upload | http://localhost:5000/resume.html |

---

## 🔌 REST API Reference

All endpoints are prefixed with `/api/`

### `POST /api/predict-career`
**Input (JSON):**
```json
{
  "programming": 8, "data_analysis": 7, "machine_learning": 9,
  "web_dev": 3, "database": 6, "cloud": 5,
  "communication": 5, "project_management": 4,
  "design": 2, "networking": 3, "cybersecurity": 2,
  "math": 8, "statistics": 7
}
```
**Output:**
```json
{
  "predicted_career": "Data Scientist",
  "confidence": 87.5,
  "top3": [
    {"career": "Data Scientist", "probability": 87.5},
    {"career": "ML Engineer",    "probability": 10.0},
    {"career": "Data Analyst",   "probability": 2.5}
  ]
}
```

---

### `POST /api/analyze-resume`
**Input:** `multipart/form-data` with key `resume` (PDF file)

**Output:**
```json
{
  "skills_found": ["Python", "Machine Learning", "SQL", "Docker"],
  "word_count": 412,
  "text_snippet": "John Doe | Software Engineer..."
}
```

---

### `POST /api/skill-gap`
**Input (JSON):**
```json
{
  "career": "Data Scientist",
  "user_skills": {"programming": 8, "statistics": 7},
  "resume_skills": ["Python", "SQL"]
}
```
**Output:**
```json
{
  "career": "Data Scientist",
  "present_skills": ["Python Programming", "Statistics"],
  "missing_skills": ["Deep Learning", "Cloud Platforms"],
  "match_score": 62.5,
  "gap_details": [...]
}
```

---

### `POST /api/roadmap`
**Input (JSON):**
```json
{
  "career": "Web Developer",
  "missing_skills": ["React", "Docker"]
}
```
**Output:**
```json
{
  "career": "Web Developer",
  "phases": [...],
  "highlighted": ["React.js (components, hooks, state management)", "Docker basics"],
  "total_duration": "8 months"
}
```

---

### `GET /api/careers`
Returns list of all supported careers.

---

## 🧠 Machine Learning Details

| Property | Value |
|----------|-------|
| Algorithm | Random Forest Classifier |
| Library | Scikit-learn |
| Features | 13 skill dimensions (1–10 scale) |
| Training samples | 50 (5 per career × 10 careers) |
| Model file | `models/career_model.pkl` |

**Supported Careers:**
- Data Scientist
- Web Developer
- Data Analyst
- DevOps Engineer
- Product Manager
- Cybersecurity Analyst
- UX/UI Designer
- Software Project Manager
- Network Engineer
- ML Engineer

---

## 🛠 Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python 3.10, Flask 2.x |
| ML | Scikit-learn (Random Forest) |
| PDF Parsing | PyPDF2 |
| Frontend | HTML5, CSS3, Vanilla JavaScript |
| Fonts | Syne + Space Mono (Google Fonts) |
| Data | Pandas, NumPy |
| Model Storage | Pickle (.pkl) |

---

## 🎓 Project Modules Summary

1. **ML Career Predictor** — `services/career_predictor.py` — loads pkl, returns top-3 predictions
2. **Resume Analyser** — `services/resume_parser.py` — PDF → text → skill keywords
3. **Skill Gap Engine** — `services/skill_gap_service.py` — compares user vs required skills
4. **Roadmap Generator** — `services/roadmap_service.py` — phase-by-phase learning plan
5. **Knowledge Base** — `utils/career_knowledge.py` — skills matrix + roadmap data
6. **REST API** — `routes/api_routes.py` — 5 Flask endpoints
7. **Frontend** — 4 HTML pages with shared CSS + Vanilla JS

---

## ❗ Troubleshooting

**"Model not found" error:**
→ Run `python train_model.py` first.

**PDF upload returns empty skills:**
→ Ensure the PDF has selectable text (not a scanned image). Try copy-pasting text from the PDF to verify.

**CORS error in browser:**
→ Make sure you're accessing via `http://localhost:5000`, not opening the HTML file directly from disk.

**Port already in use:**
→ Change the port in `app.py`: `app.run(debug=True, port=5001)`
