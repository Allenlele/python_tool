# !usr/bin/python3.4
# -*- coding:utf-8 -*-

import os
import time
import random
import json
import requests
import urllib.request
import re
from tool.jfile.file import *


# 伪装头部抓json
def gethtml(url, postdata):
    header = {'User-Agent':
                  'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0',
              'Referer':
                  'http://image.baidu.com',
              'Host': 'image.baidu.com',
              'Accept': 'text/plain, */*; q=0.01',
              'Accept-Encoding': 'gzip, deflate',
              'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
              'Connection': 'keep-alive'}

    # 解析网页
    html_bytes = requests.get(url, headers=header, params=postdata)

    return html_bytes


# 伪装头部抓图片
def getimg(url):
    # 制作一个专家
    opener = urllib.request.build_opener()

    # 打开专家头部
    opener.addheaders = [('User-Agent',
                          'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0'),
                         ('Referer',
                          'http://image.baidu.com'),
                         ('Host', 'image.baidu.com')]
    # 分配专家
    urllib.request.install_opener(opener)

    # 解析img
    html_img = urllib.request.urlopen(url)

    return html_img


if __name__ == '__main__':

    # 搜索的关键字
    keyword = input('请输入你要查找的关键字：')

    pictype = {
        "1": "thumbURL",
        "2": "middleURL",
        "3": "hoverURL"
    }

    temp = input("抓大图按3，中图2，小图1：")
    if temp != '1' and temp != '2' and temp != '3':
        baibai = pictype['1']
    baibai = pictype[temp]
    # 页数
    page = int(input('你要抓取多少页：'))

    number = 1

    # 建立文件夹
    dirpath = "../../data/baidu/" + todaystring() + "/" + keyword
    jsonpath = dirpath + "/json"
    picpath = dirpath + "/pic"
    createjia(jsonpath)
    createjia(picpath)

    while number <= page:
        # 构造页数
        pn = 30 + (page - 1) * 60

        # 构造时间戳
        timerandom = random.randint(100, 999)
        nowtime = int(time.time())
        lasturl = str(nowtime) + str(timerandom) + '='

        # 构造post
        postdata = {
            'tn': 'resultjson_com',
            'ipn': 'rj',
            'ct': 201326592,
            'is': '',
            'fp': 'result',
            'queryWord': keyword,
            'cl': 2,
            'lm': -1,
            'ie': 'utf-8',
            'oe': 'utf-8',
            'adpicid': '',
            'st': -1,
            'z': '',
            'ic': 0,
            'word': keyword,
            's': '',
            'se': '',
            'tab': '',
            'width': '',
            'height': '',
            'face': 0,
            'istype': 2,
            'qc': '',
            'nc': 1,
            'fr': '',
            'pn': pn,
            'rn': 30,
            'gsm': '1e',
            lasturl: ""
        }

        url = 'http://image.baidu.com/search/acjson?'

        # 解析网址
        contents = gethtml(url, postdata)

        # 将文件以json的格式保存在json文件夹
        file = open(jsonpath + '/' + str(pn) + '.json', 'wb')
        file.write(contents.content)
        file.close()

        print('已经抓取' + str(number) + '页')

        number = number + 1

    # 找到json文件夹下的所有文件名字
    files = listfiles(jsonpath + "/", '.json')

    for filename in files:
        # 读取json得到图片网址
        doc = open(filename, 'rb')

        # ('UTF-8')('unicode_escape')('gbk','ignore')
        doccontent = doc.read().decode('utf-8', 'ignore')
        product = doccontent.replace(' ', '').replace('\n', '')
        product = json.loads(product)

        # 得到字典data
        onefile = product['data']

        for item in onefile:
            try:
                pic = getimg(item[baibai])
                # 保存地址和名称
                if item['fromPageTitleEnc']:
                    filenamep = picpath + '/' + validateTitle(item['fromPageTitleEnc'])
                else:
                    filenamep = picpath + '/' + validateTitle(time.strftime('%H%M%S', time.localtime()))

                # 保存为gif
                houzhui = "gif"
                xxpic = filenamep + "." + houzhui
                filess = open(xxpic, 'wb')
                filess.write(pic.read())
                filess.close()
                print('图片:' + xxpic + ' 下载完成')

                # 改名
                realxxpic = filenamep + "." + filetype(xxpic)
                os.rename(xxpic, realxxpic)
                print('图片改名:' + realxxpic)

                # 每一次下载都暂停1-3秒
                loadimg = random.randint(1, 3)
                print('暂停' + str(loadimg) + '秒')
                time.sleep(loadimg)

            except Exception as err:
                print(err)
                print('暂停' + str(loadimg) + '秒')
                time.sleep(loadimg)
                continue
