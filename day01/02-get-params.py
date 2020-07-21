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
    url = "https://www.baidu.com/s?wd="
    # 拼接字符串
    name = "美女"
    final_url = url+name
    print(final_url)
    # 使用代码发送请求
    encode_new_url = urllib.parse.quote(final_url, safe=string.printable)
    print(encode_new_url)
    response = urllib.request.urlopen(encode_new_url)
    print(response)

get_method_params_parse()
