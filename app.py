import streamlit as st
import fitz  # PyMuPDF

# Predefined skill list
SKILL_DB = [
    "Python", "Java", "SQL", "Flask", "Django", "React", "JavaScript", "Machine Learning",
    "NLP", "Git", "Docker", "HTML", "CSS", "Pandas", "NumPy", "TensorFlow"
]

def extract_text_from_pdf(uploaded_file):
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def extract_skills(text):
    extracted = set()
    for skill in SKILL_DB:
        if skill.lower() in text.lower():
            extracted.add(skill)
    return list(extracted)

def compare_skills(resume_skills, job_skills):
    resume_set = set(resume_skills)
    job_set = set(job_skills)
    matched = resume_set & job_set
    missing = job_set - resume_set
    score = round((len(matched) / len(job_set)) * 100, 2) if job_set else 0
    return score, matched, missing

# UI
st.title("AI-Powered Resume Analyzer")

uploaded_resume = st.file_uploader("Upload Your Resume (PDF)", type=["pdf"])
job_desc = st.text_area("Paste Job Description Here")

if uploaded_resume and job_desc:
    resume_text = extract_text_from_pdf(uploaded_resume)
    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_desc)

    score, matched, missing = compare_skills(resume_skills, job_skills)

    st.subheader(f"Resume Match Score: {score}%")
    st.write("**Matched Skills:**", matched)
    st.write("**Missing Skills:**", missing)

           
