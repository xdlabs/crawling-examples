from __future__ import absolute_import
from flask import Flask

app = Flask(__name__)


@app.route('/task')
def task1():
    return "hello"


if __name__ == '__main__':
    app.run()
