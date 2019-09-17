from urllib import parse
import requests
from lxml import etree

an = '//dt[contains(@alog-alias,"result-title")]/a/@href'

s = requests.get('https://zhidao.baidu.com/search?lm=0&rn=10&pn=0&fr=search&ie=gbk&word=舞蹈').text
ang = '//dd[contains(@alog-group,"result-userinfo")]/span[1]/text()'
s = etree.HTML(s)
print(len(s.xpath(ang)))
print(len(s.xpath(an)))



