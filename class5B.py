"""
    OOPS- OBJECT ORIENTED PROGRAMMING STRUCTURE
    HOW WE DESIGN SOFTWARE
    ITS A METHODOLOGY

    1. OBJECT
    2.CLASS
     Principle of OOPS:
     1.THINK OF OBJECT-
     NEED TO ANALYSE DETAILED REQUIREMENTS FROM CLIENT REGARDING S/W NEEDS, IDENTIFY ALL TERMS HAVING LOTTA DATA ASSOCIATED WITH IT
     THAT TERM--OBJECT AND ASSOCIATED DATA IS--ATTRIBUTES

     JOHN:

     2.CREATE ITS CLASS
     3. CREATE REAL OBJECT FROM THE CLASS
   UNDER COMPUTER SCIENCE--->
    OBJECT:-DATA IN OBJECT IS STORED IN THE FORM O F DICTIONARY WHRE KEYS ARE KNOWN AS ATTRIBUTES --
    WHICH WILL HOLD VALUES AS DATA
    CLASS:- HOW AN OBJECT LOOKS LIKE,WHAT IT SHUD CONTAIN AS DATA,
    PERFORMS CERTAIN FUNCTIONALITY TO PROCESS DATA AS WELL AS OBJECT
    -----SAME PRINCIPLE OF OOPS---

    PROJECT USING OOPS:
     MOVIES APP
     1.country
     2.




"""


#2. making a class

class Customer:
    pass # not doing or implementing anything


#3. to create an object referring to the class
cRef = Customer()

print(">>cRef is:",cRef)
print(">>cRef hashcode",hex(id(cRef)),"and type is :",type(cRef))
# to know what is in oject--denoted as Dictionary
print(">>cRef Dictionary",cRef.__dict__) # denotes empty dictionary

cRef.name = "John Watson"
cRef.phone = "89898989"
cRef.email = "john3232@gmail.com"
print(">>cRef Dictionary",cRef.__dict__)# now prints the output in the form of dictionary

# updating
cRef.phone = "5656565"
print(">>cRef Dictionary Updated",cRef.__dict__) # easily updated

del cRef.email
print(">>cRef Dictionary",cRef.__dict__)
del cRef
print(">>cRef Dictionary",cRef.__dict__) # whole cref is deleted