from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from hnscrapper.spiders.posts import PostsSpider


def run_crawler():
    process = CrawlerProcess(get_project_settings())

    process.crawl(PostsSpider)
    process.start()

# for testing
if __name__ == '__main__':
    run_crawler()
