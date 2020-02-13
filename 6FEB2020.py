
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

def executeSqlQuery(sql):
    con = lib.connect(user= "root",password="",database = "manmeetdb", host="127.0.0.1", port="3306")
    print("CONNECTION CREATED")
    cursor = con.cursor()
    cursor.execute(sql)
    con.commit()


repeat = "yes"
while repeat == "yes":

    print("=====~Welcome to Customer Management System~=====")
    print("1. Register new customer")
    print("2. Update Existing customer")
    print("3. Delete Existing customer")
    print("4. View all Customer")
    print("5. View all Customer by ID")
    print("6. View Customer BY Phone")

    choice = int(input("Enter your Choice: "))
    if choice == 1:  #if choice is 1 then it directs to the mode == 1 i.e asks to insert the customer data
        customer = Customer(1)
        customer.showCustomerDetails()

        save = input("Would you like to Save the Customer?(yes/no): ")
        if save == "yes":
           sql = "insert into Customer values(null,'{}','{}','{}')".format(customer.name, customer.phone, customer.email)
           executeSqlQuery(sql)
           print("CUSTOMER SAVED->")

    elif choice == 2:
            customer = Customer(2)
            customer.showCustomerDetails()

            save = input("Would you like to Update the Customer Details?(yes/no): ")
            if save == "yes":
                sql = "update Customer set name = '{}',phone = '{}',email='{}'".format(customer.name, customer.phone, customer.email)
                executeSqlQuery(sql)
                print("---------CUSTOMER UPDATED->")

    elif choice == 3:  # to delete the customer of provided id
            idd = int(input("Enter the id to delete: "))
            delete = input("Would you like to delete the Customer?(yes/no): ")
            if delete == "yes":
                sql = "delete from Customer where id = {}".format(idd)  #alterntve way of writing-(id)
                con = lib.connect(user="root", password="", database="manmeetdb", host="127.0.0.1", port="3306")
                cursor = con.cursor()
                rows = cursor.fetchall()
                for row in rows:
                    customer = Customer(3)
                    customer.id = row[0]
                    if customer.id == idd:
                        cursor.execute(sql)
                    else:
                      print("Reccord for {} Dont Exist".format(idd))


    elif choice == 4:
            sql = "select * from Customer"
            con = lib.connect(user="root", password="", database="manmeetdb", host="127.0.0.1", port="3306")
            cursor = con.cursor()
            cursor.execute(sql)
            # todisplay all the data we save the data from the file into the variable and then display column wise
            rows = cursor.fetchall()  # this fetches all data in the format of rows
            for row in rows:
               customer = Customer(3)
               customer.id = row[0]   # as data is stored in the form of rows separated with commas
               customer.name = row[1]
               customer.phone = row[2]
               customer.email = row[3]
               print(row)  #prints all the rows

               #customer.showCustomerDetails()


    elif choice == 5:  #to search with given id
            id = int(input("Enter the id to be searched: "))
            sql = "select * from Customer where id = {}".format(id)
            con = lib.connect(user="root", password="", database="manmeetdb", host="127.0.0.1", port="3306")
            cursor = con.cursor()
            cursor.execute(sql)
            # todisplay all the data we save the data from the file into the variable and then display column wise
            row = cursor.fetchone()  # this fetches a row in the format of row
            if row is not None:
                print(row)  # prints the row if data exists
            else:
                print("Record for id {} dont Exist".format(id))



    elif choice == 6:   #record to be searched using phone number
            phone = input("Enter phone no of Customer to be searched: ")
            sql = " select * from Customer where phone= '{}'".format(phone)
            con = lib.connect(user="root", password="", database="manmeetdb", host="127.0.0.1", port="3306")
            cursor = con.cursor()
            cursor.execute(sql)
            row = cursor.fetchone()
            if row is not None:
                print(row)
            else:
                print("Cusomter with phone number {} Not found".format(phone))

    else:
            print("Enter a Valid Choice>>")


repeat = print("Would You like to Re-use this App(yes/no)?: ")

