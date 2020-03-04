import pandas as pd

# pandas contains SERIES--> 1D ARRAY,   DATAFRAMES---> 2D ARRAY LIKE STRUCTURE

num1 =[10,20,30,40,50]
num2 = [11,22,33,44,55]

emp1 = {"name": "John",
        "age": 22,
        "salary": 3000
        }

emp2 = {"name": "Dave",
        "age": 25,
        "salary": 40000
        }

emp3 = {"name": "Annie",
        "age": 22,
        "salary": 60000
        }

emp4 = {"name": "Kia",                    #NaN---> IS FOR MISSING DATA FOR PARTICULAR KEY
        "age": 28,
        "salary": 35000,
        "email": "kia@example.com"
        }


frame1 = pd.DataFrame([num1,num2])
frame2 = pd.DataFrame([emp1,emp2,emp3,emp4])

print(frame1)
print("---------")
print(frame2)

print(frame1[0])
print(frame2["name"])  # printing the data column-wise

print(frame1[1][1]) # 22 value
print(frame2["salary"][2])  # prints salary of 2 column

print("-----slicing------")

print(frame1[1:])
print(frame2[3:])

print("----deleting-------")

del(frame1[0]) # columnwise deletion
print(frame1)
print("---dropping the row-----")
frame3= frame1.drop(0, axis=0, inplace=True) #inplace = True makes sure that deletion takes place in one frame only
print(frame3)


# frame1[1][0] = 23
# print(frame1)