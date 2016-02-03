from flask import Flask, request, render_template, jsonify, send_from_directory
import pymongo
import json
import re
import math
import os
from celery import Celery
from scrapy import settings
from scrapy_amazon.spiders.new_crawl import NewSpider
from scrapy.settings import Settings
from scrapy.crawler import Crawler
from scrapy import signals
from twisted.internet import reactor


app = Flask(__name__)

app.config["CELERY_BROKER_URL"] = "mongodb://localhost:27017"
app.config["CELERY_RESULT_BACKEND"] = "mongodb://localhost:27017"

celery = Celery(app.name, broker=app.config["CELERY_BROKER_URL"], backend=app.config["CELERY_RESULT_BACKEND"])
celery.conf.update(app.config)


def spider_closing():
    return "Spider is closed"


@celery.task
def crawl():
    settings = Settings()
    spider = NewSpider()
    crawler = Crawler(settings)
    crawler.signals.connect(spider_closing, signal=signals.spider_closed)
    crawler.crawl(spider)
    crawler.start()
    print "The processing is started ..."
    reactor.run()


@app.route('/start_crawl', methods=['GET', 'POST'])
def crawl_spider():
    if request.method == "GET":
        result = crawl.delay()
        print "result.ready() : ", result.ready()
        return "the crawling is started ... "


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        return
    return render_template('se.html')


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == "GET":
        val = request.args.get("val")
        index = request.args.get("index")
        print "value : ", val
        print "index : ", index
        db = "amazon_data"
        collection = "data"
        client = pymongo.MongoClient()
        #client = pymongo.MongoClient('172.31.36.253')
        db = client[db]
        list = []
        value_list = val.split()
        print "value_list : ", value_list
        regexp = re.compile(r"|".join(value_list), re.IGNORECASE)
        page = 5
        start = (int(index)-1)*page
        print "start : ", start
        docs = db[collection].find({"$and": [{"name": {"$exists": "true"}}, {"category": {"$exists": "true"}}, {"url": {"$exists": "true"}}, {"$or": [{"name": regexp}, {"category": regexp}]}]}).skip(start).limit(page)
        for doc in docs:
            dic = dict()
            dic["name"] = doc["name"]
            dic["category"] = doc["category"]
            dic["url"] = doc["url"]
            if "reviews" in doc:
                dic["reviews"] = doc["reviews"]
            else:
                dic["reviews"] = 'No reviews'
            if "review_link" in doc:
                dic["review_link"] = doc["review_link"]
            else:
                dic["review_link"] = '#'
            if "stars" in doc:
                dic["stars"] = doc["stars"]
                print "\n stars : ", dic["stars"]
                stars = dic["stars"].split()
                rating = float(stars[0])
                print "rating : ", rating
                if rating == 1.0:
                    img = "starone.png"
                elif rating == 2.0:
                    img = "startwo.png"
                elif rating == 3.0:
                    img = "starthree.png"
                elif rating == 4.0:
                    img = "starfour.png"
                elif rating == 5.0:
                    img = "starfive.png"
                elif rating < 1.0 and rating > 0:
                    img = "starhalf.png"
                elif rating < 2.0 and rating > 1.0:
                    img = "staronehalf.png"
                elif rating < 3.0 and rating > 2.0:
                    img = "startwohalf.png"
                elif rating < 4.0 and rating > 3.0:
                    img = "starthreehalf.png"
                elif rating < 5.0 and rating > 4.0:
                    img = "starfourhalf.png"
            else:
                dic["stars"] = '0 Stars'
                img = "stars.png"
            dic["image"] = img
            dic["image"] = "http://127.0.0.1:5001"+"/uploads/"+dic["image"]
            if "price" in doc:
                dic["price"] = doc["price"]
            else:
                dic["price"] = ''
            list.append(dic)
        print "list : ", list
        return jsonify(result=list)


@app.route("/pages", methods=["GET", "POST"])
def pages():
    if request.method == "GET":
        val = request.args.get("val")
        db = "amazon_data"
        collection = "data"
        client = pymongo.MongoClient()
        #client = pymongo.MongoClient('172.31.36.253')
        db = client[db]
        list = []
        value_list = val.split()
        print "value_list : ", value_list
        regexp = re.compile(r"|".join(value_list), re.IGNORECASE)
        total = db[collection].find({"$and": [{"name": {"$exists": "true"}}, {"category": {"$exists": "true"}}, {"url": {"$exists": "true"}}, {"$or": [{"name": regexp}, {"category": regexp}]}]}).count()
        print "total : ", total
        page = 5
        if total%page == 0:
            count = int(math.ceil(total/page))
        else:
            count = int(math.ceil(total/page))+1
        print "count : ", count
        return jsonify({"count": count})


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    root_dir = os.path.dirname(os.getcwd())
    return send_from_directory(root_dir+"/scrapy_amazon/static/stars",filename)

if __name__ == "__main__":
    app.run(port=5001)
    #app.run(host="172.31.36.253", port=5001)
