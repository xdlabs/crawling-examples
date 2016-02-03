import scrapy
from news.items import NewsItem, SubNewsItem
from bs4 import BeautifulSoup
from scrapy.http import FormRequest
import urllib
import json


class NewsSpider(scrapy.Spider):

    name = "bbcnews"

    allowed_domains = ["bbc.com"]

    start_urls = ["http://www.bbc.com/news"]

    def parse(self, response):
        html = response.body
        soup = BeautifulSoup(html, 'html.parser')

        #item = NewsItem()

        ul = soup.find("ul", {"class": "navigation-wide-list"})
        for li in ul.find_all("li"):
            a = li.find("a")
            span = a.find("span")
            title = str(span.text)
            #item["title"] = title
            link = response.urljoin(a["href"])
            #item["link"] = link
            #yield item
            yield scrapy.Request(link, callback=self.parse_links)

    def parse_links(self, response):
        print "\n\n url : ", response.url
        html1 = response.body
        soup1 = BeautifulSoup(html1, 'html.parser')

        item = SubNewsItem()

        for a in soup1.find_all("a", {"class": "title-link"}):
            url = response.urljoin(a["href"])
            item["link"] = url
            h3 = a.find("h3", {"class": "title-link__title"})
            span = h3.find("span")
            name = span.text
            item["name"] = name
            yield item

        div = soup1.find("div", {"class": "secondary-navigation secondary-navigation--wide"})
        if div:
            a = div.find("a", {"class": "secondary-navigation__title navigation-wide-list__link selected"})
            span = a.find("span")
            title = span.text
            item["title"] = title
            ul = div.find("ul")
            for li in ul.find_all("li"):
                a1 = li.find("a")
                span1 = a1.find("span")
                name = span1.text
                item["name"] = name
                url = response.urljoin(a["href"])
                item["link"] = url
                yield item
                yield scrapy.Request(url, callback=self.parse_content)

    def parse_content(self, response):
        html2 = response.body
        soup2 = BeautifulSoup(html2, 'html.parser')
        print "soup2 : ", soup2.prettify()