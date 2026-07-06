def recommend_jobs(found_skills):

    jobs = []

    skills = [skill.lower() for skill in found_skills]

    if "python" in skills:
        jobs.append("Python Developer")

    if "sql" in skills:
        jobs.append("Data Analyst")

    if "machine learning" in skills:
        jobs.append("Machine Learning Engineer")

    if "deep learning" in skills:
        jobs.append("AI Engineer")

    if "power bi" in skills:
        jobs.append("Business Intelligence Analyst")

    if "tableau" in skills:
        jobs.append("Data Visualization Engineer")

    if len(jobs) == 0:
        jobs.append("Software Engineer")

    return jobs