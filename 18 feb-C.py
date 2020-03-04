import numpy as np

chessBoard = np.zeros((8,8),dtype=int)

chessBoard[1::2,::2] = 1   # [1::2]--- means start from 1st index and go to every 2nd index(1,3,5,7);
# [::2]---> means start from 0th index and go to every 2nd index i.e(0,2,4,6)
chessBoard[::2,1::2] = 1  # this reverses the above process i.e (0 2 4 6)--->(1 3 5 7)


print(chessBoard)

def rowCheck(indices):

def colCheck():
    pass

def diagonalCheck():
    pass


index = []
for i in range(0,len(chessBoard)):
    print("where would you like to place the queen:{} ".format(i+1))
    row = int(input("Row: "))
    col = int(input("Col: "))

    if (row>=0 and row<=7) or (col>=0 and col<=7):
        chessBoard[row][col] = 9
    else:
        print("Please choose some Valid Row/Column")

    index.append([row, col])
print("Chessboard is---->\n")
print(chessBoard)
print("Queens placed at {}".format(index))

print(index[0])



