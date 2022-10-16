import requests
from selectorlib import Extractor
import first_web.first_website as fw
import second_web.second_website as sw
import third_web.third_website as tw
import csv

class WebScraping():

    def __init__(self, base_url, cities, yml_path, slash, csv_file ):
        self.base_url = base_url
        self.cities = cities
        self.yml_path = yml_path
        self.slash = slash
        self.csv = csv_file

    headers = {
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': '*',
    }


    def _build_url(self):
        """Builds the url string with city data"""
        urls = []
        for city in self.cities:
            url = self.base_url + city + self.slash
            urls.append(url)
        return urls     

    def _scrape(self):
        """Extracts a value"""
        urls = self._build_url()
        extractor = Extractor.from_yaml_file(self.yml_path)
        data_result = []
        result = []
        for url in urls:
            r = requests.get(url=url,headers=self.headers)
            full_content = r.text
            raw_content = extractor.extract(full_content)
            data_result.append(raw_content)
        for data in data_result:
            result.append({'WebSites data': data['temp']})
        return result
    
    def to_csv(self):
        with open(self.csv, 'w') as file:
            writer = csv.writer(file)
            writer.writerow(self._scrape())

        with open(self.csv, 'r') as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                print(row)

if __name__ == "__main__":
    # first_website = WebScraping(base_url=fw.base_url, cities=fw.cities, yml_path=fw.yml_path, slash=fw.slash,csv_file=fw.csv_path )
    second_website = WebScraping(base_url=sw.base_url, cities=sw.cities, yml_path=sw.yml_path, slash=sw.slash, csv_file=sw.csv_path )
    # third_website = WebScraping(base_url=tw.base_url, cities=tw.cities, yml_path=tw.yml_path, slash=tw.slash, csv_file=tw.csv_path  )
    # first_website.to_csv()
    second_website.to_csv()
    # third_website.to_csv()
