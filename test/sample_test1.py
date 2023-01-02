import requests
import json

# Simple API Test
BASE_URL = "https://reqres.in"

# Adding Query Parameter
params = {'page': 2}
response = requests.get(BASE_URL + "/api/users", params=params)
print(response)
print(response.json())
print(json.dumps(response.json(), indent=4))

# Parsing the JSON response
resp = response.json()
first_names = [d['first_name'] for d in resp["data"]]
print(first_names)