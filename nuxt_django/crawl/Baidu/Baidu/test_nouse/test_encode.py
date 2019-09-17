# import re
# import urllib
#
# # import requests
#
#
#
# s = """
#
# t('tagList', {"0":["MBA","lim","mba","\u6578\u5b78","\u6fb3\u6d32\u7559\u5b66","\u516b\u5e74\u7ea7","\u767e\u79d1\u77e5\u8bc6","\u529e\u6bd5\u4e1a\u8bc1","\u5317\u4eac\u5927\u5b66","\u5317\u4eac\u4ea4\u901a\u5927\u5b66","\u5317\u4eac\u5916\u56fd\u8bed\u5927\u5b66","\u5317\u7eac","\u672c\u79d1","\u672c\u79d1\u5b66\u5386","\u53d8\u7535\u7ad9","\u8fa9\u8bba","\u535a\u58eb","\u90e8\u9996","\u8336\u6587\u5316","\u957f\u65b9\u5f62","\u957f\u6c99\u7406\u5de5\u5927\u5b66","\u6210\u6559","\u6210\u8003","\u6210\u4eba\u6559\u80b2","\u521d\u4e09","\u521d\u4e00","\u521d\u4e2d\u5730\u7406","\u521d\u4e2d\u5386\u53f2","\u521d\u4e2d\u4f5c\u6587","\u53a8\u5e08\u8bc1","\u78c1\u573a","\u6253\u6807\u673a","\u5927\u5b66\u5316\u5b66","\u5927\u4e13","\u6ef4\u80f6","\u5730\u7406\u4fe1\u606f\u7cfb\u7edf","\u5730\u576a\u6f06","\u7535\u573a","\u7535\u6c14\u5de5\u7a0b","\u7535\u6c14\u63a7\u5236","\u4e1c\u7ecf","\u4e1c\u5357\u5927\u5b66","\u8bfb\u540e\u611f","\u8bfb\u4e66\u7b14\u8bb0"
#
# """
#
# # rrrr = re.compile(r"""F.context\('tagList', [\s\S]*?"\]\}\);""")  # 截取带有三级的文本的 F.context
# # s = rrrr.findall(s)[0]
#
# r2 = re.compile(r'"(\w*?)",')  # 所有，除了尾部
# end = re.compile(r'"(\w*?)"]}')  # 尾部一个
#
# b = set(r2.findall(s))  # 正则有限，set去重
# print(len(b))
# # end = end.findall(s)[0]
# # b.add(end)  # 所有
#
from urllib import parse
from chardet import detect
parse.quote()
parse.u
a = parse.unquote('%B4%F3%D7%DA%C9%CC%C6%B7')
a = a.encode('')
print(a)
print(detect(a))
