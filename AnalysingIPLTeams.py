from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import pandas as pd
import numpy as np

table = pd.read_csv("IPL-TEAMS-2019.csv")
print(table)

year = table.Year.values
wonMatches = table.Won.values

# X and Y are 1-D Arrays | 200, 0
# print(X, X.shape)
# print(Y, Y.shape)

# (scikit library) sklearn shall work on 2d arrays
X = np.array(year).reshape(-1,1)
Y = np.array(wonMatches)

# converted X and Y as 200, 1
#print(X, X.shape)
#print(Y, Y.shape)

model = LinearRegression()
model.fit(X, Y)

b0 = model.intercept_
b1 = model.coef_

print("Interceptor is:", b0)
print("Coefficient is:", b1)

Y1 = model.predict(2020)
print(Y1, Y1.shape)

print(">> Equation of Line: Y = {} + {}X".format(b0, b1))



