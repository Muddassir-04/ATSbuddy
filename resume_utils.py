import pdfplumber
import re
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ✅ Download required NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# ✅ Extract text from uploaded PDF
def extract_text_from_pdf(uploaded_file):
    with pdfplumber.open(uploaded_file) as pdf:
        text = ''
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
    return text

# ✅ Extract keywords from text (with stopword removal)
def extract_keywords(text):
    stop_words = set(stopwords.words('english'))
    custom_exclude = {
        "job", "work", "skills", "ability", "experience", "full", "phone",
        "good", "required", "tools", "data", "team", "training", "role"
    }

    tokens = re.findall(r'\b[a-zA-Z]{3,}\b', text.lower())  # only words with 3+ letters
    words = [word for word in tokens if word not in stop_words and word not in custom_exclude]
    return set(words)


# ✅ TF-IDF vector creation
def get_tfidf_vectors(resume_text, job_desc_text):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume_text, job_desc_text])
    return vectors

# ✅ Cosine similarity-based match score
def calculate_similarity(resume_text, job_desc_text):
    vectors = get_tfidf_vectors(resume_text, job_desc_text)
    similarity = cosine_similarity(vectors[0], vectors[1])
    return round(float(similarity[0][0]) * 100, 2)

# ✅ Get matched keywords
def get_matched_keywords(resume_text, job_desc_text):
    resume_keywords = extract_keywords(resume_text)
    jd_keywords = extract_keywords(job_desc_text)
    return resume_keywords.intersection(jd_keywords)


