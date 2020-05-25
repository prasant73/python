def add_val_dict(d1, d2):
    print(d1, '\n', d2)
    d = {}
    count = 0
    for i in d1:
        if i in d2: 
            d[i] = d1[i] + d2[i]
            print(count, d)
            count += 1
        else:
            d[i] = d1[i]
            print(count, d)
            count += 1
    for i in d2:
        if i in d:
            pass
        else:
            d[i] = d2[i]
            print(count, d)
            count += 1
    return d

d1 = {'a' : 100, 'b' : 200, 'c' : 300}
d2 = {'a' : 300, 'b' : 200, 'd' : 400}
print(add_val_dict(d1,d2))