"""
class WhatsAppGroup:

    title = "PropertyOfClass" # common attribute to all, attribute to class itself

    def __init__(self): # they are directly or indirectly working with class, but are made in class yet not working in class
     #self.title = "PropertyOfObject"
     self.img = "abc.jpg"

# two storage containers---> Class and Object
group = WhatsAppGroup()
print(">>Group is :",group.title)
"""
#class has its own member variables and functions, and canbe accessed by Class name
# object has its properties, we can access members which are pointed by reference variables, can be accessed by self, refernce variable etc.

class Counter:
    sCount = 1
    def __init__(self):
        self.count = 1
    def increment(self):
        self.count += 1
        #self.sCount += 1 # INCREMENT IS OF SCOUNT WHICH IS A PROPERTY OF CLASS
        Counter.sCount += 1
    def decrement(self):
        self.count -= 1
        #self.sCount -= 1 # this adds scount in the object hence value will be 2
        Counter.sCount -= 1 # this increments the scount of class
    def showCount(self): # WHEN CALLED BY C1 THEN SELF = C1
        print(">> count is:",self.count)# ACCESSING COUNTOF SELF
        print(">>sCount is:",self.sCount) #SELF DO NOT HAVE SCOUNT
        print(">>sCount is :",Counter.sCount) # access the SCOUNT OF CLASS BY CLASSNAME

c1 = Counter()
c2 = Counter()
c3 = c1 # copy reference operation
c1.increment()
c1.decrement()
c1.showCount()


c2.increment()
c2.





