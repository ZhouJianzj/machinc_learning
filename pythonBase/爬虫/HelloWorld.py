import requests
from bs4 import BeautifulSoup
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}
request = requests.get("http://10.255.200.11/portal/index.html?v=202103260001", headers=headers)
if request.ok:
    print(request)
    content = BeautifulSoup(request.text,"html.parser")
    print(content)
else:
    print("服务器拒绝服务！")
