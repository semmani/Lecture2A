# quiz on OOPS!!!

class Counter:
    sCount = 1

    def __init__(self):
        self.count = 1 # property of class done today added to yesterdays concept--combination

    def increment(self):
        self.count += 1
        #Counter.sCount += 1
        self.sCount += 1 # self.scount = self.sCount +1
    def decrement(self):
        self.count -= 1
        #Counter.sCount -= 1
        self.sCount -= 1
    def showCount(self):
        print(">> Count is: {}".format(self.count),"and sCount is:{}".format(Counter.sCount)) # sCount is called by class Counter adn it will be increment whether calle dby c1, c2,c3 and
        #hence decrement accorsingly---> therefore valueu is 6 for c1,c2,c3


c1 = Counter()  # c1/c3 count = 1
c2 = Counter()  # c2    count = 1
c3 = c1

c1.increment()  # c1/c3 count = 2
c1.increment()  # c1/c3 count = 3
c2.increment()  # c2    count = 2
c3.increment()  # c1/c3 count = 4

c1.decrement()  # c1/c3 count = 3
c3.increment()  # c1/c3 count = 4       -> 4
c2.increment()  # c2    count = 3       -> 3

# How many Object : 2 OK
c1.showCount()  # >> Count is: 4
c2.showCount()  # >> Count is: 3
c3.showCount()  # >> Count is: 4

print(hex(id(c1)), c1.__dict__)
print(hex(id(c2)), c2.__dict__)
print(hex(id(c3)), c3.__dict__)

