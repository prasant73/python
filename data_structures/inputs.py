def list_input(num):
    inputs = []
    for i in range(num):
        inputs.append(int(input("enter value {} : ".format(i+1))))
    return inputs


# def dict_input(n):
#     d = {}
#     for i in range(n):
#         ask_type_key = input("""Enter 'i' if you want the key in Integer
# Enter 's' if you want to take the input in String 
# """)
#         if ask_type_key == 'i':
#             a = int(input("Enter integer key : "))
#         else:
#             a = input("Enter string key")

#         ask_type_value = input("""Enter 'i' if you want the value in Integer
# Enter 's' if you want to take the value in String 
# """)
#         if ask_type_value == 'i':
#             b = int(input("Enter integer key : "))
#         else:
#             b = input("Enter string key")
#         b = input("enter value : ")
#         d[a] = b
#     return d
# print(dict_input(int(input("enter the numbe

print(list_input(int(input("enter the number of inputs you want (inside inputs.py) : "))))