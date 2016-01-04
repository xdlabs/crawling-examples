import scrapy
from bs4 import BeautifulSoup
from scrapy_example.items import SpiderItem


class NewSpider(scrapy.Spider):
    name = "new_sample"
    allowed_domains = ["pegasusdirectory.com"]
    start_urls = ["http://www.pegasusdirectory.com/"]

    def parse(self, response):
        data = response.body
        soup = BeautifulSoup(data, 'html.parser')
        for div in soup.find_all("div", {'class': 'content'}):
            for center in div.find_all("center"):
                for table in soup.find_all("table"):
                    for tr in table.find_all("tr"):
                        for td in tr.find_all("td"):
                            for h1 in td.find_all("h1"):
                                a = h1.find('a')
                                url = response.urljoin(a['href'])
                                yield scrapy.Request(url, callback=self.parse_content)

    def parse_content(self, response):
        new_data = response.body
        new_soup = BeautifulSoup(new_data, 'html.parser')
        item = SpiderItem()
        title = new_soup.find("title").text
        item["title"] = title
        for div in new_soup.find_all("div", {'class': 'content'}):
            for center in div.find_all("center"):
                for table in center.find_all("table"):
                    for tr in table.find_all("tr"):
                        for td in tr.find_all("td"):
                            for h2 in td.find_all("h2"):
                                a = h2.find('a')
                                name = a.string
                                item["name"] = name
                                yield item
                                url = response.urljoin(a['href'])
                                yield scrapy.Request(url, callback=self.parse_content)
