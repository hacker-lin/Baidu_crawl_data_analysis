# -*- coding: utf-8 -*-


import scrapy


class First_category(scrapy.Item):
    first_id = scrapy.Field()
    first_name = scrapy.Field()


class Second_category(scrapy.Item):
    second_id = scrapy.Field()
    second_name = scrapy.Field()
    first_id = scrapy.Field()


class Third_category(scrapy.Item):
    third_id = scrapy.Field()
    third_name = scrapy.Field()
    second_id = scrapy.Field()


class Answer_question(scrapy.Item):
    content_id = scrapy.Field()
    question = scrapy.Field()
    answer = scrapy.Field()
    question_time = scrapy.Field()
    third_id = scrapy.Field()
