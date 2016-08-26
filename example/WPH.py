# !/usr/bin/python3.4
# -*- coding: utf-8 -*-
# 这是一个强大的库！！！
# http://docs.python-requests.org/en/latest/user/quickstart/
#
# 更新安装
# pip3 install requests --upgrade

import requests
import json

if __name__ == '__main__':
    # url = "http://m.vip.com/classify.html#page=classify"
    # http://m.vip.com/server.html?f=123test123&_=1472190107136
    # url = "http://m.vip.com/server.html?"
    header = {
        'User-Agent': 'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
        'Referer': 'http://m.vip.com/',
        'Host': 'm.vip.com',
    }
    postdata = {"method": "getClassifyBrand",
                "params": {"brand_store_sn": "", "page": "classify-list-47301-0-0-0-0-1-20.html"
                    , "query": ""}, "id": 1472203604524, "jsonrpc": "2.0"}

    vip = "http://m.vip.com/server.html"
    print(vip)

    res = requests.post(url=vip, headers=header, json=postdata)
    print(res.status_code)
    print(res.headers)
    print(res.content.decode("utf-8","ignore"))
