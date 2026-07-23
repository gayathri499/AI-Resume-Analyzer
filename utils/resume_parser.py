import re


def extract_candidate_details(text):

    details = {
        "name": "Not Found",
        "email": "Not Found",
        "phone": "Not Found",
        "github": "Not Found",
        "linkedin": "Not Found",
        "location": "Not Found"
    }

    # Email
    email = re.search(
        r'[\w\.-]+@[\w\.-]+\.\w+',
        text
    )

    if email:
        details["email"] = email.group()

    # Phone
    phone = re.search(
        r'(\+91[- ]?)?[6-9]\d{9}',
        text
    )

    if phone:
        details["phone"] = phone.group()

    # GitHub
    github = re.search(
        r'github\.com/[A-Za-z0-9_-]+',
        text,
        re.IGNORECASE
    )

    if github:
        details["github"] = github.group()

    # LinkedIn
    linkedin = re.search(
        r'linkedin\.com/in/[A-Za-z0-9_-]+',
        text,
        re.IGNORECASE
    )

    if linkedin:
        details["linkedin"] = linkedin.group()

    # Name (first non-empty line)
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    if lines:
        details["name"] = lines[0]

    return details