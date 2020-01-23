# Views

#name = input("Enter the name:")
#print(">> name:", name, type(name))

#age = input("Enter your age:")
#print(">>age:",age,type(age))

#casting
#age = int(input("Enter your age"))
#print(">>age:",age,type(age))
#age = age +1
#print("age after one year is:", age)
#evrything is string and at the back end we need to chnge it to numeric

#age1 = float(age)# type casting
#age2 = list(age)
#age3 = set(age2)

#print(age1)

""" Model --> SVC AND MVS
  View--> input()
  Controller | Logic
   Computation
   Operators
   
   
   """

print("\u20b9") # unicode for rupee symbol in hindi language- refer UNICODE for all similar symbols

num1 = 10
num2 = 3
num3 = num1 // num2
print(num3)


#arithmetic , assignment operators, conditional operators,

cabPrice = 100
wallet = 700
 #print("can i book cab",(cabPrice<=wallet)



#shift operator

num = 8
result = num >>2# rgt shifting ,
result1 = num <<2 # left shift multiply by 4
print("numbr is:",result1)
# WHY SHIFTING IS IMP--->

data = 12
key = 2
result = data >> key
print(result)

anotherResult = result << 2
print(anotherResult)

amount = int(input("enter a amount:"))
promocode = input(("enter promo code:"))

if amount >= 100:
    if promocode == "ZOMATO":
        amount -= 0.4 * amount
        print(">> promocode applied successfully")
        print(">. please pay \u20b9", amount)
    else:
        print(">. Invalid")
        print("use zomato to avail 40% off")
else:
    print(">.Please pay \u20b9",amount)
    print(">. to avail......")


