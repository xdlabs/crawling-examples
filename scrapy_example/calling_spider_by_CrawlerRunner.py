from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
from scrapy_example.spiders.new_crawling import MySpider

configure_logging()

runner = CrawlerRunner(get_project_settings())
d = runner.crawl(MySpider)
d.addBoth(lambda __: reactor.stop())
reactor.run()
