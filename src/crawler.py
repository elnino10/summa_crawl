import requests
from bs4 import BeautifulSoup

def crawl_website(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, "html.parser")

        # kill all scripts and styles
        for script in soup(["script", "style", "nav", "footer", "header"]):
            script.decompose()

        # find the main content - grab all paragraphs
        paragraphs = soup.find_all('p')
        text = " ".join([p.get_text() for p in paragraphs])

        # cleanup extra white-space
        text = " ".join(text.split())

        if len(text) < 100:
            return "Error: page content too short or couldn't be extracted."
        
        return text
    except Exception as e:
        return f"Error crawling the url: {str(e)}"
