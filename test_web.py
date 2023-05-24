import requests
from bs4 import BeautifulSoup
import webbrowser

def get_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if href:
            links.append(href)
    return links

webpage_url = 'https://familysearch.org'  # Replace with your desired webpage URL

links = get_links(webpage_url)

for link in links:
    webbrowser.open(link)

for link in links:
    print(link)
