import requests
from crawler.parser import extract_links
from crawler.utils import obey_robots_txt
import requests
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


def fetch_page(url):
    """Fetch page content with HTTPS support"""
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=10, verify=True)
        response.raise_for_status()
        return response.text
    except requests.exceptions.SSLError:
        print(f"⚠ SSL Error: Trying without verification: {url}")
        return requests.get(url, headers=headers, timeout=10, verify=False).text
    except requests.exceptions.RequestException as e:
        print(f"❌ Failed to fetch {url}: {e}")
        return None


def fetch_page(url):
    """Fetch page content"""
    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException:
        return None

def crawl_website(start_url, max_pages=10):
    """Crawl website and extract links recursively"""
    visited = set()
    to_visit = {start_url}
    crawled_data = []

    while to_visit and len(visited) < max_pages:
        url = to_visit.pop()
        if url in visited or not obey_robots_txt(url):
            continue

        html = fetch_page(url)
        if html:
            links = extract_links(url, html)
            to_visit.update(links - visited)
            visited.add(url)
            crawled_data.append((url, links))

    print("Crawled Data:", crawled_data)  # DEBUG PRINT
    return crawled_data

def crawl_website(start_url, max_pages=10):
    """Crawl website and extract links recursively"""
    visited = set()
    to_visit = {start_url}
    crawled_data = []

    while to_visit and len(visited) < max_pages:
        url = to_visit.pop()
        if url in visited:
            continue

        html = fetch_page(url)
        if html:
            links = extract_links(url, html)
            to_visit.update(links - visited)
            visited.add(url)
            crawled_data.append((url, links))

    print(f"🌐 Crawled {len(crawled_data)} pages.")  # Debug print
    return crawled_data
