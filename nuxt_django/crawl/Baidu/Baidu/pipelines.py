# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from copy import deepcopy
from datetime import datetime

import pymysql
import redis
from scrapy.exporters import JsonItemExporter
from scrapy.pipelines.images import ImagesPipeline
from Baidu.items import First_category, Second_category, Third_category, Answer_question

from twisted.enterprise import adbapi


class BaiduPipeline(object):
    def process_item(self, item, spider):
        return item


class MysqlPipeline(object):
    def __init__(self):
        """
            host=None, user=None, password="", database=None, port=0,
        """
        self.conn = pymysql.Connect('39.107.86.223', 'root', '123', 'baidu', 3306, )
        self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)
        self.first_items = []  # [(),()]
        self.second_items = []  # [(),()]
        self.third_items = []  # [(),()]
        self.question_items = []  # [(),()]

    # if isinstance(item, First_category):
    #       self.first_items.append((item['first_id'], item['first_name']))  # ((),())
    #           sql = """insert into first_category values (%s,%s) ON DUPLICATE KEY UPDATE first_id = VALUES(first_id), first_name=VALUES(first_name)"""
    #           self.cursor.executemany(sql, self.first_items)
    #           self.conn.commit()

    def process_item(self, item, spider):
        if isinstance(item, First_category):
            sql = """insert into first_category values (%s,%s) ON DUPLICATE KEY UPDATE first_id = VALUES(first_id), first_name=VALUES(first_name)"""
            # sql = """insert into first_category values (%s,%s)"""

            self.cursor.execute(sql, (item['first_id'], item['first_name']))
            self.conn.commit()

        if isinstance(item, Second_category):
            sql = """insert into second_category values (%s,%s,%s) ON DUPLICATE KEY UPDATE second_id = VALUES(second_id), second_name=VALUES(second_name),first_id=VALUES(first_id)"""
            # sql = """insert into second_category values (%s,%s,%s)"""

            self.cursor.execute(sql, (item['second_id'], item['second_name'], item['first_id']))
            self.conn.commit()

        if isinstance(item, Third_category):
            items = []  # ((1,2),(1,3),(1,4))
            if len(items) < 13:
                items.append((item['third_id'], item['third_name'], item['second_id']))  # ((),())
            if len(items) >= 13:
                sql = """insert into third_category values (%s,%s, %s) ON DUPLICATE KEY UPDATE third_id = VALUES(third_id), third_name=VALUES(third_name), second_id=VALUES(second_id)"""
                self.cursor.executemany(sql, items)
                self.conn.commit()

            return item
        if isinstance(item, Answer_question):
            items = []  # ((1,2),(1,3),(1,4))
            if len(items) < 13:
                items.append((item['question'], item['answer'], item['third_id']))  # ((),())
            if len(items) >= 13:
                sql = """insert into answer_question (question,answer,third_id_id,question_time) values (%s,%s, %s, %s) ON DUPLICATE KEY UPDATE question = VALUES(question), answer=VALUES(answer), third_id=VALUES(third_id_id), question_time=VALUES (question_time)"""
                self.cursor.executemany(sql, items)
                self.conn.commit()

            return item


