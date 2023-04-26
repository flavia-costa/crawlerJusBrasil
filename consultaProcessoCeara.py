import json
import requests

with open('numero_processoCeara.json') as f:
    data = json.load(f)

url = "http://127.0.0.1:5000/api"

headers = {
    'Content-Type': 'application/json'
}

response = requests.post(url, headers=headers, json=data)


with open("processoCeara.json", "w", encoding="utf-8") as outfile:
    json.dump(response.json(), outfile, ensure_ascii=False)
 