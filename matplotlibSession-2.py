import numpy as np
import matplotlib.pyplot as plt

X = np.random.randn(50)
plt.hist(X)



# X = np.arange(1,21)
# Y = np.sin(X) # numpy is used to calculate the sin of a value and then using matplotlib to plot it
#
# plt.plot(X,Y)
# plt.show()

# A = [1,2,3,4,5]
# B = [10,20,30,40,50]
# plt.bar(A,B)

scores = {"sachin":200,"rohit":264,"Yuvraj":139,"dhoni":183,"virat":183}
plt.bar(0,scores["sachin"])
plt.bar(1,scores["rohit"])
plt.bar(2,scores["Yuvraj"])
plt.bar(3,scores["dhoni"])
plt.bar(4,scores["virat"])

plt.xlabel("Batsman")
plt.ylabel("scores")

for i, key in enumerate(scores):
    plt.bar(key,scores[key])

plt.show()


