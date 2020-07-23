import urllib.request


def proxy_user():
    url = "https://www.baidu.com"

    # 添加代理
    proxy_list = [
        {"http": "125.108.101.73:9000"},
        {"http": "110.243.23.74:9999"},
        {"http": "113.195.224.15:9999"},
        {"http": "120.83.111.7:9999"},
        {"http": "175.42.123.217:9999"},
    ]

    for proxy in proxy_list:
        print(proxy)

        # 创建处理器
        proxy_handler = urllib.request.ProxyHandler(proxy)

        # 创建opener
        opener = urllib.request.build_opener(proxy_handler)

        try:
            data = opener.open(url, timeout=1).read()
            print(data)
        except Exception as e:
            print(e)


proxy_user()
