'''
    What are decorators in Python?
    Python has an interesting feature called decorators to add functionality to an existing code.

    This is also called metaprogramming as a part of the program tries to modify another part of the program at compile time.
'''

'''
    Everything in Python (Yes! Even classes), are objects. 
    Names that we define are simply identifiers bound to these objects. 
    Functions are no exceptions, they are objects too (with attributes). 
    Various different names can be bound to the same function object.
'''

# def first(msg):
#     print(msg)    

# first("Hello")

# second = first
# second("Hello")

"""Functions can be passed as arguments to another function.

If you have used functions like map, filter and reduce in Python, 
then you already know about this.

Such function that take other functions as arguments are also called higher order functions. 
Here is an example of such a function.
"""

# def inc(x):
#     return x + 1

# def dec(x):
#     return x - 1

# def operate(func, x):
#     result = func(x)
#     return result

# list_of_functions = [inc, dec]

# for i in list_of_functions:
#     print("calling ", i)
#     print(operate(i, 
#                 int(input("enter the number to be passed : "))
#                 ))

# print(operate(inc, 3))
# print(operate(dec, 3))


'''
    >>> operate(inc,3)
    4
    >>> operate(dec,3)
    2
'''

# a function can return another function.

# def is_returned():
#     print("Hello")
#     return 1
# # closures
# def is_called():
#     print("inside is_called")
#     def is_returned():
#         print("Hello")
#         return 1 # is_returned = 1
#     return is_returned

# new = is_called() # (is_called())() # new = is_returned
# print(new, new()) # new -> is_returned,  new() -> is_returned() 
# print(new())
# # Outputs "Hello"
# new()

'''
Here, is_returned() is a nested function which is defined and returned, 
each time we call is_called().

Functions and methods are called callable as they can be called.

In fact, any object which implements the special method __call__() is termed callable. 
So, in the most basic sense, a decorator is a callable that returns a callable.

Basically, a decorator takes in a function, adds some functionality and returns it.'''


# def make_pretty(func): # func = ordinary
#     def inner():
#         print("I got decorated")
#         return func()
#     return inner

# def ordinary():
#     print("I am ordinary")
#     return 1

# ordinary()
# pretty = make_pretty(ordinary) # pretty = inner()
# print(pretty())
# pretty()
# print(pretty.__call__()) # preety()

'''
When you run the following codes in shell,

>>> ordinary()
I am ordinary

>>> # let's decorate this ordinary function
>>> pretty = make_pretty(ordinary)
>>> pretty()
I got decorated
I am ordinary

'''

'''
In the example shown above, make_pretty() is a decorator. In the assignment step.

pretty = make_pretty(ordinary)

The function ordinary() got decorated and the returned function was given the name pretty.

We can see that the decorator function added some new functionality to the original function. This is similar to packing a gift. The decorator acts as a wrapper. The nature of the object that got decorated (actual gift inside) does not alter. But now, it looks pretty (since it got decorated).

Generally, we decorate a function and reassign it as,

ordinary = make_pretty(ordinary).
This is a common construct and for this reason, Python has a syntax to simplify this.

We can use the @ symbol along with the name of the decorator function and place it above the definition of the function to be decorated. For example,
 '''

# def make_pretty(func):
#     def inner():
#         print("I got decorated")
#         return func()
#     return inner

# @make_pretty
# def ordinary():
#     print("I am ordinary")
#     return 1

# print(ordinary())

# is equivalent to

# def ordinary():
#     print("I am ordinary")
# ordinary = make_pretty(ordinary)

# print(ordinary.__call__())
# This is just a syntactic sugar to implement decorators.

# # Decorating Functions with Parameters
# # The above decorator was simple and it only worked with functions that did not have any parameters. What if we had functions that took in parameters like below?

# def divide(a, b):
#     return a/b


'''
This function has two parameters, a and b. We know, it will give error if we pass in b as 0.

>>> divide(2,5)
0.4
>>> divide(2,0)
Traceback (most recent call last):
...
ZeroDivisionError: division by zero
'''

# Now let's make a decorator to check for this case that will cause the error.

# def smart_divide(func):
#    def inner(a,b):
#       print("I am going to divide",a,"by",b)
#       if b == 0:
#         print("Whoops! cannot divide")
#         return
#       return func(a,b)
#    return inner

# @smart_divide
# def divide(a,b):
#     return a/b

# a = int(input("Enter a : "))
# b = int(input("Enter b : "))

# print(divide(a, b))
# divide = smart_divide(divide)
# divide = inner
# print(divide(a,b))

# print(divide(a, b))

'''
This new implementation will return None if the error condition arises.

>>> divide(2,5)
I am going to divide 2 and 5
0.4

>>> divide(2,0)
I am going to divide 2 and 0
Whoops! cannot divide
In this manner we can decorate functions that take parameters.

A keen observer will notice that parameters of the nested inner() function inside the decorator is same as the parameters of functions it decorates. Taking this into account, now we can make general decorators that work with any number of parameter.

In Python, this magic is done as function(*args, **kwargs). In this way, args will be the tuple of positional arguments and kwargs will be the dictionary of keyword arguments. An example of such decorator will be.
'''
# def works_for_all(func):
#     def inner(*args, **kwargs):
#         print("I can decorate any function")
#         return func(*args, **kwargs)
#     return inner

'''
Chaining Decorators in Python
Multiple decorators can be chained in Python.

This is to say, a function can be decorated multiple times with different (or same) decorators. We simply place the decorators above the desired function.
'''

def star(func):
    def inner(*args, **kwargs): # (2,3,4, "a" : 5, "b": 6)
        print("*" * 30)
        func(*args, **kwargs) # -> output of percent(printer)
        print("*" * 30)
    return inner

def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner

@star
@percent
def printer(msg):
    print(msg)

printer("Hello")

# printe = star(percent(printer))
# print(printe)

# printer = percent(star(printer))

# printer = percent(printer)
# printer = star(percent(printer))

'''
This will give the output.


******************************
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
Hello
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
******************************
'''

'''
The above syntax of,

@star
@percent
def printer(msg):
    print(msg)
is equivalent to

def printer(msg):
    print(msg)
printer = star(percent(printer))
'''

'''
The order in which we chain decorators matter. If we had reversed the order as,

@percent
@star
def printer(msg):
    print(msg)
The execution would take place as,

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
******************************
Hello
******************************
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
'''

import time

# def timeit(method):
#     def timed(*args, **kw):
#         ts = time.time()
#         result = method(*args, **kw)
#         te = time.time()
#         print(result, te - ts)
#         # print ('%r  %2.2f ms' % (method.__name__, (te - ts) * 1000000))
#         # if 'log_time' in kw:
#         #     name = kw.get('log_name', method.__name__.upper())
#         #     kw['log_time'][name] = int((te - ts) )
#         # else:
#         #     print ('%r  %2.2f ms' % (method.__name__, (te - ts) * 1000))
#     return timed

# @timeit
# def get_all_employee_details(*args,**kwargs):
#     print ('employee details : ', args, kwargs)
#     return 1

# get_all_employee_details(4, 5 , a = 2, b = 3)

'''
Adding decorator to the method

@timeit
def get_all_employee_details(**kwargs):
    print 'employee details'
The code will look like this after removing the redundant code.

logtime_data ={}
employees = Employee.get_all_employee_details(log_time=logtime_data)
'''



'''
basic schema of a decorator

def outer(func):
    def inner(a,b):
        ...
        ...

        return func(a,b)
    return inner
'''