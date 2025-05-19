from flask import Flask, render_template, request
from job_scraper import scrape_jobs
from database import create_table, save_job, get_all_jobs

app = Flask(__name__)

create_table()  # Ensure DB is ready at startup

@app.route("/", methods=["GET"])
def home():
    keyword = request.args.get("keyword")
    location = request.args.get("location")

    if keyword and location:
        location = location.replace(" ", "+")
        jobs = scrape_jobs(keyword, location)
        for job in jobs:
            save_job(job)
    else:
        jobs = get_all_jobs()

    return render_template("index.html", jobs=jobs)

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)


