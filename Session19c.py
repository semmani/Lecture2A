"""
import Package1.FILE1  # IMPORTING THE PACKAGE HERE, WE CAN SELECTIVLY IMPORT PACKAGE AS IN ONLY IMPORT SHOW METHOD ONLY

Package1.FILE1.fun()
Package1.FILE1.show()
ref1 = Package1.FILE1.CA()


"""
# using 2nd way of importing Package1
import Package1.FILE1 as o
o.show()
o.fun()

ref1 = o.CA()