



johnshop ='John\'s Coffee Shop' # or we can write "Johns Coffee Shop", using escape sequence
print(johnshop,type(johnshop))

johnshop = r'John\'s Coffee Shop' # Raw String where an escape sequence will becm part of data
print(johnshop)

quote = "Work hard \t -Anonymous" # using escape seq
print(quote)
# below you can see is you write a continuous multiline message but  putput will print it in one line
message = "This day had a bad starting" \
          "But i ll deal with it" \
          ".c yaa"
print(message)
# triple quote helps you to write multiple lines in one two lines
quotes= """ Work hard,get Luckier
Search the candle rather than cursing the darkness """

name = "John Watson" # name is a reference variable which will hold the hash code of john watson where john watson is a string in contant pool and name exists in Main frame

print(len(name)) # len is 11
print(max(name)) # maximumm ascii char is t hence max in name is t
print(min(name)) # minimum is space as it is the lowest ascii char-32

print(name[1])
print(name[len(name)-1]) # 11-1=10

print(name[1:4])
print(name[1],name[-1]) # prints o and n...as -1 is negative index prints char in reverse order
print(name[1],name[-2] ) # prints o and o

print(name[::-1]) # prints reverse string

#using member ship we can check if email is valid or not
email = input("Enter your email")
print("You Entered: ",email)

if '@' in email and '.' in email: # using memberhsip
    print("Valid email")
else:
    print("Invalid email")

phnum= input("enter your mobile number: ")
print("Number is: ", phnum)

if len(phnum)==10:
    print("Valid Number")
else:
    print("Invalid")



