import requests
import json

API_URL = "https://pokeapi.co/api/v2/ability/?limit=10&offset=0"  # Fixed URL

def poki():
    """Checks API connection before running other functions."""
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        print("Connection success... Retrieving results")
        return response  # Return response object for reuse
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")  
    except requests.exceptions.ConnectionError:
        print("Connection error! Please check your internet connection.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    
    return None  # Return None if request fails

def get_pki():
    """Fetches and prints a list of abilities from the API."""
    response = poki()  # Use poki() to check connection
    if response is None:
        print("Skipping get_pki due to an error in API request.")
        return
    
    try:
        data = response.json()
        if "results" not in data:
            print("Unexpected response format.")
            return

        for ability in data["results"]:
            print(f"Name: {ability['name']}")
            print(f"URL: {ability['url']}")
            print("-" * 40)

    except (KeyError, json.JSONDecodeError) as e:
        print(f"Error processing JSON data: {e}")

def get_pki_detail(name):
    """Fetches details of a specific ability by name."""
    url = f"https://pokeapi.co/api/v2/ability/{name}/"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        print(json.dumps(data, indent=2))

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error: {http_err}")
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")

# Run functions safely
get_pki()
get_pki_detail("damp")  # Uncomment to test fetching details
