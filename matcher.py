def calculate_final_score(resume_skills, jd_skills, resume_exp, jd_required_exp):
    skill_score = len(set(resume_skills) & set(jd_skills)) / len(jd_skills) if jd_skills else 0
    exp_score = min(resume_exp / jd_required_exp, 1.0) if jd_required_exp else 1.0
    return round((0.7 * skill_score + 0.3 * exp_score) * 100, 2)


def get_missing_skills(resume_skills, jd_skills):
    return list(set(jd_skills) - set(resume_skills))