from django.apps import AppConfig


class CrawlConfig(AppConfig):
    name = 'crawl'
    verbose_name = '百度知道数据'

    def ready(self):
        import crawl.signals
