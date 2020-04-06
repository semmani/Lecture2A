"""
Vehicles-->
0-> Bike
1-> Car

weight    engine      vehicle
200kg      100cc       0
250kg      200cc       0
300kg      250cc       0
350kg       300cc      0

800kg       800cc        1
100kg       1100cc       1
1200kg       1300cc      1
1500kg       1500cc      1

"""
from sklearn import tree
#SUPERVISED MACHINE LEARNING

bike = 0
car = 1

bike1 = [200,100]
# representing Training Data
X = [
      bike1,[250,200],[300,250],[350,300],
     [800,880],[100,1100],[1200,1300],[1500,1500]

    ]

Y = [0,0,0,0,1,1,1,1]
#OR WE CAN WRITE Y = [bike,bike,bike,bike,car,car,car,car]

model = tree.DecisionTreeClassifier()
model = model.fit(X,Y)

result = model.predict([[220,200]]) # here we predicted through sending the values....and our code guessed that values matches
#the bike config...so it is bike

result2 = model.predict([[1250,1100]])
print(result2) # this predicted the values to be in Car category




