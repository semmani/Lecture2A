

"""
Linear Regression--> Predictive Modeling Technique

Initial Data-->
X =[1,2,3,4,5]
Y= [2,4,5,4,5]

Regression Line | linear
Y = b0 + b1X

PRIMARY OBJECTIVE--> to find the slope of line with the given data points
i.e b1 -> since b1 is slope of line-

Mean of X = 3
Mean of Y = 4

STEP1->

X   Y      X-MEANX    Y - MEANY     SQ(X-MEANX)    (X-MEANX)(Y-MEANY)

1   2       -2         -2              4              4
2   4        -1         0              1              0
3   5        0          1              0               0
4   4        1          0               1              0
5   5        2          1               4              2

STEP2->

SUM OF SQ(X-MEANX) = 10
SUM OF (X-MEANX)(Y-MEANY) = 6

TO FIND SLOPE OF LINE
b1 = [ SUM OF (X-MEANX)(Y-MEANY))] / [ SUM OF SQ(X-MEANX)]

b1 = 0.6

STEP3--->
----------------------------------
EQUATION OF LINE IS : Y = b0 + 0.6X

for b0:

put mean value of X and Y in equation:
4 = b0 + 3 * 0.6
b0 = 2.2

======================
final equation:

Y = 2.2 + 0.6 X

=====================================================

Now,. in case we put a value of X as 6 , we will come to know the value of y i.e Prediction shall work
But is this prediction  accurate or erroneous i.e not known to us!!

STEP4-->
Calculate Error-->

1.Mean Squared Error
2. R2
3. Variance

Y = 2.2 + 0.6 X
FOR ORIGINAL VALUES OF X = [1,2,3,4,5]
WE WILL GET THE PREDICTED VALUES OF Y AND CALL THEM Y'
--------------------------------------------------------------------------
X   Y     Y'        Y - MEANY     SQ(Y-MEANY)      Y'-MEANY     SQ(Y'-MY)

1   2     2.8          -2             4              -1.2        1.44
2   4     3.4          0              0              -0.6         0.36
3   5      4           1              1              0              0
4   4    4.6           0              0              0.6          0.36
5   5    5.2           1              1              1.8          3.24
------------------------------------------------------------------------

MeanSquareError(MSE) = [SUM OF SQ(Y'-MY) ] / [SUM OF SQ  SQ(Y-MEANY) ]
MSE = 5.4/6
MSE= 0.9

0 ~ 1
"""
import numpy as np

class LinearRegression:
    def __init__(self,X,Y):
        self.X = X
        self.Y = Y
        self.b0 = 0
        self.b1 = 0

    def fit(self,X,Y):
        self.X = X
        self.Y = Y

        Meanx = np.mean(self.X)
        Meany = np.mean(self.Y)

        self.b1 = np.sum((self.X-np.mean(self.X))*(self.Y-np.mean(self.Y))) / np.sum(np.square(np.mean(self.X)))
        self.b0 = np.mean(self.Y) - self.b1 * np.mean(self.X)                                       # y = b0 + b1 * x
        print(self.b1)


    def predict(self,X):
        Y = self.b0 +self.b1 * X
        return Y



X = [1,2,3,4,5]
Y =[2,4,5,4,5]

model = LinearRegression(X,Y)
model.fit(X,Y)
predictedoutput = model.predict(5)
print("predicted output is: ",predictedoutput)



