"""" "Sequence in python
includes data with quitesimilartype

  sequences listed below are also called Data Structuresor built in Python


   Whydata shud4 be structured:
  1. Sort
  2. Search
  3  . Filter
    tuple
    list
    strings
    sets
    dictionary


    operations:-
    concatenation
    repetition
    membership testing
    slicing
    indexing
"""""
    #tuple- we cnnot add into tuples anything except printing updations by concatenating
students =("John","Jennie","jim","Joe")
print(students)
print(students + ("Fionna","George"))
print(students,hex(id(students)))
#Concatenation - Immutable(cnt be updtaed
newStudents = students +("Fionna","George")
print(newStudents,hex(id(newStudents)))


# Repetition

print(students*2)

#MEMBERSHIP TESTING
print("john" in students) # searching
print("Dave" not in students)

#indexing

print(students[0]) #john
#print(students[len(students)]) # joe




# Slicing - filtering data within ranges

print(students[0:2]) # this will include 0th data but exclude 2thdata...i.e. john and jennie
print(students[1:4])
filteredStudents = students[1:4]
print(filteredStudents)


print()

#for anyNameOfYourChoice in students:
 #print()

 #for i in range(0,
 # Foreach loop-enhanced version of for loop
for student in students:
     print(student)


# Using Lists and operations all above within Lists

stud = ["John","Jennie","Jack","Joe"]
print(stud)

print(stud + ["Fionna","Dave"]) # updating list by concatenating...if yes then true...else no
# print(stud + students) # checking for list + tuple # when run--->Not possible
print(stud,hex(id(stud)))# hashcode of stud list

newStudents = stud + ["Fionna", "Harris"]
print(stud)
print(newStudents,hex(id(newStudents)))



#Sets----Check for concatenation, concat list plus tupe into set, see if for loop range weorks, for each loop works or not,
#No repetition, indexing and slicing-

studd = {"John","Jennie","Jack","Joe"} #sets
# Concatenation
print(studd,hex(id(studd))) # printing dataof setss
#print(studd + {"Harris","Davis"}) # concatenation---->Not Possible

#print(students + stud + studd )---- Notworking


# Indexing
# print(studd[1])----> Not working

#Slicing
#print(studd[1:2]) # Not Working


# Simple for loop dont work
#using for each loop

for students in studd: # for each loop works
 print(students)


# Membership testing---> Working
print("John" in studd) # searching if john in sets---> True
print("Dave" not in studd) # Dave is not in Sets--->true

#Dictionary- indexes are replaced with Keys and keys can be of our choice and they must be string in nature

student = {
     "RollNo" : 1011,
     "Name" : "Manmeet Kaur",
     "Email" : "semmanemet2@gmail.com"
}
# here in dictionary data structure roll no is a key whose value is 1011 and so on. We can give any Key values of our choice
print(student)
print(type(student))


#List Comprehension

data = [1,2,3,4,5]
print(data)
print(len(data)) # it shud be length of values that datahasthat is 5
print(max(data)) # maximum data from list--->5
print(min(data)) # minimum data from list--->1


print([x**2 for x in student])
