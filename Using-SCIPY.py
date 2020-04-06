from scipy import stats
from matplotlib import pyplot as plt
import numpy as np

X =[1,2,3,4,5]
Y = [2,4,5,4,5]
data = stats.linregress(X,Y)  # linear regression in one line-->  done where we are writing 50 lines of code in earliar progg

print(data[0])
print(data[1])

maxX = np.max(X) + 10
minY = np.min(Y)-10
print("maximum value is :", maxX)
print("minimum value is :",minY)

x = np.linspace(minY,maxX,100) # here the x and y are divided into 100 points using numpy linspace funct()
y = data[1] + data[0]* x

print(x)
print("------------------")
print(y)

plt.plot(x,y,color = "red")
plt.scatter(X,Y)
plt.xlabel("")
plt.show()