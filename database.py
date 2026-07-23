import sqlite3

DATABASE = "resume_analyzer.db"


def get_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def create_database():
    conn = get_connection()
    cursor = conn.cursor()

    # Users Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # Resume History Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS resume_history(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        filename TEXT,
        ats_score INTEGER,
        jd_match INTEGER,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    """)

    conn.commit()
    conn.close()


# -----------------------------
# User Functions
# -----------------------------

def add_user(username, email, password):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
        INSERT INTO users(username,email,password)
        VALUES(?,?,?)
        """, (username, email, password))

        conn.commit()
        return True

    except sqlite3.IntegrityError:
        return False

    finally:
        conn.close()


def get_user_by_email(email):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM users
    WHERE email=?
    """, (email,))

    user = cursor.fetchone()

    conn.close()

    return user


def get_user_by_id(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM users
    WHERE id=?
    """, (user_id,))

    user = cursor.fetchone()

    conn.close()

    return user


# -----------------------------
# Resume History
# -----------------------------

def save_resume_history(user_id, filename, ats_score, jd_match):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO resume_history
    (user_id, filename, ats_score, jd_match)
    VALUES(?,?,?,?)
    """, (user_id, filename, ats_score, jd_match))

    conn.commit()
    conn.close()


def get_resume_history(user_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM resume_history
    WHERE user_id=?
    ORDER BY created_at DESC
    """, (user_id,))

    history = cursor.fetchall()

    conn.close()

    return history


def get_total_resumes(user_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT COUNT(*)
    FROM resume_history
    WHERE user_id=?
    """, (user_id,))

    total = cursor.fetchone()[0]

    conn.close()

    return total


def get_average_ats(user_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT AVG(ats_score)
    FROM resume_history
    WHERE user_id=?
    """, (user_id,))

    avg = cursor.fetchone()[0]

    conn.close()

    if avg is None:
        return 0

    return round(avg, 2)


# -----------------------------
# Initialize Database
# -----------------------------

if __name__ == "__main__":
    create_database()
    print("Database created successfully.")