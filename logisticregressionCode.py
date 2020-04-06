import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
import tensorflow as tf


dataSet = pd.read_csv("purchases.csv")
print(dataSet)

# sns.countplot("Gender", hue="Purchased", data = "dataSet")
sns.countplot("Age", hue="Purchased", data = "dataSet")
plt.show()

X = dataSet.drop("Gender", axis = )
Y = dataSet["Gender"]

print(X)
print(Y)

x_train, x_test, y_train, y_test = train_test_split(X,Y,test_size=0.2, random_state= 1)
model = LogisticRegression()
model.fit(x_train, y_train)

# Make Predictions
predictions = model.predict(x_test)
print(y_test)       # Expected Output for x_test
print(predictions)  # Predicted Output for x_test

print(">> ACCURACY SCORE:", accuracy_score(y_test, predictions))
# classification report
classificationReport = classification_report(y_test, predictions)
print(classificationReport)

"""


dataSet = pd.read_csv("purchases.csv")
print(dataSet)

# sns.countplot("Age", hue="Purchased", data=dataSet)
sns.countplot("Gender", hue="Purchased", data=dataSet)
plt.show()

X = dataSet.drop("Gender", axis=1)
Y = dataSet["Gender"]

print(X)
print(Y)
# 100 rows
# 80 for training and 20 for Testing

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=1)

# Creating the Model
model = LogisticRegression()

# Train the Model
model.fit(x_train, y_train)

# Make Predictions
predictions = model.predict(x_test)
print(y_test)       # Expected Output for x_test
print(predictions)  # Predicted Output for x_test

print(">> ACCURACY SCORE:", accuracy_score(y_test, predictions))

# Classification Report :)
"""
    Classification Report displays precision, recall, f1-score, support
    precision: level upto which predictions made by model are precise
    recall: amount upto which model can predict the output
    f1score and support : amount of data tested for the predictions

"""
classificationReport = classification_report(y_test, predictions)
print(classificationReport)

# Confusion Matrix
"""
    Its a Table which describes performance of a prediction model
    It contains Actual Values and Predicted Values.
    We can use the data in this matrix to compute accuracy score
"""
matrix = confusion_matrix(y_test, predictions)
print(matrix)


# Assignment: In the current data set, change Gender to numerical data
# Work on Purchased Column as Output to be predicted
# Explore what is a HEAT MAP
# Draw the same using SeaBorn, and find what it represents

# reference example :)
dfConfMatrix = pd.DataFrame(matrix)
print(dfConfMatrix)
sns.heatmap(dfConfMatrix)
plt.show()

"""