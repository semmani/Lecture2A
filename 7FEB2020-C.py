..import math
class Point:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    def show(self):
        print("X is {}| Y is {}".format(self.x,self.y))


def calculateDistance(self,point1,point2):
    distance = math.sqrt((point2.y - point1.y)**2 + (point2.x - point1.x)**2)
    return distance

pref1 = Point(4,5)
pref2 = Point(6,10)

#@staticmethod-- no self,no class and @classmethod-- no self are the decortors in python