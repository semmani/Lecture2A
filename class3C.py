# THIS SESSION INCLUDES DIFFERENT STRING BUILT IN FUNCTIONS SUCH AS isdigit()-checks if number is digit or not
# and various similar functions such as isalphanumeric, etc

quote = "Live Life King Size"

for i in range(0,len(quote)):
    # print(quote[i],end=" ") # prints space after evry letter i.e L i v e
     print(quote[i],end="--")

# reversing the quote
for i in range(len(quote),-1,-1): #from let suppose 15 to 0 and -1 means decrement
  print(quote[i])


#sets
S1 = {1, 2, 3, 4, 5, 2}
S2 = {3, 4, 5}
S3 = S1 | S2
S4 = S1 & S2
S5 = S1 - S2
print(S3)
print(S4)
print(S5)


S1 = {1, 2, 3, A, B, C}
S2 = {A, B, C}
print(1 not in S1)
print('X' not in S2)

print(S2.issubset(S1))
print(S1.issuperset(S2))

S3 = S1.union(S2)
#INTERSECTION


S1.add('X') # ADDS X
print(S1)

S1.remove('A') # REMOVES A
S1.pop() # POPS THE FIRST ELEMENT FROM THE S1
print(S1)

S1.clear() # S1 will be cleared
 # converting sets into lists or vice versa

S = {10,20,30}
L = list(S) # MAKING SETS AS LISTS

#and vice versa





