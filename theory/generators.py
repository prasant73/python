'''
    What are generators in Python?
    There is a lot of overhead in building an iterator in Python; 
    we have to implement a class with __iter__() and __next__() method, 
    keep track of internal states, raise StopIteration when there was no values to be returned etc.

    This is both lengthy and counter intuitive. Generator comes into rescue in such situations.

    Python generators are a simple way of creating iterators. 
    All the overhead we mentioned above are automatically handled by generators in Python.

    Simply speaking, a generator is a function that returns an object (iterator) 
    which we can iterate over (one value at a time).
'''

'''
    How to create a generator in Python?
    It is fairly simple to create a generator in Python. 
    It is as easy as defining a normal function with yield statement instead of a return statement.

    If a function contains at least one yield statement (it may contain other yield or 
    return statements), it becomes a generator function. Both yield and return will 
    return some value from a function.

    The difference is that, while a return statement terminates a function entirely, 
    yield statement pauses the function saving all its states and later continues 
    from there on successive calls.
'''

'''
    Differences between Generator function and a Normal function
    Here is how a generator function differs from a normal function.

    1. Generator function contains one or more yield statement.
    2. When called, it returns an object (iterator) but does not start execution immediately.
    3. Methods like __iter__() and __next__() are implemented automatically. 
       So we can iterate through the items using next().
    4. Once the function yields, the function is paused and the control is transferred 
       to the caller.
    5. Local variables and their states are remembered between successive calls.
    6. Finally, when the function terminates, StopIteration is raised automatically 
       on further calls.
'''

#A simple generator function
# def my_gen():
#     n = 1
#     print('This is printed first')
#     # Generator function contains yield statements
#     yield n

#     n += 1
#     print('This is printed second')
#     yield n

#     n += 1
#     print('This is printed at last')
#     yield n

# a = my_gen()

# # print(my_gen())
# # print(my_gen())
# # print(my_gen())

# print("first", next(a))
# print("second", next(a))
# print("third", next(a))
# print(next(a))
'''
    >>> # It returns an object but does not start execution immediately.
    >>> a = my_gen()

    >>> # We can iterate through the items using next().
    >>> next(a)
    This is printed first
    1
    >>> # Once the function yields, the function is paused and the control is transferred 
        to the caller.

    >>> # Local variables and theirs states are remembered between successive calls.
    >>> next(a)
    This is printed second
    2

    >>> next(a)
    This is printed at last
    3

    >>> # Finally, when the function terminates, StopIteration is raised automatically on further calls.
    >>> next(a)
    Traceback (most recent call last):
    ...
    StopIteration
    >>> next(a)
    Traceback (most recent call last):
    ...
    StopIteration
'''

'''
    One interesting thing to note in the above example is that, the value of variable n 
    is remembered between each call.

    Unlike normal functions, the local variables are not destroyed when the function yields. 
    Furthermore, the generator object can be iterated only once.

    To restart the process we need to create another generator object using something like 
    a = my_gen().

    Note: One final thing to note is that we can use generators with for loops directly.

    This is because, a for loop takes an iterator and iterates over it using next() function. 
    It automatically ends when StopIteration is raised.
'''

# A simple generator function

# def my_gen():
#     n = 1
#     print('This is printed first')
#     # Generator function contains yield statements
#     yield n

#     n += 1
#     print('This is printed second')
#     yield n

#     n += 1
#     print('This is printed at last')
#     yield n

# # Using for loop
# for item in my_gen():
#     print(item)    

# a = my_gen()

# print(next(a))
# print(next(a))
# print(next(a))


'''
    Python Generators with a Loop
    The above example is of less use and we studied it just to get an idea of what was 
    happening in the background.

    Normally, generator functions are implemented with a loop having a suitable terminating condition.

    Let's take an example of a generator that reverses a string.
'''

# def rev_str(my_str):
#     length = len(my_str)
#     for i in range(length):
#         yield my_str[i]

# def rev_str():
#     my_str = "lavanya"
#     for i in my_str[::-1]:
#         yield i

# a = rev_str()
# while True:
#     try:
#         p = input("enter y/N")
#         if p == 'y':
#             print(a.__next__())
#     except StopIteration:
#         break
# length - 1,-1,-1

# for char in rev_str("hello"):
#      print(char)

# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# a = my_gen()
# print(next(a))
# print(next(a))
# print(next(a))

# For loop to reverse the string
# Output:
# o
# l
# l
# e
# h
'''
    In this example, we use range() function to get the index in reverse order using the for loop.

    It turns out that this generator function not only works with string, 
    but also with other kind of iterables like list, tuple etc.
'''

