import requests
import json
import pandas as pd

# def hello(name):
#   print(f"Hello", name)

# hello("Bob")
# hello("Frank")
# hello("King")

url = "https://jsonplaceholder.typicode.com/users/1"

response = requests.get(url)
data = response.json()



# print(json.dumps(data, indent=4))

# name = data["name"]
# addy = data["address"]["street"]
# print(f"The name is {name}")
# print(f"The addy is {addy}")

df = pd.DataFrame(data)

new_row = [
{"id": 2, "name": "Frank", "username": "fonwenu", "email": "fonwe@gmail.com", "address": "123 street", "phone": "", "website": "site.local", "company": "Tesla"},
{"id": 3, "name": "Test", "username": "Lisa", "email": "lisa@gmail.com", "address": "123 street", "phone": "", "website": "site.local", "company": "GM"}
]
new_df = pd.DataFrame(new_row) # Convert new rows into a DataFrame

df = pd.concat([df, new_df], ignore_index=True) # add new data to a row
df['username'] = df['username'].str.upper()
df.to_excel("output.xlsx", index=False) # prints out the data to and excel sheet

