class McDonalds:

    def __init__(self,ordername,price):
        self.ordername = ordername
        self.price = price

    def showMeal(self):
        print("YOUR MEAL:\n {} \t {}".format(self.ordername,self.price))

class UpgradeMeal(McDonalds): # inheritance

    def upgrade(self):
            self.frenchFries = True
            self.mcflurry = True

    def showUpgradedMeal(self):
        self.showMeal()
        print("\tAdded into Your Meal is: french-fries {}\tmcflurry {}".format(self.frenchFries, self.mcflurry))



burger = McDonalds("Burger(Aloo-Tikki)","\u20b9250")
burger.showMeal()
ans = input("\nDo You want to upgrade your meal?(yes/no): ")
if ans == "yes":

    UpgradeMeal.showUpgradedMeal(burger)
    print(burger.__dict__)



else:
    print("Enjoy your meal")


