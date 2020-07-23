import urllib.request

def handler_opener():
    # 系统的urlopen并没有添加代理的功能，故需要自定义这个功能
    # urllib.request.urlopen()

    url = "https://blog.csdn.net/wangqing84411433/article/details/89600335"

    # 创建自己的处理器
    handler = urllib.request.HTTPHandler()

    # 创建自己的opener
    opener = urllib.request.build_opener(handler)

    # 用自己创建的opener调用open方法
    response = opener.open(url)
    print(response)

    data = response.read().decode("utf-8")
    with open("05.html", "w") as f:
        f.write(data)


handler_opener()
