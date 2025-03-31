from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import logging
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def extract_links(url, html):
    """Extract all links from HTML content"""
    soup = BeautifulSoup(html, "html.parser")
    links = set()

    for anchor in soup.find_all("a", href=True):
        link = urljoin(url, anchor["href"])
        if is_valid_url(link):
            links.add(link)

    print(f"Extracted {len(links)} links from {url}")  # DEBUG PRINT
    return links

def is_valid_url(url):
    """Check if the URL is valid"""
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

def extract_links(url, html):
    """Extract all links from HTML content"""
    soup = BeautifulSoup(html, "html.parser")
    links = set()
    for anchor in soup.find_all("a", href=True):
        link = urljoin(url, anchor["href"])
        if is_valid_url(link):
            links.add(link)
    
    logging.info(f"Extracted {len(links)} links from {url}")
    return links

def is_valid_url(url):
    """Check if the URL is valid"""
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)
