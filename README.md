# 📄 Resume Screener Tool

A resume screening tool built using **Python**, **Streamlit**, **spaCy**, and **scikit-learn** that matches resumes to a job description based on skills and experience.

---

## 🚀 Features

- Upload or paste a job description (supports `.txt` and `.docx`)
- Upload multiple resumes in `.pdf` or `.docx`
- Extracts:
  - Relevant **skills**
  - **Experience** in years
- Computes a **match score** based on:
  - Skill match (70%)
  - Experience match (30%)
- Displays missing skills and saves results in `output/results.csv`

---

## 📂 How to Run

```bash
# 1. Clone the repository
git clone https://github.com/your-username/resume-screener.git
cd resume-screener

# 2. Install dependencies
pip install -r requirements.txt

# 3. Download spaCy model
python -m spacy download en_core_web_sm

# 4. Run the app
streamlit run app.py
