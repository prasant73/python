''' 
*
**
***
****
****
***
**
* '''
def pattern3(n):
    print ("Pattern C")
    for i in range (0,n):
     print( i * '*')
    for i in range (n-1,0,-1):
     print(i * '*')
n=int(input("Enter limit"))
pattern3(n)
