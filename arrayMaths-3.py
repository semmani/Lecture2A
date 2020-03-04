import numpy as np

x = np.array([(1,2,3),(4,5,6)])
y = np.array([(1,2,3),(4,5,6)])

print(np.vstack((x,y))) # prints row vertically and then----> Vertical Stack joins both arrays in one
print(np.hstack((x,y))) # prints row horizontally---> stacking horizontal addition

z = np.arange(1,101,10)
print(np.sin(z))
print(np.tan(z))
print("log 10")
print(np.log10(z)) # works with 1 to infinite range but not with 0 as log 0 is undefined...works with exponent tho

#http://numpy.org/devdocs/user/quickstart.html-----------> this website for further tutorial on Numpy array Mathematics