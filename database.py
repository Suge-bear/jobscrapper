import sqlite3

DB_NAME = "jobs.db"

def create_table():
    with sqlite3.connect(DB_NAME) as conn:
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS jobs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                link TEXT UNIQUE,
                company TEXT,
                location TEXT,
                summary TEXT
            )
        ''')
        conn.commit()

def save_job(job):
    with sqlite3.connect(DB_NAME) as conn:
        c = conn.cursor()
        try:
            c.execute('''
                INSERT INTO jobs (title, link, company, location, summary)
                VALUES (?, ?, ?, ?, ?)
            ''', (job["title"], job["link"], job["company"], job["location"], job["summary"]))
            conn.commit()
        except sqlite3.IntegrityError:
            # Duplicate link (job already saved)
            pass

def get_all_jobs():
    with sqlite3.connect(DB_NAME) as conn:
        c = conn.cursor()
        c.execute("SELECT title, link, company, location, summary FROM jobs")
        return [
            {
                "title": row[0],
                "link": row[1],
                "company": row[2],
                "location": row[3],
                "summary": row[4]
            }
            for row in c.fetchall()
        ]
