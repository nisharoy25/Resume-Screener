import pdfplumber
from docx import Document
import os
import spacy
import re
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
from flashtext import KeywordProcessor

nlp = spacy.load("en_core_web_sm")

def extract_text(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    if ext == '.pdf':
        with pdfplumber.open(file_path) as pdf:
            return ''.join([page.extract_text() or '' for page in pdf.pages])
    elif ext == '.docx':
        doc = Document(file_path)
        return '\n'.join([p.text for p in doc.paragraphs])
    else:
        raise ValueError("Unsupported file type")

def extract_ner_entities(text):
    doc = nlp(text)
    entities = {
        "PERSON": [],
        "ORG": [],
        "SKILL": [],
        "EXPERIENCE": []
    }
    for ent in doc.ents:
        if ent.label_ in entities:
            entities[ent.label_].append(ent.text)
    return entities

SKILL_DB = ["Python", "Java", "SQL", "Django", "React", "Machine Learning", "Excel", "python", "java", "c++", "sql", "nosql", "mongodb", "postgresql", "aws", "azure",
    "GCP", "Docker", "Kubernetes", "Linux", "Git", "Angular", "Node.js",
    "Machine Learning", "Data Analysis", "Tensorflow", "Pandas", "Numpy", "HTML", "CSS"]

def extract_skills(text):
    kp = KeywordProcessor()
    for skill in SKILL_DB:
        kp.add_keyword(skill)
    return list(set(kp.extract_keywords(text)))

def extract_years_of_experience(text):
    matches = re.findall(r"(\d+(\.\d+)?)\+?\s*years?", text, re.IGNORECASE)
    if matches:
        years = [float(match[0]) for match in matches]
        return max(years)
    return 0.0


