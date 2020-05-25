from inputs import list_input

def add_list_to_dict(l1,l2):
    d = {}
    # for i in range(len(l2)):
    #     d[l1[i]] = l2[i]
    # print(i)
    # for i in range(i+1, len(l1)):
    #     d[l1[i]] = 0
    # return d

    for i in range(len(l1)):
        if i < len(l2):
            d[l1[i]] = l2[i]
        else:
            d[l1[i]] = 0
    return d

def  make_dict_by_2_list(l1, l2):
    if len(l1)  > len(l2):
        return(add_list_to_dict(l1, l2))
    else:
        return(add_list_to_dict(l2, l1))

# l1 = ['a','b','c','d', 'e', 'f']
# l2 = [1,2,3,4]
l1 = list_input(int(input("enter the length you want : ")))
l2 = list_input(int(input("enter the length you want : ")))
print(make_dict_by_2_list(l1, l2))

