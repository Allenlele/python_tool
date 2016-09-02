# -*-coding:utf-8-*-
# Created by 一只尼玛 on 16-8-26.
# 功能:
#  文件类
#
#


import os, time, re
import xlsxwriter as wx


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


# 将数据写入Excel
def writeexcel(path, dealcontent=[]):
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
            if dealcontent[i][j]:
                worksheet.write(i, j, dealcontent[i][j].replace(' ', ''), formatt)
            else:
                worksheet.write(i, j, '', formatt)

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


# 今天日期的字符串
def todaystring():
    today = time.strftime('%Y%m%d', time.localtime())
    return today


if __name__ == "__main__":
    path = "./test"
    createjia(path)
    content = [['第一列', '第二列'], ['１', '２']]
    writeexcel(path + "/" + todaystring() + ".xlsx", content)
