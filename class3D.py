# USING SPLIT AND ATRIP FUNCTION
"""
names = "John, Jennie, Jim, John, Jack, Joe"
splittedNames = names.split(",")
print(splittedNames, type(splittedNames))

for name in splittedNames:
    print(name.strip())


quotes = Work Hard, Get Luckier
"Search the Candle, rather than cursing the darkness

words = quotes.split(" ")
print(words)
for word in words:
    print(word)
"""
# HW:
def split(sentence):
 start = 0
 space_idx = sentence.find(" ") # find function finds the space in a given sentence and returns the index
 # We can also use-- (issapce()\index())
 while space_idx != -1:
     print(sentence[start:space_idx])# slicing and indexing is required in these
     start = space_idx + 1
     space_idx = sentence.find(" ", space_idx + 1)
 print(sentence[start::])# start :: means starting from 0 to end or :: start means reverse


split("I am in a Darkness which i can only draw away from me")
 #split("Search the Candle, rather than cursing the darkness")
 
#sentence = input("enter any sentence: ")
#if sentence ==" ":



 
 
 




