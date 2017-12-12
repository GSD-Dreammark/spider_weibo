# 爬取微博的信息
import scrapy
from bson.objectid import ObjectId
from scrapy.http import Request
# 把起点首页的所有列表
class crawl_weibo(scrapy.Spider):
    name = "crawl_weibo" #要调用的名字
    allowed_domains = ["weibio.com"] #分一个域
    start_urls = [#所有要爬路径
        "https://weibo.com/?category=2"
    ]
    #每爬完一个网页会回调parse方法
    def parse(self, response):
        print('++++++')
        # 转码有问题？？？ 改为gbk 就好 ，多式几次编码类型
        print(response.body.decode('gbk'))