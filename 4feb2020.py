
"""
file = open("session5.py","r")
data = file.read() # reading entire data in the file
print(data)

print("--------------------------")
# lets reread the data again
data = file.read()
print(data) # it will not give you the data as we have already read it above,hence no output
"""
# Reading with conditions
file = open("session5.py","r")
data = file.read(16) # reading the file upto 16 characters-----> NOT A GOOD APPROACH
print(data)


# HENCE READING BY READLINE
file = open("session5.py","r")
line1 = file.readline() # reading entire data in the file
print(line1)

line2 = file.readline() # reading entire data in the file
print(line2)

lines = file.readlines() # reads entire lines
for line in lines: # using loop i print all lines
    print(line)
file.close()
# toprint only functions in the file---->
file=open("MakingLinkedList-Implementing.py","r")
lines = file.readlines()
functions = 0
for line in lines:
    if "def" in line:
        functions += 1
print(">>total functions are:",functions)
file.close()
# to print the names of the functionsin the opened file

file = open("session5.py")
print(file.tell())

file.seek(10) # takes the cursor to 10 th character
data = file.read(15) #starts printing from 10 th to 15 th character
print(data)
print(file.tell())# value will be -->26







