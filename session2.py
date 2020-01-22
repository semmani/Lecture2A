print(">> Welcome to Python App")

num=5
print(">> 1. no is",num) # main frame

def square(n):
    #using global variable will belong it to main
    global num # data interaction between frames in the memory as a result, num is same as num defined above
    #num wil be local num to square
    n = n*n
    num = n
    print(">> 2. n is:",n)
    print(">>3 no is:", num)
    return num  # can be optional   when return is called the frame is remove from the memory

square(7) # frame square
print(">>4 no is:",num)
# here also main fucn is returned and as a result these func will be removed from the memory
