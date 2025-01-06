import logging
from scripts.fetch_categories import fetch_categories
from scripts.scrape_repositories import scrape_repositories
from scripts.process_data import process_data

def main():
    try:
        logging.info("Starting the GitHub Awesome Scraper")

        categories = fetch_categories()
        for category in categories:
            repositories = scrape_repositories(category)
            # Here, you could save the raw data to `data/raw/` as JSON files

        process_data()

        logging.info("GitHub Awesome Scraper completed successfully")

    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
