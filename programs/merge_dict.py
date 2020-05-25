import sys
def max_min_dict(d):
    print(d)
    max = sys.maxsize
    min = -sys.maxsize - 1
    for i in d : 
        if d[i] > min:
            min = d[i]
        if d[i] < max:
            max = d[i]
        print(d[i], min, max)
    return (max, min)





def sum_of_all_items_in_dict(d):
    sum = 0
    for i in d:
        sum = sum + d[i]
    return sum


def merge_two_dict(d1, d2):
    print(d1, d2)
    for i in d2 : 
        d1[i] = d2[i] 
    return d1


def dict_input(n):
    d = {}
    for i in range(n):
        d[input("Enter key {} : ".format(i+1))] = int(input("Enter value : "))
    return d


# print(
#     merge_two_dict
#     (dict_input(int(input("Enter number of elements for d1 : "))), 
#     dict_input(int(input("Enter number of elements for d2 : ")))
#     )
# )

print(max_min_dict({'2': 1, '3': 2, '4': 3, '5': 4, '6': 5}))

# print(dict_input(int(input("Enter the number of elements in the dictionary : "))))