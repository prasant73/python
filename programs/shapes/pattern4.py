''' 
*****
 ****
  ***
   **
    * '''

def pattern4(n):
    print ("Pattern Cw")
    for i in range (n,0,-1):
     print((n-i) * ' ' + i * '*')
n=int(input("Enter limit"))
pattern4(n)
