import requests

r = requests.get("https://raw.githubusercontent.com/zhaoyuxuan/CMPUT404-lab1/master/get.py")
print(r.status_code)
