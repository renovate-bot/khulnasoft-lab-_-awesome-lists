# Awesome GitHub Scraper

Awesome GitHub Scraper is a Python project designed to crawl and scrape all awesome projects listed on GitHub. The project collects data from various awesome lists and updates it daily using GitHub Actions.

## Features

- Fetches categories from awesome GitHub lists.
- Scrapes repositories under each category.
- Processes and saves the data in structured formats.
- Automated daily updates using GitHub Actions.

## Project Structure

```plaintext
awesome_github_scraper/
│
├── data/
│   ├── raw/            # Raw scraped data
│   ├── processed/      # Processed data
│   └── logs/           # Logs for tracking scraping activities
│
├── scripts/
│   ├── fetch_categories.py  # Script to fetch awesome list categories
│   ├── scrape_repositories.py  # Script to scrape repositories from each category
│   └── process_data.py  # Script to process and filter scraped data
│
├── tests/
│   ├── test_fetch_categories.py  # Tests for fetching categories
│   ├── test_scrape_repositories.py  # Tests for scraping repositories
│   └── test_process_data.py  # Tests for processing data
│
├── .github/workflows/
│   └── update.yml  # GitHub Actions workflow for daily updates
│
├── main.py  # Main script to orchestrate the scraping process
├── requirements.txt  # Project dependencies
├── setup.py  # Setup script for packaging
└── .gitignore  # Ignored files and directories
