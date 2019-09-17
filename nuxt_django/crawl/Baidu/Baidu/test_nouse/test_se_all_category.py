import requests
import re
from chardet import detect


s = requests.get('https://zhidao.baidu.com/list?cid=105100').text
s = s.encode('latin-1').decode('unicode_escape')
print(s)

rrrr = re.compile(r"""F.context\('tagList', [\s\S]*?"\]\}\);""")  # 截取带有三级的文本的 F.context

s = rrrr.findall(s)[0]
r2 = re.compile(r'"(\w*?)",')  # 所有，除了尾部
end = re.compile(r'"(\w*?)"\]')  # 尾部一个
b = set(r2.findall(s))  # 正则有限，set去重
end = end.findall(s)[0]
b.add(end)  # 所有
print(len(b))
