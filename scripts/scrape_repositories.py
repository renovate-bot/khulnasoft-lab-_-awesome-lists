import requests
from bs4 import BeautifulSoup

def scrape_repositories(category_url):
    base_url = "https://github.com"
    response = requests.get(f"{base_url}{category_url}")
    soup = BeautifulSoup(response.content, "html.parser")

    repositories = []
    for a_tag in soup.find_all('a', href=True):
        if a_tag['href'].startswith('/'):
            repo_url = f"{base_url}{a_tag['href']}"
            repositories.append(repo_url)

    return repositories
