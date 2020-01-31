
class Customer:
    #def __init__(self):  # constructor---a kind of temporary memory holder, called as function which when runs, a frame is made in the memory
        # name of sef can be any name of your choice, but its always first input to init
    # if we create _init_ again then it will be a new init and the previous one will be deleted, hence not followed---> No Need
     def __init__(self,name,phone,email,gender,address):
        print("init executed")
        print(">>self is ", self)
        self.name = "Fionna Davis"
        self.phone = phone
        self.email = email
        self.gender = gender
        self.address = address
# above format defines the standard of the class which if not followed then produces error


    def showCustomer(self):
    print("{} has phone number {}, email as {} whose gender is {} lives in {}".format(self.name, self.phone, self.email,
                                                                                      self.gender, self.address))


cRef1 = Customer("Jenna Davis", "91 852963145", "jenna@gmail.com", "Female", "london city")
# cRef1 = Customer()
# print("cRef:",cRef1.__dict__)# gives error as we dont provide arguments to customer that goes into name,gender,phone etc
cRef1.showCustomer()  # check from github ishantk repo
print(cRef1.__dict__)  # now runs successfully


def myData(self,custtype,wallet):
        self.custType = custtype
        self.wallet = wallet

"""
cRef1 = Customer() # object construction statement
print(">>cRef1 is:", cRef1, hex(id(cRef1)))
cRef1.phone = "91 2225 68595" # cRef1 is print phone along with name by self

print(">>cRef1 is:",cRef1.__dict__)

#self and cRef1 both are reference variable holds hashcode of current object Customer
cRef2 = Customer()# ---> contains
cRef2.email = "fionna234@gmail.com"
print(">>cRef2 is:",cRef2.__dict__) # it adds email with name but not phoneno

cRef3 = cRef1 # reference copy operation---copies hashcode
cRef3.name = "Jenna Davis" # prints name jenna davis and phone number declared by cRef1
print(cRef3.__dict__) # prints nothing as its refernce to cRef1 as it contains only hashcode of cRef1

"""
# to display function to show customized values

def updateCustomerDetails(self,name,phone,email,gender,address): # in order to define the updation in customer details
    #we use this fucntion accessing self within
    self.name = name
    self.phone = phone
    self.email = email
    self.gender = gender
    self.address = address





cRef2 = Customer("Fionna","91525252","fionna@gmail.com","female","London City") # same hashcode of self, hence should take same inputs
print(cRef2.__dict__)

#cref2 has same hashcode of self



