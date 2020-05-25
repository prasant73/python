''' 
  



 ********* 
 
 
 
  '''
def diamond(n):
    print ("Horizontal line")
    for i in range (0,n):
        if(i==n-1):
            print((n-i) * ' ' + (2*i+1) * '*'+(n-i) * ' ')
        else:
            print(i*' ')
    for i in range (n,0,-1):
     print(i*' ')
n=int(input("Enter limit"))
diamond(n)
