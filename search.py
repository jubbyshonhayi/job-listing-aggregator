def search_jobs(jobs, keyword):
    """Search for jobs by title, company, or location."""

    keyword = keyword.lower()

    matches = []

    for job in jobs:

        if (keyword in job["title"].lower() or
            keyword in job["company"].lower() or
            keyword in job["location"].lower()):
            
            matches.append(job)

    return matches