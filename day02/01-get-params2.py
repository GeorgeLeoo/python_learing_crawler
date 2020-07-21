import urllib.request
import urllib.parse
import string

def get_param():
    url = "http://www.baidu.com/s"

    params = {
        "wd": "中文",
        "key": "张",
        "value": "san"
    }
    str_params = urllib.parse.urlencode(params)
    print(str_params)

    final_url = url + str_params
    print(final_url)

    # 将带有中文的url转义为计算机可识别的url
    end_url = urllib.parse.quote(final_url, safe=string.printable)

    response = urllib.request.urlopen(end_url)

    data = response.read().decode("utf-8")

    print(data)


get_param()
