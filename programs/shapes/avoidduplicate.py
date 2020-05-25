import cProfile
def listonce(l,n):
    f=0
    l2=[]
    print("List after finding repeated elements only once")
    for i in range(0,n):
       a=l[i]
       c=0
       for j in range(i+1,n):
            if(a==l[j]):
                c+=1
       if(c==0):
            l2.append(l[i])
    print(l2)
l=[]
n=int(input("Enter the limit : "))
for i in range(0,n):
    a=int(input("Enter the element : "))
    l.append(a)

cProfile.run('listonce(l,n)')