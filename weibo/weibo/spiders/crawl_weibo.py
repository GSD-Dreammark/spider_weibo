# 爬取微博的信息
import scrapy
import redis
from weibo.spiders import bloomfilter
from scrapy_splash import SplashRequest
# 爬搞笑
class crawl_weibo(scrapy.Spider):
    name = "crawl_weibo" #要调用的名字
    allowed_domains = ["weibio.com"] #分一个域
    bf = bloomfilter.BloomFilter()
    start_urls = [#所有要爬路径
        "https://weibo.com/?category=10011"
    ]
    ii=0
    red = redis.Redis(host='127.0.0.1', port=6379)
    def start_requests(self):
        # script = """
        #                    function main(splash)
        #                        splash:set_viewport_size(1028, 10000)
        #                        splash:go(splash.args.url)
        #                        local scroll_to = splash:jsfunc("window.scrollTo")
        #                        scroll_to(0, 8000)
        #                        splash:wait(20)
        #                        return {
        #                            html = splash:html()
        #                        }
        #                    end
        #                    """
        # 爬取滑动
        # script = """
        #         function main(splash)
        #             local scroll_to = splash:jsfunc("window.scrollTo")
        #             local get_body_height = splash:jsfunc(
        #                 "function() {return document.body.scrollHeight;}"
        #             )
        #             assert(splash:go(splash.args.url))
        #             splash:wait(4)
        #             scroll_to(300, get_body_height())
        #             splash:wait(3)
        #             scroll_to(300, get_body_height()*2)
        #             splash:wait(3)
        #             return splash:html()
        #         end
        #         """
        # for url in self.start_urls:
        #     yield SplashRequest(url, self.parse,
        #                     endpoint='execute',
        #                     args={'lua_source': script,'wait':4})
        #笨方法：多次爬微博去重
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, args={'wait':4})
    def parse(self, response):
        # 转码有问题？？？ 改为gbk 就好 ，多式几次编码类型
        #print(response.body.decode('utf-8'))
        # 好像是识别出来我是爬虫,没有cookie ,每次访问都会自动创建一个cookie去判断是否是爬虫文件
        # 那splash就可以抓取，但是要延长加载的时间\
        # 怎样去查看去重的redis
        # 爬取搞笑的链接
        rss=response.xpath('//div[@class="UG_list_b"]/@href')
        for rs in rss:
            href='https:'+rs.extract()
            print(href)
            if self.bf.isContains(href):  # 判断字符串是否存在
                self.ii+=1
            else:
                self.bf.insert(href)
                self.red.lpush('weibo_href', href)
            print(self.ii)
            if self.ii<10:
                print('++++++')
                yield SplashRequest(response.url, callback=self.parse, args={'wait': 4})

