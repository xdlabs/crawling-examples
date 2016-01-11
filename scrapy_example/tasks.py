from celery import Celery
from calling_spider_by_CrawlerRunner import crawl
from scrapy.utils.project import get_project_settings
from scrapy_example.spiders.new_crawling import MySpider
from scrapy_example.spiders.crawl_images import ImagesSpider
from scrapy_example.spiders.new_spider import NewSpider
from scrapy.crawler import CrawlerProcess
import celery_config

app = Celery('tasks', broker='mongodb://localhost:27017/celery_data', backend='mongodb://localhost:27017/celery_data')
app.config_from_object(celery_config)


@app.task
def task1():
    print "\n\n in task1 method ... "
    crawl()


@app.task
def new_task():
    print "\n\n in new_task method"
    process = CrawlerProcess(get_project_settings())
    process.crawl(ImagesSpider)
    process.crawl(MySpider)
    process.crawl(NewSpider)
    process.start()
