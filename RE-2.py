import re

quote = "WORK HARD AND GET LUCKIER"

result = re.findall(".",quote)  #"." prints the character seperated with . gives all the characters
print(result,type(result))
print(len(result))

result2 = re.findall("\w",quote) # removes the space along with printing every word of string
print(result2)

result3 = re.findall("\w*",quote) #\w* ---> thsi pattern prints all the words along with spaces printing under single quotes
#\w+ this pattern prints the words as an outpput
print(result3)


"""
PS: WWW.VOGELLA.COM/TUTORIALS/JAVAREGULAREXPRESSIONS/ARTICLE.HTML
VALIDATION check
Take the input of car number and check for its validity
also check for email
 
 
 

"""