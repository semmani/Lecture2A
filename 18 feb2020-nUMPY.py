import numpy as np

numbers = [10,20,30,40]

print(numbers,type(numbers))


print()

#numpy array is optimized as compared to the List
#array = np.array(numbers) # ndarray---> n dimension array
array = np.array([10,20,30,40])
print(array,type(array))

#string,tuple,set and dictionary

array1 = np.array((10,20,300))
print(array1,type(array1))


array2 = np.array("HELLO World")
print(array2,type(array2))

array3 = np.array([{"100": 100, "200": 200}])
#print(array3,type(array3))

for n in array3: # needs a lookout
    print(n)