class MysqlTwistedPipeline(object):
    """异步插入数据"""

    def __init__(self, dbpool):
        self.dbpool = dbpool
        # self.answer = []

    @classmethod
    def from_settings(cls, settings):
        db_info = dict(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWORD'],
            port=settings['MYSQL_PORT'],
            charset=settings['MYSQL_CHARSET'],
            cursorclass=pymysql.cursors.DictCursor,
            use_unicode=True,
        )
        dbpool = adbapi.ConnectionPool('pymysql', **db_info)
        return cls(dbpool)

    def process_item(self, item, spider):
        """异步插入"""
        if isinstance(item, First_category):
            copy_item = deepcopy(item)
            query = self.dbpool.runInteraction(self.do_insert1, copy_item)  # 第一个参数是自定义功能函数，第二个参数是数据

        if isinstance(item, Second_category):
            copy_item = deepcopy(item)
            query = self.dbpool.runInteraction(self.do_insert2, copy_item)  # 第一个参数是自定义功能函数，第二个参数是数据

        if isinstance(item, Third_category):
            copy_item = deepcopy(item)
            query = self.dbpool.runInteraction(self.do_insert3, copy_item)  # 第一个参数是自定义功能函数，第二个参数是数据

        if isinstance(item, Answer_question):
            # copy_item = deepcopy(item)
            query = self.dbpool.runInteraction(self.do_insert4, item)  # 第一个参数是自定义功能函数，第二个参数是数据

            query.addErrback(self.handle_error)  # 处理异步异常，参数是：回调函数
        return item

    def do_insert1(self, cursor, item):
        sql = """insert into first_category values (%s,%s) ON DUPLICATE KEY UPDATE first_id = VALUES(first_id), first_name=VALUES(first_name)"""
        # sql = """insert into first_category values (%s,%s)"""
        cursor.execute(sql, (item['first_id'], item['first_name']))

    def do_insert2(self, cursor, item):
        sql = """insert into second_category values (%s,%s,%s) ON DUPLICATE KEY UPDATE second_id = VALUES(second_id), second_name=VALUES(second_name),first_id_id=VALUES(first_id_id)"""
        # sql = """insert into second_category values (%s,%s,%s)"""
        cursor.execute(sql, (item['second_id'], item['second_name'], item['first_id']))

    def do_insert3(self, cursor, item):
        sql = """insert into third_category values (%s,%s, %s) ON DUPLICATE KEY UPDATE third_id = VALUES(third_id), third_name=VALUES(third_name), second_id_id=VALUES(second_id_id)"""
        cursor.execute(sql, (item['third_id'], item['third_name'], item['second_id']))

    def do_insert4(self, cursor, item):
        # self.answer.append((item['question'], item['answer'], item['third_id'], item['question_time']))  # ((),())
        sql = """insert into answer_question (question,answer,third_id_id,question_time) values (%s,%s, %s, %s) ON DUPLICATE KEY UPDATE question = VALUES(question), answer=VALUES(answer), third_id_id=VALUES(third_id_id), question_time=VALUES (question_time)"""
        # if len(self.answer) >= 10:
        #     cursor.executemany(sql, self.answer)
        # self.answer = []
        cursor.execute(sql, (item['question'], item['answer'], item['third_id'], item['question_time']))

    def handle_error(self, failure, ):
        """
            处理异步异常的回调函数
            :param failure: 错误信息
        """
        print(failure)


# class RedisPipeline(object):
#     def process_item(self, item, spider):
#         return item
#
# def __init__(self, redis_conn):
#     self.redis_conn = redis_conn
#
# @classmethod
# def from_settings(cls, settings):
#     redis_info = dict(
#         host=settings['REDIS_HOST'],
#         port=settings['REDIS_PORT'],
#         db=settings['REDIS_DB'],
#     )
#     r = redis.Redis(**redis_info)
#     return cls(r)
#
# def process_item(self, item, spider):
#     """异步插入"""
#     while True:
#
#         # process queue as FIFO, change `blpop` to `brpop` to process as LIFO
#
#         source, data = self.redis_conn.blpop(["dmoz:items"])
#
#         item = json.loads(data)

class ExamplePipeline(object):
    def process_item(self, item, spider):
        item["crawled"] = datetime.utcnow()
        item["spider"] = spider.name
        return item


class JsonInputPipeline:
    """自定义保存到文件中API"""

    def __init__(self):
        self.file = open('')

    def process_item(self, item, spider):
        lines = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.file.write(lines)
        return item

    def spider_closed(self, spider):
        self.file.close()


class JsonOutputPipeline:
    """
        导出item为各种格式
        scrapy crawl 爬虫名 -o 本地文件名 (eg: t.json)    #表示把管道中return返回的数据导出到文件

    """

    def __init__(self):
        self.file = open('')
        """创建Json导出器"""
        self.output = JsonItemExporter(self.file, encoding='utf-8', ensure=False)
        """开启导出器，等待添加"""
        self.output.start_exporting()

    def process_item(self, item, spider):
        """把item导出去"""
        self.output.export_item(item)
        return item

    def close_spider(self, spider):
        """关闭导出器"""
        self.output.finish_exporting()
        self.file.close()


class BaiduImagePipeline(ImagesPipeline):
    """
        处理图片的Pipeline，提取result中的 图片url并保存在item中
        settings.py配置
        IMAGE_URLS_FIELD = 'front_image_url'
        IMAGE_STORE = '本地路径'
        过滤图片大小:
            IMAGE_MIN_HEIGHT = 100
            IMAGE_MIN_WIDTH = 100

    """

    def item_completed(self, results, item, info):
        for ok, value in results:
            image_file_path = value['path']
            item['front_image_path'] = image_file_path
        return item
