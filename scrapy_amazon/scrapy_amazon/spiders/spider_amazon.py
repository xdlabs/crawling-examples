import scrapy
import urllib2
from bs4 import BeautifulSoup
from scrapy_amazon.items import ScrapyAmazonItem
import re


class SpiderAmazon(scrapy.Spider):
    name = "amazon"

    allowed_domains = ['amazon.in']

    start_urls = ['http://www.amazon.in/gp/site-directory/ref=nav_shopall_btn']

    def parse(self, response):
        page = urllib2.urlopen(response.url).read()
        soup = BeautifulSoup(page)

        print "soup : ", soup.prettify()

        item = ScrapyAmazonItem()

        list = soup.find_all("div", {"class": "popover-grouping"})
        print "list : ", list
        print "length : ", len(list)
        for h2 in list:
            h = h2.find('h2')
            print "h : ", h.text
            a = h2.find_all('a')
            for links in a:
                item['heading'] = h.text
                item['title'] = links.text
                if not links['href'].startswith("http://") or not links['href'].startswith("https://"):
                    item['link'] = "www.amazon.in"+links['href']
                else:
                    item['link'] = links['href']
                print "heading : ", item['heading']
                print "title : ", item['title']
                print "link : ", item['link']
                print "\n"
                yield item
