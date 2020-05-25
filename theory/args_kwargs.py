"""
>>> def abc(*args, **kwargs):
...     print(args, kwargs)
...
>>> abc(1,2,3, a = 0, b = 1)
(1, 2, 3) {'a': 0, 'b': 1}
>>> def abc(*args, **kwargs):
...     for i in args:
...             print(i, "args")
...     for i in kwargs:
...             print(i, kwargs[i])
...
>>> abc(1,2,3,4,5,6,7,a=8,b=9,c = [1,2,3,4,5,6,7])
1 args
2 args
3 args
4 args
5 args
6 args
7 args
a 8
b 9
c [1, 2, 3, 4, 5, 6, 7]
>>>
"""