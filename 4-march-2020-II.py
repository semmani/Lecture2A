import pandas as pd
import numpy as np

oddNumbers = np.arange(1,100,2)
evenNumber = np.arange(0,100,2)
# printing in the form of columns we write oddnumbers and evennumbers in the Dictionary format
numbers = {"oddNumber: ": oddNumbers," evenNumbers: ":evenNumber}
table = pd.DataFrame(numbers)
print(table)


data = np.random.randn(5,4)
print(data)
# writing data into the columns---->
table = pd.DataFrame(data, columns=["COL1","COL2","COL3","COL4"])
print(table)

print("================================")
# TO ACCESS ONLY COLUMN 3--->
print(table["COL3"])

# TO ACCESS THE DATA OF COL 3--->
print(table.COL3)

# iterating in Dataframe----> going to iterate column-wise

for key, value in table.iteritems():
    print(key)
    print("=========")
    print(value)
    print("---end---")

print("iterating in the rows--->")
for key, value in table.iterrows():
    print(key)
    print("=========")
    print(value)
    print("---end---")

print("iterating tuples-wise")

for row in table.itertuples():
    print(row)
    print("=========")
print("---end---")

