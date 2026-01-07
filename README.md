# Books Scraper

A Python scraper for [Books to Scrape](https://books.toscrape.com/). This repository contains two versions of the scraper: a basic version (v1) and an updated version (v2).

---

## Versions

### v1 (Basic)
- Simple scraper for Books to Scrape
- Collects the following data for each book:
  - Title
  - Price
  - Stock availability
  - Rating
  - Image URL
  - Book URL
- Saves data to **CSV** and **JSON**
- Ideal for learning basic web scraping

### v2 (Updated)
- Uses `requests.Session()` for faster and more efficient scraping
- Includes **error handling** for network issues and timeouts
- More robust scraping across multiple pages
- Collects the same data as v1
- Saves data to **CSV** and **JSON**
- Recommended for practical scraping tasks

---

## ⚡ Features

- Multi-page scraping
- Progress logging in terminal
- Clean output in CSV and JSON
- Easy to extend for additional fields or websites

---

## 📦 Requirements

Make sure you have Python 3.x installed. Then install the required packages:

```bash
pip install requests beautifulsoup4
