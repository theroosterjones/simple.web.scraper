# WebScraper

This is a simple Python web scraping tool that allows you to scrape text from any web page using a CSS selector.

## Requirements
- Python 3.x
- `requests` library
- `beautifulsoup4` library
- `pandas` library

You can install the required libraries with:

```
pip install requests beautifulsoup4 pandas
```

## Usage

1. Run the script:

```
python scraper.py
```

2. When prompted, enter the URL of the web page you want to scrape.
3. Enter the CSS selector for the elements you want to extract (e.g., `span.text`).

The script will scrape the text content of all elements matching the selector and save the results to a file called `scraped_results.csv` in the same directory.

If no elements are found for the given selector, the script will notify you. 