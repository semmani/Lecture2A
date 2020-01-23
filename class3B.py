# built in functions i.e built in APIs

name = "Fionna"
#print.upper()
print(name) # Not possible , because data Fionna is constant hence cnt be updated and so cnt be chnged to uppercase
# hence STRINGS ARE IMMUTABLE

newName = name.upper() # now possible, i.e output will be in uppercase
print(newName)

authorName = "John Keats"
print(authorName,hex(id(authorName))) # hashcode
authorName = authorName.capitalize() # we are copying hashcode of old variable authorName into the same variable but string has new hashcode
#capitalizes, first letter J --->Memory leak takes place i.e. No reference to john watson is there hence it will eb deleted later but untill then it lies in constant pool called as constant pool
print(authorName,hex(id(authorName)))

# there should be no Memory leaks....use instant deletion to avoid overflowing the constant pool--> Memory leak
# using various algorithms at the back end...

names = "John", "Jennie", "Jack", "Joe" # this is string
print(names[0]) # output is John
print(names[len(names)-1]) # name is Joe
idx = names.index("Jennie") # index will be 6 because whole names are exactly string
print(idx)

"""num = names.count("John", 0, len(names))
print(">> num is :",num)
"""


#using function to count a no of word occuring in the given string

quotes= """ Work hard,get Luckier
Search the candle rather than cursing the darkness """
#HOME WORK---> DONE IN 5 MIN
def count(data, word, start, end):
    c = 0
    j = 0
    print("we r finding word--> the")
    for i in range(start,end):
        if data[i]==word[j]:
            if data[i+1] == word[j+1]:
                if data[i+2] == word[j+2]:
                    c = c+1


        else:
            continue


    return c
print(">> the occurs :", count(quotes,"the",0,len(quotes)),"times") # we are checking the no of times the occurs
# in the above quotes



#Using split function
names = "John, Jennie, Jack, Joe"
splittedNames = print(names.split(",")) # splitting names on the basis of ',' along with the spaces
print(splittedNames)
 # in order to strip spaces in the output of splittedNames---> use STRIP()

for name in splittedNames:
    print(name.strip())



#HW is to implement functioning of split...which is to print words in the sentence




