FROM python:3.6
RUN python -V
RUN apt-get update
RUN mkdir -p /usr/src/app
ENV HOME=/usr/src/app
WORKDIR $HOME
COPY requirements.txt $HOME
COPY xadmin-django2.zip $HOME
RUN pip install -r requirements.txt -i https://pypi.douban.com/simple
RUN pip install $HOME/xadmin-django2.zip
COPY . $HOME


