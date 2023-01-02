import requests
import json

BASE_URL = "https://reqres.in"
params = {'page': 2}
response = requests.get(BASE_URL + "/api/users", params=params)
print(response)
print(response.json())
print(json.dumps(response.json(), indent=4))