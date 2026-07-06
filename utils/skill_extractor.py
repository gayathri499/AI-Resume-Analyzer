ALL_SKILLS = [
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
    "Scikit-learn",
    "Docker",
    "AWS",
    "React"
]


def extract_skills(text):

    found_skills = []

    for skill in ALL_SKILLS:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    missing_skills = []

    for skill in ALL_SKILLS:
        if skill not in found_skills:
            missing_skills.append(skill)

    return found_skills, missing_skills