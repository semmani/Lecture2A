import numpy as np

x = np.array ([[1,2,3],[4,5,6],[7,8,9]])
print("x is")
print(x)
print(x.shape)

v = np.array([1,0,1])
print("v is")
print(v)
print(v.shape)

y = np.empty_like(x) # arranges randomly anything in its
print("y is\t",y)
print(y.shape)

for i in range(3):
    y[i, :]=x[i,:]+v   # i,: means starting from 0 go till end---> here we added 1 0 1 into every row of x array



print("y now is-->")
print(y)


