FROM python:3.6
RUN mkdir -p /usr/src/app
ENV HOME=/usr/src/app
WORKDIR $HOME
ADD requirements.txt $HOME
RUN pip install -r requirements.txt -i https://pypi.douban.com/simple
COPY . $HOME
WORKDIR $HOME/chatbot_web
RUN ls

