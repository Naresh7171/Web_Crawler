import requests
from urllib.parse import urljoin

def obey_robots_txt(url):
    """Check robots.txt for crawl permissions"""
    robots_url = urljoin(url, "/robots.txt")
    try:
        response = requests.get(robots_url, headers={"User-Agent": "Mozilla/5.0"}, timeout=5)
        if "Disallow" in response.text:
            return False
    except requests.exceptions.RequestException:
        pass  # Assume allowed if robots.txt is unreachable
    return True
