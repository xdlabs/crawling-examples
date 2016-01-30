from flask import Flask, request, render_template, jsonify
import pymongo
import json

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        return
    return render_template('se.html')


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == "GET":
        val = request.args.get("val")
        print "value : ", val
        db = "amazon_data"
        collection = "data"
        client = pymongo.MongoClient()
        #client = pymongo.MongoClient('172.31.36.253')
        db = client[db]
        list = []
        reg = "%s.*" % val
        print "reg : ", reg
        docs = db[collection].find({"$and": [{"name": {"$exists": "true"}}, {"category": {"$exists": "true"}}, {"url": {"$exists": "true"}}, {"$or": [{"name": {"$regex": reg, "$options": "i"}}, {"category": {"$regex": reg, "$options": "i"}}]}]})
        for doc in docs:
            dic = dict()
            dic["name"] = doc["name"]
            dic["category"] = doc["category"]
            dic["url"] = doc["url"]
            if "reviews" in doc:
                dic["reviews"] = doc["reviews"]
            else:
                dic["reviews"] = ''
            if "stars" in doc:
                dic["stars"] = doc["stars"]
            else:
                dic["stars"] = ''
            if "price" in doc:
                dic["price"] = doc["price"]
            else:
                dic["price"] = ''
            list.append(dic)
        print "list : ", list
        return jsonify(result=list)


if __name__ == "__main__":
    app.run(port=5001)
    #app.run(host="172.31.36.253", port=5001)