from utils import TABLE_WIDTH, pause

def display_menu():
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
            print("Finding jobs...")
            pause()

        elif choice == "2":
            print("Viewing saved jobs...")
            pause()

        elif choice == "3":
            print("Searching saved jobs...")
            pause()

        elif choice == "4":
            print("Filtering jobs...")
            pause()

        elif choice == "5":
            print("Sorting jobs...")
            pause()

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