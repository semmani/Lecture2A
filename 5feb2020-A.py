
"""
DATA BASE---> Permanent data store
      prefer data base over files---> security;centralization;operations are much easier and faster--> time optimized
                                                              ----> INSERT/UPDATE/DELETE/QUERY
      DATA IS STRUCTURED DATA STORAGE---> STORE DATA IN THE FORAMT OF
                              TABLES
                                 ROWS & COLUMNS

      DATABASE REPRESENTS THE DATA STRUCTURE

MYSQL AND ORACLE----> FOLLOW TREE DATA STRUCTURE
AND FOLLOWS SQL TECHNIQUE

Neo4J---> USES GRAPH DATA STRUCTURE

FireBaseFirestore---> NOSQL LANGUAGAE; USES GRAPH DATA STRUCTURE


ORM(OBJECT RELATIONAL MAPPING)
WORKS ON SQL
1.CREATE TABLE
  create table Customer( id int primary key auto_increment,name varchar(256),phone varchar(11),email varchar(256))
2.INSERT
insert into Customer values('manmeet','62626 452896','sem@gmail.com')

1.download the python MYSQL LIBRARY---> TWO STDEPS TO DO IT
    > GO TO THE SETTING OF YOUR PROJECT
    >EXECUTE PIP INSTALL COMMAND ON THE COMMAND TERMINAL AVAILABLE BELOW
2.WRITE SQL STATEMENT TO BE EXECUTED AND substitute the data
3.import mysql.connector in your program
4. Create Connection to DataBase with library
5. Obtain Cursor from Connection to execute SQL Statement
6. Execute SQL Statement and Commit It :)

singleton---> design pattern where only one insatance is made to the class such as only opening connection once during the call   zzz

"""
#import mysql.connector as conn
import mysql.connector as connection
class Customer:
    def __init__(self,updateMode):
        if updateMode:
         self.id = input("enter customer ID: ")
         self.name = input("enter your name")
         self.phone = input("enter your mobile number")
         self.email = input("enter your email:")
        else:
            self.id = 0
            self.name = input("enter your name")
            self.phone = input("enter your mobile number")
            self.email = input("enter your email:")

    def showCustomDetails(self):
        print("{}, {}, {}".format(self.name,self.phone,self.email))

print("====Welcome to Customer Management System====")
print("1. Register new customer")
print("2. Update Existing customer")
print("3. Delete Existing customer")
print("4. View all Customer")
print("5. View all Customer by ID")
print("6. View Customer BY Phone")

choice = int(input("Enter your Choice:"))
usage = "yes"
while usage =="yes":
 if choice == 1:
    customer = Customer(True)
    customer.showCustomDetails()

    save = input("Would you like to Save Customer?(yes/no) ")
    if save == "yes":
        sql = "insert into Customer values(null,'{}','{}','{}')".format(customer.id,customer.name,customer.phone,customer.email) # sql query
        con = connection.connect(user="root",password="",database="manmeetdb",host= "127.0.0.1",port="3306") # connecting with database
        # con = conn.connect()
        cursor = con.cursor() # Cursor pointed
        cursor.execute(sql) # executing sql command here
        con.commit() # this commit command will make sure that all the transaction commands should take place, if not then it will not produce any changes

        print(">>Customer saved--->")

    usage= print("would you like to enter more:(yes/no)")
 elif choice == 2:



