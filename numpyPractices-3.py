import numpy as np

a1 = np.arange(10, 51, 3)
print(a1)
print(type(a1))
print(a1.shape) #
print(a1.ndim)
print(a1.size)

print()

a2 = np.array([[1,2,3],[4,5,6],[6,7,8]])
print(a2)
print(type(a2))
print(a2.shape)  # this tells basically that what is the row x column
print(a2.ndim) # given array is
print(a2.size)

print("slicing-------------")
print(a1[::3])
print(a1[5:])
print(a1[5:8])

print(a2[0:2])

print("Indexing------------")
print(a1[1])
print(a1[-1])
print(a2[0][1])
print(a2[0,1])

print("Indexing + Slicing------")

print(a2[0:2, 0:1])  # 0:2 reads 0 and 1 row but 0:1 reads only 0th col...so prints single-single element.-->1,4
print(a2[0:2])