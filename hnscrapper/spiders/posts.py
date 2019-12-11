import scrapy

from hnscrapper.items import PostItem


class PostsSpider(scrapy.Spider):
    name = 'posts'
    start_urls = [
        'https://news.ycombinator.com/',
    ]

    def parse(self, response):
        post = PostItem()

        post_details_list = response.css('tr.athing')
        sub_texts_list = response.css('td.subtext')

        for index in range(0, len(post_details_list)):
            post_details = post_details_list[index].css('td.title')
            sub_texts = sub_texts_list[index]

            post['number'] = int(str(post_details.css('td.title span.rank::text').get())[:-1])
            post['title'] = post_details.css('td.title a.storylink::text').get()
            post['url'] = post_details.css('a.storylink::attr(href)').get()
            post['score'] = sub_texts.css('span.score::text').get()
            post['user'] = sub_texts.css('a.hnuser::text').get()
            post['age'] = sub_texts.css('span.age a::text').get()

            yield post

        next_page = response.css('td.title a.morelink::attr(href)').get()
        count = int(next_page[-1])

        if next_page is not None and count < 4:
            yield response.follow(next_page, callback=self.parse)
