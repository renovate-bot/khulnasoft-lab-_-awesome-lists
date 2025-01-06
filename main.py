import logging
from scripts.fetch_categories import fetch_categories
from scripts.scrape_repositories import scrape_repositories
from scripts.process_data import process_data

# Configure logging
logging.basicConfig(
    filename='data/logs/scraper.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
)

def main():
    try:
        logging.info("Starting the GitHub Awesome Scraper")

        # Step 1: Fetch categories
        logging.info("Fetching categories")
        categories = fetch_categories()
        logging.info(f"Fetched {len(categories)} categories")

        # Step 2: Scrape repositories for each category
        for category in categories:
            logging.info(f"Scraping repositories for category: {category}")
            repositories = scrape_repositories(category)
            logging.info(f"Scraped {len(repositories)} repositories for category: {category}")

        # Step 3: Process data
        logging.info("Processing data")
        process_data()

        logging.info("GitHub Awesome Scraper completed successfully")

    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
