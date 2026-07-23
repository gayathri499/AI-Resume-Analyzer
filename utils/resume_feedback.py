def generate_feedback(ats_score, match_score, found_skills, missing_skills):

    feedback = []

    if ats_score < 60:
        feedback.append("Improve resume formatting.")

    if match_score < 70:
        feedback.append("Resume does not match the Job Description well.")

    if len(found_skills) < 5:
        feedback.append("Add more technical skills.")

    if missing_skills:
        feedback.append(
            "Missing Skills: " + ", ".join(missing_skills)
        )

    feedback.append("Add measurable achievements.")

    feedback.append("Include GitHub profile.")

    feedback.append("Include LinkedIn profile.")

    feedback.append("Add certifications.")

    feedback.append("Mention internships.")

    feedback.append("Use strong action verbs.")

    feedback.append("Highlight important projects.")

    return feedback