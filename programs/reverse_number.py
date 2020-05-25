import cProfile

def rev_num(n):
    a = 0
    rev = 0
    while n != 0:
        a = n % 10
        rev = rev * 10 + a
        n = n // 10
    return rev

n = int(input("enter a number to be reversed "))
cProfile.run('rev_num(n)')
print("the reverse of {} is {}".format(n, rev_num(n)))