from celery import Celery
import settings

app = Celery('demo', broker='mongodb://localhost:27017/celery', backend='mongodb://localhost:27017/celery')

app.config_from_object(settings)


@app.task
def add(x, y):
    return x + y

if __name__ == '__main__':
    app.worker_main()