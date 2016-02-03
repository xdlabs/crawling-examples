from flask import Flask, request, jsonify
import pymongo


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "GET":
        db = "news_data"
        collection = "data"
        client = pymongo.MongoClient()
        db = client[db]
        list = []
        docs = db[collection].find().limit(15)
        for doc in docs:
            name = doc["name"]
            link = doc["link"]
            list.append({"name": name, "link": link})
        return jsonify(result=list)


if __name__ == "__main__":
    app.run()
