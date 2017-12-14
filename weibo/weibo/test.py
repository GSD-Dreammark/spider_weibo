import urllib.request
from lxml import etree
import json


url = "https://www.qiushibaike.com/8hr/page/2/ "

headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36"

}

request = urllib.request.Request(url,headers=headers)

response = urllib.request.urlopen(request).read().decode('utf-8').encode("utf-8")
# 返回字符串
xml = etree.HTML(response)
# 作为根节点
node_list = xml.xpath('//div[contains(@id, "qiushi_tag")]')


item = {}
for node in node_list:

    username = node.xpath('//h2/text()')[0]
    image = node.xpath('.//div[@class="thumb"]//@src')
    content = node.xpath('.//div[@class="content"]/span')[0].text
    zan = node.xpath('.//i')[0].text
    comment = node.xpath('.//i')[1].text
    print(username,image,content,zan,comment)
    item = {
        "username": username,
        "image": image,
        "content": content,
        "zan": zan,
        "comment": comment
    }
    items = json.dumps(item,ensure_ascii=False)
    with open("qiushi.json", "a") as f:
        f.write(json.dumps(items).encode("utf-8",'ignore').decode("utf-8") + "\n")
