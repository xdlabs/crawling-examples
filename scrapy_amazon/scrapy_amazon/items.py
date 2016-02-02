# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyAmazonItem(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    stars = scrapy.Field()
    reviews = scrapy.Field()
    review_link = scrapy.Field()
    category = scrapy.Field()
    url = scrapy.Field()

