# references again
def square(number):
    print(">> [SQUARE] numbers is:", number,hex(id(number)))

# we are squaring the numbers
for i in range(0, len(number)):
    number[i] = number[i]*number[i]
print(">> [SQUARE] numbers is:", number,hex(id(number)))


# list in python

number = [10,20,30,40,50]
print(number, hex(id(number)))
square(number)
print(number, hex(id(number)))