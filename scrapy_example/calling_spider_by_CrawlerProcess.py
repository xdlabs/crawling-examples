from scrapy.crawler import CrawlerProcess
from scrapy_example.spiders.new_crawling import MySpider
from scrapy.utils.project import get_project_settings

process = CrawlerProcess(get_project_settings())

process.crawl(MySpider)
process.start()
