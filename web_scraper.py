"""
Web Scraper Module
Extract data from websites
"""

import requests
from bs4 import BeautifulSoup
import json
import csv
from datetime import datetime

class WebScraper:
    def __init__(self, url):
        self.url = url
        self.soup = None

    def fetch_page(self):
        """Fetch webpage content"""
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            response = requests.get(self.url, headers=headers, timeout=10)
            response.raise_for_status()
            self.soup = BeautifulSoup(response.content, 'html.parser')
            print(f"✅ Page fetched successfully!")
            return True
        except Exception as e:
            print(f"❌ Error fetching page: {e}")
            return False

    def scrape_all_text(self):
        """Extract all text"""
        if not self.soup:
            return []
        text = self.soup.get_text(separator='\n', strip=True)
        return [{'content': text}]

    def scrape_headings(self):
        """Extract headings"""
        if not self.soup:
            return []
        headings = []
        for i in range(1, 7):
            for heading in self.soup.find_all(f'h{i}'):
                headings.append({
                    'type': f'h{i}',
                    'text': heading.get_text(strip=True)
                })
        return headings

    def scrape_links(self):
        """Extract all links"""
        if not self.soup:
            return []
        links = []
        for link in self.soup.find_all('a', href=True):
            links.append({
                'text': link.get_text(strip=True),
                'url': link['href']
            })
        return links

    def scrape_images(self):
        """Extract images"""
        if not self.soup:
            return []
        images = []
        for img in self.soup.find_all('img'):
            images.append({
                'alt': img.get('alt', ''),
                'src': img.get('src', '')
            })
        return images

    def scrape_tables(self):
        """Extract tables"""
        if not self.soup:
            return []
        tables_data = []
        for table in self.soup.find_all('table'):
            rows = []
            for tr in table.find_all('tr'):
                cells = [td.get_text(strip=True) for td in tr.find_all(['td', 'th'])]
                if cells:
                    rows.append(cells)
            tables_data.append({'table': rows})
        return tables_data

    def scrape_custom(self, selector):
        """Custom CSS selector scraping"""
        if not self.soup:
            return []
        elements = []
        for element in self.soup.select(selector):
            elements.append({
                'tag': element.name,
                'text': element.get_text(strip=True)
            })
        return elements

    def save_data(self, data, format_type):
        """Save scraped data"""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"scraped_data_{timestamp}.{format_type}"

        if format_type == 'csv' and data and isinstance(data[0], dict):
            with open(filename, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=data[0].keys())
                writer.writeheader()
                writer.writerows(data)
        elif format_type == 'json':
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        else:
            with open(filename, 'w', encoding='utf-8') as f:
                for item in data:
                    f.write(str(item) + '\n\n')

        print(f"✅ Data saved to: {filename}")

    def scrape_and_save(self, scrape_choice, css_selector, output_format):
        """Main scraping function"""
        data = []

        if scrape_choice == '1':
            data = self.scrape_all_text()
        elif scrape_choice == '2':
            data = self.scrape_headings()
        elif scrape_choice == '3':
            data = self.scrape_links()
        elif scrape_choice == '4':
            data = self.scrape_images()
        elif scrape_choice == '5':
            data = self.scrape_tables()
        elif scrape_choice == '6':
            data = self.scrape_custom(css_selector)

        print(f"\n✓ Found {len(data)} items")
        self.save_data(data, output_format)
