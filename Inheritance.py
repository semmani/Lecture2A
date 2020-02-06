"""
Inheritance--where do we use it,,why we use it and what is it
Lookup Rule: if we donthave an attribute in ts object then look up in its class,
if it doesnt have it in its own class, then it looks up in its parent class


"""


class Parent:
    vehicle = "PB10AD0041"

    def __init__(self,fname,lname,wealth):
        self.fname = fname
        self.lname = lname
        self.wealth = wealth

    def show(self):
        print("{}\n{}\n{}\n{}".format(self.fname,self.lname,self.wealth,self.vehicle)) # it will provide error as arguments dont match with funct def given in parent class


class Child(Parent): # reference to this will not work unless we give 3 arguments
     vehicle = "PB10AB4100"

     def __init__(self,name,salary): # parent init wont be accessible,child refernce willa ccess child init---->CUSTOMIZING
         self.name = name
         self.salary = salary


     def show(self,name,salary):
         print("{}\n{}\n{}".format(self.name,self.salary,Child.vehicle))

     def show(self, ref):
         print("{}\n{}\n{}".format(self.name, self.salary, Child.vehicle))
         Parent.show(ref)


# empty class i.e providing no init...also works

#pRef = Parent("manmeet","kaur",100000)
cRef = Child("john watson",200000) # without giving init and arguments it will access parent class but wont work unless fields are unfilled
#print(pRef.__dict__)
#print(">>parent dictionary")
#print(Parent.__dict__)
#print(">>child dictionary",Child.__dict__)
# providing two inputs to Child above will work according to the init of Child class
print(">>child dictionary",cRef.__dict__) # working when above code is commented,prints Child class data inherited from
# Parent class-----> Reusability of Code

#print(Child.vehicle) # Child class dont have vehicle but its Parent class have it so it accesses
#print(cRef.vehicle) # cref is reference to Child class accesses the Parent class, it has vehicle so is printed by cRef

#Classes cnt access data of object bcoz class dont know which ovjects property it is accessing.

#Child.show(cRef)# explicit call



