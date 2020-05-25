# def longestEvenWord(sentence):
#     words = sentence.split()
#     if (len(words) == 1) and (len(words[0]) % 2 != 0):
#         return "00"
#     else:
#         word1, len_word = words[0], len(words[0])
#     for i in range(len(words)):
#         if (len(words[i]) % 2 == 0) and (len(words[i]) > len_word) :
#             word1 = words[i]
#             len_word = len(words[i])
#     return word1

# print(longestEvenWord("Time To write great code"))





# import re

# st = """unicomp6.unicomp.net - - [01/Jul/1995:00:00:06 -0400] "GET /shuttle/countdown/ HTTP/1.0" 200 3985"""
# for i in str.split():
#     print(i)
# l = st.split()
# l[3] = l[3] + l[4]
# l[4] = l[5] + l[6] + l[7]
# l[5] = l[8]
# l[6] = l[9]
# l = l[:6]
# print(l)
 
# filename = input()
# def read_input_from_file(filename):
#     filename = filename.split(".")[0]
#     with open("bytes" + filename, "w") as f:
# filename = input()
# def return_file(filename):
# f = open(filename, "r")
# inputs = f.readlines()
# f.close()
# count = 0
# sum_of_bytes = 0
# for i in inputs:
#     if int(i.split()[-1]) > 5000:
#         count += 1
#         sum_of_bytes = sum_of_bytes + int(i.split()[-1])
# with open("bytes_" + filename.split(".")[0] + ".txt" , "w") as f:
#     f.write(str(count))
#     f.write("\n")
#     f.write(str(sum_of_bytes))
#     f.write("\n")





# print(int(input("Enter a : ")) + int(input("Enter b : ")))
# print(sum(int(x) for x in input("Enter 2 integers separated by space : ").split()))

def add_num(a, b): # a, b are the local variables, parameters or instance variables
    return a + b

def sub_num(a, b):
    if a > b : 
        return a - b
    else:
        return b - a

a = int(input("Enter a : ")) # global variable declaration
b = int(input("Enter b : "))

print(add_num(a, b), sub_num(a, b)) # argument to the function add_num\



# Enter your code here. Read input from STDIN. Print output to STDOUT
"""
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

"""

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

# class Solution:
#     def merge(self, intervals: List[Interval]) -> List[Interval]:
        # add code here

def merge_overlapping_intervals(input_list):
    l = []
    for itv in input_list:
        # print (itv.start, itv.end)
        if not l:
            l.append([itv.start, itv.end])
        else:
            for i in l:
                if itv.start in range(i[0], i[1] + 1):
                    i[1] = itv.end
                else:
                    l.append([itv.start, itv.end])
                # print(l)
    return l
# [[1,3],[2,6],[8,10],[15,18]]
    
a = Interval(1,3)
b = Interval(5,6)
c = Interval(2,4)
input_list = [a, b, c]
print(merge_overlapping_intervals(input_list))