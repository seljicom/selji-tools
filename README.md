# 🧰 **SELJI Tools**  
### Data-Driven Utilities Supporting SELJI.com Research Workflows  
https://selji.com

---

## 📌 Overview

**SELJI Tools** is a growing collection of lightweight utilities used to support SELJI.com’s internal research workflows, automation pipelines, and data-driven product analysis.

These tools reflect the real methods behind SELJI’s structured comparison guides, product deep dives, and evidence-based recommendations. By open-sourcing selected components, we aim to provide value to developers, researchers, and anyone interested in transparent and ethical data processing.

The repository currently focuses on **HTML-based scraping utilities** designed to extract publicly visible structural identifiers—starting with Amazon ASIN extraction.

---

## 📂 Repository Structure

selji-tools/
└── scrapers/
├── asin_scraper_for_amazon_search_results.py
└── asin-scraper-for-amazon-search-results.js

### Folder: `scrapers/`
This folder contains small, focused utilities used to extract ASINs from Amazon search results pages.  
These tools:

- Use **HTML parsing only** (no price or review scraping)  
- Require **no Amazon API credentials**  
- Follow Amazon’s ToS by avoiding restricted data types  
- Produce clean identifiers for downstream workflows

---

# 🔍 **Available Utilities**

## 1. **ASIN Scraper — Amazon Search Results (Python)**  
**Path:** `scrapers/asin_scraper_for_amazon_search_results.py`  
:contentReference[oaicite:0]{index=0}

### ✔ Description  
A robust HTML parser that extracts **unique ASINs** from any Amazon search results URL.  
It can fetch the page remotely using `requests` or process saved HTML files.

### ✔ Key Features  
- Performs a safe HTML fetch with headers  
- Extracts ASINs from `data-asin` attributes  
- Ensures validity (10-char alphanumeric)  
- Deduplicates results while preserving order  
- Outputs a clean, ready-to-use ASIN list

### ✔ Example Usage

```bash
python scrapers/asin_scraper_for_amazon_search_results.py


