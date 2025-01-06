import requests
from bs4 import BeautifulSoup

def fetch_categories():
    url = "https://github.com/sindresorhus/awesome"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch {url}: {response.status_code}")
    
    soup = BeautifulSoup(response.content, "html.parser")
    categories = {}

    # Find all category headers and their corresponding list items
    for header in soup.find_all("h2"):
        category_name = header.get_text(strip=True)
        category_list = header.find_next("ul")
        links = category_list.find_all("a", href=True) if category_list else []
        categories[category_name] = [link['href'] for link in links]
    
    return categories

if __name__ == "__main__":
    categories = fetch_categories()
    for category, links in categories.items():
        print(f"{category}: {len(links)} links")
