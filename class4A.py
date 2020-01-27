# STRING FORMATTING

name = "Fionna"
age = 22

print(">. welcome to our app %s" %(name)) # using % to print output i.e name fionna at the end

print(name,">> since your  age is" ,age, " you can vote") # when written this way...you get ouput with space and then the message is printed

print(">> { } years old and your name is { }") # we cn use fill in the blank
#msg = "{ } since you are { } old, you can vote".format(name,age) # formatting #3

# running sql query
cid = int(input("enter your id:"))
name = input("enter your name: ")
email = input("enter your email: ")

sql = "insert into Customer values({},'{}','{}')".format(cid,name,email)
print(">>SQL:",sql)



products = [2454,2411,1135,6895]

for i in range(0,len(products)):
    oldPrice = products[i]
    #remaining


