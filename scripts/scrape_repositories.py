import requests
from bs4 import BeautifulSoup

def scrape_repository_details(repo_url):
    response = requests.get(repo_url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch {repo_url}: {response.status_code}")
    
    soup = BeautifulSoup(response.content, "html.parser")
    repo_details = {
        "name": soup.find("strong", {"itemprop": "name"}).get_text(strip=True),
        "description": soup.find("p", {"itemprop": "description"}).get_text(strip=True) if soup.find("p", {"itemprop": "description"}) else None,
        "stars": soup.find("a", {"href": f"{repo_url}/stargazers"}).get_text(strip=True) if soup.find("a", {"href": f"{repo_url}/stargazers"}) else "0",
        "forks": soup.find("a", {"href": f"{repo_url}/network/members"}).get_text(strip=True) if soup.find("a", {"href": f"{repo_url}/network/members"}) else "0",
    }
    return repo_details

if __name__ == "__main__":
    test_url = "https://github.com/sindresorhus/awesome"
    repo_details = scrape_repository_details(test_url)
    print(repo_details)
