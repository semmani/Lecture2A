import numpy as np

a1 = np.array(list(range(10,21))) #one way of printing numbers from 10 - 21
a2 = np.arange(10, 21) #----> second way of perfroming above thing with step--difference
a3 = np.arange(10, 21,3) #second way of perfroming above thing with step--difference of 3
print(a1)
print(a2)
print(a3)

a4 = np.ones((3, 3, 3), dtype=int)
print(a4)

a5 =np.linspace(0,21,4) # divides the numbers from 0 to 21 in 4 parts----> linspace divides the range of numbers in equal parts
print(a5)