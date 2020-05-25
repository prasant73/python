def demo(n):
    print ("Diamond inside square")
    k=n
    for i in range (n,0,-1):
     print( i * '*'+(n-k)*' '+i*'*')
     k-=2
    k=2*n-2 
    for i in range (0,n,):
      print((i+1) * '*'+(k)*' '+(i+1)*'*')
      k-=2
n=int(input("Enter the limit"))
demo(n)
