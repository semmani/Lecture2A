# SUPERVISED MACHINE LEARNING-->
# LINEAR REGRESSION -> PREDICTIVE MODELING TECHNIQUE
"""
Initial Data
    X = [1, 2, 3, 4, 5]
    Y = [2, 4, 5, 4, 5]
    Regression Line | Linear
    Y = b0 + b1X
    Primary Objective : To find the Slope of Line with given data points:)
    i.e. b1 -> since b1 is slope of line
    Mean of X [MX] = 3
    Mean of Y [MY] = 4
    Step1:
    ------------------------------------------------
    X   Y   X-MX    Y-MY    sq(X-MX)    (X-MX)(Y-MY)
    ------------------------------------------------
    1   2   -2      -2      4           4
    2   4   -1       0      1           0
    3   5    0       1      0           0
    4   4    1       0      1           0
    5   5    2       1      4           2
    ------------------------------------------------
    Step2:
    ------------------------------------------------
    Sum of sq(X-MX) =       10
    Sum of (X-MX)(Y-MY) =   6
    To find slope of line:
    b1 = [Sum of (X-MX)(Y-MY)] /  [Sum of sq(X-MX)]
    b1 = 6/10
    b1 = 0.6
    Step3:
    ------------------------------------------------
    Equation of Line is:
    Y = b0 + 0.6 X
    For b0:
    Put mean values of X and Y in equation :)
    4 = b0 + 3 * 0.6
    b0 = 2.2
    =======================
    Final Equation of Line:
    Y = 2.2 + 0.6 X
    =======================
    Now, in case we put a value for X as 6, we will come to know the value of Y
    i.e. Prediction shall work
    But is this prediction accurate or erroneous, i.e. not known to us !!
    Step4:
    ------------------------------------------------
    Calculate Errors
    We need to check if errors are more or less
    if errors are less we are good to go with our model, else we need to work on data or changing the model
    1. Mean Squared Error | MSE *
    2. R2
    3. Variance
    Y = 2.2 + 0.6 X
    For original values of X = [1, 2, 3, 4, 5]
    We will get predicted values of Y call them as Y'
    ------------------------------------------------
    X   Y   Y'   Y-MY    sq(Y-MY)    Y'-MY  Sq(Y'-MY)
    ------------------------------------------------
    1   2   2.8  -2      4          -1.2     1.44
    2   4   3.4   0      0          -0.6     0.36
    3   5   4     1      1           0       0
    4   4   4.6   0      0           0.6     0.36
    5   5   5.2   1      1           1.2     1.44
    ------------------------------------------------
    MSE: [Sum of  Sq(Y'-MY)] /  [Sum of sq(Y-MY)]
    MSE: 3.6/6
    MSE: 0.6
    MSE: 0 ~ 1
"""

