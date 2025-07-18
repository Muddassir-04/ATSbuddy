# ATSBuddy — AI-Powered Resume Analyzer

**ATSBuddy** is a smart Streamlit-based web application that helps job seekers **optimize their resumes** by comparing them to any job description and highlighting matched keywords. It provides a **match score** using NLP techniques such as **TF-IDF vectorization** and **cosine similarity**.

> ⚠️ *This project is currently under development. The keyword matching algorithm will be further improved to deliver more accurate and meaningful results.*

---

## 💪 Built With

* **Python**
* **Streamlit**
* **Scikit-learn** (for TF-IDF and cosine similarity)
* **pdfplumber** (for extracting text from resumes)
* **Regex** (for keyword extraction)

---

## 🚀 Features

* 📅 Upload resume as PDF
* 📕 Paste any job description
* 📊 Get real-time **match score** between resume and JD
* ✅ View **matched keywords**
* 🚀 Minimal, responsive UI built with Streamlit

---

## 🔬 How It Works

1. **Upload Resume**: Upload your resume in PDF format.
2. **Paste JD**: Paste the job description into the provided field.
3. **Analyze**: The app uses **TF-IDF vectorization** to compare the semantic similarity between the resume and the job description.
4. **Match Score**: Displays a similarity score (0-100%) and lists the matched keywords.

---

## 📙 Example Use Case

```
Job Description:
"Proficiency with Microsoft Excel (VLOOKUP, Pivot Tables), good communication skills, and experience in dashboarding."

Resume PDF:
Includes: "Experienced in using Excel formulas, pivot tables, and building dashboards."

Match Score: ~75%
Matched Keywords: excel, pivot, dashboard
```

---

## 💡 Future Improvements

* Refine keyword extraction using POS tagging (nouns, verbs only)
* Add PDF export of match report
* Add LinkedIn integration to fetch job descriptions automatically
* Improve UI with animations and dashboard visuals

---

## 🚫 Disclaimer

This is an academic/portfolio project to demonstrate Natural Language Processing techniques in the context of resume analysis. It is **not meant for production-level ATS systems**.

---

## 💼 Author

**Mohd Muddassir Ahmed**
[LinkedIn](https://www.linkedin.com/in/muddassir-ahmed-715393260?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app) | [GitHub](https://github.com/Muddassir-04)

---

## 📁 Project Setup

```bash
# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install requirements
pip install -r requirements.txt

# Run Streamlit app
streamlit run app.py
```

---


---

## 🚩 License

This project is licensed under the MIT License.
