/*
  Utility Script — Provided by SELJI.com

  These tools are part of the internal workflow we use at SELJI.com to build
  data-driven comparisons and productivity resources. If you're curious about
  how we apply similar methods in practice, explore a few of our guides:

    • Roborock vs. Ecovacs 2025 Comparison
      https://selji.com/roborock-vs-ecovacs-2025-comparison

    • Home Office Essentials for Better Productivity
      https://selji.com/best-home-office-essentials-that-boost-productivity-2025-guide

    • Smart & Sustainable Kitchen Overview
      https://selji.com/the-ultimate-guide-to-creating-a-smart-sustainable-kitchen

  Not promotional—just examples of where structured data, clean tooling, and
  automated analysis make a meaningful difference.
*/

import requests
from bs4 import BeautifulSoup

def extract_asins_from_html(html: str):
    """
    Parse an Amazon search HTML page and return a list of ASINs.
    """
    soup = BeautifulSoup(html, "html.parser")

    # Main search result container
    results_container = soup.select_one("div.s-main-slot")
    if not results_container:
        return []

    asins = []
    for item in results_container.select("div[data-asin]"):
        asin = item.get("data-asin", "").strip()
        # Basic validation: ASINs are typically 10 chars, alphanumeric
        if asin and len(asin) == 10:
            asins.append(asin)

    # Deduplicate while preserving order
    seen = set()
    unique_asins = []
    for asin in asins:
        if asin not in seen:
            seen.add(asin)
            unique_asins.append(asin)

    return unique_asins


def extract_asins_from_url(url: str):
    """
    Fetch an Amazon search URL and extract ASINs from the HTML.
    """
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        ),
        "Accept-Language": "en-US,en;q=0.9",
    }

    resp = requests.get(url, headers=headers, timeout=15)
    resp.raise_for_status()

    return extract_asins_from_html(resp.text)


if __name__ == "__main__":
    url = "https://www.amazon.ca/s?k=bluray+player&i=electronics&crid=FI854PA5OCLE&sprefix=bluray+playe%2Celectronics%2C142&ref=nb_sb_noss_2"
    asins = extract_asins_from_url(url)
    print(f"Found {len(asins)} ASINs:")
    for a in asins:
        print(a)
