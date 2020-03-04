# tutorial on Json--->
#import tkinter--> used in machine learning and AI, NOT USED IN MARKET OTHERWISE
from tkinter import *
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

class Customer:

    def __init__(self, name=None, phone=None, email=None, property=None):
        self.name = name
        self.phone = phone
        self.email = email

    def showDetails(self):
        print("{},{},{}".format(self.name,self.phone,self.email))

#creating a window-  a aframe containing min, max button along with close button
def clickHandler():# TO APPLY FUNCTION TO PERFORM

    customer = Customer()
    customer.name = entryname.get()
    customer.phone = entryphone.get()
    customer.email = entryemail.get()

    customer.showDetails()
    customer_data = customer.__dict__

    db = firestore.client()  # making connection to the firestore on firebase
    db.collection("New_Customers").document(customer.email).set(customer_data)  # making collection and then document and then setting it to data
    print("Customer saved")


window = Tk() # tkinter is a module used to make graphical user interfaces and Tk class in tkinter----> needs exploration


label = Label(window, text="Customer managment solution")
label.pack() # ADDS THE LABEL INSIDE THE WINDOW
lblname = Label(window,text="Enter Customer Name")
lblname.pack()
entryname=Entry(window)
entryname.pack()


lblphone = Label(window,text="Enter Customer Phone")
lblphone.pack()
entryphone=Entry(window)
entryphone.pack()


lblemail = Label(window,text="Enter Customer Email")
lblemail.pack()
entryemail=Entry(window)
entryemail.pack()

btnAddCustomer = Button(window,text="Add Customer", command=clickHandler)
btnAddCustomer.pack()


window.mainloop()  #INFINITE LOOP LIKE TO LET THE WINDOW APPEAR INFINITLY


# to explore tkinter in python documentation,
# prob1.py make it in GUI using tkinter and add data into cloud firestore,