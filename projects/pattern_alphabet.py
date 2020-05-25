def alphabet_a(n,pat):
    a=''
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i == 1:
                if(j==1) or(j==n):
                    a+=' '
                else:
                    a+=pat
            else:
                if(j==1) or (j==n):
                    a+=pat
                elif (i==(n+1)//2) and ((j>1) or (j<n)):
                    a+=pat

                else:
                    a+=' '
        a+='\n'

    print(a)

def alphabet_b(n,pat):
    b=''
    for i in range(1,n+1):
        for j in range(1,(n-1)):
            if (i==1) or (i==(n//2)+1) or (i==n):
                if j == n-2:
                    b+=' '
                else:
                    b+=pat
            else:
                if (j>1) and (j<(n-2)):
                    b+=' '
                else:
                    b+=pat

        b+='\n'
    print(b)

def alphabet_c(n,pat):
    c=''
    for i in range(1,n+1):
        for j in range(1,n):
           if (i==1) or (i==n):
               if j==1:
                   c+=' '
               else:
                   c+=pat
           else:
               if j==1:
                   c+=pat
               else:
                   c+=' '
        c+='\n'
    print(c)

def alphabet_d(n,pat):
    d=''
    for i in range(1,n+1):
        for j in range(1,n+1):
            if j==1:
                d+=pat

            else:
                if(i==1)or (i==n):
                   if j>(n//2):
                       d+=' '
                   else:
                        d+=pat
                elif(i==2)or(i==(n-1)):
                    if(j>1)and(j<(n//2)+1):
                        d+=' '
                    elif j==n-2:
                        d+=pat
                    else:
                        d+=' '
                else:
                    if j==n-1:
                        d+=pat
                    else:
                        d+=' '
        d+='\n'
    print(d)

def alphabet_e(n,pat):
    e=''
    for i in range(1,n+1):
        for j in range(1,n+1):
            if(j==1)or ((j<(n-1))and ((i==1)or(i==(n//2)+1)or(i==n))):
                e+=pat
            else:
                e+=' '
        e+='\n'
    print(e)

def alphabet_f(n,pat):
    f=''
    for i in range(1,n+1):
        for j in range(1,n+1):
            if(j==1)or ((j<(n-1))and ((i==1)or(i==(n//2)+1))):
                f+=pat
            else:
                f+=' '
        f+='\n'
    print(f)

def alphabet_g(n,pat):
    g=''
    for i in range(1,n+1):
        for j in range(1,n+1):
            if (((j==1)or(j==(n//2)+2)and (i!=n//2))and((i>1)and(i<n)))or((i==1)or(i==n))and(j>=2)and(j<=n-(n//2)) or(i==n-(n//2))and((j>2)and(j<=(n-n//2))):
                g+=pat
            else:
                g+=' '
        g+='\n'
    print(g)

def alphabet_h(n,pat):
    h=''
    for i in range(1,n+1):
        for j in range(1,n+1):
            if (j==1)or ((i==(n//2)+1) and (j<n))or (j==n):
                h+=pat
            else:
                h+=' '
        h+='\n'
    print(h)

def alphabet_i(n,pat):
    ii=''
    for i in range(1,n+1):
        for j in range(1,n+1):
            if(j==n//2)or(((i==1)or(i==n))and(j<=n-2)):
                ii+=pat
            else:
                ii+=' '
        ii+='\n'
    print(ii)

def alphabet_j(n,pat):
    jj = ''
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if ((j == (n-(n//2)))and (i<n)) or ((i == 1)  and (j>=2)and(j<=n-1)) or((i==n)and(j>=1)and(j<(n-(n//2))))or((i==n-1)and(j==1)):
                jj += pat
            else:
                jj += ' '
        jj += '\n'
    print(jj)

def alphabet_k(n,pat):
    k=''
    y=3
    z = n // 2 + 1
    for i in range(1,n+1):
        for j in range(1,n+1):
            x=n-(n//2)+2-i
            if(j==1)or (j==x):
                k+=pat
            elif (i>z)and(j==y):
                y=y+1
                z=z+1
                k+=pat
            else:
                k+=' '
        k+='\n'
    print(k)


def alphabet_l(n,pat):
    l=''
    for i in range(1,n+1):
        for j in range(1,n+1):
            if (j==1)or ((i==n)and(j>1)and(j<=n-2)):
                l+=pat
            else:
                l+=' '
        l+='\n'
    print(l)

def alphabet_m(n,pat):
    m=''
    for i in range(1,n+1):
        for j in range(1,n+1):
            k=(n+1)-i
            if (j==1)or (j==n):
                m+=pat
            elif (j==i)or (j==k):
                if i<=(n//2)+1:
                    m+=pat
                else:
                    m+=' '
            else:
                m+=' '
        m+='\n'
    print(m)

def alphabet_n(n,pat):
    nn=''
    for i in range(1,n+1):
        for j in range(1,n+1):
            if (j==1)or (j==n):
                nn+=pat
            elif j==i:
                nn+=pat
            else:
                nn+=' '
        nn+='\n'
    print(nn)

def alphabet_o(n,pat):
    o=''
    for i in range(1,n+1):
        for j in range(1,n+1):
            if (((j==1)or (j==(n-(n//2)+1)))and((i>1)and(i<n))) or (((i==1) or (i==n))and(j>=2) and (j<=n-(n//2))):
                o+=pat
            else:
                o+=' '
        o+='\n'
    print(o)

def alphabet_p(n,pat):
    p=''
    for i in range(1,n+1):
        for j in range(1,n+1):
            if j==1 or ((j>=2)and(j<=(n//2)+1)and(i==1))or ((i>1)and(i<=n//2)and(j==n-(n//2)+1))or(i==(n//2)+1)and(j>=2)and(j<=(n//2)+1):
                p+=pat
            else:
                p+=' '
        p+='\n'
    print(p)

def alphabet_q(n,pat):
    q=''
    for i in range(1,n+1):
        for j in range(1,n+1):
            if (((j==1))and((i>1)and(i<n))) or (((i==1) or (i==n))and(j>=2) and (j<=n//2))or(i==n-(n//2)+1)and (j==n//2) or(i==n)and(j==(n-1))or((j==n-(n//2)+1)and(i>1)and(i<n-1))or(j==n//2+1)and((i==n-1)or(i==1)):
                q+=pat
            else:
                q+=' '
        q+='\n'
    print(q)

def alphabet_r(n,pat):
    r=''
    for i in range(1,n+1):
        x=n//2
        y=n-(n//2)+1
        for j in range(1,n+1):
            if j==1 or ((j>=2)and(j<=(n//2)+1)and(i==1))or ((i>1)and(i<=n//2)and(j==n-(n//2)+1))or(i==(n//2)+1)and(j>=2)and(j<=(n//2)+1)or(j==(i-1)and i>n//2):
                r+=pat
            else:
                r+=' '
        r+='\n'
    print(r)


def alphabet_s(n,pat):
    s=''
    for i in range(1,n+1):
        for j in range(1,n+1):
            if ((i==1) or (i==n) or (i==(n//2)+1))and(j>=2) and (j<n-(n//2)):
                s+=pat
            elif ((j==1)and((i==n)or ((i>1)and(i<=n//2)))):
                s+=pat
            elif (j==n-(n//2))and ((i==1)or(i>(n//2)+1)and(i<n)):
                s+=pat

            else:
                s+=' '
        s+='\n'
    print(s)


def alphabet_t(n,pat):
    t=''
    for i in range(1,n+1):
        for j in range(1,n+1):
            if(i==1)or ((j==(n//2)+1)and(i<=n)):
                t+=pat
            else:
                t+=' '
        t+='\n'
    print(t)

def alphabet_u(n,pat):
    u=''
    for i in range(1,n+1):
        for j in range(1,n+1):
            if ((j==1)or (j==(n-(n//2))))and(i!=n):
                u+=pat
            if (i==n) and(j>=2) and (j<=n-(n//2)):
                u+=pat
            else:
                u+=' '
        u+='\n'
    print(u)

def alphabet_v(n, pat):
    v=''

    for i in range(1,n+1):
        k=(n*2)-i
        for j in range(1,n*2):
            if (j==i) or (j==k):
                v+=pat
            else:
                v+=' '
        v+='\n'
    print(v)

def alphabet_w(n,pat):
    w=''

    y=1
    for i in range(1,n+1):
        for j in range(1,(n*3)+1):
            # x=(n+1)-i
            x = (n * 3)+1 - i
            y=(2*n)-i
            z=n+1+i
            if i==j or (j==x)or(j==y)and(i>=n//2)and(y>=n) or(j==z)and (i>=n//2):
                w+=pat
                # y=y+1
                # x=x-1


            else:
               w+=' '
        w+='\n'
    print(w)


def alphabet_x(n, pat):
    x=''

    for i in range(1,n+1):
        k=(n+1)-i
        for j in range(1,n+1):
            if (j==i) or (j==k):
                x+=pat
            else:
                x+=' '
        x+='\n'
    print(x)

def alphabet_y(n,pat):
    x=''
    for i in range(1,n+1):
        k=(n+1)-i
        for j in range(1,n+1):
            if(j==i)or (j==k):
                if i >= (n//2) + 1:
                    if j > (n // 2) + 1:
                        x += ' '
                    else:
                        x+=pat
                else:
                    x+=pat

            else:
                x+=' '
        x+='\n'
    print(x)


def alphabet_z(n,pat):
    z=''
    for i in range(1,n+1):
        for j in range(1,n+1):
            k=(n+1)-i
            if(i==1)or (i==n)or(j==k):
                z+=pat
            else:
                z+=' '
        z+='\n'
    print(z)


n=7
pat=input("enter the pattern:")

list_of_patterns = []

alphabet_a(n,pat)
alphabet_b(n,pat)
alphabet_c(n,pat)
alphabet_d(n,pat)
alphabet_e(n,pat)
alphabet_f(n,pat)
alphabet_g(n,pat)
alphabet_h(n,pat)
alphabet_i(n,pat)
alphabet_j(n,pat)
alphabet_k(n,pat)
alphabet_l(n,pat)
alphabet_m(n,pat)
alphabet_n(n,pat)
alphabet_o(n,pat)
alphabet_p(n,pat)
alphabet_q(n,pat)
alphabet_r(n,pat)
alphabet_s(n,pat)
alphabet_t(n,pat)
alphabet_u(n,pat)
alphabet_v(n,pat)
alphabet_w(n,pat)
alphabet_x(n,pat)
alphabet_y(n,pat)
alphabet_z(n,pat)



# alphabet=[alphabet_a,
#           alphabet_b,
#           alphabet_c,
#           alphabet_d,
#           alphabet_e,
#           alphabet_f,
#           alphabet_g,
#           alphabet_h,
#           alphabet_i,
#           alphabet_j,
#           alphabet_k,
#           alphabet_l,
#           alphabet_m,
#           alphabet_n,
#           alphabet_o,
#           alphabet_p,
#           alphabet_q,
#           alphabet_r,
#           alphabet_s,
#           alphabet_t,
#           alphabet_u,
#           alphabet_v,
#           alphabet_w,
#           alphabet_x,
#           alphabet_y,
#           alphabet_z]
# n1=input("Enter the alphabet you want to be print: ")
# pat=input("enter the pattern:")
# num=ord(n1)
# if(num>=97)and(num<=122):
#     num=num-32
# print(num)
# num1=[65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90]
# for i in range(len(num1)):
#     if(num==num1[i]):
#         num2=i
#         # print(i)
# for j in range(len(alphabet)):
#     if(i+1==j):
#         # alphabet_r(n,pat)
#         print(i)
#

