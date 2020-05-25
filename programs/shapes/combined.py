''' 
   *
  **
 ***
****
 ***
  **
   * 
'''
import cProfile
def pattern3(n):
    print ("Pattern C")
    for i in range (0,n+1,1):
     print((n-i) * ' ' + i * '*')
    for i in range (n-1,0,-1):
     print((n-i) * ' ' + i * '*')
n=int(input("Enter limit"))
cProfile.run('pattern3(n)')
