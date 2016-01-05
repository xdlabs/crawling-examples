from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy_example.spiders.new_crawling import MySpider
from scrapy_example.spiders.new_spider import NewSpider
from scrapy_example.spiders.crawl_images import ImagesSpider

process = CrawlerProcess(get_project_settings())

process.crawl(ImagesSpider)
process.crawl(MySpider)
process.crawl(NewSpider)
process.start()
