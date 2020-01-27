#def fun(n1,n2):
    #sum = n1 +n2
   # print(">>sum is {}".format(sum),type(sum))

#def fun(n1,n2):
   # sum = n1+n2
   # print("sum is {}".format(sum),type(sum))# error as we are overloading the function---> Not possible

#fun(10,35)


# Variable arguments in Python
def add(*args): # we can send any no of arguments....it will add all or perform
    print(args)
    print(type(args))
    sum = 0
    for data in args:
        sum = sum+ data
    print("Data is:",sum)


# chk it from github



# Key word arguments---> Dictionary

def fun(**kwargs):# it works like dictionary
    print(kwargs)
    print(type(kwargs))

fun(a = 10, b = 20, name = "John") # type is dictionary


def fun(*args,**kwargs):
#def fun(**kwargs,*args):
    print(kwargs)
    print(args)


#fun(name="Manmeet",email="semmanemet2@gmail.com",10,25) # arguments(numbers) and dictionary format printed together

# **kwargs and *args pattern will not work bcoz right pattern is *args and then **kwargs

"""
def maxNumber(data):
    max = data[0]
    for num in data:
        if num > max:
           max = num

    return max



number=[20,52,11]
print("maximum number is{}".format(number,maxNumber(number)))
"""

#below we are calling the function i.e recursing---/, where we are cmparing nubers to find maximum numbers without using loops as recursion do not
# leads to the Memory Leak i.e. it is memory optimizes
def maxNumber(data,length):
    if length == 1:
        return data[0]
    else:
         num =  maxNumber(data,length-1)

    if num>data[length-1]:
         return num
    else:
        return data[length-1]


number =[20,140,60]
print(">>maximum number is:",maxNumber(number,3))

# number is compared untill length is 1 and then that number is sent to



# printing binary format of any decimal no in python using recursion--->

def binary(num):
  if num == 0:
      return
  else:
      binary(num//2) # / is for floating point and // is used for integer dividing
      print(num%2,end=" ")



number = 8
print(bin(8))
print(binary(number))


#Gist

"""

 types of recursion-->
direct recursion
indirect recursion
tail recursion

"""

def fun():
     fun() # direct recurs

def fun1():

    fun2(): # indirect recursion

def tailRecur():
    #if __name__ == '__main__':
        #.....
        #if __name__ == '__main__':
            #....
tailRecur() # tail recursion





