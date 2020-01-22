def square(num): # num is reference variable holding hashcode
    print(">> [SQUARE] num is", num, hex(id(num)))
    num = num * num
    print(">> [SQUARE] num is:",num, hex(id(num)))

num =10 # reference variable holds
print(">> [MAIN] num is",num, hex(id(num)))
square(num)
print(">> [MAIN] num is",num, hex(id(num)))

