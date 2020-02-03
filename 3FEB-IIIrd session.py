
name = "Johny Depp"
phone = "+91888896324"
address = "redwood shores"
file = open("data.csv","a") # to append the code
file = open("data.csv","w") # writes into the file,overwrites if already written, creates the file if file do not exists
"{},{},{}".format(name,phone,address) # format of excel file, data will be saved in the form of columns and

file.write(name)
file.write(phone)
#file.write(phone) #overwriting
file.close()

print("data saved in file")


@staticmethod # it is a decorator ----> no self is needed in the method


