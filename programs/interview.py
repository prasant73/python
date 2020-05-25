# from math import ceil

# def isPrime(num):
#     count = 0
#     if num == 1:
#         return "Not Prime"
#     else:
#         for i in range(1, ceil(num/2)):
#             if num % i == 0 :
#                 count += 1
#             if count == 2:
#                 return "Not Prime"
#     return "Prime"

# print(isPrime(int(input("Enter a number : "))))


"""
*0
**00
***000
****0000
"""

# def print_pattern(n):
#     for i in range(1, n +1):
#         print(i * "*", i * "0", sep = "")

# print_pattern(10)

# for i in dir(dict):
#     print(i)

"""
input : kiran REDDY
output : kRiErDaDnY
"""
def build_pattern(f_Str, s_Str):
    rem_str = ""
    for i in range(len(f_Str)):
        rem_str = rem_str + f_Str[i] + s_Str[i]
    return rem_str

def alt_pattern(s):
    rem_str = ""

    if len(s.split()) == 2:
        f_Str = s.split()[0]
        s_Str = s.split()[1]
        if len(f_Str) >= len(s_Str):
            rem_str = build_pattern(s_Str, f_Str)
            rem_str = rem_str + f_Str[len(s_Str):]
        elif len(f_Str) < len(s_Str):
            rem_str = build_pattern(f_Str, s_Str)
            rem_str = rem_str + s_Str[f_Str:]
    else:
        return "length must be 2"
    return rem_str


print(alt_pattern(input()))
