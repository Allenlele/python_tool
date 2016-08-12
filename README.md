# Python_Tool工具库
>本库功能强劲,python3专用.

# 包介绍
1.jjson json处理库的封装
```
# json字符串解析成对象
def stringToObject(jstring)

# json字符串校验是否正确,可打印错误
def isRightJson(jstring, printerror=False)

# 对象解析成json字符串,支持排序和缩进
def objectToString(jobject, sort=False, indent=None)

# 格式化json字符串,默认按键排序
def formatStringToString(jstring, sort=True)

# 格式化json字符串,并可选择存入文件
def formatStrigToFile(filepath, sort=True, filesavepath="")
```