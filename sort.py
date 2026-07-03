import pandas as pd

def sort_jobs(jobs, field):
    """Sort jobs by a specific field."""

    VALID_FIELDS = ("title", "company", "location")

    if field not in VALID_FIELDS:
        raise ValueError(f"Invalid field. Must be one of {VALID_FIELDS}")
    
    df = pd.DataFrame(jobs)
    
    df = df.sort_values(by=field)

    return  df.to_dict(orient="records")