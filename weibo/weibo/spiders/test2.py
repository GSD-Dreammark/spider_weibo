# 使用PhantomJS
from scrapy.spiders import Spider
import time
from selenium import webdriver
class TmallAndTaoBaoSpider(Spider):
    name = "tts2"
    allowed_domains = []
    start_urls = []
    def __init__(self, *args, **kwargs):
        self.driver = webdriver.PhantomJS()
        url = "https://weibo.com/?category=1760"
        self.start_urls.append(url)
    def __del__(self):
        if self.driver is not None:
            self.driver.quit()
    def parse(self, response):
        self.driver.get(response.url)
        time.sleep(4)
        print(self.driver.page_source)

