import csv
import os

CSV_FILE = os.path.join("data", "jobs.csv")

def save_job(jobs):
    """Save jobs to a CSV file."""

    try:

        os.makedirs("data", exist_ok=True)

        with open(CSV_FILE, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(
                file, 
                fieldnames = ["title", "company", "location"]
            )
            writer.writeheader()
            
            for job in jobs:
                writer.writerow(job)

    except OSError:
        print("Error: Unable to write to the CSV file.")


def load_jobs():
    """Load jobs from the CSV file."""

    jobs = []

    try:
        with open(CSV_FILE, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                jobs.append(row)

    except FileNotFoundError:
        print("Error: CSV file not found.")
        return []

    except OSError:
        print("Error: Unable to read the CSV file.")
        return []

    return jobs