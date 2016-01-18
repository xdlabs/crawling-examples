import pymongo
import requests

db = "scrapy_data"
collection = "data"

client = pymongo.MongoClient()
db = client[db]

data = db[collection].find({"image_urls": {"$exists": "true"}})

f = open("new_data.txt", 'a')

for documents in data.limit(10):
    print "\n"
    f.write("\n")
    print "\t discount : ", documents["discount"]
    f.write("\n\t Discount : "+documents["discount"])
    print "\t name : ", documents["name"]
    f.write("\n\t Product Name : "+documents["name"])
    print "\t image_urls : ", documents["image_urls"]
    f.write("\n\t Image_Url : "+documents["image_urls"])
    f.write("\n\t"+requests.get(documents["image_urls"]).content)

f.close()

