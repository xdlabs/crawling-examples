# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.settingsrapy.org/en/latest/topics/item-pipeline.html
import json
import pymongo
from scrapy.conf import settings
import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
import requests


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
        #self.port = settings['MONGODB_PORT']
        self.db = settings['MONGODB_DB']
        self.collection = settings['MONGODB_COLLECTION']

    def open_spider(self, spider):
        self.client = pymongo.MongoClient()
        self.db = self.client[self.db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection].insert(dict(item))
        return item


class MyImagesPipeline(ImagesPipeline):
    def process_item(self, item, spider):
        if 'image_urls' in dict(item):
            url = item['image_urls']
            response = requests.get(url)
            filename = url.split('/')[-1]
            with open((settings['IMAGES_STORE']+filename), 'wb') as f:
                f.write(response.content)
                f.close()
            return item
        else:
            raise DropItem("Not containing image .. ")
