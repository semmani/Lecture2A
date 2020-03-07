import pandas as pd
import seaborn as sns   #--> plotting module
import matplotlib.pyplot as plt

table = pd.read_csv("soccerdata.csv")
print(table.head(10))

#sns.countplot(y=table.Nationality,palette="Set2")  #palette isi color palette
#sns.countplot(x="Age",data=table)

sns.countplot(x="Name", data=table.head(10)) # plotting x axis and then fetching data from data
# plt.show()


# Do the data analysis to find the Goalkeeper who is best to stop the kicks
# lets us create some weights

w1 = 1
w2 = 2
w3 = 3
w4 = 4

table["BEST_GK"]= w1*table.GK_Kicking + w2*table.GK_Diving + w3*table.GK_Positioning + w4*table.GK_Reflexes
#print(table["BEST_GK"])

sortedData = table.sort_values("BEST_GK")
print(sortedData)  # best goalkeeper is Manuel Neuer
print("tail---->")

print(sortedData.tail(5))


# explored dialoglow....explore it a lot at home....using intents and responses and google assistant thing.