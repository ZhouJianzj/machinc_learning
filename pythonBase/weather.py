import requests
import re

"""发起请求"""


def get_request():
    url = "http://www.weather.com.cn/forecast/"
    response = requests.get(url)
    response.encoding = "utf-8"
    return response.text


"""处理数据"""


def data_parse(html_data):
    city = re.findall("<span class=\"name\">(.*?)</span>", html_data)
    print("城市为：", city)
    weather = re.findall("<span class=\"weather\">(.*?)</span>", html_data)
    print("天气：", weather)
    wd = re.findall("<span class=\"wd\">(.*?)</span>", html_data)
    print("温度：", wd)
    zs = re.findall("<span class=\"zs\">(.*?)</span>", html_data)
    print("情况：", zs)
    data_zip = zip(city, weather, wd, zs)
    data = list(data_zip)
    return data
