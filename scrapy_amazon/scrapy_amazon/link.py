import urllib2
import json
from flask import Flask, jsonify, request, render_template
from elasticsearch import Elasticsearch

app = Flask(__name__)

es = Elasticsearch(timeout=100)


@app.route('/SearchData', methods=['GET', 'POST'])
def search_data():
    if request.method == "GET":
        search_data = request.args.get('data')
        print "search_data : ", search_data
        dic = {}

        response = urllib2.urlopen("http://localhost:9200/amazon/scraped_data/_search?pretty=true")
        res = json.load(response)

        size = res['hits']['total']
        print "size : ", size

        url = "http://localhost:9200/amazon/scraped_data/_search?pretty=true&size=%s" % size

        resp = urllib2.urlopen(url)

        list = []

        data = json.load(resp)

        for r in range(size):
            heading = "%s" % data['hits']['hits'][r]['_source']['heading']
            if search_data in heading:
                print "heading : ", heading
                title = data['hits']['hits'][r]['_source']['title']
                link = data['hits']['hits'][r]['_source']['link']
                list.append({'title': title, 'link': link})

        for r in range(size):
            title = "%s" % data['hits']['hits'][r]['_source']['title']
            if search_data in title and title not in dic:
                print "title : ", title
                title = data['hits']['hits'][r]['_source']['title']
                link = data['hits']['hits'][r]['_source']['link']
                list.append({'title': title, 'link': link})
        print "list : ", list
        return jsonify(data=list)


@app.route('/Search', methods=['GET', 'POST'])
def search():
    return render_template('search.html')


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True, threaded=True)
