
# # [ output_expression() for(set of values to iterate) if(conditional filtering) ]\

def abc(a , b):
    print("inside abc")
    return a + b, a - b

print("addition and substraction of {} and {} is {} and {}".format(6, 4, abc(6,4)[0], abc(6,4)[1]))














# [x for x in range(100, 501) if (x % 400 == 0) or (x % 4 == 0 and not x % 100 == 0)]

# def leap(start, end):
#     return [x for x in range(start, end + 1) if (x % 400 == 0) or (x % 4 == 0 and not x % 100 == 0)]

# print(leap(4, 4001))

# l = []
# n = int(input("enter n : "))
# for i in range(n):
#     l.append(int(input("enter element {}".format(i+1))))
# print(l)

# a = set((input("enter the string : ")).split(","))
# print(type(a), a, len(a))
# for i in a : 
#     print(i, type(i))


# Convert a list of integers to a list of strings?

my_list = [0,1,2,3,4,5]

[str(x) for x in my_list]

# ['0', '1', '2', '3', '4', '5']


# get tuples from two lists with List Comprehensions

my_list1 =[0,1]
my_list2 =['zero','one']

[(x,y) for x in my_list1 for y in my_list2]
# [(0, 'zero'), (0, 'one'), (1, 'zero'), (1, 'one')]


# Get Index of Each Element of List with enumerate and List Comprehensions

my_list= ['a','b','c','d','e']
[(i,j) for (i,j) in enumerate(my_list)]
# [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd'), (4, 'e')]


# if statement in lis comprehensions
my_list = range(10)
my_list
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
['even' if i%2==0 else 'odd' for i in my_list]
# ['even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd']

# Nested Conditionals
[i for i in range(8) if i%2==0 if i%3==0]
# [0, 6]

# if..else in List Comprehension
["Even" if i%2==0 else "Odd" for i in range(8)]

# Nested list comprehensions
[[i*j for j in range(1,11)] for i in range(7,9)]