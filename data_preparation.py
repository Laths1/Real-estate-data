import pandas as pd
import threading
from scraper import *
import time
import random

class DataCollector:
    def __init__(self, url, start_page, end_page):
        self.url = url
        self.start_page = start_page
        self.end_page = end_page
        self.data = []
        self.lock = threading.Lock()

    def _safe_extend(self, properties):
        with self.lock:
            self.data.extend(properties)

    def collect_data(self):
        def crawl(url):
            time.sleep(random.uniform(3, 180))
            try:
                page = Scraper(url)
                props = page.get_properties()
                if not props:
                    print(f"[WARNING] No data from {url}")
                return props
            except Exception as e:
                print(f"[ERROR] {url}: {e}")
                return []

        urls = [self.url.format(i=i) for i in range(self.start_page, self.end_page + 1)]

        threads = []

        for url in urls:
            thread = threading.Thread(target=lambda u=url: self._safe_extend(crawl(u)))
            threads.append(thread)

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        print(f"Collected {len(self.data)} properties.")
        return self.data

class DataPreparator:
    def __init__(self, properties):
        self.properties = properties

    def clean_number(self, text):
        if not text:
            return None
        text = text.replace("²", "")
        if not text.isdigit():
            return None
        return int(text)

    def to_dataframe(self):
        data = {
            "Title": [prop.title for prop in self.properties],
            "Price": [self.clean_number(prop.price) for prop in self.properties],
            "Beds": [self.clean_number(prop.bed) for prop in self.properties],
            "Baths": [self.clean_number(prop.bath) for prop in self.properties],
            "Garage": [self.clean_number(prop.garage) for prop in self.properties],
            "Size_sqm": [self.clean_number(prop.sqm) for prop in self.properties],
            "Location": [prop.location for prop in self.properties],
            "Details_URL": [prop.details_url for prop in self.properties],
        }
        return pd.DataFrame(data)
    
    def save_to_csv(self, filename):
        df = self.to_dataframe()
        df.to_csv(filename, index=False)
        print(f"Data saved to {filename}.")

