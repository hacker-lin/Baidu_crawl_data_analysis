FROM python:3.6
RUN pip install --upgrade pip -i https://pypi.douban.com/simple

RUN mkdir /root/mycode 
ENV HOME=/root/mycode

WORKDIR $HOME
COPY Baidu  $HOME

RUN pip install -r requirements.txt -i https://pypi.douban.com/simple
