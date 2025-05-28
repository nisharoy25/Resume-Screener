# 🧠 Resume Screener Tool (Python + Streamlit)

A smart resume screener built in Python using PDF/DOCX parsing, TF-IDF, spaCy, and Streamlit.

## 🚀 Features
- Upload multiple resumes
- Match against a job description
- Extract skills and experience using spaCy NER
- Upload job descriptions from `.txt` or `.docx`
- View ranked results with match scores
- Save results to CSV

## 📦 Requirements
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

## ▶️ Run the App
```bash
streamlit run app.py
```
