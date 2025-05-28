import streamlit as st
import os
from parser import extract_text, extract_years_of_experience, extract_skills
from matcher import calculate_final_score, get_missing_skills
import pandas as pd
from docx import Document

st.title("📄 Resume Screener Tool")

jd_option = st.radio("📄 Job Description Input", ["Paste manually", "Upload (.txt or .docx)"])

jd_text = ""
if jd_option == "Paste manually":
    jd_text = st.text_area("📝 Paste Job Description")
else:
    jd_file = st.file_uploader("📂 Upload Job Description", type=["txt", "docx"])
    if jd_file:
        ext = os.path.splitext(jd_file.name)[1].lower()
        if ext == ".txt":
            jd_text = jd_file.read().decode()
        elif ext == ".docx":
            doc = Document(jd_file)
            jd_text = "\n".join([p.text for p in doc.paragraphs])

uploaded_files = st.file_uploader("📂 Upload Resumes (PDF/DOCX)", type=["pdf", "docx"], accept_multiple_files=True)

if st.button("🔍 Screen Resumes"):
    if not jd_text or not uploaded_files:
        st.warning("Please provide both job description and resumes.")
    else:
        jd_skills = extract_skills(jd_text)
        jd_required_exp = extract_years_of_experience(jd_text)

        st.info(f"🧠 Extracted JD Skills: {', '.join(jd_skills)}")
        st.info(f"📈 Required Experience (approx): {jd_required_exp} years")

        results = []

        os.makedirs("resumes", exist_ok=True)

        for uploaded_file in uploaded_files:
            file_path = os.path.join("resumes", uploaded_file.name)
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            resume_text = extract_text(file_path)
            resume_skills = extract_skills(resume_text)
            resume_exp = extract_years_of_experience(resume_text)

            score = calculate_final_score(resume_skills, jd_skills, resume_exp, jd_required_exp)
            missing_skills = get_missing_skills(resume_skills, jd_skills)

            results.append({
                "Resume": uploaded_file.name,
                "Match Score (%)": score,
                "Skills Found": ", ".join(resume_skills),
                "Missing Skills": ", ".join(missing_skills),
                "Experience (Years)": resume_exp
            })

        df = pd.DataFrame(results).sort_values(by="Match Score (%)", ascending=False)
        st.dataframe(df)

        os.makedirs("output", exist_ok=True)
        df.to_csv("output/results.csv", index=False)
        st.success("✅ Results saved to `output/results.csv`")