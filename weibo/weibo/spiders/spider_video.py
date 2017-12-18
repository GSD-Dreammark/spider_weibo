# #根据微博爬取具体内容爬取微博的信息
# import scrapy
# import requests
# from scrapy.http import Request
# # 爬搞笑
# class crawl_weibo(scrapy.Spider):
#     name = "crawl_video" #要调用的名字
#     allowed_domains = [] #分一个域
#     headers = {
#         'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
#     }
#     def start_requests(self):
#         url =  "https://wsqncdn.miaopai.com/stream/VEHxpEUhiwvJlmGVP12NaFWPux8LhSC2ZxRyFA___0_1513490590.mp4?ssig=fd90007813dd7aa7fa33e7a312c1fe98&time_stamp=1513605335365"
#         yield Request(url, headers=self.headers)
#     # red = redis.Redis(host='127.0.0.1', port=6379)
#     # def start_requests(self):
#     #     for url in self.start_urls:
#     #         yield SplashRequest(url, self.parse, args={'wait':2})
#     def parse(self, response):
#         dest_resp = requests.get(response.url)
#         # 视频是二进制数据流，content就是为了获取二进制数据的方法
#         data = dest_resp.content
#         # 保存数据的路径及文件名
#         path = 'test.mp4'
#         f = open(path, 'wb')
#         f.write(data)
#         f.close()
#         print('下载完成')
# 使用scrapy 爬视屏有问题
import requests
import re
link="https://wsqncdn.miaopai.com/stream/VEHxpEUhiwvJlmGVP12NaFWPux8LhSC2ZxRyFA___0_1513490590.mp4?ssig=fd90007813dd7aa7fa33e7a312c1fe98&time_stamp=1513605335365"
dest_resp = requests.get(link)
#视频是二进制数据流，content就是为了获取二进制数据的方法
data = dest_resp.content
#保存数据的路径及文件名
path = 'sss.mp4'
f = open(path, 'wb')
f.write(data)
f.close()
print('下载完成')