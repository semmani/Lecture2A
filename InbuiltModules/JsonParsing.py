#JSON IS A DICTIONARY CONTAINING LISTS OR DICTIONARY NESTED IN IT
#open https://newsapi.org----> JSON API KEY

import json

employee = {
    "eid": 201,
    "name": "John",
    "salary": 20000,
    "projects": ["CMS","MDS"],  # WE SEE THAT WE CAN WRITE A LIST AS A VALUE OF KEY PROJECTS
    "manager": {"mid": 221,"name": "Fionna"}  #HERE WE WRITE A DICTIONARY CONTAINING KEY AND VALUE OF KEY MANAGER
}

print(employee)
print(type(employee))


#Convert dicitionary employee into JSON
jsonData = json.dumps(employee)  #OUTPUT IS JUST LIKE THE NORMAL DICTIONARY IS PRINTED,CAN'T BE DESERIALIZED
print(jsonData) # json data is of string type
print(type(jsonData))


#CONVERTING JSON DATA INTO DICTIONARY
empDict = json.loads(jsonData)
print(empDict) # data is printed into the dict format again
print(type(empDict))  #type is dictionary



