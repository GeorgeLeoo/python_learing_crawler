import urllib.request
import urllib.parse
import string

def get_method_params():
    url = "https://www.baidu.com/s?wd="
    # 拼接字符串
    name = "美女"
    final_url = url+name
    print(final_url)
    # 使用代码发送请求
    response = urllib.request.urlopen(final_url)
    print(response)
    # UnicodeEncodeError: 'ascii' codec can't encode characters in position 10-11
    # python 是解释性语言，解析器只支持 ascii 0 -127， 即不支持中文，故需要转义

def get_method_params_parse():
    url = "http://www.baidu.com/s?wd="
    # 拼接字符串
    name = "美女"
    final_url = url+name
    print(final_url)
    # 使用代码发送请求
    # 中文转义
    encode_new_url = urllib.parse.quote(final_url, safe=string.printable)
    print(encode_new_url)
    response = urllib.request.urlopen(encode_new_url)
    print(response)
    # 读取内容
    data = response.read().decode()
    print(data)
    # 保存到本地
    with open("02-encode.html", "w", encoding="utf-8") as f:
        f.write(data)

get_method_params_parse()
