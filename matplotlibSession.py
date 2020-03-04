import matplotlib as plt

print(plt.__version__)

import matplotlib.pyplot as plt
# we use pyplot module of matplotlib in order to perfrom various mathematical functions
# Y = [1,2,3,4]
# plt.plot(Y)
# plt.show()

X = list(range(1,11))  # x-axis data
Y1 = [n for n in X ]
Y2 = [n*n for n in X ]
Y3 = [n*n*n for n in X ]

plt.plot(X,Y1,label="Y1")  # PLOTTING THE PPOINTS ALONG WITH THE LABELS, IN ORDER TO SHOW THE LABELS WE USE LEGEND() FUCNTIONS
plt.plot(X,Y2,label="Y1")
plt.plot(X,Y3,label="Y1")
plt.legend()

plt.xlabel("X-AXIS") # to label x axis and y axis
plt.ylabel("Y-AXIS")


plt.title("polynomial Graphs") # to provide the title to the graph
plt.grid(True)



plt.show()






