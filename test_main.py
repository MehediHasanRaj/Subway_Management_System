import json

import requests

URL = "http://127.0.0.1:8000/api/"
data = {
    'name':'big break wich',
    'price': '1.55',
    'type':'sandwich'

}

json_data = json.dumps(data)
r = requests.post(url=URL, data = json_data)

data = r.json()
print(data)