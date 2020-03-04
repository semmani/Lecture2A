import re  # REGULAR EXPRESSIONS

quote = "SEARCH THE CANDLE RATHER THAN CURSING THE DARKNESS"
#result = re.match("SEARCH", quote) # match funct starts matching from the start i.e 0 to the last of the string
#print(result)

#result = re.search("THE",quote) # finds the string the, stops when found one of 'the' match and returns the output

#print(result,type(result))

# result = re.findall("THE",quote) # finds all strings for THE match and returns the match
# print(result)

# data = re.split("THE",quote)  # performs the splitting on the basis of 'THE' string
# print(data)

data = re.sub("THE","A",quote) # sub is substitute the string with other string in the given pattern of sentence
print(data)

