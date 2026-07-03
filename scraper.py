import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"

def get_page():
    """Retrieve the job listings from the jobs website."""

    try:
        response = requests.get(URL, timeout=10)  # Set a timeout for the request
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.text

    except requests.RequestException:
        print("Error: Unable to connect to the jobs website.")
        return None
    
    
def create_soup(html):
    """"Convert HTML into a BeautifulSoup object for parsing."""

    return BeautifulSoup(html, "html.parser")


def extract_text(element, tag, class_name):
    """"Find an element and return its text."""

    found = element.find(tag, class_=class_name)

    return element.find(tag, class_=class_name).get_text(strip=True) if found else ""


def parse_jobs(soup):
    """Extract job information from the webpage."""

    jobs = []

    job_cards = soup.find_all("div", class_="column is-half")

    for job in job_cards:

        title = extract_text(job, "h2", "title is-5")

        company = extract_text(job, "h3", "subtitle is-6 company")

        location = extract_text(job, "p", "location")

        job_data = {
            "title": title,
            "company": company,
            "location": location
        }

        jobs.append(job_data)

    return jobs


def scrape_jobs():

    html = get_page()
    
    if not html:
        return []

    soup = create_soup(html)

    return parse_jobs(soup)

