import streamlit as st
import base64
from resume_utils import extract_text_from_pdf, extract_keywords, calculate_similarity, get_matched_keywords

# --- Page Setup ---
st.set_page_config(page_title="ATSBuddy - Resume Matcher", layout="centered")

# --- Custom CSS Styling ---
st.markdown(
    """
    <style>
        .main {
            background-color: #f5f7fa;
            padding: 2rem;
            border-radius: 10px;
        }
        h1, h2, h3 {
            color: #2C3E50;
        }
        .stButton > button {
            background-color: #2ECC71;
            color: white;
            font-weight: bold;
            border-radius: 8px;
            padding: 0.4em 1em;
            margin-top: 10px;
        }
        .stMetric {
            font-size: 18px !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Title ---
st.title("📄 ATSBuddy - Resume Keyword Analyzer")

# --- File Upload Section ---
st.subheader("Upload Your Resume and Job Description")
resume_file = st.file_uploader("📎 Upload your Resume (PDF)", type=["pdf"])
job_description = st.text_area("📝 Paste the Job Description Here")

# --- Analyze Button ---
if st.button("🔍 Analyze Resume"):
    if resume_file and job_description.strip() != "":
        with st.spinner("Processing... Please wait..."):
            # Extract text and keywords
            resume_text = extract_text_from_pdf(resume_file)
            jd_text = job_description

            resume_keywords = extract_keywords(resume_text)
            jd_keywords = extract_keywords(jd_text)

            match_percentage = calculate_similarity(resume_text, jd_text)
            matched_keywords = get_matched_keywords(resume_text, jd_text)

        # --- Results ---
        st.success("✅ Analysis Complete!")

        st.subheader("📊 Match Summary")
        st.metric(label="🎯 Match Score", value=f"{match_percentage}%")
        st.markdown(f"**Total JD Keywords:** {len(jd_keywords)}")
        st.markdown(f"**Matched Keywords:** {len(matched_keywords)}")

        if matched_keywords:
            st.markdown("✅ **Matched Keywords:**")
            st.write(", ".join(matched_keywords))
        else:
            st.warning("❗ No matching keywords found. Try updating your resume.")

    else:
        st.warning("⚠️ Please upload a resume and enter the job description before analyzing.")

# --- Sample Resume/Job Description Downloads ---
st.markdown("---")
st.subheader("📥 Try with Sample Files")

def get_download_link(file_path, file_label):
    try:
        with open(file_path, "rb") as f:
            data = f.read()
        b64 = base64.b64encode(data).decode()
        return f'<a href="data:application/octet-stream;base64,{b64}" download="{file_label}">{file_label}</a>'
    except FileNotFoundError:
        return f"❌ {file_label} not found."

sample_resume_link = get_download_link("samples/sample_resume.pdf", "Sample Resume")
sample_jd_link = get_download_link("samples/sample_jd.txt", "Sample Job Description")

st.markdown(f"📄 {sample_resume_link} | 📃 {sample_jd_link}", unsafe_allow_html=True)
