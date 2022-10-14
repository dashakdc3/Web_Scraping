
import requests
from selectorlib import Extractor
import first_website as fw
import second_website as sw
import third_website as tw

class WebScraping():

    def __init__(self, base_url, cities, yml_path, slash ):
        self.base_url = base_url
        self.cities = cities
        self.yml_path = yml_path
        self.slash = slash

    # h = {
    #     'pragma': 'no-cache',
    #     'cache-control': 'no-cache',
    #     'dnt': '1',
    #     'upgrade-insecure-requests': '1',
    #     'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
    #     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    #     'accept-language': '*',
    # }
    headers ={
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 OPR/40.0.2308.81',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'DNT': '1',
    'Accept-Encoding': 'gzip, deflate, lzma, sdch',
    'Accept-Language': '*'
    }


    def _build_url(self):
        """Builds the url string with city data"""
        urls = []
        for city in self.cities:
            url = self.base_url + city + self.slash
            urls.append(url)
        return urls     

    def scrape(self):
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
        print(urls)
        for data in data_result:
            result.append(data['temp'])
        print(result)
        return result


if __name__ == "__main__":
    first_Website = WebScraping(base_url=fw.base_url, cities=fw.cities, yml_path=fw.yml_path, slash=fw.slash )
    second_Website = WebScraping(base_url=sw.base_url, cities=sw.cities, yml_path=sw.yml_path, slash=sw.slash )
    third_Website = WebScraping(base_url=tw.base_url, cities=tw.cities, yml_path=tw.yml_path, slash=tw.slash  )
    first_Website.scrape()
    second_Website.scrape()
    third_Website.scrape()

# if __name__ == "__main__": that helps us not to execute this code, if we importing it to another


    # def get(self):
    #     """Cleans the output of _scrape"""
    #     scraped_content = self._scrape()
    #     new = []
    #     x = []
    #     # result = {'Adress: ', f'{}'}
    #     address = 'Адрес'
    #     telephone = 'Телефон'
    #     working_hours = 'Время'
    #     for x in scraped_content:
    #         new.append(x.split())
    #     for word in new:
    #         for w in word:
    #             index_address = word.index(address)
    #             index_telephone = word.index(telephone)
    #             index_hours = word.index(working_hours)
    #     print(new)
    #     print(index_telephone)
    #     return scraped_content
    #         # splited = content.split()
    #         # for data in splited:
    #         #     print(data)
