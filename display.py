from utils import TABLE_WIDTH, pause

JOBS_PER_PAGE = 10  # Number of jobs to display per page

def display_jobs(jobs):
    """"Display the list of jobs in a formatted table."""

    if not jobs:
        print("No jobs found.")
        return

    print("=" * TABLE_WIDTH)
    print("JOB LISTINGS".center(TABLE_WIDTH))
    print("=" * TABLE_WIDTH)

    for index, job in enumerate(jobs, start=1):
        print(f"\nJob {index}:")
        print("-" * TABLE_WIDTH)
        print(f"Title:    {job['title']}")
        print(f"Company:  {job['company']}")
        print(f"Location: {job['location']}")

        if index % JOBS_PER_PAGE == 0 and index != len(jobs):
            pause("Press Enter to view the next 10 jobs...")

    pause("End of job listings. Press Enter to return to the menu...")

   