# max element of a list

# def max_element(a):
#     max = 0
#     count = 0
#     value_change = 0
#     for i in range(len(a)): 
#         count+=1
#         if a[i] > max:
#             value_change += 1
#             max = a[i]
#     return max, count, value_change
# a = [12,25,36,85,93,48,59,64,78]
# print(max_element(a)[1])

# def repetition(a):
#     d = dict() # d = {}
#     for i in a:
#         if i in d: # if d.has_key(i)
#             d[i] += 1 #{'a': 2}
#         else:
#             d[i] = 1 # {'a' : 1}
#     return d
#     '''
#     if the element is present inside the dictionary, increase the count by 1
#     if the element is not present inside the dictionary, make its count as 1
#     '''
# a = 'aakjfkahdlasdoqgbfgh'
# print(repetition(a))

# a = [12,23,35,46,58]
# b = ['a','b','c','d','e']
# {'a':12, 'b':23, 'c':35, 'd': 46, 'e': 58}
# d = {}
# for i in range(len(a)):
#     d[b[i]] = a[i] # d[b[i]]
#     print(b[i] , a[i])

# print(d)
# Input : 'Prashanth'
# O/P : {'P':1, 'r': 1, 'a':2, 'h':2,'n':1, 't':1}


# def func_name(l):
#     d = {}
#     print(l)
#     for i in l :
#         if i not in d: 
#             print("Inside if:  ","i is ",i)
#             d[i] = 1 # putting 'i' as key and 1 as value
#             print("d is ", d)
#         else:
#             print("Inside else:  ","i is ",i)
#             d[i] += 1 # putting 'i' as key and incrementing the value of the key by 1
#             print("d is ", d)
#     return d

# a = ['a', 'b', 'b', 'a', 'a',  'c']
# print(func_name(a))

# def count(a):
#     count = 0
#     for i in a : 
#         count += 1
#     print("length of the passed list is ", count)
#     if count < 5:
#         return True
#     else:
#         return False

# a = [1,2,3,4,5,6]
# b = [2,4,6,8]
# print(count(a[2:4]))
# print(count(b))



# '''
# Write a Python program 
# which accepts a sequence of comma-separated numbers from user 
# and generate a list 
# and a tuple with those numbers
# '''

# def generate_list_and_tuple_from_string(a):
#     t = tuple()
#     l = []
#     # print(type(t), type(l))
#     p = (a.split(','))
#     print(p, type(p))
#     return ( tuple(p), p )

# a = input("Enter some comma separated numbers : ")
# print(generate_list_and_tuple_from_string(a)[0], generate_list_and_tuple_from_string(a)[1])


'''
    write a program to 
    find the maximum non-negative value in a dictionary
'''

# the dict will have several key value pairs
# all the values will be integers/numericals
# you need to call a function with a dict as an argument
# the function will return the maximum value inside the dict
try:
    def return_max_value_from_dict(d):
        
        max = 0
        min = 1000000000000000000000000000000000000
        for i in d.keys():
            if max < d[i]:
                max = d[i]
            if min > d[i]:
                min = d[i]
            print(max, i, d[i])
            print(min, i, d[i])
        
        return max, min
except IndentationError as i:
    print (i)

dic = {'a':1, 'b': 2, 'c':3, 'd':2, 'e':9}
print(return_max_value_from_dict(dic))