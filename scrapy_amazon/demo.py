from flask import Flask, request, render_template, jsonify
import pymongo

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == "GET":
        client = pymongo.MongoClient()
        db = "amazon_data"
        collection = "data"
        db = client[db]
        list = []
        data = db[collection].find({"$and": [{"name": {"$exists": "true"}}, {"price": {"$exists": "true"}}, {"stars": {"$exists": "true"}}, {"reviews": {"$exists": "true"}}]})
        for docs in data:
            name = docs["name"]
            price = docs["price"]
            stars = docs["stars"]
            reviews = docs["reviews"]
            list.append({"name": name, "price": price, "stars": stars, "reviews": reviews})
        print "list : ", list
        return jsonify(result=list)


if __name__ == '__main__':
    app.run()
