import requests
from bs4 import BeautifulSoup

def fetch_categories():
    url = "https://github.com/sindresorhus/awesome"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    
    categories = []
    for a_tag in soup.find_all('a', href=True):
        href = a_tag['href']
        if href.startswith('/sindresorhus/awesome'):
            categories.append(href)
    
    return categories
