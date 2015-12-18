from __future__ import absolute_import
from celery import Celery

app = Celery("tasks", broker='mongodb://localhost:27017', backend='mongodb://localhost:27017')


if __name__ == '__main__':
    app.worker_main()
