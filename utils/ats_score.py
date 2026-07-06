def calculate_ats_score(found_skills):

    total_skills = 21

    score = int((len(found_skills) / total_skills) * 100)

    return score