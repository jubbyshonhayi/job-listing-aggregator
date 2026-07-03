from display import display_jobs
from filter import filter_jobs
from utils import TABLE_WIDTH, pause
from scraper import scrape_jobs
from storage import save_jobs, load_jobs
from search import search_jobs
from sort import sort_jobs

def handle_find_jobs():
    """Handle finding and saving jobs."""
    jobs = scrape_jobs()

    if jobs:
        save_jobs(jobs)
        print(f"{len(jobs)} jobs found and saved successfully.")

    else:
        print("No jobs found.")

    pause()

def handle_view_saved_jobs():
    """Handle viewing saved jobs."""

    jobs = load_jobs()

    if jobs:
        print(f"Found {len(jobs)} saved jobs.")
        display_jobs(jobs)

    else:
        print("No saved jobs found.")
        pause()


def handle_search():
    """Handle searching saved jobs."""
    keyword = input("Enter search keyword: ")

    jobs = load_jobs()
    matches = search_jobs(jobs, keyword)

    if matches:
        print(f"Found {len(matches)} job(s) matching '{keyword}':")
        display_jobs(matches)

    else:
        print(f"No jobs found matching '{keyword}'.")
        pause()


def handle_filter():
    """Handle filtering saved jobs."""

    print("\nFilter jobs by field:\n")
    print("1. Title")
    print("2. Company")
    print("3. Location")

    
    choice = input("Enter your choice: ")

    if choice == "1":
        field = "title"

    elif choice == "2":
        field = "company"

    elif choice == "3":
        field = "location"

    else:
        print("Invalid choice.")
        pause()
        return
        
    jobs = load_jobs()

    value = input(f"Enter value to filter {field} by: ")
    filtered_jobs = filter_jobs(jobs, field, value)

    if filtered_jobs:
        print(f"Found {len(filtered_jobs)} job(s) matching '{value}' in '{field}':")
        display_jobs(filtered_jobs)

    else:
        print(f"No jobs found matching '{value}' in '{field}'.")
        pause()


def handle_sort():
    """Handle sorting saved jobs."""

    jobs = load_jobs()
    
    if not jobs:
        print("No saved jobs to sort.\n")
        pause()
        return

    print("\nSort jobs by field:\n")
    print("1. Title")
    print("2. Company")
    print("3. Location")

    
    choice = input("Enter your choice: ")

    if choice == "1":
        field = "title"

    elif choice == "2":
        field = "company"

    elif choice == "3":
        field = "location"

    else:
        print("Invalid choice.")
        pause()
        return

    
    sorted_jobs = sort_jobs(jobs, field)

    print(f"Jobs sorted by '{field}':")
    display_jobs(sorted_jobs)

        
    
def display_menu():
    """Display the main menu."""

    print("=" * TABLE_WIDTH)
    print("JOB LISTING AGGREGATOR".center(TABLE_WIDTH))
    print("=" * TABLE_WIDTH)

    print("1. Find Jobs")
    print("2. View Saved Jobs")
    print("3. Search Saved Jobs")
    print("4. Filter Jobs")
    print("5. Sort Jobs")
    print("6. Notifications")

    print("0. Exit")


while True:

    try:
        display_menu()

        print()

        choice = input("Enter your choice: ")

        if choice == "1":

            handle_find_jobs()

        elif choice == "2":
            handle_view_saved_jobs()

        elif choice == "3":
            handle_search()
            

        elif choice == "4":
            handle_filter()
            

        elif choice == "5":
            handle_sort()
            

        elif choice == "6":
            print("Managing notifications...")
            pause()

        elif choice == "0":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
            pause()

    except KeyboardInterrupt:
        print("\nProgram interrupted. Goodbye!")
        break

