# complete it from github and try to add delete function


class Product:

    def __init__(self,pid,name,price,quantity):
        self.pid = pid
        self.name = name
        self.price = price
        self.nextProduct = None
        self.previousProduct = None
        self.quantity = quantity

    def showProdDetails(self):
        print("------------------------------------------")
        print("{}\t{}\t{}\t{}\t".format(self.pid,self.name,self.price,self.quantity))
        print("-------------------------------------------")


class LinkdList:
    #size = 0
    #items = 0 #add items in as class property
    #price = 0

    def __init__(self):
        print(">>Linked list Created--->")
        print(self)# prints hashcode of self
        self.head = None
        self.current = None
    def append(self,product):
        print(product)
        #LinkdList.items += 1
        #LinkdList.price += (product.quantity * product.price)


     # head is pointing to Product i.e whichever




        if self.head == None:
            self.head = product
            self.current = product
        else:
            product.previousProduct = self.current
            self.current.nextProduct = product

            self.current = product
            product.nextProduct = self.head # adds circular feature
            self.head.prevProduct = self.current # inorder to iterate backward, we set previous product of head as current



    def showForward(self):
        #print("Iterating forward--------->>")
        temp = self.head
        while temp.nextProduct != self.head:
            temp.showProdDetails()
            temp = temp.nextProduct

        temp.showProdDetails()



    def showBackward(self):
        print("Iterating Backward------------------>")
        last = self.current
        while last.previousProduct != self.current:
            last.showProdDetails()
            last = last.previousProduct
            print(">>Last is:",last)
        last.showProdDetails

    def getTotalPrice(self):

        totalPrice = 0
        totalItems = 0
        totalProducts = 0

        temp = self.head

        while temp.nextProduct != self.head:
            totalPrice = totalPrice + (temp.price * temp.quantity)
            totalItems = totalItems + temp.quantity
            totalProducts += 1
            temp = temp.nextProduct

        totalPrice = totalPrice + (temp.price * temp.quantity)
        totalItems = totalItems + temp.quantity
        totalProducts += 1

        #return (totalPrice, totalItems, totalProducts)
        print("Price ",totalPrice) # price is multiplied by its quantity and then price is shown!
        print("Items ",totalItems) # items---> items * quantity = items
        print("Products ",totalProducts) # products if given three irrespective of the quantity prints 3 only



shoppingCart = LinkdList() # reference to LinkdList class--->object when made
#product1 = Product(1001,"IphoneX","70000",2) # provided value product1,now we want to append it
#product2 = Product(1002,"Samsung S9",55000,1)
#product3 = Product(1005,"Motorola g10",50000,3)
#shoppingCart.append(product1) # we donot use this criteria as it will create hashcode of object in Main frame
shoppingCart.append(Product(1001,"1.IphoneX",70000,2)) # here when object is made, value is provided, which do not make its hashcode in Main Frame
shoppingCart.append(Product(1002,"2.Samsung S9",90000,1))
shoppingCart.append(Product(1005,"3.Motorola g10",50000,3))


shoppingCart.showForward()
#shoppingCart.showBackward()

#print("Items In Cart:",LinkdList.totalPrice())
#print("Price: ",LinkdList.totalItems)
print(LinkdList.getTotalPrice(shoppingCart))