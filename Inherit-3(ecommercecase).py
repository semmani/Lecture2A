# why inheritance:-   to reuse the code, only additional htings in child classes, saves time(Development time)
# inheritance leads to Generalization

class hello1:
     a = 10
     def __init__(self,b):
        print("hello A")
        self.b = b
     def show(self):
         print("a is",hello1.a)
         print("b is", self.b)

class hello2:
    x = 25
    def __init__(self,y,z):
       print("hello B")
       self.y = y
       self.z = z

    def show(self):
        print("x is", hello2.x)
        print("y is", self.y)
        print("z is", self.z)

class hello3(hello1,hello2):
     pass
   #def __init__(self, y):
        #print("hello c")
        #self.y = y


hey = hello3(100,33)
print("cref dictionary",hey.__dict__) # A init is used by Child C as parent A
print("Show function--->") # SHOW FUNCTION WORKS WITH A

hey.show()


#question 1--->which init should work? : 2. which show should work? : 3.how it 