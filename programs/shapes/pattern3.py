''' 
   *
  **
 *** '''
def pattern3(n):
    print ("Pattern C")
    for i in range (0,n+1,1):
     print((n-i) * ' ' + i * '*')
n=int(input("Enter limit"))
pattern3(n)
