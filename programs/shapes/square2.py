def square2(n):
    print ("Vertical line")
    for i in range (0,n):
     if(i==1 or i==n-2):
       print("*"+(n-2)*' '+"*")
     else:
      print(n * '*')
n=int(input("Enter limit"))
square2(n)