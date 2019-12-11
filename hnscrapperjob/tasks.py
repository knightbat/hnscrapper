from hnscrapper.run_crawler import run_crawler
from hnscrapperjob.celery import app


@app.task
def start():
    run_crawler()

