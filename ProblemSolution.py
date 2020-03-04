fee = {
    "100" : 100,
    "200": 200,
    "300": 300,
    "400": 400,
    "500": 500
}


class Property: # we can have limited number of attributes of property
    def __init__(self, area=None, size=None):
        self.area = area
        self.size = size

    def inputPropertyDetails(self):
        self.area = input("Enter the area: ")
        self.size = input("Enter the size: ")

    def PropertyDetails(self):
        print("{},{}".format(self.area, self.size))

    def toCSV(self):
        return "{},{}".format(self.area, self.size)

class Customer:
    def __init__(self, name, phone, email, property):
        self.name = name
        self.phone = phone
        self.email = email
        self.property = property

    def inputCustomerDetails(self):
        self.name = input("Enter Customer Name: ")
        self.phone = input("Enter Customer Phone: ")
        self.email = input("Enter Customer Email: ")

    # HAS-A RELATIONSHIP
    def PropertyLinkCustomer(self,property):
        self.property = property


    def showCustomerDetails(self):
        print("{},{},{}".format(self.name,self.phone,self.email))
        self.property.PropertyDetails()

    def toCSV(self):
        return "{},{},{},{}\n".format(self.name,self.phone,self.email,self.property.toCSV())


class Fee:
    def __init__(self, phone= None, month= None, year=None, amount=None):
        self.phone = phone
        self.month = month
        self.year = year
        self.amount = amount

    def inputFeeDetails(self):
        self.phone = input("Enter PhoneNum: ")
        self.month = input(" Enter Month: ")
        self.year = input("Enter Year: ")

    file = open("gc-customers.csv","r")
    lines = file.readlines()

    for line in lines:
        data = line.split(",")
        if data[1] == self.phone:
            size = data[len(data)-1].strip()
            self.amount = fee[size]





