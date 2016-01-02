import scrapy
from bs4 import BeautifulSoup
from scrapy_example.items import SpiderItem


class MySpider(scrapy.Spider):
    name = "sample"
    allowed_domains = ["dmoz.org"]
    start_urls = ["http://www.dmoz.org/"]

    def parse(self, response):
        data = response.body
        soup = BeautifulSoup(data, 'html.parser')

        for div in soup.find_all("div", {'class': 'one-third'}):
            for span in div.find_all('span'):
                #print "category : ", span.string
                a = span.find('a')
                url = response.urljoin(a['href'])
                yield scrapy.Request(url, callback=self.parse_content)

    def parse_content(self, response):
        new_data = response.body
        new_soup = BeautifulSoup(new_data, 'html.parser')
        item = SpiderItem()
        title = new_soup.find("title").text
        item["title"] = title
        for ul in new_soup.find_all('ul', {'class': 'directory dir-col'}):
            for li in ul.find_all('li'):
                a = li.find('a')
                item["name"] = a.string
                yield item
                url = response.urljoin(a['href'])
                yield scrapy.Request(url, callback=self.parse_content)

