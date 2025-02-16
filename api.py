# Sample API response
import requests
import json

api_response = {
    "logs": [
        {"user": "alice", "event": "login", "timestamp": "2025-02-15T12:30:00Z"},
        {"user": "bob", "event": "failed_login", "timestamp": "2025-02-15T12:45:00Z"}
    ]
}

# Extracting specific fields
# logs = api_response["logs"]
# for log in logs:
#     print(f"User: {log['user']}, Event: {log['event']}, Time: {log['timestamp']}")


json_formatted_str = json.dumps(api_response, indent=2)
data1 = (api_response["logs"][0]["user"])
data2 = (api_response["logs"][0]["event"])

print(data1, data2)