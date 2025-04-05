import requests
import json
import pandas as pd
import logging
from dotenv import load_dotenv
import os

load_dotenv()

API = os.getenv("API")
logging.basicConfig(filename="/Users/franklin/Documents/Git/pandas-prj/stock app/stock.log", level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

stock = "AAPL"
TIME_SERIES = "TIME_SERIES_DAILY"

url = f"https://www.alphavantage.co/query?function={TIME_SERIES}&symbol={stock}&apikey={API}"

r = requests.get(url)
logging.info(f"Retriving stock info from {url}")
if r.status_code == 200:
    print(r.status_code)
    logging.info(f"status code is {r.status_code}")
    data = r.json()
    print(data)
    
# Pretty-print the JSON response
formatted_json = json.dumps(data, indent=2)

# Extract time series data
time_series_key = "Time Series (Daily)"
logging.info(f"grabbing current data for {time_series_key}")
if time_series_key in data:
    latest_date = next(iter(data[time_series_key]))  # Get the most recent date
    latest_data = data[time_series_key][latest_date]  # Fetch stock details for that date

    # Store it in a dictionary
    stock_info = {
        "date": latest_date,
        "open": latest_data.get("1. open", "N/A"),
        "high": latest_data.get("2. high", "N/A"),
        "low": latest_data.get("3. low", "N/A"),
        "close": latest_data.get("4. close", "N/A"),
        "volume": latest_data.get("5. volume", "N/A"),
    }

    print(stock_info)
    logging.info(f"print out current data{stock_info}")
    # Convert to a DataFrame
    df = pd.DataFrame([stock_info], index=[0])
    #print(df["open"]) 
    print(df.head())  # Print first few rows
    df.to_csv("/Users/franklin/Documents/Git/pandas-prj/stock app/output.csv", sep="|", index=False)
else:
    print("Error: No time series data found.")
    
    
    
    


