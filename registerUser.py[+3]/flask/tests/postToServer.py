import requests
import json

url = "http://52.59.231.135:8080/registerUser"
obj = json.dumps({"firstName":"Shivam",
    "lastName":"Smith",
    "email":"bob@smith",
    "passHash": "password"
})

x = requests.post(url, data = obj)

print(x.text)