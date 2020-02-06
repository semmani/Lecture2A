"""

class Customer:
    def __init__(self,name,phone,email):
        self.name = name
        self.phone = phone
        self.email = email

    def showPrimeCustomer(self):
        print("{}\t{}\t{}\t".format(self.name,self.phone,self.email))


cref1 = Customer("Kieraa nightly",+315264856,"kiera@eg.com")
ref2 = Customer("Johny depp",+3155554856,"johny@eg.com")

ref2.type = "ACTOR"
print(cref1.__dict__)
print(ref2.__dict__) # adding type attribute externally , not necessarily to define it within __init__

"""
#Extendibilty--->
class Customer:
    def __init__(self,name,phone,email):
        self.name = name
        self.phone = phone
        self.email = email

    def showCustomer(self):
        print("{}\t{}\t{}\t".format(self.name,self.phone,self.email))


class PrimeCustomer(Customer):  # inheritance
    def upgradeCust(self): # a function with attributes
        self.type = 1
        self.videos = True
        self.music = True

    def showPrimeCustomer(self):
        self.showCustomer()
        print("Prime Features are: Videos {} | Music {}".format(self.videos,self.music))

cref1 = Customer("Johny Depp",3152226989,"johny@gmail.com")
#Customer.showCustomer(cref1)

PrimeCustomer.upgradeCust(cref1) # we extend the feature of Customer to PrimeCustomer
PrimeCustomer.showPrimeCustomer(cref1)


# this is how we can add new attributes in a already defined class, we call this approach a DECORATOR I.E Design Pattern
"""
class PrimeCustomer(Customer):  # inheritance
    def __init__(self,Customer): # a function with attributes
        Customer.type = 1
        Customer.videos = True
        Customer.music = True

    def showPrimeCustomer(self,Customer):
        Customer.showCustomer()
        print("Prime Features are: Videos {} | Music {}".format(self.videos,self.music))

cref1 = Customer("Johny Depp",3152226989,"johny@gmail.com")
primeRef = PrimeCustomer(cref1)
print(cref1.__dict__)
print(primeRef.__dict__)

#Customer.showCustomer(cref1)
#primeRef.showPrimeCustomer(cref1)
"""

#PrimeCustomer.upgradeCust(cref1) # we extend the feature of Customer to PrimeCustomer
#print(cref1.__dict__)


# Making an Burger upgraded meal














