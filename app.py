from flask import send_from_directory
from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    session,
    flash,
    send_file
)
from utils.resume_parser import extract_candidate_details
import os
from functools import wraps

from auth import register, login
from database import (
    create_database,
    save_resume_history,
    get_resume_history,
    get_user_by_id,
    get_total_resumes,
    get_average_ats
)

from utils.pdf_reader import read_pdf
from utils.skill_extractor import extract_skills
from utils.ats_score import calculate_ats_score
from utils.jd_matcher import calculate_match
from utils.job_recommender import recommend_jobs
from utils.report_generator import generate_report
from utils.resume_feedback import generate_feedback


app = Flask(__name__)

app.secret_key = "resume_analyzer_secret_key"

UPLOAD_FOLDER = "uploads"
REPORT_FOLDER = "reports"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["REPORT_FOLDER"] = REPORT_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(REPORT_FOLDER, exist_ok=True)

create_database()

latest_report = ""


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):

        if "user_id" not in session:
            flash("Please login first.", "warning")
            return redirect(url_for("login_page"))

        return f(*args, **kwargs)

    return decorated_function


@app.route("/")
def home():

    if "user_id" in session:
        return redirect(url_for("dashboard"))

    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register_page():

    if request.method == "POST":

        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        success, message = register(
            username,
            email,
            password
        )

        flash(message)

        if success:
            return redirect(url_for("login_page"))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login_page():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        user = login(email, password)

        if user:

            session["user_id"] = user["id"]

            flash("Login Successful!")

            return redirect(url_for("dashboard"))

        flash("Invalid Email or Password")

    return render_template("login.html")


@app.route("/logout")
@login_required
def logout():

    session.clear()

    flash("Logged out successfully.")

    return redirect(url_for("login_page"))
@app.route("/dashboard")
@login_required
def dashboard():

    user = get_user_by_id(session["user_id"])

    total_resumes = get_total_resumes(session["user_id"])

    average_ats = get_average_ats(session["user_id"])

    history = get_resume_history(session["user_id"])

    return render_template(
        "dashboard.html",
        user=user,
        total_resumes=total_resumes,
        average_ats=average_ats,
        history=history
    )


@app.route("/upload", methods=["POST"])
@login_required
def upload():

    global latest_report

    if "resume" not in request.files:

        flash("Please upload a resume.")

        return redirect(url_for("dashboard"))

    file = request.files["resume"]

    if file.filename == "":

        flash("No file selected.")

        return redirect(url_for("dashboard"))

    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        file.filename
    )

    file.save(filepath)

    resume_text = read_pdf(filepath)

    found_skills, missing_skills = extract_skills(resume_text)

    ats_score = calculate_ats_score(
        found_skills,
        resume_text
    )

    job_description = request.form.get(
        "job_description",
        ""
    )

    match_score = calculate_match(
        resume_text,
        job_description
    )

    jobs = recommend_jobs(found_skills)

    feedback = generate_feedback(
        ats_score,
        match_score,
        found_skills,
        missing_skills
    )

    save_resume_history(
        session["user_id"],
        file.filename,
        ats_score,
        match_score
    )

    latest_report = os.path.join(
        app.config["REPORT_FOLDER"],
        "Resume_Report.pdf"
    )

    generate_report(
        latest_report,
        ats_score,
        match_score,
        found_skills,
        missing_skills,
        jobs
    )

    return render_template(
    "result.html",
    score=ats_score,
    match_score=match_score,
    skills=found_skills,
    missing_skills=missing_skills,
    jobs=jobs,
    feedback=feedback,
    text=resume_text,
    pdf_file=file.filename
)
@app.route("/history")
@login_required
def history():

    history_data = get_resume_history(session["user_id"])

    return render_template(
        "history.html",
        history=history_data
    )


@app.route("/download")
@app.route("/uploads/<filename>")
@login_required
def uploaded_file(filename):
    return send_from_directory(
        app.config["UPLOAD_FOLDER"],
        filename
    )
@login_required
def download():

    global latest_report

    if latest_report == "":
        flash("No report available.")
        return redirect(url_for("dashboard"))

    return send_file(
        latest_report,
        as_attachment=True
    )


@app.route("/profile")
@login_required
def profile():

    user = get_user_by_id(session["user_id"])

    total_resumes = get_total_resumes(session["user_id"])

    average_ats = get_average_ats(session["user_id"])

    return render_template(
        "profile.html",
        user=user,
        total_resumes=total_resumes,
        average_ats=average_ats
    )


@app.route("/about")
def about():

    return render_template("about.html")


@app.route("/contact")
def contact():

    return render_template("contact.html")


@app.errorhandler(404)
def page_not_found(error):

    return render_template(
        "404.html"
    ), 404


@app.errorhandler(500)
def internal_server_error(error):

    return render_template(
        "500.html"
    ), 500
if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)