"""
OOP- HAS A RELATIONSHIP
 A. THINK OF AN OBJECT:-
 Restaurant - name,phone,email,address,priceperperson,openingHours
 menu : name,description
 Dish : name,price,description,type
B. TO MAKE A SOFTWARE WE  NEED TO IDENTIFY RELATIONSHIPS
 1.restaurant - 1 menu --> one to one relationship(1:1) MAPPING
 1. restaurant - 2 menu --> one to many relationship ( 1:N)

 Many menus have many dishes
 many restaurant have many menus--- Many to Many relations(N:M)

 Restaurant - name,phone,email,address,priceperperson,openingHours,menu
 menu : name,description,dish
 Dish : name,price,description,type



"""

class Restaurant:
    def __init__(self,name,phone,email,address,pricePerPerson,openingHours,menu):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        self.pricePerPerson = pricePerPerson
        self.openingHours = openingHours
        self.menu = menu


class Menu:
    def __init__(self,name,description,dish):
        self.name = name
        self.description = description
        self.dish = dish

class Dish:
    def __init__(self,name,price,description,type):
        self.name = name
        self.price = price
        self.description = description
        self.type = type
        self.quantity = 0

    def showDish:
        print("\t\t {}".format())

dish1 = Dish("Manchoorian","200","Stuffed With Vegs","Chinese")
dish2 = Dish("Noodles","150","Shezwaan With Chopped-Veg","Indo-Chinese")
dish3 = Dish("Cheese Tomato","200","Indian Most Loved Cury Food","IndianVeg1")
#remaining...complete it!
# adding cart as well to show quantities
cart =[]
totalDishes = 0
def showDishTo Cart(dish):
   global totalDishes
   cart.append(dish)
   totalDishes += 1

dish1.quantity = 1
cart.append(dish1)

dish3.quantity = 2
cart.append(dish3)

for dish in cart:
    print("dish quantities")
    totalPrice = totalPrice +(dish.price*dish.quantity)







