class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def showPoint(self):
        print("{},{}".format(self.x, self.y))


    def add(self,point):
        temp = Point()
        temp.x = self.x + point.x
        temp.y = self.y + point.y
        return temp

p1 = Point(10,20)
print(p1.__str__())

p2 = Point(33,55)
p3 = p1.add(p2)
p3.showPoint()