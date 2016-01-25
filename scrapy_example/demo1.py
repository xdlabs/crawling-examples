from flask import Flask, request, render_template, jsonify
import pymongo
import json

app = Flask(__name__)


@app.route('/searchfirst', methods=['GET', 'POST'])
def search():
    if request.method == "POST":
        var = request.form['var']
        print "variable : ", var
    return render_template("first.html")


@app.route('/getdata', methods=['GET', 'POST'])
def getdata():
    if request.method == "GET":
        var = request.args.get('var')
        print "variable : ", var
        list = []
        db = "scrapy_data"
        collection = "data"
        client = pymongo.MongoClient()
        db = client[db]
        #data = db[collection].find(limit=20)
        reg = "%s.*" % var
        print "reg : ", reg
        data = db[collection].find({"name": {"$regex": reg, "$options": 'i'}})
        for docs in data:
            discount = docs["discount"]
            name = docs["name"]
            link = docs["image_urls"]
            list.append({'discount': discount, 'name': name, 'link': link})
        if list == []:
            list.append({'name': 'Not Found', 'discount': '', 'link': ''})
        return jsonify(result=list)


@app.route('/Search', methods=['GET', 'POST'])
def second():
    if request.method == "POST":
        return
    return render_template("second.html")


@app.route('/getlist', methods=['GET', 'POST'])
def getlist():
    if request.method == "GET":
        db = "scrapy_data"
        collection = "data"
        client = pymongo.MongoClient()
        db = client[db]
        list = []
        data = db[collection].find(limit=5)
        for docs in data:
            discount = docs["discount"]
            name = docs["name"]
            link = docs["image_urls"]
            list.append({'discount': discount, 'name': name, 'link': link})
        return jsonify(result=list)


if __name__ == "__main__":
    app.run()
