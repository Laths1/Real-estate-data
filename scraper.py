from bs4 import BeautifulSoup
import requests
from property import *
    
class Scraper:
    def __init__(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Error fetching the URL: {e}")

        soup = BeautifulSoup(response.content, 'html.parser')
        self.info_container = soup.find_all('a', class_='p24_content')

        if not self.info_container:
            raise ValueError("Error with finding listings.")

    def safe_text(self, element, tag, **kwargs):
        try:
            return element.find(tag, **kwargs).text.strip()
        except:
            return ""

    def clean_number(self, text):
        return ''.join(filter(str.isdigit, text))

    def get_properties(self):
        properties = []
        for i in range(len(self.info_container)):
            title = self.safe_text(self.info_container[i], 'span', class_='p24_title')
            price = self.safe_text(self.info_container[i], 'span', class_='p24_price')
            location = self.safe_text(self.info_container[i], 'span', class_='p24_address')
            bed = self.safe_text(self.info_container[i], 'span', class_='p24_featureDetails', title='Bedrooms')
            bath = self.safe_text(self.info_container[i], 'span', class_='p24_featureDetails', title='Bathrooms')
            sqm = self.safe_text(self.info_container[i], 'span', class_='p24_size', title='Erf Size')
            garage = self.safe_text(self.info_container[i], 'span', class_='p24_featureDetails', title='Parking Spaces')

            prop = Property(title,
                            self.clean_number(price),
                            self.clean_number(bed),
                            self.clean_number(bath),
                            self.clean_number(garage),
                            self.clean_number(sqm),
                            location)
            
            properties.append(prop)

        return properties
