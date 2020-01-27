#Creating functions:-
#Recursion
 def show(num):
     if num == 0:
         return # terminates the execution
     print(num)
     num-=1
     show(num)

     show(10)# calling the fun
     #show(9)
     show(8)
     show(7)
     show(6)

     # Need to check the time complexity i.e whether