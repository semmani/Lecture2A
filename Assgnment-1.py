"""
 Cyclic Rotation: Shift the elements of Multi Value Container A to the right with R shifts
A = [3, 8, 9, 7, 6]
R = 3
Output [9, 7, 6, 3, 8]
"""

A = [3, 8, 9, 7, 6]
R = 3
res = len(A)
ans = A[len(A)-R:len(A)]  # saves 3,2,1 from the backward in the ans and the prints the list of indices having values
print(ans)





# to be continued