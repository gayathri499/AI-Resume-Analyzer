from utils.skill_extractor import ALL_SKILLS


def calculate_ats_score(found_skills):

    total_skills = len(ALL_SKILLS)

    score = int((len(found_skills) / total_skills) * 100)

    return score