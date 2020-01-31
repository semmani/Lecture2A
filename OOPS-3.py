class Customer:
    pass

cRef1 = Customer()# object 1--object construction statement
cRef2= Customer()  # object 2
cRef3 = cRef1 # copy referencing  object 2--reference copy operation
print(cRef1,hex(id(cRef1)))
print(cRef2,hex(id(cRef2)))
print(cRef3,hex(id(cRef3)))


# operations on object

cRef1.name = "John" # cref1 points to the information
cRef3.phone ="+91 565656565" # cref3 is copy reference to cref1 hence whtevr the cref1 can access, cref3 can too,so cref3 can access phone defined by cref1
cRef1.email = "john123@gmail.com"
cRef1.gender = "male"
cRef3.address = " London City"

# describing data for reference variable 2 i.e cRef2
cRef2.name = "Fionna"
cRef2.phone ="+91 56542476565"
cRef2.email = "fionna123@gmail.com"
cRef2.gender = "female"
cRef2.address = " New York City"
cRef2.vehicle = "KA10235" # DYNAMIC FEATURE OF PYTHON TO ADD DIFFERENT ATTRIBUTES IN DIFFERENT OBJECTS DURING OBJECT IS MADE
cRef2.company = "ABCInternational" # extra attribute can be added as it is not standardised

#2. to read data in object

print(">>cRef1 details")
print(cRef1.__dict__) # prints the data in a dictionary format bcoz data is stored in a dictionary format
# customizable format
print("{} CAN BE CALLED ON {} AND HE/SHE LIVES IN {} and email is-".format(cRef3.name,cRef1.phone,cRef3.address))



# 3. update data in objects

cRef1.name = "John Abigail" # i can simply add another name referred by any reference variable to the same class as we r not implementing standardisation
print("{} CAN BE CALLED ON {} AND HE/SHE LIVES IN {} and email is-".format(cRef1.name,cRef1.phone,cRef3.address))
#4. deleting data

del cRef1.phone

print(">> cRef1 is:",cRef1.__dict__) # phone is deleted

del cRef1
print(">> cref1 is:",cRef1.__dict__) # cref1 is deleted hence it shows error

print(">>cref3",cRef3.__dict__) # cref1 is deleted but cref3 is poiting to the heap, hence cRef3 wil run



# challenges:
 #for n no of objects then we need to write data for each object
 # for reading data , we will be rewriting data and so the display need to be chnged as well
 # objects data is not standardised---eg. we can add any type of attribute in Cutomer

