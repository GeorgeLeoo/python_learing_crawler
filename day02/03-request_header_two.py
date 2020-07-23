import urllib.request
import string


def load_baidu():
    url = "https://www.baidu.com"

    # 添加请求头信息
    header = {
        # 浏览器的版本
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
    }

    # 创建请求对象
    # 方式1 默认
    # request = urllib.request.Request(url, headers=header)

    # 方式2 动态添加请求头
    request = urllib.request.Request(url)
    request.add_header("User-Agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36")

    # 请求网络数据
    response = urllib.request.urlopen(request)

    data = response.read().decode("utf-8")

    # 获取到完整的url
    final_url = request.get_full_url()
    print(final_url)

    # 响应头
    # print(response.headers)

    # 请求头
    request_headers = request.headers
    # print(request_headers)

    # 注意，次方法需要首字母大些，其他小写
    ua = request.get_header("User-agent")
    # print(ua)

    with open("02-request_header.html", "w") as f:
        f.write(data)


load_baidu()
