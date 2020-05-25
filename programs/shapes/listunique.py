def listuniq(l,n,l1):
    l2=[]
    for i in range(0,n):
       c=1
       for j in range(i+1,n):
            if(l[i]==l[j]):
                c+=1
                l1[j]=0
       if(l1[i] != 0):
            l1[i] = c
    for i in range(0,n):
        if(l1[i]==1):
            l2.append(l[i])
    print(l2)
l=[]
l1=[]
n=int(input("Enter the limit"))
for i in range(0,n):
    a=int(input("Enter the element"))
    l1.append(-1)
    l.append(a)
listuniq(l,n,l1)
