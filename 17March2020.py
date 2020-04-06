# Session 41 -> Decision classifier with sklearn
from sklearn.datasets import load_iris
from sklearn import tree
import graphviz

irisdata = load_iris()
print("=====Iris Dataset=====")
print(irisdata)
print("type of irisdata is:", type(irisdata))

print()

print("====iris data feature=====")
print(irisdata.data)  # to only print the data

print("====To print IRIS targets====")
print(irisdata.target_names)

# Create the Model
model = tree.DecisionTreeClassifier()
# 2.training a model
model.fit(irisdata.data,irisdata.target)

# 3.lets test a model with a sample input
inputData1 = [5.5,2.3,4.0,1.3]  # this data is associated to versicolor --> 1
predictedTarget = model.predict([inputData1])
print(predictedTarget)  # 1
inputData2 = [5.43,3.90,1.15,0.32]

data = tree.export_graphviz(model,out_file=None)
graph = graphviz.Source(data)
graph.render("IRIS DATA SET DECISION TREE")
graph.view()




