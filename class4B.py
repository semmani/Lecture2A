employee = {
    "0" : "John Watson", # 0 having min ascii vlue, hence shown as minimum key
     "eid" : 1011,
      "rating" : 4.5,
     "salary" : 30000
} # HETEROGENOUS DATA , HENCE CANT BE UPDATED AS IN COMPARED
print(employee,type(employee))
print(max(employee)) #salary bcoz maximum ascii value is max of s-->salary
print(min(employee)) # same reason as above---> min ascii is of e

employee["address"] = "Redwood shores"
print(employee) # adress is added even if it doesnt exist

del employee["eid"] # eid key is deleted
print(employee)

#del employee # gets deleted in memory
#print(employee) # error, but employee is already deleted from the memory

#keys = employee.keys()---> to just save all the keys from the dictionary employee
keys = list(employee.keys()) # converted in list format
print(">>keys: ",keys,type(keys)) # all the keys will be printed in the form of list


