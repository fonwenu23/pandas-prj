import pandas as pd

# Read CSV
def read_csv():
    df = pd.read_csv("usernames.csv")
    # Clean leading/trailing spaces from strings
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
    # Convert empty strings to NaN
    df.replace("", float("NaN"), inplace=True)
    # Strip column names of spaces
    df.columns = df.columns.str.strip()
    # Fill missing "ID" with 109.0
    df["ID"] = df["ID"].astype("Int64")
    x = df["ID"].mean()
    df["ID"].fillna(109.0, inplace=True)

    # Fill missing "Salary" with 109.0
    df["Salary"] = pd.to_numeric(df["Salary"], errors='coerce')
    n = df["Salary"].median()
    df["Salary"].fillna(n, inplace=True)
    # df["Salary"] = df["Salary"] * 1000
    df["Salary"] = df["Salary"].astype(int)

    # Calculate mean of "Age" and fill missing "Age" values with the mean
    df["Age"] = pd.to_numeric(df["Age"], errors='coerce')
    x = df["Age"].median()
    df["Age"] = df["Age"].astype("Int64")
    df["Age"].fillna(x, inplace=True)

   # fill missing "Date" 
    df["Joining Date"] = pd.to_datetime(df["Joining Date"])
    # Fill missing dates with "2025-03-19"
    df["Joining Date"].fillna(pd.Timestamp("2025-03-19"), inplace=True)
    
    df["Department"].fillna("IT", inplace=True)
    
    df.dropna(subset=["Name"], inplace=True)



    # Fix email addresses that don't end with ".com"
    df["Email"] = df["Email"].apply(lambda x: x + ".com" if isinstance(x, str) and not x.endswith(".com") else x)

    # Print the cleaned dataframe
    print(df.to_string())
    print(df.isnull().sum())
read_csv()