from __future__ import absolute_import
import scrapy
import urllib2
from bs4 import BeautifulSoup
from celery_scrapy.items import AmazonItem


class SpiderAmazon(scrapy.Spider):
    name = 'amazon'

    allowed_domains = ['amazon.in']

    start_urls = ['http://www.amazon.in/gp/site-directory/ref=nav_shopall_btn']

    def parse(self, response):
        page = urllib2.urlopen(response.url).read()
        soup = BeautifulSoup(page)

        list = soup.find_all("div", {"class": "popover-grouping"})

        print "list : ", list
        print "length of list : ", len(list)
        yield list
