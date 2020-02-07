
import mysql.connector as lib

class Customer:
    def __init__(self,mode):
        if mode == 1:
           self.pid = 0
           self.name = input("ENTER CUSTOMER NAME: ")
           self.phone = input("ENTER CUSTOMER PHONE NUMBER:")
           self.email = input("ENTER CUSTOMER EMAIL:")

        elif mode == 2:
            self.pid = int(input("ENTER CUSTOMER ID: ")) #id is changed into the integer value and then saved in pid
            self.name = input("ENTER CUSTOMER NAME: ")
            self.phone = input("ENTER CUSTOMER PHONE NUMBER:")
            self.email = input("ENTER CUSTOMER EMAIL:")

        else:
            pass

    def showCustomerDetails(self):
        print("ID:{}, NAME:{}, PHONE:{}, EMAIL:{}".format(self.pid,self.name,self.phone,self.email))


