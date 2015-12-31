# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.settingsrapy.org/en/latest/topics/item-pipeline.html
import json
import pymongo
from scrapy.conf import settings


class ScrapyExamplePipeline(object):

    def __init__(self):
        self.filename = "data.txt"

    def open_spider(self, spider):
        self.file = open(self.filename, "wb")

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item


class MongoDBPipeline(object):

    def __init__(self):
        self.server = settings['MONGODB_SERVER']
        self.host = settings['MONGODB_HOST']
        self.db = settings['MONGODB_DB']
        self.collection = settings['MONGODB_COLLECTION']

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.server, self.host)
        self.db = self.client[self.db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection].insert(dict(item))
        return item
