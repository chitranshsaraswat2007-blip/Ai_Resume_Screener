# 📄 AI Resume Screening & Candidate Ranking System

An intelligent system that automatically screens resumes and ranks candidates based on how well they match a given job description.

---

## 👥 Team

| Programmer | Role |
|---|---|
| Programmer 1 | Resume Text Extraction & Preprocessing |
| Programmer 2 | AI Similarity & Candidate Ranking |
| Programmer 3 | Frontend & User Interface (Streamlit) |
| Programmer 4 | Testing, Integration & Documentation |

---

## 📁 Project Structure

```
project/
├── app.py                      # Main Streamlit web application (Programmer 3)
├── test_project.py             # Integration tests (Programmer 4)
├── requirements.txt            # Python dependencies
├── README.md                   # This file
│
├── preprocessing/              # Programmer 1's module
│   ├── __init__.py
│   ├── extractor.py            # PDF text extraction
│   └── cleaner.py              # Text cleaning & preprocessing
│
├── ai_engine/                  # Programmer 2's module
│   ├── __init__.py
│   ├── similarity.py           # TF-IDF + Cosine Similarity
│   └── ranking.py              # Candidate ranking logic
│
├── documentation/              # Project docs (Programmer 4)
├── report/                     # Final report
└── screenshots/                # App screenshots
```

---

## ⚙️ Setup Instructions

### Step 1: Install Python
Make sure Python 3.8 or higher is installed.
Check with: `python --version`

### Step 2: Install Required Libraries

```bash
pip install -r requirements.txt
```

### Step 3: Run the Web Application

```bash
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`

### Step 4: Run Integration Tests

```bash
python test_project.py
```

---

## 🚀 How to Use the App

1. Open the app in your browser (`streamlit run app.py`)
2. **Upload Resumes** — Click "Choose PDF files" and upload one or more PDF resumes
3. **Enter Job Description** — Paste the job description in the text area
4. **Click "Analyze Resumes"** — The system will process and rank all candidates
5. **View Results** — See the ranking table and bar chart showing match scores

---

## 🧠 How It Works

```
PDF Resumes ──► Extract Text ──► Clean Text ──► TF-IDF Vectors ──► Cosine Similarity ──► Ranked Results
```

1. **Text Extraction** (`extractor.py`): Reads PDF files using PyPDF2 and extracts all text
2. **Text Cleaning** (`cleaner.py`): Removes numbers, punctuation, symbols; converts to lowercase
3. **TF-IDF Vectorization** (`similarity.py`): Converts text into numerical vectors
4. **Cosine Similarity** (`similarity.py`): Measures how similar each resume is to the job description
5. **Ranking** (`ranking.py`): Sorts candidates from highest to lowest match score

---

## 📦 Requirements

```
PyPDF2==3.0.1
scikit-learn==1.3.0
pandas==2.0.3
streamlit==1.28.0
```

---

## 🔍 Match Score Interpretation

| Score | Meaning |
|---|---|
| 70% - 100% | 🟢 Strong Match — Highly recommended |
| 40% - 69% | 🟡 Moderate Match — Consider with review |
| 0% - 39% | 🔴 Weak Match — May not be a good fit |

---

## ⚠️ Known Limitations

- Only supports PDF format resumes
- Scanned/image-based PDFs may not extract text correctly
- Results depend on keyword overlap, not deep semantic understanding

---

## 🔮 Future Scope

- Support for DOCX format resumes
- BERT/GPT-based semantic similarity (beyond keyword matching)
- Email notification to selected candidates
- Database storage for candidate history
- Admin dashboard with analytics
