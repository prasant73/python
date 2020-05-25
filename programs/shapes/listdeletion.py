def listdeletion(l,n,dele):
    print(l)
    f=0
    for i in range(0,n):
        if(l[i]==dele):
            pos=i
            f=1
    if(f==0):
        print("Element not present")
    else:
        for i in range(pos,n-1):
            l[i]=l[i+1]
    print(l[0:n-1])
l=[]
n=int(input("Enter the limit"))
for i in range(0,n):
    a=int(input("Enter the element"))
    l.append(a)
dele=int(input("Enter the element to be deleted"))
listdeletion(l,n,dele)

