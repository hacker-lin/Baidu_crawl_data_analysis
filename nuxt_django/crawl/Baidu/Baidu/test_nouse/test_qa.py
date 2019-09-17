import requests
from lxml import etree
# # a = 'https://zhidao.baidu.com/list?keyWord=%E5%AE%89%E5%85%A8%E5%91%98&ie=utf8&cid=101100&_pjax=%23j-question-list-pjax-container'
# # a = 'https://zhidao.baidu.com/list?tagType=my&tag=%E6%B4%BB%E6%9C%9F%E5%AE%9D&cid=101102&rn=40&pn=80&ie=utf8&_pjax=%23j-question-list-pjax-container'

#
a = 'https://zhidao.baidu.com/question/1958774813532784940.html?fr=iks&word=%CE%E5%CC%A8%C9%BD&ie=gbk'
text = requests.get(a).content
text = text.decode('gb2312')

node = etree.HTML(text)


answer = node.xpath('//h1[@accuse="qTitle"]/span[@class="ask-title"]/text()')  # 回答

#
print(answer)
#
# all_urls = node.xpath('//dt[contains(@alog-alias,"result-title")]/a/@href')
# print(all_urls)
# # answer = node.xpath('//div[contains(@id,"answer-content")]/text()')
# # question = node.xpath('//h1[@accuse="qTitle"]/span[@class="ask-title"]/text()')
# # print(question)
# # print(text)
# # print(all_urls)
#
# # print(''.join(text).split()[0])
# #
# #
# # <a href="http://zhidao.baidu.com/question/566679372189026164.html?fr=qlquick&amp;is_force_answer=0"
# #
#
#
# https://zhidao.baidu.com/search?lm=0&rn=10&pn=0&fr=search&ie=gbk&word=%B0%B2%C8%AB%D4%B1
#
# # class ="title-link" target="_blank" >
# https://zhidao.baidu.com/search?word=%B0%B2%C8%AB%D4%B1&ie=gbk&site=-1&sites=0&date=0&pn=0
# https://zhidao.baidu.com/search?word=%B0%B2%C8%AB%D4%B1&ie=gbk&site=-1&sites=0&date=0&pn=20