from __future__ import absolute_import
from flask import Flask
from tasks import hello

app = Flask(__name__)


@app.route('/task')
def task1():
    result = hello()
    return result


if __name__ == '__main__':
    app.run()
