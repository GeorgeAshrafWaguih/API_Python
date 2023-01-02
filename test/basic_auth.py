import requests
from test import keys

url = "https://defendtheweb.net/auth"
payload = {
    "username": keys.USERNAME,
    "password": keys.PASSWORD
}

resp = requests.post(url=url, data=payload)
print(resp.status_code)

