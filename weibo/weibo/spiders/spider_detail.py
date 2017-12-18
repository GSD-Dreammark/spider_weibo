#根据微博爬取具体内容爬取微博的信息
import scrapy
from scrapy.http import Request
# 爬搞笑
class crawl_weibo(scrapy.Spider):
    name = "crawl_detail" #要调用的名字
    allowed_domains = ["weibio.com"] #分一个域
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }
    def start_requests(self):
        url =  "https://weibo.com/1852220282/FzD45ll5R?ref=feedsdk"
        yield Request(url, headers=self.headers)
    # red = redis.Redis(host='127.0.0.1', port=6379)
    # def start_requests(self):
    #     for url in self.start_urls:
    #         yield SplashRequest(url, self.parse, args={'wait':2})
    def parse(self, response):
        print(response.body.decode("gbk"))

