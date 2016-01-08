from celery import Celery
from calling_spider_by_CrawlerRunner import crawl
from scrapy.utils.project import get_project_settings
from scrapy_example.spiders.new_crawling import MySpider
from scrapy_example.spiders.crawl_images import ImagesSpider
from scrapy_example.spiders.new_spider import NewSpider
from scrapy.crawler import CrawlerProcess


app = Celery('tasks', broker='mongodb://localhost:27017/celery_data', backend='mongodb://localhost:27017/celery_data')


@app.tasks
def tasks():
    crawl()


@app.tasks
def new_task():
    process = CrawlerProcess(get_project_settings())
    process.crawl(ImagesSpider)
    process.crawl(MySpider)
    process.crawl(NewSpider)
    process.start()
