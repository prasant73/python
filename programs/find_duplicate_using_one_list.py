def remove_duplicate(l, elem, index):
    for i in range(index + 1, len(l)):
        if l[i] == elem:
            a = l.pop(i)
    print(a)
    return l

def find_duplicate(l):
    for i in range(len(l) - 1):
        if l[i] in l[i+1 : len(l)] :
            print(l, l[i], i)
            return remove_duplicate(l, l[i], i)
    

l = [1,2,3,2]
print(find_duplicate(l))