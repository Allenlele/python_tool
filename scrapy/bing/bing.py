# !usr/bin/python3.4
# -*- coding:utf-8 -*-

import json
# import grequests
import requests
import re
import time
from tool.jfile.file import *


def exception_handler(request, exception):
    print('连接错误...')


# def geturl(urls):
#     header = {'User-Agent':
#                   'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0',
#               'Referer': 'http://cn.bing.com',
#               'Host': 'cn.bing.com'}
#
#     # 保持连接畅通
#     sn = requests.Session()
#     rs = [grequests.get(url, headers=header, session=sn) for url in urls]
#
#     return grequests.map(rs, exception_handler=exception_handler, gtimeout=10)

def geturlnot(urls):
    header = {'User-Agent':
                  'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0',
              'Referer': 'http://cn.bing.com',
              'Host': 'cn.bing.com'}

    rs = [requests.get(url, headers=header) for url in urls]
    return rs


def get(url):
    header = {'User-Agent':
                  'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0',
              'Referer': 'http://cn.bing.com',
              'Host': 'cn.bing.com'}

    # 解析网页
    html_bytes = requests.get(url, headers=header)
    return html_bytes


def prints(timesleep):
    print('暂停' + str(timesleep) + '秒后开始批量下载图片，请保持网络畅通...')
    time.sleep(timesleep)


if __name__ == '__main__':
    dirpath = '../../data/bing/' + todaystring()
    createjia(dirpath)
    i = 0
    # 抓取频次
    every = 5
    # 休息时间
    timesleep = 1
    img = []
    imgname = []
    # 错误个数
    errortimes = 0
    errormax = 3
    while True:
        url = 'http://cn.bing.com/HPImageArchive.aspx?format=js&idx=' + str(i) + '&n=1'

        contents = get(url)
        data = contents.content.decode('utf-8', 'ignore')
        data = json.loads(data)
        try:
            onefile = data['images']
            for item in onefile:
                img.append(item['url'])
                imgname.append(item['copyright'].replace(' ', ''))
                print(img[i])
            i = i + 1
        except Exception as err:
            print(err)
            errortimes = errortimes + 1
            if errortimes == errormax:
                break
            else:
                pass

        # 每次累计到一定程度就并发抓取
        if i % every == 0:
            print('已经搜集好网址...')
            prints(timesleep)
            print('正在下载...')
            try:
                pics = geturlnot(img)
            except Exception as err:
                print(err)
                errortimes = errortimes + 1
                if errortimes == errormax:
                    break
                else:
                    pass

            j = 0
            for pic in pics:
                filenamep = dirpath + "/" + validateTitle(imgname[j] + '.jpg')
                filess = open(filenamep, 'wb')
                filess.write(pic.content)
                filess.close()
                print('已经写入第' + str(j + 1) + '张图片')
                j = j + 1

        prints(timesleep)
