# 🔍 Smart Resume Screening Tool

This project is an AI-powered tool built to match resumes against job descriptions using NLP techniques.

## 👩‍💼 Developed By:
**Jigyasha Chouhan**

---

## ✅ Your Approach

1. Accepts a job description and multiple resumes (PDF/JPEG).
2. Uses `pdfplumber` for PDFs and `pytesseract` for image OCR.
3. Applies **TF-IDF Vectorization** on job description and resumes.
4. Measures similarity using **cosine similarity**.
5. Displays ranked output with scores, progress bars, and medals for top resumes.

---

## 🧰 Libraries Used

- `streamlit` – Web interface
- `pdfplumber` – PDF text extraction
- `Pillow` & `pytesseract` – OCR for JPEG files
- `scikit-learn` – TF-IDF & cosine similarity
- `pandas` – Data handling
- `nltk` – Stopword support (optional)

---

## 🚀 How to Run This Project

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/resume-screener.git
cd resume-screener
