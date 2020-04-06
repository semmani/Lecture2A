import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics



diabetesDataSet = pd.read_csv("PimaDiabeticData.csv")
print(diabetesDataSet)

columns = ['pregnant', 'plasma', 'bp', 'skinfold', 'insulin', 'bodymass', 'pedigree', 'age,']

X = diabetesDataSet[columns]
Y = diabetesDataSet.label

