# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3


class HnscrapperPipeline(object):

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.connection = sqlite3.connect("results.sqlite3")
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.cursor.execute(""" drop table if exists posts_table """)
        self.cursor.execute("""create table posts_table (
         number int,
         title  text,
         url text,
         score  text,
         user text,
         age text)
         """)

    def store_db(self, post):

        self.cursor.execute("""insert into posts_table values ( ?, ?, ?, ?, ?, ?)""", (
            post['number'],
            post['title'],
            post['url'],
            post['score'],
            post['user'],
            post['age'],
        ))
        self.connection.commit()

    def process_item(self, item, spider):
        self.store_db(item)
        return item
