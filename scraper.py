
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="urllib3")

import requests
from bs4 import BeautifulSoup
import pandas as pd
from collections import Counter

#input this into terminal: pip install requests beautifulsoup4 pandas

def main():
    url = input('Enter the URL to scrape: ')
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Analyze and display common tags with descriptions
    common_tags = [
        ('p', 'Paragraph'),
        ('h1', 'Main heading'),
        ('h2', 'Subheading'),
        ('div', 'Generic container'),
        ('span', 'Inline container'),
        ('li', 'List item'),
        ('a', 'Link'),
    ]
    tag_counts = {tag: len(soup.find_all(tag)) for tag, _ in common_tags}
    print('\nCommon tags found on the page:')
    for tag, desc in common_tags:
        print(f"  {tag} ({desc}): {tag_counts[tag]}")
    print("\nYou can choose one of these tags, or enter a custom CSS selector (e.g., 'span.text', 'div.chapter').")

    selector = input('Enter the CSS selector for what to scrape: ')
    elements = [el.get_text(strip=True) for el in soup.select(selector)]
    if not elements:
        print('No elements found for the given selector.')
        return
    df = pd.DataFrame({'result': elements})
    df.to_csv('scraped_results.csv', index=False)
    print(f'Scraped {len(elements)} elements. Results saved to scraped_results.csv.')

if __name__ == "__main__":
    main()
