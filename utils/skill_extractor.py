def extract_skills(text):

    all_skills = [
        "Python",
        "Java",
        "C",
        "C++",
        "SQL",
        "HTML",
        "CSS",
        "JavaScript",
        "Flask",
        "Django",
        "Machine Learning",
        "Deep Learning",
        "Power BI",
        "Tableau",
        "Git",
        "GitHub",
        "Excel",
        "Pandas",
        "NumPy",
        "TensorFlow",
        "Scikit-learn"
    ]

    found_skills = []

    for skill in all_skills:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    missing_skills = []

    for skill in all_skills:
        if skill not in found_skills:
            missing_skills.append(skill)

    return found_skills, missing_skills