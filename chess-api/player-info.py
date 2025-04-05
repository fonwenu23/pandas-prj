import requests
import pandas as pd
import datetime
import json

def headers():
    headers = {'User-Agent': 'myapi'}
    return headers
          
def get_player_stats(name, headers):
    if get_player_info(name, headers):
        url = f"https://api.chess.com/pub/player/{name}/stats"
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            data = r.json()
            print(json.dumps(data, indent = 2))
            print("Player stats retrieved successfully.")
            return data  # Returning stats
        else:
            print("Error retrieving stats.")
    else:
        print("Error: Player info not found.")
    
def get_player_info(name, headers):

# Convert Unix timestamp to human-readable format
    url = f"https://api.chess.com/pub/player/{name}"
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        data = r.json()
       # print(json.dumps(data, indent = 2))
        player_info = {
            'Username' : data.get('username', 'N/A'),
            'Title': data.get('title', 'N/A'),
            'Country': data.get('country','N/A').split('/')[-1],
            'Last_Online': (change_time(data.get('last_online', 'N/A')))
        }
        df = pd.DataFrame([player_info])
        print(df)
        return True
    return False
def change_time(timestamp):
    """Converts a Unix timestamp to UTC."""
    utc_time = datetime.datetime.fromtimestamp(timestamp)
    return utc_time.strftime('%Y-%m-%d')
    



headers = headers()
get_player_stats("udodili23", headers)
