import streamlit as st
from utils import extract_text_from_pdf, analyze_resume

st.set_page_config(page_title="AI Resume Analyzer", layout="wide")

st.title("📄 AI Resume Analyzer")


uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])


job_desc = st.text_area("Paste Job Description")

if uploaded_file and job_desc:
    with st.spinner("Analyzing Resume..."):
        resume_text = extract_text_from_pdf(uploaded_file)
        result = analyze_resume(resume_text, job_desc)

    st.subheader("📊 Analysis Result")
    st.write(result)

else:
    st.info("Upload a resume and enter job description to proceed.")