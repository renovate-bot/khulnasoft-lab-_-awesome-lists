from scripts.fetch_categories import fetch_categories
from scripts.scrape_repositories import scrape_repository_details

def main():
    categories = fetch_categories()
    for category, links in categories.items():
        for link in links:
            print(f"Scraping {link}")
            details = scrape_repository_details(f"https://github.com{link}")
            print(details)

if __name__ == "__main__":
    main()
