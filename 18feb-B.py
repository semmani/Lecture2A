import numpy as np
import time

#timeStamp = time.time()
#print(timeStamp) # prints the time in milliseconds
"""
to check the difference between array and list
array1 = np.array([10,20,30,40,50])
array1 = np.array(list(range(1,1001,1)))
timeStamp1 = time.time()
for num in array1:
    print(num)
timeStamp2 = time.time()
print("for arrays",timeStamp2-timeStamp1) #0.0119999

numbers = list(range(1,1001))
timeStamp3 = time.time()
for num in numbers:
    print(num)
timeStamp4 = time.time()
print("for numbers:",timeStamp4-timeStamp3) # 0.127

"""
array = np.array([10,20])
array1 = np.array([[10,20,30],[30,40,50]])
array2 = np.array([[10,20],[30,70,66,44],[31,33,50]])
print(array2)
print(array2.shape) # 2,3 means 2 rows and 3 columns
print(len(array)) # in case of single dimensional array we have 2 elements so the length becomes 2 only
print(len(array1))
print(len(array2))


