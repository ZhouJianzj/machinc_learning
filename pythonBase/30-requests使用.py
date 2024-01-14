"""
使用requests 第三方模块爬取各个景点的天气
"""
import requests
import re

url = "http://www.weather.com.cn/forecast/"
response = requests.get(url)
response.encoding = "utf-8"
print(response.text)
# <span class="name">九寨沟</span>
# <span class="weather">晴转多云</span>
# <span class="wd">13/-2℃</span>
# <span class="zs">适宜</span>
city = re.findall("<span class=\"name\">(.*?)</span>", response.text)
print("城市为：", city)
weather = re.findall("<span class=\"weather\">(.*?)</span>", response.text)
print("天气：", weather)
wd = re.findall("<span class=\"wd\">(.*?)</span>", response.text)
print("温度：", wd)
zs = re.findall("<span class=\"zs\">(.*?)</span>", response.text)
print("情况：", zs)
data_zip = zip(city, weather, wd, zs)
data = list(data_zip)
for item in data:
    print(item)

# content = response.content
# print(content)

# 将百度的logo保存到本地
url = "https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png"

requests.get(url)
with open("baidu.png", 'wb') as file:
    file.write(response.content)
