from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def generate_report(filename, score, match_score, skills, missing_skills, jobs):

    doc = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph("<b>AI Resume Analyzer Report</b>", styles["Title"]))
    story.append(Paragraph(f"<b>ATS Score:</b> {score}%", styles["Normal"]))
    story.append(Paragraph(f"<b>Resume vs JD Match:</b> {match_score}%", styles["Normal"]))

    story.append(Paragraph("<br/><b>Skills Found</b>", styles["Heading2"]))
    for skill in skills:
        story.append(Paragraph(f"• {skill}", styles["Normal"]))

    story.append(Paragraph("<br/><b>Missing Skills</b>", styles["Heading2"]))
    for skill in missing_skills:
        story.append(Paragraph(f"• {skill}", styles["Normal"]))

    story.append(Paragraph("<br/><b>Recommended Jobs</b>", styles["Heading2"]))
    for job in jobs:
        story.append(Paragraph(f"• {job}", styles["Normal"]))

    doc.build(story)