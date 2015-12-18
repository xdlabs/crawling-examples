from __future__ import absolute_import
from celery_scrapy.__celery import app
from scrapy.crawler import CrawlerProcess
from celery_scrapy.spider import SpiderAmazon
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy.settings import Settings
from scrapy import signals
from scrapy.conf import settings


@app.task
def hello():
    return "Hello .. "


def spider_closing():
    print "spider is closed"


@app.task
def simple_call():
    return "the task is called..."


@app.task
def scrap():
    #settings = get_project_settings()
    settings = Settings()
    settings.set('AUTOTHROTTLE_ENABLED', False)
    spider = SpiderAmazon()
    crawler = Crawler(settings)
    crawler.signals.connect(spider_closing, signal=signals.spider_closed)
    crawler.crawl(spider)
    crawler.start()
    reactor.run()

