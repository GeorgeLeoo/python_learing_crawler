import urllib.request

def create_proxy():
    url = "https://blog.csdn.net/wangqing84411433/article/details/89600335"

    # 添加代理
    proxy = {
        # 免费写法
        # "http": "http://125.108.101.73:9000"
        # "http": "125.108.101.73:9000"
    }

    # 代理处理器
    proxy_handler = urllib.request.ProxyHandler(proxy)

    # 创建opener
    opener = urllib.request.build_opener(proxy_handler)

    # 拿着代理ip发送请求
    data = opener.open(url).read()

    print(data)


create_proxy()
