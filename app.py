from flask import Flask, render_template, request
import os

from utils.pdf_reader import read_pdf
from utils.skill_extractor import extract_skills
from utils.ats_score import calculate_ats_score
from utils.job_recommender import recommend_jobs

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():

    file = request.files["resume"]

    if not file:
        return "No file selected"

    filepath = os.path.join("uploads", file.filename)
    file.save(filepath)

    text = read_pdf(filepath)

    found_skills, missing_skills = extract_skills(text)

    score = calculate_ats_score(found_skills, text)

    jobs = recommend_jobs(found_skills)

    return render_template(
        "result.html",
        score=score,
        skills=found_skills,
        missing_skills=missing_skills,
        jobs=jobs,
        text=text
    )


if __name__ == "__main__":
    app.run(debug=True)