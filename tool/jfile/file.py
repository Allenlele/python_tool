# -*-coding:utf-8-*-
# Created by 一只尼玛 on 16-8-26.
# 功能:
#  文件类
#
#

import xml.dom.minidom
import json
from openpyxl import Workbook
from openpyxl import load_workbook
import urllib.request, urllib.parse, http.cookiejar
import os, time, re
import http.cookies
import xlsxwriter as wx
from PIL import Image
import pymysql
import socket


# 找出文件夹下所有html后缀的文件
def listfiles(rootdir, prefix='.xml'):
    file = []
    for parent, dirnames, filenames in os.walk(rootdir):
        if parent == rootdir:
            for filename in filenames:
                if filename.endswith(prefix):
                    file.append(rootdir + '/' + filename)
            return file
        else:
            pass


def writeexcel(path, dealcontent):
    workbook = wx.Workbook(path)
    top = workbook.add_format(
        {'border': 1, 'align': 'center', 'bg_color': 'white', 'font_size': 11, 'font_name': '微软雅黑'})
    red = workbook.add_format(
        {'font_color': 'white', 'border': 1, 'align': 'center', 'bg_color': '800000', 'font_size': 11,
         'font_name': '微软雅黑', 'bold': True})
    image = workbook.add_format(
        {'border': 1, 'align': 'center', 'bg_color': 'white', 'font_size': 11, 'font_name': '微软雅黑'})
    formatt = top
    formatt.set_align('vcenter')  # 设置单元格垂直对齐
    worksheet = workbook.add_worksheet()  # 创建一个工作表对象
    width = len(dealcontent[0])
    worksheet.set_column(0, width, 38.5)  # 设定列的宽度为22像素
    for i in range(0, len(dealcontent)):
        if i == 0:
            formatt = red
        else:
            formatt = top
        for j in range(0, len(dealcontent[i])):
            if i != 0 and j == len(dealcontent[i]) - 1:
                if dealcontent[i][j] == '':
                    worksheet.write(i, j, ' ', formatt)
                else:
                    try:
                        worksheet.insert_image(i, j, dealcontent[i][j])
                    except:
                        worksheet.write(i, j, ' ', formatt)
            else:
                if dealcontent[i][j]:
                    worksheet.write(i, j, dealcontent[i][j].replace(' ', ''), formatt)
                else:
                    worksheet.write(i, j, '无', formatt)

    workbook.close()


# 去除标题中的非法字符 (Windows)
def validateTitle(title):
    rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/\:*?"<>|'
    new_title = re.sub(rstr, "", title)
    return new_title


# 递归创建文件夹
def createjia(path):
    try:
        os.makedirs(path)
    except:
        print('目录已经存在：' + path)


def todaystring():
    today = time.strftime('%Y%m%d', time.localtime())
    return today
