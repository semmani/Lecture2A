import numpy as np

array = np.arange(10,51,2)

# for fetching based on indexes -->
slices = slice(1,20,2)
indexes = array[list(range(1,20,2))]   #to print the indexes, if used as subscript to array[] then prints the numbers
print(indexes)
print(array[1::2])
print(array)
print(slices)

print(array[slices]) #to see how slice works use it as subscript of array