'''
    Python Generator Expression
    Simple generators can be easily created on the fly using generator expressions. 
    It makes building generators easy.

    The syntax for generator expression is similar to that of a list comprehension in Python. 
    But the square brackets are replaced with round parentheses.

    The major difference between a list comprehension and a generator expression is that 
    while list comprehension produces the entire list, generator expression produces 
    one item at a time.

    They are kind of lazy, producing items only when asked for. 
    For this reason, a generator expression is much more memory efficient than an 
    equivalent list comprehension.
'''

# # Initialize the list
# my_list = [1, 3, 6, 10]

# # square each term using list comprehension
# # Output: [1, 9, 36, 100]
# [x**2 for x in my_list]

# # same thing can be done using generator expression
# # Output: <generator object <genexpr> at 0x0000000002EBDAF8>
# (x**2 for x in my_list)


# We can see above that the generator expression did not produce the required result immediately. 
# Instead, it returned a generator object with produces items on demand.

# Intialize the list
# my_list = [1, 3, 6, 10, 15]

# a = (x**2 for x in my_list)
# # Output: 1
# print(next(a))

# # Output: 9
# print(next(a))

# # Output: 36
# print(next(a))

# # Output: 100
# print(next(a))

# # Output: StopIteration
# print(next(a))

# Generator expression can be used inside functions. When used in such a way, 
# the round parentheses can be dropped.

'''
    >>> sum(x**2 for x in my_list)
    146

    >>> max(x**2 for x in my_list)
    100
'''

'''
    Why generators are used in Python?
    There are several reasons which make generators an attractive implementation to go for.

    1. Easy to Implement
    Generators can be implemented in a clear and concise way as compared to their iterator class 
    counterpart. Following is an example to implement a sequence of power of 2's 
    using iterator class.
'''

# class PowTwo:
#     def __init__(self, max = 0):
#         self.max = max

#     def __iter__(self):
#         self.n = 0
#         return self

#     def __next__(self):
#         if self.n > self.max:
#             raise StopIteration

#         result = 2 ** self.n
#         self.n += 1
#         return result
# a = PowTwo(5)
# a.__iter__()
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())

# # lets do the same using a generator function.

# def PowTwoGen(max = 0):
#     n = 0
#     while n < max:
#         yield 2 ** n
#         n += 1

# Since, generators keep track of details automatically, 
# it was concise and much cleaner in implementation.

'''
    2. Memory Efficient
    A normal function to return a sequence will create the entire sequence in memory 
    before returning the result. This is an overkill if the number of items in the sequence 
    is very large.

    Generator implementation of such sequence is memory friendly and is preferred since 
    it only produces one item at a time.

    3. Represent Infinite Stream
    Generators are excellent medium to represent an infinite stream of data. 
    Infinite streams cannot be stored in memory and since generators produce 
    only one item at a time, it can represent infinite stream of data.

    The following example can generate all the even numbers (theortically at least).
'''

# def all_even():
#     n = 0
#     while True:
#         yield n
#         n += 2

'''
    4. Pipelining Generators
    Generators can be used to pipeline a series of operations. This is best illustrated 
    using an example.

    Suppose we have a log file from a famous fast food chain. The log file has a column 
    (4th column) that keeps track of the number of pizza sold every hour and we want to 
    sum it to find the total pizzas sold in 5 years.

    Assume everything is in string and numbers that are not available are marked as 'N/A'. 
    A generator implementation of this could be as follows.
'''

# with open('sells.log') as file:
#     pizza_col = (line[3] for line in file)
#     per_hour = (int(x) for x in pizza_col if x != 'N/A')
#     print("Total pizzas sold = ",sum(per_hour))

# from sys import getsizeof
# value = int(input("Enter range : "))
# list_values = [x*2 for x in range(value)]
# gen_values = (x*2 for x in range(value))
# print(list_values)
# print(getsizeof(list_values), getsizeof(gen_values))


# unpack operator -> can unpack any iterable
# numbers = [1,2,3]
# print(*numbers)

# values = list(range(5))
# print(values, *values, *range(10), *"hello")  

# first = [x for x in range(4)]
# second = [x for x in range(6)]
# values = [*first, "a", *second]   
# # values = [*(range(5))]
# print(values)

# first = {chr(x):x for x in range(65,71)}
# second = {chr(x):x for x in range(75,81)}
# combined = {**first, **second, "z" : 1}
# print(combined)
# print(dict(**first, **second))


# def find_freq(s):
#     char_freq = {}
#     for i in s:
#         if i not in char_freq:
#             char_freq[i] = 1
#         else:
#             char_freq[i] += 1
#     return char_freq
# # print(find_freq(input("Enter a string : ")))

# print(sorted(
#     find_freq(input("Enter a string : ")).items(), 
#     key = lambda kv : kv[1], 
#     reverse = True)[0])


