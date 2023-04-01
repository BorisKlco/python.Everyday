import json

import requests

ISS_URL = "http://api.open-notify.org/iss-now.json"

resp = requests.get(ISS_URL, timeout=5)
data = resp.json()

print(data)
