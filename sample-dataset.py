import pandas as pd

data = {'name': ['Xavier', 'Ann', 'Jana', 'Yi', 'Robin', 'Amal', 'Nori'],
        'city': ['Mexico City', 'Toronto', 'Prague', 'Shanghai','Manchester', 'Cairo', 'Osaka'],
        'age': [41, 28, 33, 34, 38, 31, 37],
         'py-score': [88.0, 79.0, 81.0, 80.0, 68.0, 61.0, 84.0]
    }

row_labels = [101, 102, 103, 104, 105, 106, 107]

df = pd.DataFrame(data=data, index=row_labels)
cities = df['city']

l = [{'first_name':'John', 'last_name': 'Owens','compliance_report': 75},
      {'first_name':'Kim', 'last_name': 'Carton','compliance_report': 83},
      {'first_name':'Steve', 'last_name': 'Knicks','compliance_report': 96}]

# Print out top 3 rows of the data-set
# def data_set():
#     print(df.head(n=3))

# data_set()

# Prints out just the cities
print(cities)

# Using dot notation to access citites.
print(df.city)

print(cities[103])

print(pd.DataFrame(l))


