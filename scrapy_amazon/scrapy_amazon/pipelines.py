# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from scrapy.conf import settings


class ScrapyAmazonPipeline(object):

    def __init__(self):
        self.server = settings["MONGODB_SERVER"]
        self.db = settings["MONGODB_DB"]
        self.collection = settings["MONGODB_COLLECTION"]

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.server)
        self.db = self.client[self.db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection].insert(dict(item))
        return item
