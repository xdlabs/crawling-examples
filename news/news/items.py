# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NewsItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()


class SubNewsItem(scrapy.Item):
    title = scrapy.Field()
    name = scrapy.Field()
    link = scrapy.Field()
