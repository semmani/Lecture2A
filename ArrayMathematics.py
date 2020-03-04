import numpy as np

data = [
    (8,9),
    (10,11),
    (55,23)

]

arr1 = np.array(data)
print(arr1)
print(arr1[0:2,1]) # prints the 0,1 rows and 1-column values
print(arr1.min())
print(arr1.max())

print(arr1.sum())

print(arr1.min(axis=0)) # minimum according to the column wise
print(arr1.max(axis=1)) # maximum row wise

print(arr1.min(axis=1))

print("============")
print(np.std(arr1))  # std deviation is used to check how mean values are deviating from the actual value of mean

print("II PART")
a1 = np.array([(1,2,3),(4,5,6)])
a2 = np.array([(1,2,3),(4,5,6)])
print(a1)
print(a2)
print(a1 + a2)
print(a1 - a2)
print(a1*a2)
print(a1/a2)# FLOATING POINT DIVISION
print(a1//a2) # TRUE DIVISION ----IN INTEGRAL
print("using inbuilt functions under numpy")
a3=np.add(a1,a2)
print(a3)

a4 = np.multiply(a1,a2)
print(a4)


x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])
z = np.dot(x,y)
print(z)