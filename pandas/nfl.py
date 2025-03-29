import pandas as pd

# pd.options.display.max_rows = 9999
df = pd.read_csv("Basic_Stats.csv")
# print(df.head(10))
#new_df = df.dropna()
# print(new_df.to_string())
# df['Position'].fillna('TE', inplace=True)
# print(new_df.to_string())
df.dropna(subset=['Date'], inplace = True)
import pandas as pd

# Adjust display settings
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 1000)
pd.set_option("display.colheader_justify", "center")

# Read the CSV
df = pd.read_csv("Basic_Stats.csv")
x = df["Birthday"].mode()[0]
# Fill NaN values with 130
df["Birthday"].fillna(x, inplace=True)

# Print DataFrame without index
print(df.to_string(index=False))


df.to_csv("Basic_Stats_Cleaned.csv", sep="|", index=False)

df.to.csv


# json2 = pd.read_json('data.json')
# #outputs data into a stting
# #print(df.to_string())

# json1 = pd.json_normalize(json2)
# #print(json2.to_string())

# df = pd.read_csv('data.csv')
# df.fillna(130, inplace = True)
# print(df.to_string())

