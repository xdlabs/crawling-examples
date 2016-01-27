# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyExampleItem(scrapy.Item):
    name = scrapy.Field()
    link = scrapy.Field()


class SpiderItem(scrapy.Item):
    title = scrapy.Field()
    name = scrapy.Field()


class ImagesItem(scrapy.Item):
    name = scrapy.Field()
    image_urls = scrapy.Field()
    discount = scrapy.Field()


class AmazonItem(scrapy.Item):
    item_name = scrapy.Field()