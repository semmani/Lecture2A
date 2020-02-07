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

# implementing Stack---LIFO
class Stack:
    size = 0
    items = 0
    price = 0

    def __init__(self):
        print(">>Stack Created--->")
        print(self)
        self.head = None
        self.current = None

    def push(self,product):
        print(product)

        if self.head == None:
            self.head = product
            self.current = product
        else:
            product.previousProduct = self.current
            self.current.nextProduct = product
            self.current = product
            product.nextProduct = self.head # adds circular feature
            self.head.previousProduct = self.current #Inorder to iterate backward, we set previous product of head as current

    def iterate(self):
            print("-----------STACK OF PRODUCTS--------------->")
            temp = self.current
            while temp.previousProduct != self.current:
                temp.showProdDetails()
                temp = temp.previousProduct
                print(">>temp is:",temp)
            temp.showProdDetails

    def pop(self):
        print("-----------Deleting the head-------------")
        self.current = self.current.previousProduct
        self.current.nextProduct = self.head
        self.head.previousProduct = self.current




cart = Stack()
cart.push(Product(1001, "1.IphoneX", 70000, 2))      #here when object is made, value is provided, which do not make its hashcode in Main Frame
cart.push(Product(1002, "2.Samsung S9", 90000, 1))
cart.push(Product(1005, "3.Motorola g10", 50000, 3))
cart.push(Product(4006, "4.Addidas Shoes", 15000, 1))

cart.iterate()
print("==========================")

#cart.pop()
#cart.pop()

#cart.iterate()




