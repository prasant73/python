# nested if - else block

"""
    Write the question
    sample i/p : 
    sample o/p : 
"""


def leap_year(year):
    if(year % 4 == 0):
        if (year % 100 == 0):
            if(year % 400 == 0):
                return ("leap")
            else:
                return ("not leap")
        else:
            return ("leap")
    else:
        return ("not leap")
# print(leap_year(int(input("Enter a year : "))))

def list_input(n):
    l = []
    for i in range(n):
        l.append(int(input("Enter year {} : ".format(i + 1))))
        print(l)
    return l

n = int(input("Enter the number of numbers you want as an input : "))
for i in list_input(n):
    print(i, leap_year(i))




# print(leap_year(int(input("Enter a year : "))))
# years = [] 
# [years.append(int(input("Enter year {} : ".format(i+1)))) for i in range(int(input("Enter the number of inputs you want to give : ")))]

# [print(int(input("Enter year {} : ".format(i+1))), leap_year(i)) for i in range(int(input("Enter the number of inputs you want to give : ")))]
# [print(i, leap_year(i)) for i in years]

# l = [] # list declaration
# n = int(input("enter the number of years you want to test : "))
# for i in range(n):
#     print(
#         leap_year(
#             int(
#                 input(
#                     "Enter year {} : ".format(i+1)
#                     )
#                 )
#             )
#         )






# for i in range(n):
#     l.append(int(input("enter year {} : ".format(i+1))))
#     print(l[i], l)

# for i in range(len(l)):
#     # n = input("y/n")
#     # if n == "y":
#     #     print(l[i] , leap_year(l[i]))
#     # else:
#     #     break
#     print(l[i] , leap_year(l[i]))



# # print(leap_year(int(input("enter year : "))))

# # def convert_to_int(a):
# #     return int(a)

# # n = input("enter the years you want to test separated by comma : ")
# # l = []
# # count = 0
# # for i in n:
# #     if i == ',':
# #         count +=1
# # i = 0
# # while(i < count +1):
# #     print(leap_year(convert_to_int(n.split(',')[i])))

# # l = []
# # n = int(input("Enter the number of years you want to test : "))

# # for i in range(n):
# #     l.append(int(input("enter year {} ".format(i+1))))
# #     print(l)

# # i = 0
# # while(i in  range(len(l))):
# #     print(i)
# #     i+=1 # i = i + 1
# # print("I a outside the loop",i)

# # for i in l: # working with the values
# #     print(i, leap_year(i))

# # for i in range(len(l)): # working with the indices
# #     print(l[i], leap_year(l[i]))

# # year = int(input("enter a year : "))
# # print(leap_year(year))


# # def convert_to_int(i):
# #     return int(i)

# # # l = []
# # s = input("enter the years separated by comma ")
# # # l = s.split(',')
# # # print(l)

# # # n = int(input("enter the number of years you want to test : "))
# # # for i in range(n):
# # #     l.append(int(input("Enter year {} ".format(i+1))))
# # #     print(l)

# # for i in s.split(','):
# #     print(i, type(i), leap_year(convert_to_int(i)))

# # def leap(year):
# #     if year % 4 == 0:
# #         if year % 100 == 0:
# #             if year % 400 == 0:
# #                 return "leap"
# #             else:
# #                 return "not leap"
# #         else:
# #             return "leap"
# #     else:
# #         return "not leap"

# # l = [] # list declaration
# # n = int(input("enter the number of years you want to test : "))
# # for i in range(n):
# #     l.append(int(input("Enter year {} ".format(i+1))))
# # print(l)

# # for i in l:
# #     print(i , leap(i))

# # while(i<n):
# #     l.append(int(input("enter year {} {} ".format(i+1, "hi"))))
# #     i+=1 # i = i+1

# # while(j<len(l)):
# #     print(l[j], leap(l[j]))
# #     j+=1

# # for i in range(n): # taking values as indices
# #     l.append(int(input("enter year {} ".format(i+1))))

# # print("entered years are {}".format(l))

# # for i in l: #having values as values itself
# #     print(i, leap(i))

# # year = int(input("enter a year"))
# # print(leap(year))


# finding the unique elements and the frequency of a character in a string
# def uniq_elem(d):
#     l = []
#     print(d)
#     for i in d:
#         if d[i] != 1:
#             pass
#         else:
#             l.append(d[i])
#     return l

# def freq_elem(l):
#     d = {}
#     print(l)
#     for i in l:
#         if i not in d:
#             d[i] = 1
#         else:
#             d[i] += 1
    
#     return d

# l = []
# n = int(input("enter the number of numbers : "))
# for i in range(n):
#     l.append(int(input("enter value at position {} ".format(i+1))))

# print(uniq_elem(freq_elem(l)))

# even_list = []
# odd_list = []
# for i in range(1,21):
#     if i%2 == 0:
#         even_list.append(i)
#     else:
#         odd_list.append(i)
# print("even_list : ", even_list, "odd_list : ", odd_list)

