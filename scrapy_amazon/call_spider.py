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
        client = pymongo.MongoClient('172.31.36.253')
        db = client[db]
        list = []
        reg = "%s.*" % val
        print "reg : ", reg
        docs = db[collection].find({"$or": [{"name": {"$regex": reg, "$options": "i"}}, {"category": {"$regex": reg, "$options": "i"}}]})
        print "docs : ", docs
        for doc in docs:
            dic = dict()
            if "name" in doc:
                print "name : ", doc["name"]
                dic["name"] = doc["name"]
            if "category" in doc:
                print "category : ", doc["category"]
                dic["category"] = doc["category"]
            if "reviews" in doc:
                print "reviews : ", doc["reviews"]
                dic["reviews"] = doc["reviews"]
            if "stars" in doc:
                print "stars : ", doc["stars"]
                dic["stars"] = doc["stars"]
            if "price" in doc:
                print "price : ", doc["price"]
                dic["price"] = doc["price"]
            print "dic : ", dic
            list.append(dic)
        print "list : ", list
        return jsonify(result=list)


if __name__ == "__main__":
    app.run(host="172.31.36.253", port=5001)
