from __future__ import absolute_import
from celery_scrapy.__celery import app
from scrapy.crawler import Crawler
from celery_scrapy.spider import SpiderAmazon
from scrapy.utils.project import get_project_settings
from scrapy import log, signals
from twisted.internet import reactor



@app.task
def hello():
    return "Hello .. "


@app.task
def simple_call():
    return "the task is called..."


@app.task
def scrap():
    settings = get_project_settings()
    spider = SpiderAmazon()
    crawler = Crawler(settings)
    crawler.signals.connect(reactor.stop, signal = signals.spider_closed)
    crawler.configure()
    crawler.crawl(spider)
    crawler.start()
    log.start()
    reactor.run()
