def get_resume_suggestions(score, missing_skills):

    suggestions = []

    if score < 60:
        suggestions.append("Increase the number of relevant technical skills.")
        suggestions.append("Add internships or work experience.")
        suggestions.append("Include certifications.")

    elif score < 80:
        suggestions.append("Improve your project descriptions.")
        suggestions.append("Add measurable achievements.")
        suggestions.append("Tailor your resume to the job description.")

    else:
        suggestions.append("Excellent resume. Keep it updated.")
        suggestions.append("Customize your resume for each job application.")

    if missing_skills:
        suggestions.append(
            "Consider learning: " + ", ".join(missing_skills[:5])
        )

    return suggestions