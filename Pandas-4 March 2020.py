import pandas as pd
import numpy as np

array1 = np.arange(1,101,2)
array2 =list(range(1,101,3))

print(array1)
print("-----------------")
print(array2)

s1 = pd.Series(array2)
print(s1)

print(s1.axes) # start, stop, step

values = s1.values
print(values) # acts as numpy arrays
print("-------------")
print(s1.head(5))

print("----------")

print(s1.tail(5))



