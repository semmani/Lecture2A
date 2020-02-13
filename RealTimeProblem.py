#A Customer Has a Property
#fee structure for the payment of garbage collection acc to the space cleaned


#Customer has a Property
# class Customer:

    def __init__(self,id,name,address):
        self.id = int(input("Customer ID: "))
        self.name = input("Enter the Customer Name: ")
        self.address = input("Enter the Address to Collect the Garbage from: ")


    def showDetails(self):
        print("id:{},name:{},address:{}".format(self.id, self.name, self.address))

    def saveData(self):
        data = "{},{},{}\n".format(self.id, self.name, self.address)
        file = open("customer.csv","a")
        file.write(data)
        print("Customer Data is saved")
        file.close()

    def Property(self):
        fee = {
            "100sq": 100,
            "200sq": 200,
            "300sq": 300,
            "400sq": 400,
            "500sq": 500
        }
        print("The fee structure for Garbage Collection is:", fee)
        size = input("What is the size of your property?: ")
        for key, value in fee.items():
            key = size
            if key == "100sq":
                print("Bill for Customer ID-{} per Month is:\u20b9{}".format(self.id, value))
                break
            elif key == "200sq":
                print("Bill for Customer ID- {} per Month is:\u20b9{}".format(self.id, fee[key]))
                break
            elif key == "300sq":
                print("Bill for Customer ID-{} per Month is:\u20b9{}".format(self.id, fee[key]))
                break
            elif key == "400sq":
                print("Bill for Customer ID-{} per Month is:\u20b9{}".format(self.id, fee[key]))
                break
            elif key == "500sq":
                print("Bill for Customer ID-{} per Month is:\u20b9{}".format(self.id, fee[key]))
                break
            else:
                print("Land Coverage is out of Range")
                break



class GarbageCollector():
    # creating the file named as bill.csv to add customers who have added the bill for month-year et
    @staticmethod
    def data():
        print("Saving Customer-Bill Data")
        file = open("customer.csv","r")
        lines = file.readlines()
        for line in lines:
            data = line.split(",")
            print(data)
            customer = Customer(data[1], data[2], (data[3]))
            customer.id = Customer(data[1])
            customer.showDetail()
        print()
        file.close()









#class GarbageCollector: # it will add the customer into the bills file and checks fif he has paid the bill then
# to calculate its next bill, otherwise to





customer1 = Customer()
customer1.showDetails()
customer1.saveData()
customer1.Property()

