from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin


def scrape(site, depth):
    req_headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.8',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0'
    }
    ans = [site]
    visited = set()
    queue = [site]
    num = 0
    while queue and num < depth:
        current_url = queue.pop(0)
        if current_url in visited:
            continue

        visited.add(current_url)

        try:
            r = requests.get(current_url, timeout=10, headers=req_headers)

        except requests.exceptions.RequestException as e:

            print(f"Error connecting to {current_url}: {e}")
            continue

        soup = BeautifulSoup(r.text, "html.parser")
        for link in soup.find_all("a"):
            href = link.get("href")
            full_url = urljoin(site, href)

            if site in full_url and full_url not in visited:
                # visited.add(full_url)
                queue.append(full_url)
                num +=1
                ans.append(full_url)
    return ans

site = "https://www.nadra.gov.pk/"
print(scrape(site, 40))