import urllib.request
import string

def load_baidu():
    url = "http://www.baidu.com"

    # 创建请求对象
    request = urllib.request.Request(url)

    # 请求网络数据
    response = urllib.request.urlopen(request)

    data = response.read().decode("utf-8")

    with open("02-request_header.html", "w") as f:
        f.write(data)

    # 响应头
    # print(response.headers)

    # 请求头
    request_headers = request.headers
    print(request_headers)


load_baidu()
