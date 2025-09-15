from bs4 import BeautifulSoup
import requests

def crawl_web(url: str) -> dict:
    """Crawls a webpage and extracts text, metadata, and links."""
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    text = soup.get_text()
    metadata = {meta.get('name', ''): meta.get('content', '') for meta in soup.find_all('meta') if meta.get('name')}
    links = [a['href'] for a in soup.find_all('a', href=True)]

    return {
        "text": text[:1000],  # limit for display
        "metadata": metadata,
        "links": links[:10]   # limit for display
    }
