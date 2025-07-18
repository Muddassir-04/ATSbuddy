# 🤖 ATSBuddy - Resume Keyword Analyzer

ATSBuddy is an AI-powered resume analyzer that compares your resume with a job description and calculates the keyword match percentage. It simulates how an Applicant Tracking System (ATS) might evaluate your resume.

---

## 📌 Features

- 📄 Upload Resume (PDF)
- 📝 Paste Job Description
- 🧠 Extract and Compare Keywords
- 📊 Match Score & Summary
- ✅ Highlighted Matching Keywords
- 🎯 Built with Streamlit

---



---

## 🚀 Live Demo

👉 [Click here to try ATSBuddy on Streamlit](https://atsbuddy.streamlit.app/) 

---

## 🛠️ Tech Stack

- Python 🐍
- Streamlit 📊
- spaCy (NLP) 🧠
- PyPDF2 / pdfplumber 📄

---

## 📂 Project Structure

```bash
atsbuddy/
├── app.py                  # Streamlit app
├── resume_utils.py         # Keyword extraction & matching logic
├── requirements.txt        # Dependencies
├── example_resume.pdf      # Sample resume
├── samples/
│   ├── sample_jd.txt
│   └── sample_resume.pdf
└── README.md


 ##  📥 Installation
git clone https://github.com/Muddassir-04/ATSbuddy.git
cd ATSbuddy
pip install -r requirements.txt
streamlit run app.py


📌 Note
This is a portfolio project and is still under development. Keyword matching can be improved further with NLP techniques like Named Entity Recognition (NER) and context-aware embeddings.

👤 Author
Mohd Muddassir Ahmed
📧 LinkedIn | 🐙 GitHub


