import scrapy
from bs4 import BeautifulSoup
from scrapy_example.items import ImagesItem


class ImagesSpider(scrapy.Spider):
    name = "crawl_images"
    allowed_domains = ["amazon.in"]
    start_urls = ["http://www.amazon.in/"]

    def parse(self, response):
        data = response.body
        soup = BeautifulSoup(data, 'html.parser')
        item = ImagesItem()
        for div in soup.find_all("div", {'class': 'a-section feed-carousel-viewport'}):
            for ul in div.find_all("ul", {'class': 'a-nostyle a-horizontal feed-carousel-shelf'}):
                for li in ul.find_all("li"):
                    for span in li.find_all("span", {'class': 'a-list-item'}):
                        for a in span.find_all('a'):
                            img = a.find('img')
                            item["name"] = img['alt']
                            item["image_urls"] = response.urljoin(img['src'])
                            if a.find("span"):
                                dis = a.find("span")
                                item["discount"] = ''.join(dis.text.split())
                            yield item

