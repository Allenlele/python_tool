# -*-coding:utf-8-*-
# Created by 一只尼玛 on 16-8-26.
# 功能:
# 测试爬虫

from tool.jhttp.spider import getHtml

if __name__ == "__main__":
    url="http://m.vip.com/server.html"
    postdata={"method":"getClassifyList","params":{"page":"classify-list-47301-0-0-0-0-1-20.html","np":1,"ep":20,"category_id"
:"4","brand_store_sn":"","filter":"","sort":"3","query":""},"id":1472195242113,"jsonrpc":"2.0"}
    cookie=r''''''
    header = [('User-Agent',
               'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0'),
              ('Referer', 'http://m.vip.com/classify-list-47301-0-0-0-0-1-20.html'),
              ('Host', 'm.vip.com'),
              ('Origin-Referer','http://m.vip.com/classify.html'),
              ('Cookie',cookie)]
    bytedata=getHtml(url,'',postdata,header)
    print(bytedata.decode('utf-8'))