import math

def eucilideanDistance(point1, point2):
    sumOfSquaredDistance = 0

    for i in range(len(point1)):
        sumOfSquaredDistance += math.pow(point1[i] - point2[i],2) # sqaure of (point1 - point2)

        return math.sqrt(sumOfSquaredDistance)  # sqrt(sumOfsquareddistance)




def main():

# dataset has feature of weight and height
    dataSet = [
                [65, 120.22],
                [71.5, 35.77],
                [69.8, 153.27],
                [67.2, 148.55],
                [68.5, 133.21],
                [69.11, 148.5],
                [70.55, 160.0],
                [67.33, 1128.9],
                [66.49, 127.11]
    ]

   # we need to predict the value of weight given the valueof height
    givenWgt = [60]
    k = 3                   # with k nearest neighbours, we solve this with regression problem

    for idx, dataPoint in enumerate(dataSet):
      print(idx,dataPoint)


if __name__ == '__main__':
    main()
#-----> next seesion to this is sklearn classification