# OBJECT IS AN BUILT IN CLASS IN PYTHON, BY DEFAULT EVERY CLASS IS A CHILD OF OBJECT CLASS
# class Point(object)
#_---> single underscore makes any variable protected-----> means cant be accesed
#__y-----> double undercores makes variable PRIVATE----> becomes _POINT__Y---> CANT BE ACCESSED CALLED AS NAME MANGLING
class Point:
    def __init__(self,x,y):
        self._x = x
        self.__y = y
    def __showPoint(self):
        print("{},{]".format(self._x,self.__y))

    def __str__(self):    # Overriding the __str__ funct in object PARENT CLASS
        return "{},{}".format(self._x,self.__y)

p1 = Point(10,20)
p2 = Point(30,55)

#print(p1)
print(p2)
print("-------------------------------")
print(p1.__str__()) # executed automatically whenever  we are printing reference
print(p2.__str__())
print(p1.__dict__)

print(p1._Point__y) # prints 20 now
p1._Point.__showPoint()