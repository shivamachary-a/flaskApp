import requests
import json

url = "http://0.0.0.0:8080/registerUser"
obj = json.dumps({"firstName":"Bob",
    "lastName":"Smith",
    "email":"bob@smith",
    "passHash": "password"
})

x = requests.post(url, data = obj)

print(x.text)