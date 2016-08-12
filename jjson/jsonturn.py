# -*-coding:utf-8-*-
# Created by 一只尼玛 on 16-8-12.
# 功能:
#
#   序列化和反序列化json
#

import json


# json字符串解析成对象
def stringToObject(jstring):
    return json.loads(jstring)


# 对象解析成json字符串,支持排序和缩进
def objectToString(jobject, sort=False, indent=None):
    return json.dumps(jobject, sort_keys=sort, indent=indent)


if __name__ == "__main__":
    jstring = '''
    {
    "adid": "",
    "aid": "",
    "aiid": "",
    "an": "",
    "andid": ""
    }'''
    jobject = StringToObject(jstring)
    print(jobject)
    print(objectToString(jobject))
    print(objectToString(jobject,True,indent=4))
