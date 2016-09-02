# -*-coding:utf-8-*-
# Created by 一只尼玛 on 16-8-26.
# 功能:
#
#

import requests
from tool.jfile.file import *


def getIndex(type="cos", page=10):
    types = {"gif": "http://tu.duowan.com/m/bxgif", "meinv": "http://tu.duowan.com/m/meinv",
             "cos": "http://tu.duowan.com/tag/41.html"}
    offset = 0
    autoadd = 30
    url = types[type]

    dirpath = "../../data/" + type + "/" + todaystring()
    createjia(dirpath)
    for i in range(0, page):
        postdata = {'offset': offset + page * autoadd, 'order': 'created'}
        res = requests.get(url, postdata)
        filepath = open(dirpath + "/" + str(i) + ".html", "wb")
        filepath.write(res.content)
        filepath.close()


if __name__ == "__main__":
    getIndex()
