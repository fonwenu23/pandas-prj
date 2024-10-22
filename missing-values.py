import pandas as pd
import numpy as np

# Create a sample DataFrame
data = {
    'First_name': [1, 2, np.nan, 4],
    'Last_name': [np.nan, 2, 3, 4],
    'Age': [1, 2, 3, 4]
}
df = pd.DataFrame(data)
print(df)

missing_values = df.isna()
print(missing_values)

# Drop rows with any missing values
df_dropped_rows = df.dropna()
print(df_dropped_rows)

# Drop columns with any missing values
df_dropped_columns = df.dropna(axis=1)
print(df_dropped_columns)


# Fill missing values with a constant (0 in this case)
df_filled_constant = df.fillna(0)
print(df_filled_constant)

average = df['First_name'].mean()

print(average)