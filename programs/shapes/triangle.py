''' 
     *
    ***
   *****
  *******
 ********* '''
def pattern4(n):
    print ("Triangle")
    for i in range (0,n):
     print((n-i) * ' ' + (2*i+1) * '*'+(n-i) * ' ')
n=int(input("Enter limit"))
pattern4(n)
