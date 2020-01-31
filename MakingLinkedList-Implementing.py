# complete it from github and try to add delete function


class Product:

    def __init__(self,pid,name,price,quantity):
        self.pid = pid
        self.name = name
        self.price = price
        self.nextProduct = None
        self.previousProduct = None
        self.quantity = 0
    def showProdDetails(self):
        print("------------------------------------------")
        print("{}\t{}\t{}\t{}\t".format(self.pid,self.name,self.price,self.quantity))
        print("-------------------------------------------")


class LinkdList:
    size = 0
    items = 0 #add items in as class property
    def __init__(self):
        print(">>Linked list Created--->")
        print(self)# prints hashcode of self
        self.head = None
        self.current = None
    def append(self,product):
        print(product)
        LinkdList.items += product.quantity
         # head is pointing to Product i.e whichever

        self.head = product
        self.current = product
        if self.head == None:
            self.head = product
            self.current = product
        else:
            product.previousProduct = self.current
            self.current.nextProduct = product

            self.current = product
            product.nextProduct = self.head # adds circular feature
            self.head.prevProduct = self.current # inorder to iterate backward, we set previous product of head as current

print("Iterating forward--------->>")
    def showForward(self):
        temp = self.head
        while self.head != self.head:
            temp.showProdDetails()
            temp = temp.nextProduct

        temp.showProdDetails()

print("Iterating Backward------------------>")

    def showBackward(self):
        last = self.current
        while last.previousProduct != self.current:
            last.showProdDetails()
            last = last.previousProduct
            print(">>Last is:",last)
        last.showProdDetails

    def getTotalPrice(self):
        totalPrice = 0
        temp = self.head

        while temp.nextProduct != self.head:
            totalPrice = totalPrice



shoppingCart = LinkdList() # reference to LinkdList class--->object when made
product1 = Product(1001,"IphoneX","70000",2) # provided value product1,now we want to append it
product2 = Product(1002,"Samsung S9",55000,1)
product3 = Product(1005,"Motorola g10",50000,3)
#shoppingCart.append(product1) # we donot use this criteria as it will create hashcode of object in Main frame
shoppingCart.append(Product(1001,"IphoneX",70000,2)) # here when object is made, value is provided, which do not make its hashcode in Main Frame
shoppingCart.append(Product(1002,"Samsung S9",55000,1))
shoppingCart.append(Product(1005,"Motorola g10",50000,3))


#shoppingCart.showForward()
shoppingCart.showBackward()
