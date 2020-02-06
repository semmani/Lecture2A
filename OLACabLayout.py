#to be completed from the github

# Ram is volatile memory i.e temporary
# whenver process is finsished, program will beb finished
#Saving data somewhere--->Persistence
# we perform serialization and De-Serialization

class Customer:
    def __init__(self,name,phone,email):
        self.name = name
        self.phone = phone
        self.email = email

    def showCustomerDetails(self):
        print("Name: {},Phone: {},Email: {}".format(self.name,self.phone,self.email))

class Driver(Customer):   # inheritance---> inheriting Customer class
    def __init__(self,name,phone,email,licenseNumber):
        Customer.__init__(self,name,phone,email) # referring to Customer class data within Base cass Driver
        self.licenseNumber = licenseNumber # driver class own member
    def showDriverDetails(self):
        print("DRIVER DETAILS:")
        self.showCustomerDetails() # shows customer details within driver details
        print("License Number:",self.licenseNumber)

class Cab: # cab class prints details of the cab and further different cabs selected define their own cabs
    def __init__(self,regNumber,basePrice):
        self.regNumber = regNumber
        self.basePrice = basePrice

    def showCabDetails(self):
        print("CAB DETAILS:")
        print("Reg Number:{}, Base Price:{}".format(self.regNumber,self.basePrice))

class OlaMini(Cab):
    def showCabDetails(self):
        print("OLA MINI ON THE WAY!")
        print("Reg Number:{}, Base Price:{}".format(self.regNumber, self.basePrice))


class OlaMicro(Cab):
    def showCabDetails(self):
        print("OLA MICRO ON THE WAY!")
        print("Reg Number:{}, Base Price:{}".format(self.regNumber, self.basePrice))

class OlaSedan(Cab):
    def showCabDetails(self):
        print("OLA SEDAN ON THE WAY")
        print("Reg Number:{}, Base Price:{}".format(self.regNumber, self.basePrice))


class Ride:     # this class intakes various fields to provide a ride(rideno,name,source-destination,driver etc)
    rideNumber = 1
    def __init__(self,customer):
        self.ride = Ride.rideNumber
        self.customer = customer
        Ride.rideNumber += 1  #increments ride number evrytime the ride is taken

    def sourceAnddestination(self):
        self.source = input("ENTER THE SOURCE FOR PICK UP: ")
        self.destination = input("ENTER THE DESTINATION TO GO: ")
        print("RIDE SELECTED SUCCESSFULLY, {} TO {}".format(self.source,self.destination))

    def selectCab(self):
        self.cab = None
        print("WHICH CAB DO YOU WANT TO SELECT FOR THE RIDE")
        print("OLA MINI | OLA MICRO | OLA SEDAN ")
        choice = input("ENTER WHICH RIDE YOU WANT TO BOOK? ")
         # Runtime polymorphism, during runtime the call is resolved i.e during runtime the cab refers to either of olamini,micro or sedan
        if choice == "MINI":
            self.cab = OlaMini("PB10AD0041",100)

        elif choice == "MICRO":
            self.cab = OlaMicro("PB10AD1125",150)

        else:
            self.cab = OlaSedan("PB10HH0042",100)


    def attachDriver(self,driver):
        self.driver = driver

    def showRideDetails(self): # this will print all the ride details showing from source to destination,cab/driver/cust details
        print("RIDE BOOKED ( FROM {} TO {} )".format(self.source,self.destination))
        print("YOUR RIDE NUMBER: ",self.ride)
        self.cab.showCabDetails()
        self.driver.showDriverDetails()
        self.customer.showCustomerDetails()

# REFERENCE TO THE CUSTOMER CLASS AND DRIVER CLASS
customer = Customer("David Essen","+91 258369 222","davide@gmail.com")
driver = Driver("Jeevan Singh","+91 852741","jeevan@gmail.com","X1254B9")

anothrcustomer = Customer("Mike Dawson","+956325896","mike@hotmail.com")
anothrdriver = Driver("Jenna Hayer","+91 25825822","jennahayer@gmail.com","YH1234")

# REFERENCE TO RIDE NOW IN ORDER TO BOOK IT AND GO AROUND
ride = Ride(customer)
ride.sourceAnddestination()
ride.selectCab()
ride.attachDriver(driver)
ride.showRideDetails()

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
reply = input("------- WANT TO BOOK ANOTHER RIDE----------\n TYPE YES, FOR BOOKING ELSE NO----------\n")
while reply == 'YES': # IMPROVEMENTS NEEDED HERE!!

    ride = Ride(anothrcustomer)
    ride.sourceAnddestination()
    ride.selectCab()
    ride.attachDriver(anothrdriver)
    ride.showRideDetails()

print("********************************THANKYOU FOR BOOKING***************************************")








