import firebase_admin

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("manmeet_p1key.json")
firebase_admin.initialize_app(cred)
print("Firebase")


class Customer_New:
    def __init__(self):

           self.name = input("ENTER CUSTOMER NAME: ")
           self.phone = input("ENTER CUSTOMER PHONE NUMBER:")
           self.email = input("ENTER CUSTOMER EMAIL:")


    def showCustomerDetails(self):
        print(" NAME:{}, PHONE:{}, EMAIL:{}".format(self.name, self.phone, self.email))

def main():
    customer = Customer_New() # reference to the class
    customer.showCustomerDetails() # shwos details
    customer_data = customer.__dict__ # adds data into customer_data in the format of dictionary
    print(customer_data,type(customer_data))

    db = firestore.client()  #making connection to the firestore on firebase
    db.collection("customers").document(customer.email).set(customer_data) # making collection and then document and then setting it to data
    print("Customer saved")

if __name__ == "__main__"   :
    main()  # here we call the main function