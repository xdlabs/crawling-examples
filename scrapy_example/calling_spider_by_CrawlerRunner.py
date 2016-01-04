from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
from scrapy_example.spiders.new_crawling import MySpider
from scrapy_example.spiders.new_spider import NewSpider

configure_logging()
runner = CrawlerRunner(get_project_settings())


@defer.inlineCallbacks
def crawl():
    yield runner.crawl(MySpider)
    yield runner.crawl(NewSpider)
    reactor.stop()

crawl()
reactor.run()
