from __future__ import absolute_import
import scrapy
from scrapy import Item, Field


class AmazonItem(Item):
    heading = Field()
    title = Field()
    link = Field()
