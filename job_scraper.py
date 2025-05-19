import requests
from bs4 import BeautifulSoup

def scrape_jobs(keyword="python", location="new+york"):
    headers = {"User-Agent": "Mozilla/5.0"}
    url = f"https://www.indeed.com/jobs?q={keyword}&l={location}"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    jobs = []

    for div in soup.find_all("div", class_="slider_container"):
        title_elem = div.find("h2", class_="jobTitle")
        title = title_elem.text.strip() if title_elem else "No Title"
        link = "https://www.indeed.com" + title_elem.find("a")["href"] if title_elem and title_elem.find("a") else "#"
        company = div.find("span", class_="companyName")
        location = div.find("div", class_="companyLocation")
        summary = div.find("div", class_="job-snippet")

        jobs.append({
            "title": title,
            "link": link,
            "company": company.text.strip() if company else "No Company",
            "location": location.text.strip() if location else "Unknown Location",
            "summary": summary.text.strip() if summary else ""
        })

    return jobs
