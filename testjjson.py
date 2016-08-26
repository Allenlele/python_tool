# -*-coding:utf-8-*-
# Created by 一只尼玛 on 16-8-26.
# 功能: 测试jjson

from jjson.stringjson import formatStrigToFile
from jjson.basejson import stringToObject,objectToString,isRightJson

if __name__ == "__main__":
    file = "./jjson/test/testjson.md"
    savefile="./jjson/test/testjsonformat.md"
    temp = formatStrigToFile(file,True,savefile)
    print(temp)

    jstring = '''
    {
    "adid": "",
    "aid": "",
    "aiid": "",
    "an": "",
    "andid": ""
    }'''
    jobject = stringToObject(jstring)
    print(jobject)
    print(objectToString(jobject))
    print(objectToString(jobject, True, indent=4))

    errorstring = "{dddd:ddd}"
    ok = isRightJson(errorstring)
    print(ok)

    ok = isRightJson(errorstring, True)
    print(ok)
