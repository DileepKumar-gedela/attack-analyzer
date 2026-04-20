ATT&CK Pattern Finder (AI-Based)

A full-stack cybersecurity analysis tool that processes unstructured threat reports and maps them to MITRE ATT&CK techniques using semantic similarity and NLP-based embeddings.

---

🚀 Features
Threat Report Analysis
Upload or paste cyber threat reports and automatically extract attack patterns using NLP models.

Semantic Similarity Engine
Uses sentence-transformers to identify ATT&CK techniques based on contextual meaning rather than keyword matching.

Interactive Visualizations
Dynamic charts (Pie, Bar, Heatmap) to represent:

* Technique confidence levels
* Tactic distribution
* Attack trends

MITRE ATT&CK Mapping
Maps detected behaviors to standardized MITRE ATT&CK tactics and techniques.

Risk Scoring
Assigns risk levels based on detected attack patterns and similarity scores.

Mitigation Suggestions
Provides recommended actions based on identified techniques.

---

🧠 Tech Stack

Frontend:

* React.js (Vite)
* TailwindCSS
* Recharts (Data Visualization)

Backend:

* FastAPI (Python)
* Sentence-Transformers (NLP Embeddings)
* Scikit-learn (Similarity Computation)
* PyPDF2 (Text Extraction)

---

🏗️ Architecture Overview

Frontend (React + Tailwind + Recharts)
↓
Backend API (FastAPI)
↓
Text Processing & Embedding Engine
↓
Semantic Similarity Matching
↓
MITRE ATT&CK Mapping & Risk Analysis
↓
Visualization Output

---

⚙️ Setup Instructions

🔹 Backend Setup (FastAPI)

```bash
cd backend
python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
```

Run the backend:

```bash
uvicorn app.main:app --reload
```

Backend runs at:
👉 http://127.0.0.1:8000

---

🔹 Frontend Setup (React)

```bash
cd frontend
npm install
npm run dev
```

Frontend runs at:
👉 http://localhost:5173

---

📂 Project Structure

```
attack-analyzer/
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── routes/
│   │   ├── services/
│   │   └── utils/
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   └── package.json
│
└── README.md
```

---

📊 Output Visualizations

The system generates:

* Technique Confidence Graph
* Tactic Distribution Chart
* Attack Trend Graph
* Semantic Similarity Heatmap
* MITRE ATT&CK Matrix View
* Mitigation Recommendations

---

🎯 Use Case

This tool is designed for:

* Security Analysts
* SOC Teams
* Cybersecurity Researchers
* Students working on threat intelligence projects

It reduces manual effort in analyzing long threat reports and provides structured, actionable insights.

---

🔐 Future Enhancements

* Real-time threat monitoring
* Integration with SIEM tools
* Support for malware and network logs
* Explainable AI for decision transparency

---

📌 Note

This project performs all analysis locally using NLP models and does not depend on external APIs, ensuring privacy and offline usability.

---
