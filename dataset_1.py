import pandas as pd
df = pd.read_csv('tips.csv')

print(df.head(n=5))
# print(df.loc[0])
# print(df.loc[0:3])
# print(df.loc[[0,3],['sex', 'sex']])

# def row_section(table1, table2):
#     print(df.loc[[0,3],[table1, table2]])

# row_section('smoker', 'size')
# row_section('day', 'tip')

avg = df['total_bill'].mean()
filter = df[df['sex'] == 'Male']
top = filter.head(n=5)
print(top)
