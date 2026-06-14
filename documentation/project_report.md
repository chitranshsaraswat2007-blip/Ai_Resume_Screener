# AI Resume Screening & Candidate Ranking System
## Project Documentation & Report

---

## 1. Introduction

In today's competitive job market, companies receive hundreds of resumes for a single job posting. Manually reviewing each resume is time-consuming, inconsistent, and prone to human bias. This project presents an **AI-powered Resume Screening System** that automates the process of evaluating and ranking candidates based on how well their resumes match a given job description.

---

## 2. Objective

The primary objectives of this project are:

- To automatically extract text from PDF resumes
- To preprocess and clean the extracted text for NLP analysis
- To calculate a similarity score between each resume and the job description
- To rank all candidates from best match to least match
- To provide a simple, user-friendly web interface for the entire process

---

## 3. Technologies Used

| Technology | Purpose |
|---|---|
| Python 3.x | Core programming language |
| PyPDF2 | PDF text extraction |
| Scikit-learn | TF-IDF vectorization & Cosine Similarity |
| Pandas | Data manipulation and ranking tables |
| Streamlit | Web application frontend |
| re (regex) | Text cleaning and preprocessing |

---

## 4. Methodology

### Step 1: Text Extraction
- Resumes uploaded as PDF files are read using `PyPDF2.PdfReader`
- Text is extracted page by page from each PDF
- Handles empty or corrupted files gracefully

### Step 2: Text Preprocessing
The extracted text goes through the following cleaning steps:
1. Convert to lowercase
2. Remove punctuation
3. Remove numbers
4. Remove special symbols
5. Remove extra whitespace

### Step 3: TF-IDF Vectorization
- Both the job description and each resume are converted into numerical vectors using **TF-IDF (Term Frequency - Inverse Document Frequency)**
- TF-IDF gives higher weight to words that are important and unique to a document

### Step 4: Cosine Similarity
- The similarity between the job description vector and each resume vector is calculated using **Cosine Similarity**
- Score ranges from 0 (no match) to 1 (perfect match), expressed as a percentage

### Step 5: Ranking
- All candidates are sorted from highest similarity score to lowest
- Results are displayed in a ranked table with match status labels

---

## 5. System Architecture

```
┌─────────────┐     ┌──────────────────┐     ┌────────────────────┐
│  User Input  │────►│  Preprocessing   │────►│    AI Engine       │
│ (PDF + JD)  │     │ extractor.py     │     │ similarity.py      │
└─────────────┘     │ cleaner.py       │     │ ranking.py         │
                    └──────────────────┘     └────────────────────┘
                                                        │
                    ┌──────────────────────────────────▼──┐
                    │         Streamlit Frontend (app.py)  │
                    │   Upload → Analyze → View Rankings   │
                    └──────────────────────────────────────┘
```

---

## 6. Results

### Sample Test Results

| Rank | Candidate | Match Score | Status |
|---|---|---|---|
| 1 | Candidate_A (Python/ML Dev) | 91.0% | 🟢 Strong Match |
| 2 | Candidate_C (Data Scientist) | 78.5% | 🟢 Strong Match |
| 3 | Candidate_B (Java Developer) | 23.4% | 🔴 Weak Match |

**Observation:** Candidates with skills closely matching the job description (Python, ML, Data Science) receive significantly higher scores than unrelated profiles (Java development).

---

## 7. Conclusion

The AI Resume Screening System successfully automates candidate evaluation using NLP techniques. The TF-IDF + Cosine Similarity approach provides a reliable, fast, and unbiased method for initial screening. The Streamlit interface makes it accessible to non-technical HR users.

Key achievements:
- ✅ Automated PDF text extraction
- ✅ Intelligent text cleaning pipeline
- ✅ Accurate similarity scoring
- ✅ Clear candidate ranking table
- ✅ User-friendly web interface

---

## 8. Future Scope

1. **Semantic Understanding** — Use BERT or sentence transformers for deeper meaning-based matching
2. **Multi-format Support** — Accept DOCX, TXT, and image-based resumes (with OCR)
3. **Skills Extraction** — Use Named Entity Recognition (NER) to extract specific skills
4. **Database Integration** — Store candidates and job postings in a database
5. **Email Automation** — Notify shortlisted candidates automatically
6. **Admin Dashboard** — Analytics and historical comparison of candidates

---

## Viva Questions & Answers

**Q1: What is TF-IDF?**
A: TF-IDF stands for Term Frequency-Inverse Document Frequency. TF measures how often a word appears in a document. IDF reduces the weight of common words that appear everywhere. Together, they create numerical vectors that represent document content.

**Q2: What is Cosine Similarity?**
A: Cosine Similarity measures the angle between two text vectors. A score of 1.0 means identical documents, 0.0 means completely unrelated. It's preferred for text comparison because it's independent of document length.

**Q3: Why do you preprocess the text?**
A: Raw text contains noise — punctuation, numbers, symbols — that don't help in comparing documents. Cleaning the text ensures that the TF-IDF algorithm focuses on meaningful words only.

**Q4: What library is used for PDF extraction?**
A: PyPDF2 is used to read PDF files page by page and extract their text content.

**Q5: What does a 75% similarity score mean?**
A: It means 75% of the important keywords in the job description were also found in the resume. Higher scores indicate better candidate matches.

**Q6: Why Streamlit for the frontend?**
A: Streamlit allows building interactive web applications entirely in Python without needing HTML/CSS/JavaScript knowledge. It's ideal for data science and AI projects.

**Q7: How would you improve this system?**
A: Future improvements include using BERT for semantic understanding, adding OCR for scanned PDFs, extracting named entities like skills and experience, and adding a candidate database.

---

## PPT Slide Content Outline

1. **Title Slide** — AI Resume Screening & Candidate Ranking System
2. **Problem Statement** — Manual resume screening is slow and biased
3. **Solution** — Automated AI-powered screening using NLP
4. **Technologies** — Python, PyPDF2, Scikit-learn, Streamlit
5. **System Architecture** — Flow diagram
6. **How TF-IDF Works** — Simple explanation with example
7. **How Cosine Similarity Works** — Visual angle explanation
8. **Demo Screenshots** — Upload page, results table, bar chart
9. **Results** — Sample ranking table
10. **Conclusion & Future Scope**
