from bs4 import BeautifulSoup
import requests
import re  
import csv
from first_web.first_website import base_url, cities, csv_path

class Websites_Scraper():
    def __init__(self, base_url, city, csv_path=None):
        self.base_url = base_url
        self.city = city
        self.csv = csv_path

    def _build_url(self):
        """Builds the url string with city data"""
        urls = []
        for city in self.city:
            url = self.base_url + city
            urls.append(url)
        return urls     
    
    HEADERS = ({'User-Agent':
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
                (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',\
                'Accept-Language': 'en-US, en;q=0.5'})
    
    def _clear_data(self, data):
        a = str(data)
        first_convert = (re.sub("[a-z]*<", "", a))
        second_convert = (re.sub("[a-z]*>", "", first_convert))
        third_convert = second_convert.replace('<span>', '').replace('/', '').replace('"', '').replace('=', '').replace('img ', '').replace('srcresourcesimgli.', '')
        result = (re.sub("[a-z]*png", "", third_convert))
        return result

    def _scrape(self):
        urls = self._build_url()
        websites_result_data = []
        for url in urls:
            webpage = requests.get(url, headers=self.HEADERS)
            soup = BeautifulSoup(webpage.content, "html.parser")
            data = soup.find_all("span")
            address_data = data[5]
            telephone_data = data[6]
            hours_data =f"{data[8]}{data[9]}"
            address = self._clear_data(address_data)
            telephone = self._clear_data(telephone_data)
            hours = self._clear_data(hours_data)
            websites_result_data.append({"Address": address,"Telephone": telephone, "Hours": hours} )
        return websites_result_data

    def to_csv(self):
        with open(self.csv, 'w', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(self._scrape())

        with open(self.csv, 'r', encoding="utf-8") as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                return row

first_website = Websites_Scraper(base_url, cities, csv_path)
print(first_website.to_csv())