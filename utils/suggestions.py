def generate_suggestions(match_score):

    suggestions = []

    if match_score >= 80:
        suggestions.append("Excellent resume for this job.")
        suggestions.append("Keep your GitHub and LinkedIn updated.")

    elif match_score >= 60:
        suggestions.append("Add more relevant technical skills.")
        suggestions.append("Mention projects related to this role.")

    else:
        suggestions.append("Improve your resume based on the job description.")
        suggestions.append("Add certifications.")
        suggestions.append("Include internships and achievements.")

    return suggestions