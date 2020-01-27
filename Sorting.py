# performing sorting

# 1. Insertion Sort


def insertionSort(data):
 print(len(data))
 for i in range(0,len(data)):
     for j in range(i+1,len(data)):
         if data[i]> data[j]:
             word = data[i]
             data[i] = data[j]
             data[j] = word

     i+=1
     j+=1



 #print(data[i])



ages = [12,25,34,11,67,85,99,41,20,33,74]
insertionSort(ages)
for age in ages:
    print(age, end = " ")


"""
for i in range(1,len(data)):   DATA HAS SAME HASHCODE AS OF AGES
    key = data[i]
    j = i -1
    
    while j>=0 and data[j] > key:
        data[j+1] = data[j]
        j -=1
    data[j+1] = key
        
ages = [12,25,34,11,67,85,99,41,20,33,74] # REFERENCE VAR
"""


#