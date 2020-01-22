menu = {
    "paneer" : 200,
    "Manchurian" : 150,
    "Noodles" : 150,
    "Salad" : 120,
    "Dal-roti": 200
}

cart=[]
print(cart, type(cart), len(cart))
choice ="yes"

while choice == "yes":
    foodItem = input("Enter a food item:")
    if foodItem in menu:
        cart.append(foodItem)
        choice =input("Would you like to add another food item(yes/no):")
    else:
        print(">> Not Available, Please choose another item<< ")

print("Your Cart:",cart)
totalPrice = 0
for item in cart:
    totalPrice = totalPrice + menu[item]

print("TotalPrice:",totalPrice)
promoCode = input("Enter the PromoCode:")

#cart.extend(["Salad","Noddles"]) # extend is built in fucntion which is concatenating a list which was immutable earliar
# hence changes into the same list can be performed instantly using extend

#print("Surprsies in Cart:", cart)
 #cart.insert(1,"Soya Champ") # insert inserts the new data at any index isntantly
#print(">> More Surprise in Cart", cart)

#cart.pop(2)
#print(">>Final Cart", cart) # data at 1 index will be deleted as you see in output

languages = ["C","C++","JAVA"]
print(languages)
print(sorted(languages)) # sorted version of list

# reversing the list (Slicing Technique)
#print(languages::-1) # sorts reversely



#list within lists
menu =[
        ["dal","noodles","roti"]
        [100,200,300]
    ]

print(menu[0],type(menu))
print(menu[1],type(menu))

print(len(menu))
print(menu[0],menu[1]) #length of 0 th list and 1st list

print(menu[0][1])# will print list 0th 1 ist element
print(menu[1][0:2]) # print 200 and 10 as includes 1st elemnt of 1st List but excludes 2nd elemnt-->100,200

