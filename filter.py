VALID_FIELDS = ("title", "company", "location")

def filter_jobs(jobs, field, value):
    """Filter jobs based on a specific field and value."""

    field = field.lower()
    value = value.lower()

    filtered_jobs = []
    
    # Check if the field is valid
    if field not in VALID_FIELDS:
        raise ValueError(f"Invalid field. Must be one of {VALID_FIELDS}")
    
    # Filter jobs based on the specified field and value
    for job in jobs:
        if value in job[field].lower():
            filtered_jobs.append(job)

    return filtered_jobs
