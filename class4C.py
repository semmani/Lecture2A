"""
  fUNCTIONS--> called as Routines/ Methods
  COMPONENTS----
  NAME
  INPUTS-- MAY  OR MAY NOT BE THERE / CALLED AS PARAMETERS OR ARGUMENTS
  RETURN STATEMENT--->OPTIONAL (TO RETURN SOME DATA ELSE ACTS AS ACKNOWLEDGEMENT)
  DEFINITION-->WHAT FUNCTIONS SHOULD DO?
  GROUP OF STATEMENTSOR LOFIC WHICH HAS TO BE EXECUTED;
  WE CAN PROVIDE DIFFERENT INPUTS AND GET OUTPUT ACCORDINGLY


  LOOPS-->
     EXECUTE IN SQUENCE FROM 0 TO N-1 OR ANY RANGE;

"""
paneer = 50
roti = 50


def bill(n1,n2):
#def bill(n1=0,n2=0)
#def bill(n1,n2=0)
#def bill(n1=0,n2)--->bill(10)---will provide error bcoz values refer left to rgt hence values coincide hence error, so above code should be used
#def bill(n1,n2=0,n3=0)--->okk, but n1=0 won't work again even if there are three arguments
    sum = n1+n2
    return sum

print(">>bill1 is :",bill(paneer,roti))
print(">>bill2 is:",bill()) # error as no n1, n2 is given hence provide(paneer = 0,roti =0) then it will give 0 simple
#print(">>bill3 is :",bill(n1=paneer,n2=roti))# another format in python to print bill of selective eatables or inputs
#print(">>bill4",bill(10))# puts 10 in n1