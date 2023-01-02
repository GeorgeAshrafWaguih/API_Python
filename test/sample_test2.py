import requests
import json

BASE_URL = "https://reqres.in"

# POST
payload = {
    "name": "morpheus",
    "job": "leader"
}
response = requests.post(BASE_URL + "/api/users", data=payload)
print(response.json())

# PUT
payload = {
    "name": "morpheus",
    "job": "zion resident"
}
response = requests.put(BASE_URL + "/api/users/2", data=payload)
print(response.json())

# Delete
response = requests.delete(BASE_URL + "/api/users/2")
print(response.status_code)
