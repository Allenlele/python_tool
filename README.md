# Python_Tool工具库

>本库功能强劲,python3专用.
>由于对包机制不熟，所以请见谅

# 目录结构

```
---- tool 工具箱
---- example　工具箱示例
---- scrapy　爬虫例子
---- data　数据
```

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

2.jhttp　网络包

```
# 自己封装的抓取函数
getHtml(url, daili='', postdata={}, header=[])
```

3.jfile　文件包

```
# 找出文件夹下所有html后缀的文件
def listfiles(rootdir, prefix='.xml')

# 将数据写入Excel
def writeexcel(path, dealcontent=[])

# 去除标题中的非法字符 (Windows)
def validateTitle(title)

# 递归创建文件夹
def createjia(path)

# 今天日期的字符串
def todaystring()
```