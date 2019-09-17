# -*- coding: utf-8 -*-
import copy
import re
from urllib import parse
import scrapy
import json

from Baidu.items import First_category, Second_category, Third_category, Answer_question


class ZhidaoSpider(scrapy.Spider):
    name = 'zhidao'
    allowed_domains = ['zhidao.baidu.com']

    start_urls = ['https://zhidao.baidu.com/list?cid=101100']

    def parse(self, response):
        meta = copy.copy(response.meta)
        second_html = response.text
        r1 = re.compile(r"""F.context\('tagClass', (.*\}\})\);""")  # 匹配出1_2层 所有分类JSON信息

        first_category_item = First_category()
        second_category_item = Second_category()

        first_second_json = r1.search(second_html).group(1)
        json_object = json.loads(first_second_json)

        url_1_2 = []
        for key1 in json_object:  # 所有key 101,102...115
            first_obj = json_object[key1]
            first_tag_name = first_obj['name']  # 所有一级url的名字

            first_category_item['first_id'] = key1
            first_category_item['first_name'] = first_tag_name
            yield first_category_item

            second_obj = first_obj['child']
            for key2 in second_obj:  # 所有key 101100,......

                second_id = key2
                second_content = second_obj[key2]
                second_tag_name = second_content['name']

                second_category_item['second_id'] = key2
                second_category_item['second_name'] = second_tag_name
                second_category_item['first_id'] = key1
                yield second_category_item

                second_url = f'https://zhidao.baidu.com/list?cid={second_id}'

                url_1_2.append((key2, second_url))  # [(101,url),(102,url)]

        print(f"{'*' * 50}所有1_2层url采集完毕")
        # print(url_1_2)    # 验证所有1_2层 url
        # print(f'{first_tag_name}:{second_tag_name}') #  此处可验证，1、2级列表全部匹配完整

        for per_id, per_url in url_1_2:
            meta['per_id'] = per_id
            meta['per_url'] = per_url
            yield scrapy.Request(per_url, callback=self.detail_parse, meta=meta)
        # print(url_1_2)

    def detail_parse(self, response):
        """三级列的文本 """
        meta = copy.copy(response.meta)

        # second_url = response.meta.get('per_url')
        second_id = response.meta.get('per_id')

        third_html = response.body  # 字节形式
        third_html = third_html.decode("unicode_escape")

        third_category_item = Third_category()

        tagList = re.compile(r"""F.context\('tagList', [\s\S]*?"\]\}\);""")  # 截取带有三级的文本的 F.context 的 tagList

        s = tagList.findall(third_html)[0]
        content_re = re.compile(r'"(\w*?)",')  # 所有，除了尾部
        end_re = re.compile(r'"(\w*?)"\]')  # 尾部一个
        content = set(content_re.findall(s))  # 正则有限，set去重
        end = end_re.findall(s)[0]
        content.add(end)  # 所有

        # tag = parse.quote('安全员', encoding='gbk')
        # f"""https://zhidao.baidu.com/search?lm=0&rn=10&pn=0&fr=search&ie=gbk&word={parse.quote(x, encoding='gbk')"""
        all_url = [
            f"""https://zhidao.baidu.com/search?lm=0&rn=10&pn=0&fr=search&ie=gbk&word={parse.quote(x,
                                                                                                   encoding='gbk')}"""
            for x in content]
        url_content = zip(all_url, content)
        for third_id, (per_page_url, third_name) in enumerate(url_content):
            com_id = f'{second_id}_{third_id}'  # 100101_0
            third_category_item['third_id'] = com_id
            third_category_item['third_name'] = third_name
            third_category_item['second_id'] = second_id

            meta['com_id'] = com_id

            yield third_category_item
            yield scrapy.Request(per_page_url, callback=self.third_tag_url,
                                 meta=meta)

    def third_tag_url(self, response):
        meta = copy.copy(response.meta)

        com_id = response.meta['com_id']  # 100101_0
        meta['com_id'] = com_id

        per_page_url = response.xpath('//dt[contains(@alog-alias,"result-title")]/a/@href').getall()
        question_time = response.xpath('//dd[contains(@alog-group,"result-userinfo")]/span[1]/text()').getall()

        if per_page_url:
            # for index, url in enumerate(per_page_url):  # 每个详情链接， http->https防止重定向
            for url, question_time in zip(per_page_url, question_time):
                url = url.replace('http', 'https')
                meta['question_time'] = question_time
                if 'baobao' in url:
                    continue
                # yield scrapy.Request(parse.urljoin(response.url, url), callback=self.answer_question,
                #                      meta={'com_id': com_id})  # 100101_0
                yield scrapy.Request(parse.urljoin(response.url, url), callback=self.answer_question,
                                     meta=meta)  # 100101_0

        next_page = response.xpath('//a[@class="pager-next"]/@href').get()  # 下一页
        if next_page:
            yield scrapy.Request(parse.urljoin(response.url, next_page), callback=self.third_tag_url,
                                 meta=meta)

    def answer_question(self, response):
        meta = copy.copy(response.meta)

        com_id = response.meta['com_id']
        answer_question_item = Answer_question()

        question = response.xpath('//h1[@accuse="qTitle"]/span[@class="ask-title"]/text()').get()  # 问题
        answer = response.xpath('//div[contains(@id,"answer-content")]/text()').getall()  # 回答, 因为有垃圾空格，所以要getall才能全取到
        if answer == []:
            answer = None
        else:
            try:
                answer = ''.join(answer).split()[0]  # 去除各种空格,空换行
            except IndexError as e:
                answer = None

        answer_question_item['question'] = question
        answer_question_item['answer'] = answer
        answer_question_item['third_id'] = com_id
        answer_question_item['question_time'] = meta['question_time']
        print(f'{question}{"?" * 10}', '\n', answer)
        yield answer_question_item
