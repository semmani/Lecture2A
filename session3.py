# print(_name_)


def square():
    num = 20
    print(">>num is",num)
def main():
    num = 10
    print(">> This is Main()")
    square() # square is called under main which will call sqaure()
    print(">> Square ends here")


if _name_ == "_main_":
    main() # this statement give the user to control whole functioning of program