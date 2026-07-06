import requests

API_URL = "https://www.arbeitnow.com/api/job-board-api"

def fetch_jobs():
    """Fetch job data from the API."""

    try:

        response = requests.get(API_URL, timeout=10) 
        response.raise_for_status()  # Raise an exception for HTTP errors

        return response.json()
    
    except requests.RequestException:
        print(f"Error: Unable to fetch jobs from the API.")
        return None
    

def parse_jobs(data):
    """Extract job information from the API response."""

    jobs = []

    if not data:
        return jobs

    for job in data["data"]:

        job_data = {
            "title": job["title"],
            "company": job["company_name"],
            "location": job["location"]
        }

        jobs.append(job_data)

    return jobs


def fetch_api_jobs():
    """Fetch and parse jobs from the API."""

    data = fetch_jobs()
    
    if not data:
        return []

    return parse_jobs(data)

