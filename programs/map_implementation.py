def addition(n): 
    return n + n 
  
# We double all numbers using map() 
# numbers = (1, 2, 3, 4) 
# result = map(addition, numbers) 
# # print(list(result)) 
# print(result)


def map_implementation(func, x):
    if type(x) == int:
        return func(x)
    elif(type(x) == list):
        l = []
        for i in x:
            l.append(func(x))

print(map_implementation(addition, [1,2,3,4,5]))