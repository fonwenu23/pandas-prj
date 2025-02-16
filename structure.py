import requests
import pandas as pd
import json

# url = "https://pokeapi.co/api/v2/ability/?limit=5"
# response = requests.get(url)
# data = response.json()

# # Convert nested JSON into a DataFrame
# df = pd.json_normalize(data['results'])  # Normalizes nested JSON
# print(df)
# # json_formatted_str = json.dumps(data, indent=2)
# # print(json_formatted_str)

security_log = {
    "eventID": "12345",
    "user": {"id": "A1", "name": "bob"},
    "eventDetails": {
        "action": "failed_login",
        "timestamp": "2025-02-16T12:00:00",
        "ip": "192.168.1.1"
    }
}
# print(security_log)
json_formatted_str = json.dumps(security_log, indent=2)
print(json_formatted_str)
df = pd.json_normalize(security_log, sep='_')  # Flatten with custom separator
print(df)

