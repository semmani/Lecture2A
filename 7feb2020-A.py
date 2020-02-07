print("This is Session19")
print("Session19__name__is:",__name__) # __name__ will aways tell that it is under _main_
def fun():
    print("This is session 19")

class CA:
    def __init__(self):
        print("CA OBJECT IS CONSTRUCTED IN SESSION19")

def main():
    print("THIS IS FUN IN Session19")
    print("Session 19__name__ is:",__name__)

    fun()
    cREF = CA()

if __name__ == "main":
    main()

