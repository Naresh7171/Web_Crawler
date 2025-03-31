import requests

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
