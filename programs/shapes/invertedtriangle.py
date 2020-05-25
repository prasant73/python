''' 
*********
 *******
  *****
   ***
    * '''
def pattern4(n):
    print ("Inverted Triangle")
    for i in range (n,0,-1):
     print((n-i)* ' ' + (2*i-1) * '*'+(n-i) * ' ')
n=int(input("Enter limit"))
pattern4(n)
