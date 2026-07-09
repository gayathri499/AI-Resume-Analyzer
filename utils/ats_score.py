from utils.skill_extractor import ALL_SKILLS

def calculate_ats_score(found_skills, resume_text):

    score = 0

    # Skill Score (60 Marks)
    skill_score = int((len(found_skills) / len(ALL_SKILLS)) * 60)
    score += skill_score

    text = resume_text.lower()

    # Education
    if "b.tech" in text or "b.e" in text or "bachelor" in text:
        score += 10

    # Projects
    if "project" in text:
        score += 10

    # Internship / Experience
    if "intern" in text or "experience" in text:
        score += 10

    # Certifications
    if "certificate" in text or "certification" in text:
        score += 10

    return min(score, 100)