import json

SLOVAKIA = (48.14816, 17.10674)

import requests

ISS_URL = "http://api.open-notify.org/iss-now.json"


resp = requests.get(ISS_URL, timeout=5)
data = resp.json()

iss_lat = float(data["iss_position"]["latitude"])
iss_long = float(data["iss_position"]["longitude"])

if round(iss_lat) > 38 and round(iss_long) < 25:
    print("ok")

print(iss_long, iss_lat)
