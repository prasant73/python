''' 
     *
    ***
   *****
  *******
 ********* 
 *********
  *******
   *****
    ***
     * '''
def diamond(n):
    print ("Diamond")
    for i in range (0,n):
     print((n-i) * ' ' + (2*i+1) * '*'+(n-i) * ' ')
    for i in range (n,0,-1):
     print((n-i+1)* ' ' + (2*i-1) * '*'+(n-i) * ' ')
n=int(input("Enter limit"))
diamond(n)
