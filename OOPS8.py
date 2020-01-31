# IN PYTHON ,Overloading is not supported

class CA:
    def __init__(self):
        print(">> CA is initialized")

    def __init__(self,num):
        print("CA is constructed and num is:",num)

cRef1 = CA(10) #WHEN RUN IT WORKS FOR SECOND INIT NOT FOR FIRST ONE
# OVERLOADING NOT SUPPORTED


