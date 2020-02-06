class McDonalds:

    def __init__(self,ordername,price):
        self.ordername = ordername
        self.price = price

    def showMeal(self):
        print("YOUR Order:\n {} \t {}".format(self.ordername,self.price))

class UpgradeMeal(McDonalds): # inheritance

    def upgrade(self,newItem1,newPrice):
         self.newItem1 = newItem1
         self.newPrice = newPrice


    def showUpgradedMeal(self):
        totalNewItems = 0
        print("\tAdded into the Order is: {}\t{}".format(self.newItems, self.newPrice))




burger = McDonalds("Burger(Basic)","\u20b9350")
burger.showMeal()
ans = input("\n Do You want to upgrade your meal?(yes/no): ")
if ans == "yes":

    UpgradeMeal.upgrade(burger,"french-fries","\u20b9100")# we extend the feature of Customer to PrimeCustomer
    # to append bothfrenchfries and coketogether---> ask ishant sir
    UpgradeMeal.upgrade(burger, "Medium Sized Coke", "\u20b9200")
   # UpgradeMeal.upgrade(burger, "Mcflurry Chocolate Flavour", "\u20b9150")
    UpgradeMeal.showUpgradedMeal(burger)




else:
    print("Enjoy your meal")


