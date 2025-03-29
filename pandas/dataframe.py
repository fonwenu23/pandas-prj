import pandas as pd

# random data
data = {
    'Name': ['Kobe', 'Rocky', 'Lebron'],
    'Age': ['42', '60', '41'],
    'BDay': ['2/23/1983', '3/12/1964', '12/26/1982']
}
# Stores the data in a data frame
df = pd.DataFrame(data)

# adding a new record to an existing data frame
df.loc[len(df)] = ['Shaq', '42', '8/23/1983']
df['Team'] = ['Lakers', 'None', 'Lakers', 'Lakers']
df.loc[df['Name']  == 'Shaq', 'Team'] = 'Heat'

# Prints out the data frame. 
print(df)

# Prints out data types
#df.info()


