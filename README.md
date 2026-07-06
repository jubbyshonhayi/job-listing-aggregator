# Job Listing Aggregator & Notification System

## Overview

The Job Listing Aggregator & Notification System is a Python command-line application that collects job listings from multiple sources, allowing users to search, filter, sort, and manage job data in one place.

The project demonstrates both web scraping and API integration by retrieving job listings from a website using BeautifulSoup and Requests, as well as from a public job API. All job data is stored in CSV format, enabling efficient searching, filtering, sorting, and notification of newly available jobs.

This project was developed as part of a Python Programming Internship.

---

## Features

- Fetch job listings using web scraping (BeautifulSoup + Requests)
- Fetch job listings from a public Job API
- Save jobs to a CSV file
- View saved jobs with pagination
- Search jobs by title, company, or location
- Filter jobs by title, company, or location
- Sort jobs using Pandas
- Check for newly available jobs using a notification system
- Modular project architecture with separate modules for each feature

---

## Technologies Used

- Python 3
- Requests
- BeautifulSoup4
- Pandas
- CSV Module

---

## Project Structure

```
Job-Listing-Aggregator/
│
├── api_jobs.py
├── display.py
├── filter.py
├── main.py
├── notifications.py
├── scraper.py
├── search.py
├── sort.py
├── storage.py
├── utils.py
│
├── data/
│   └── jobs.csv
│
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/Job-Listing-Aggregator.git
```

Navigate to the project directory:

```bash
cd Job-Listing-Aggregator
```

Install the required packages:

```bash
pip install requests beautifulsoup4 pandas
```

---

## Usage

Run the application:

```bash
python main.py
```

The application provides the following menu options:

```
1. Find Jobs
2. View Saved Jobs
3. Search Saved Jobs
4. Filter Jobs
5. Sort Jobs
6. Notifications
0. Exit
```

When selecting **Find Jobs** or **Notifications**, users can choose between:

- Web Scraping
- API

---

## Notification System

The notification feature compares the latest job listings against the previously saved job snapshot.

If new jobs are found, they are displayed to the user before the latest snapshot replaces the old one.

On the first run, the application creates an initial snapshot for future comparisons.

---

## Learning Outcomes

This project demonstrates practical experience with:

- Web scraping using Requests and BeautifulSoup
- Consuming REST APIs
- Working with JSON data
- Reading and writing CSV files
- Data manipulation with Pandas
- Modular Python programming
- Error handling
- Building reusable functions
- Designing a command-line application

---

## Future Improvements

Possible enhancements include:

- Support for additional job APIs
- Export results to JSON
- Database integration
- Email notifications
- Keyword-based notification alerts
- Advanced filtering options
- Graphical User Interface (GUI)

---

## License

This project is intended for educational and portfolio purposes.