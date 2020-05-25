import cProfile

def freq_char(s):
    d = {}
    for i in s : 
        if i not in d :  # if i in d.keys
            d[i] = 1 # adding key value pair inside a dictionary
        else:
            d[i] += 1 # updating the value of a particular key
        print(d)
    # return d
    print(d)

s = input("Enter the string : ")
cProfile.run("freq_char(s)")

# import sys

# def remove_highest_occuring_elem(l, elem, elem_freq):
#     print(l, elem, elem_freq)
#     for i in range(len(l)):
#         # print(i, l[i])
#         # l.remove(elem)
#         if l[-i-1] == elem:
#             l = l[:-1]
#         else:
#             l[i], l[len(l) - 1] = l[len(l) - 1], l[i]
#             l = l[:-1]
            
#             # for j in range(i, len(l) - 1):
#             #     l[j], l[j + 1] = l[j + 1], l[j]
#             #     l = l[:-1]
#     return l

# def highest_freq_elem(d):
#     big = -sys.maxsize - 1
#     big_elem_freq = 0
#     for i in d:
#         # print(i, d[i])
#         if d[i] > big_elem_freq:
#             big_elem = i
#             big_elem_freq = d[i]
#     return big_elem, big_elem_freq


# def freq(l):
#     d = {}
#     for i in l:
#         if i not in d:
#             d[i] = 1
#         else:
#             d[i] += 1
#     return d


# def list_input(n):
#     l = []
#     for i in range(n):
#         l.append(int(input("Enter number {} : ".format(i + 1))))
#     return l

# def main():
#     l = list_input(int(input("Enter number of elements : ")))
#     # print(highest_freq_elem(freq(l))[0])
#     # print(remove_highest_occuring_elem(l, highest_freq_elem(freq(l))[0]))
#     print(remove_highest_occuring_elem(l,highest_freq_elem(freq(l))[0], highest_freq_elem(freq(l))[1]))
# print("inside freq_char",__name__)
# if __name__ == "__main__":
#     main()