import numpy as np

# array = np.loadtxt("data.txt", dtype=int)
# print(array)  # array written in the file should be of even length and format

arr1D = np.arange(10,200,10)
print(arr1D)
np.savetxt("arraydata.txt",arr1D,fmt="%04d")  # to save the data into the file in the exponent and mantissa format in the int part
print("data is saved")


array = np.genfromtxt("CityTemps.csv",delimiter=",")
print(array)


"""
#DATA ANALYSIS----->kaggle.com for various open source datasets and we can apply these given instructions onto it
#ASSIGNMENTS--->
1.HOW MANY YEARS?
2.find the city with max and min temp
3. find the city with max and min temp with month and year
4.Sort the months as per temperature ,city wise--form three lists
5.
"""
