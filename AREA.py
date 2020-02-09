def areaOfCircle(rad = 1.0):
    area = 3.14 * rad * rad
    return area
area = areaOfCircle # reference copy; same hashcode
print("Area Of Circle:",areaOfCircle)
print("Area is:",area)


print("area of circle with radius is:",areaOfCircle(5))
print("area of circle with radius is:",area(5))

#lambda is used to compute single expression statements
print("-----------------------------------------------------")
lref1 = lambda rad = 1.0:3.14 * rad * rad
lref2 = lambda x, y : x**y
print("area of circle is using lambda : ",lref1(7))
print("2 power 4 is:",lref2(2,4))

# lambda within another lambda expression

# lref3 = lambda x = int(input("enter x: ")), y = int(input("enter y :")): x+y
# print("X+Y=",lref3()) # returns sum of x +y
# lref4 = lambda x = 10, y = 20 : x+y
# print(lref4)


# sqaure of numbers
def squareOfNumber(num = 1):
    return num * num

lref1 = lambda num : num*num

numbers = [10,20,30,40]
# for num in numbers:
#     print("sqaure of numbers is:",lref1(num))



# using filter() and map()----filter method selects and shows it excluding it froma all; map function maps with the condition

L1 = range(10,21,1)
print(L1)

lref3 = lambda num : num%2 == 0
lref4 = lambda num : num%2 != 0

print(map(lref3,L1))# REMAINING

from functools import reduce

L3 = [10,20,30,40,50]

print(reduce(lambda X, Y : X + Y, [10,20,30,40,50])) #REDUCE IS ADDING RESULT OF PREVIOUS SUM INTO THE NEXT NUMBER AND GOES ON......