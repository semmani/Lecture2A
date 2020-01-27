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
  c=0
  words = []
  words.append(sentence)
  for word in words:
    print(word[0:6])
    print(word[7:10])
    print(word[11:18])
    print(word[19:25])
    print(word[])


 # print("No of spaces are:",c)


split("Search the Candle, rather than cursing the darkness")




