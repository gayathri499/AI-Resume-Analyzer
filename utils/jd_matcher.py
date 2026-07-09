import re

def calculate_match(resume_text, job_description):

    resume_words = set(re.findall(r'\w+', resume_text.lower()))
    jd_words = set(re.findall(r'\w+', job_description.lower()))

    if not jd_words:
        return 0

    common = resume_words.intersection(jd_words)

    score = int((len(common) / len(jd_words)) * 100)

    return min(score, 100)