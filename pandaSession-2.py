import pandas as pd
data = open("CityTemps.csv")
for row in data:
    print(row.split(","))

"""    
table = pd.read_csv("CityTemps.csv")
print(table)
print("Fetching only years")
print(table["Year"])

print("----iloc----")
print(table.iloc[1:5])
"""