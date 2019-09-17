# -*- coding: utf-8 -*-

# Scrapy settings for Baidu project


BOT_NAME = 'Baidu'

SPIDER_MODULES = ['Baidu.spiders']
NEWSPIDER_MODULE = 'Baidu.spiders'

ROBOTSTXT_OBEY = False

CONCURRENT_REQUESTS = 100

DOWNLOAD_DELAY = 0

CONCURRENT_REQUESTS_PER_DOMAIN = 100
CONCURRENT_REQUESTS_PER_IP = 100

COOKIES_ENABLED = False

DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'

}

ITEM_PIPELINES = {
    # 'Baidu.pipelines.BaiduPipeline': 300,

    'Baidu.pipelines.MysqlTwistedPipeline': 1,
    # 'Baidu.pipelines.MysqlPipeline': 1du
    # 'scrapy_redis.pipelines.RedisPipeline': 300,

}

MYSQL_HOST = '39.107.86.223'
MYSQL_DBNAME = 'baidu'
MYSQL_USER = 'root'
MYSQL_PASSWORD = '123'
MYSQL_PORT = 3306
MYSQL_CHARSET = 'utf8'

MONGO_URL = '123.206.69.15'
MONGO_PORT = 27017

# 爬虫可以暂停/开始， 从爬过的位置接着爬取
# SCHEDULER_PERSIST = True
