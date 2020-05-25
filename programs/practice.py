# # # def permutations(s):
# # #     if len(s) == 1:
# # #         return s

# # #     recursive_perms = []
# # #     for c in s:
# # #         for perm in permutations(s.replace(c,'',1)):
# # #             recursive_perms.append(c+perm)

# # #     return set(recursive_perms)

# # # print(permutations(input("Enter an input : ")))


# # # my_dict = {'A':['D','E'],'B':['F','G','H'],'C':['I','J']}
# # # res = [[]]
# # # for _, vals in my_dict.items():
# # #     res = [x+[y] for x in res for y in vals]
# # # print(res)




# # # sum and product of a number

# # # def sum_prod_num(n):
# # #     n_in_int = int(n) # n is string, n_in_int is integer
# # #     sum1 = 0
# # #     prod = 1
# # #     for i in range(len(n)):
# # #         print(i, type(i))
# # #         sum1 = sum1 + (n_in_int % 10)
# # #         prod = prod * (n_in_int % 10)
# # #         n_in_int = n_in_int // 10
# # #     return sum1, prod

# # # n = input("enter a number : ")
# # # print(type(n))
# # # print(sum_prod_num(n))



# # # def bubbleSort(arr):
# # #     n = len(arr)
# # #     for i in range(n):
# # #         for j in range(0, n-i-1):
# # #             if arr[j] > arr[j+1] :
# # #                 arr[j], arr[j+1] = arr[j+1], arr[j]
# # #     return arr

# # # print(bubbleSort([int(input("Enter the number {} : ".format(i+1))) for i in range(int(input("Enter the number of elements you want as input")))]))




# # # ordereddict, frozenset

# # # def calc(a,b):
# # #     print('ab')
# # #     return a+b, a-b

# # # a = int(input("Enter a : "))
# # # b = int(input("Enter b :"))

# # # print("addition and substraction of {} and {} is {} and {}".format(a,b, calc(a,b)[0], calc(a,b)[1]))


# # # {'b': 2, 'c': 3, 'd': 4, 'e': 6}

# # # def max_freq(d):
# # #     max = 0
# # #     for i in d : 
# # #         if d[i] > max:
# # #             max = d[i]
# # #             elem = i
# # #     return elem, max

# # # def freq_char(st) : 
# # #     d = {}
# # #     count = 0
# # #     for i in st : 
# # #         print(count)
# # #         print(i)
# # #         if i not in d : 
# # #             d[i] = 1
# # #         else:
# # #             d[i] += 1 # d[i] = d[i] + 1
# # #         print(d, '\n')
# # #         count += 1
# # #     return d

# # # s = input("enter the string : ")
# # # print(max_freq(freq_char(s)))

# # # you can change the values only by accessing the values by index
# # l = [1,2,3,4,5,6,7]
# # # for i in range(len(l)):
# # #     if i == len(l) - 1:
# # #         print(l[i], l[0])
# # #         l[i] = l[i] + l[0]
# # #     else:
# # #         print(l[i], l[i+1])
# # #         l[i] = l[i] + l[i+1]
# # # print(l)

# # # for loop - accessing by value
# # # count = 0
# # # for i in l : 
# # #     print(l[count]) # l[0], l[1]
# # #     print(i + 1) 
# # #     count = count + 1

# # # while loop
# # # count = 0
# # # while (count != len(l)):
# # #     print(l[count])
# # #     count = count + 1
# # #functions
# # # def right_angled_triangle(n, pat):
	
# # #     for i in range(1, n+1):
# # #         # print(i , n-1)
# # #         print(pat * i)

# # # def left_angled_triangle(n, pat) :
	
# # #     for i in range(1, n+1):
# # #         print(" " * (n-i), i * pat)

# # # #inputs
# # # n = int(input("Enter the number of lines you want to be printed : "))
# # # pat = input("enter the pattern : ")
# # # l = [left_angled_triangle, right_angled_triangle]
# # # for i in l:
# # #     i(n, pat)
# # # #function_call
# # # right_angled_triangle(n, pat)
# # # left_angled_triangle(n, pat)

# # # # all the funtions

# # # from inputs import list_input

# # # def find_closest_set(l1,l2,num):
# # # 	diff = l1[0] + l2[0]
# # # 	closest_set = [0,0]
# # # 	s1 = sorted(l1)
# # # 	s2 = sorted(l2)
# # # 	print(s1, s2)
# # # 	for i in s1:
# # # 		for j in s2 : 
# # # 			if abs((i + j) - num) < diff:
# # # 				closest_set[0], closest_set[1] = i,j
# # # 	return closest_set
# # 	# diff = 0
# # 	# closest_set = {}
# # 	# ret_set = []
# # 	# max = 0
# # 	# count = 0
# # 	# for i in range(len(l1)):
# # 	# 	for j in range(len(l2)):
# # 	# 		if (l1[i] + l2[j] > abs(diff)) & (count == 0):
# # 	# 			# print("in first if")
# # 	# 			closest_set[l1[i] + l2[j] - abs(diff)] = (l1[i], l2[j])
# # 	# 			count = 1
# # 	# 		if l1[i] + l2[j] == abs(diff):
# # 	# 			print("in second if")
# # 	# 			closest_set[l1[i] + l2[j] - abs(diff)] = (l1[i], l2[j])
# # 	# 		if l1[i] + l2[j] < abs(diff):
# # 	# 			print("in third if")
# # 	# 			closest_set[l1[i] + l2[j] - abs(diff)] = (l1[i], l2[j])
# # 	# for i in closest_set:
# # 	# 	if i > max:
# # 	# 		max = i
# # 	# 		ret_set = closest_set[i]
# # 	# return ret_set

# # # l1 = list_input(int(input("Enter the number of numbers you want in list 1 : ")))
# # # l2 = list_input(int(input("Enter the number of numbers you want in list 2 : ")))
# # # num = int(input("Enter the number : "))
# # # print(find_closest_set(l1,l2,num))

# # # import sys
# # # def printClosest(l1, l2, m, n, x): 
# # #     diff = sys.maxsize
# # #     l = 0
# # #     r = n-1
# # #     while((l < m) and (r >= 0)): 
# # #         if abs(l1[l] + l2[r] - x) < diff: 
# # #             res_l = l 
# # #             res_r = r 
# # #             diff = abs(l1[l] + l2[r] - x) 
# # #         if l1[l] + l2[r] > x: 
# # #             r = r-1
# # #         else:
# # #             l = l + 1
# # #     print("The closest pair is [", 
# # #          l1[res_l], ", ", l2[res_r], "]") 

# # # l1 = [1, 4, 8, 9, 12]
# # # l2 = [2,5,7,10] 
# # # m = len(l1) 
# # # n = len(l2) 
# # # x = 13
# # # printClosest(l1, l2, m, n, x) 
  



# # # finding combinations of 3 given numbers
# # # import itertools
# # # def comb(*args):
# # # 	# d=[]
# # # 	# d.append(a)
# # # 	# d.append(b)
# # # 	# d.append(c)
# # # 	# for i in range(0,3):
# # # 	# 	for j in range(0,3):
# # # 	# 		for k in range(0,3):
# # # 	# 			if(i!=j & j!=k & k!=i):
# # # 	# 				print(d[i],d[j],d[k])
# # # 	return list(itertools.combinations([a,b,c],2))


# # # a=int(input("Enter first number:"))
# # # b=int(input("Enter second number:"))
# # # c=int(input("Enter third number:"))
# # # print(comb(a,b,c))





# # # multiplication table

# # # def mult_tab(n):
# # # 	l = []
# # # 	d = {}
# # # 	for i in range(1, n+1):
# # # 		# if i not in d:
# # # 		for j in range(1,11):
# # # 			l.append(i*j)
# # # 		d[i] = l
# # # 		l = []
# # # 	return d
# # # n = int(input("Enter the number till what the multiplication table you want : "))
# # # print(mult_tab(n))



# # # alterating stars
# # # def odd_print(*args, **kwargs): # args[0] = 20, pat = &k-
# # # 	pat = args[1]
# # # 	s = ''
# # # 	for i in range(args[0]):
# # # 		if i%2 == 0:
# # # 			s = s + " "
# # # 		else:
# # # 			s = s + pat
# # # 	return s

# # # def even_print(*args, **kwargs):
# # # 	pat = args[1]
# # # 	s = ''
# # # 	for i in range(args[0]):
# # # 		if i % 2 != 0:
# # # 			s = s + " "
# # # 		else:
# # # 			s = s + pat
# # # 	return s

# # # def alternating_stars_pattern(*args, **kwargs):
# # # 	n, pat = args[0], args[1]
# # # 	for i in range(1, n+1): # 1 to 10
# # # 		if i % 2 == 0:
# # # 			print(odd_print(2*n, pat))
# # # 		else:
# # # 			print(even_print(2*n, pat))

# # # def take_inputs():
# # # 	n = int(input("Enter the number of lines you want as input : "))
# # # 	pat = input("Enter the pattern : ")
# # # 	return n, pat # returns tuple

# # # def main():
# # # 	n, pat = take_inputs()
# # # 	alternating_stars_pattern(n, pat)

# # # # abc = alternating_stars_pattern(n, pat)
# # # # print("abc")

# # # if __name__ == "__main__": # main()
# # # 	main()



# # # def a(*args, **kwargs):

# # # 	print("args : ", args)
# # # 	for i in range(len(args)): # accessing by index
# # # 		print("positional", i, args[i])
	
# # # 	print("kwargs : ", kwargs)
# # # 	for i in kwargs: # accessing by keys
# # # 		print("key-value pairs", i, kwargs[i])

# # # a( 2,5,'fdg', a = 5, b = 10)





# # # def add_two_num(a, b):
# # # 	return a + b

# # # print(add_two_num(int(input("Enter a : ")), int(input("Enter b : "))))


# # # def add_two_num():
# # # 	return (int(input("Enter a : ")) + int(input("Enter b : ")))
# # # add_two_num()

# # # print((int(input("Enter a : ")) + int(input("Enter b : "))))


# # # def sub_2_num(a,b) : 
# # # 	if a == b:
# # # 		return 0
# # # 	elif a > b : 
# # # 		return a - b
# # # 	else:
# # # 		return b - a

# # # print(sub_2_num(int(input("Enter a : ")), int(input("Enter b : "))))



# # # hollow triangle
# # # def print_hollow_triangle(n):
# # # 	pass





# # """
# # 1. procedural progg.
# # 2. functional progg. 
# # 3. oops (object oriented programming)
# # """

# # # procedural code

# # # a = int(input("enter a : "))  # = -> assignment operator
# # # b = int(input("enter b : "))
# # # # c = a + b
# # # print(type(a), type(b))
# # # print(a + b)  # sring addition or concatenation



# # # def add_num(a, b):  # : -> continuity operator  # function definition
# # # 	return a + b

# # # def sub_num(a, b): # this method should always return a positive number
# # # 	if a == b:
# # # 		return 0
# # # 	elif a > b:
# # # 		return a - b
# # # 	else:
# # # 		return b - a

# # # def div_num(a, b):
# # # 	if a == b:
# # # 		if a == 0:
# # # 			return "0/0, Division not possible"
# # # 		else:
# # # 			return 1
# # # 	elif a > b:
# # # 		if b == 0:
# # # 			return "Denominator 0, division not possible"
# # # 		else:
# # # 			return a/b
# # # 	else:
# # # 		if a == 0:
# # # 			return "Denominator 0, division not possible"
# # # 		else:
# # # 			return b/a

# # # say if the number is 
# # # 1. negative or positive 
# # # 2. divisible by 2 or not
# # # 3. odd or even
# # # check if a number is divisible by the other number
# # # is there a triangle exists with the given sides
# # # in which quadrant is the given point

# # # a = int(input("enter a : "))  
# # # b = int(input("enter b : "))

# # # print(add_num(a, b), sub_num(a, b)) # take the values from a and b, pass it to the function add_num and call the function with the given values


# # # def pop_func(l):
# # # 	pass

# # # def matrix_addition_elements(rows, cols):
# # # 	matrix = []
# # # 	for i in range(rows):
# # # 		row = []
# # # 		for j in range(cols):
# # # 			row.append(int(input()))
# # # 		matrix.append(row)
# # # 	return matrix

# # # print(matrix_addition_elements(int(input()), int(input())))

# # # import numpy
# # # print(numpy.ones((4,4)))

# # # rows, cols = int(input()), int(input());
# # # Matrix = [[int(input()) for x in range(rows)] for y in range(cols)] 
# # # print(Matrix)

# # # Matrix = []
# # # for y in range(cols):
# # # 	for x in range(rows):
# # # 		Martix.append(int(input))



# # # program to find top 10 numbers from 3 sorted lists having 10 numbers each
# # # import random

# # # def largest_10_elem(l1,l2,l3):
# # # 	return sorted(l1 + l2 + l3)[-10:]

		


# # # l1 = sorted([random.randint(1,1000) for i in range(10)])
# # # l2 = sorted([random.randint(1,1000) for i in range(10)])
# # # l3 = sorted([random.randint(1,1000) for i in range(10)])
# # # print(l1,l2,l3)
# # # print(largest_10_elem(l1,l2,l3))

# # # How to remove 2nd occurrence  of the duplicate character from a list
# # # Eg:
# # # 1,2,3,4,5,3,5
# # # Input 3
# # # Output 1,2,3,4,5,5

# # # def remove_2nd_dup_char(l, elem):
# # # 	count = 0
# # # 	for i in range(len(l)):
# # # 		if l[i] == elem:
# # # 			count += 1
# # # 			if count == 2:
# # # 				l.pop(i)
# # # 				return l
				
# # # 	return l
# # # print(remove_2nd_dup_char([1,2,3,4,5,3,5], 3))

# # # functional code

# # # def add_num(*args):
# # # 	# print(id(a), id(b))
# # # 	return a + b


# # # def sub_num(a, b):
# # # 	if a == b:
# # # 		return 0
# # # 	elif a > b:
# # # 		return a - b
# # # 	else:
# # # 		return b - a

# # # def mul_num(a,b):
# # # 	return a * b

# # # def div_num(a, b):
# # # 	if a == b:
# # # 		pass
# # # 	elif a > b : 
# # # 		pass
# # # 	else:
# # # 		pass



# # # a = int(input("Enter a : "))
# # # b = int(input("Enter b : "))
# # # # print(id(a), id(b))
# # # print(sub_num(a, b))
# # # # print(a + b, type(a + b))



# # # from math import ceil

# # # def isPrime(num):
# # # 	if num == 2:
# # # 		return True
# # # 	else:
# # # 		for i in range(2, ceil(num/2)+1):
# # # 			if num % i == 0:
# # # 				return False
# # # 		return True

# # # def find_factors(beg = 1, end = 100):
# # # 	d = {}
# # # 	for i in range(beg, end + 1):
# # # 		# i = 1 . . . . . . end + 1
# # # 		if isPrime(i) is True:
# # # 			d[i] = [1, i]
# # # 		else:
# # # 			d[i] = [1]
# # # 			for j in range(2, ceil(i/2) + 1):
# # # 				if (i % j == 0) and (isPrime(j)):d[i].append(j)
# # # 					# if j not in d[i]:
						
# # # 	return d


# # # print(find_factors(int(input("Enter beginning : ")), int(input("Enter ending"))))


# # # def right_angled_triangle(n, pat):
# # # 	for i in range(1, n + 1):
# # # 		print(pat * i)

# # # n = int(input("Enter the number of lines : "))
# # # pat = input("Enter the pattern : ")

# # # right_angled_triangle(n, pat)

# # #  Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary.

# # # {'1':['a','b'], '2':['c','d']}

# # def create_combinations(l1):
# # 	l = []
# # 	if len(l1) == 2:
# # 		for i in l1[0]:
# # 			for j in l1[1]:
# # 				l.append(i + j)
# # 	else:
# # 		for i in l1: 
# # 			if count = 0
# # 			create_combinations[l[-i-1], l[-i-2]]
# # 	return l
# # # print(create_combinations(['a','b'], ['c','d'])
# # 	# else:
# # 	# 	l = []
# # 	# 	for i in range(len(l1)-1, -1, -1):
# # 	# 		l.append(create_combinations(l[i: ]))


# # def create_list(d):
# # 	l = []
# # 	l1 = []
# # 	for i in d:
# # 		l.append(d[i])
# # 	print(l)
# # 	# for i in l:
# # 	# 	l1.append(create_combinations(l[-i-1], l[-i-2]))
# # 	# print(l)
# # 	return create_combinations(l)

# # print(create_list({'1':['a','b'], '2':['c','d'], '3':['e','f']}))



# # import os, shutil
# # import datetime

# # def modification_date(filename):
# # 	t = os.path.getmtime(filename) # getting the creation date
# # 	return datetime.datetime.fromtimestamp(t) # returning the creation date in datetime format
# # # datetime.datetime.fromtimestamp(os.path.getmtime(filename))
# # def show_path(path):
# # 	os.chdir(path) # altering the terminal path to the given location
# # 	p = os.listdir(path) # saving the contents of the given path in the p variable
# # 	files = [j for j in (map(modification_date, [i for i in p]))]
# # 	# print(p, files)
# # 	return p, files

# # def copytree(src, dst, symlinks=False, ignore=None):
# # 	if not os.path.exists(dst):
# # 		os.makedirs(dst)
# # 	for item in os.listdir(src):
# # 		s = os.path.join(src, item)
# # 		d = os.path.join(dst, item)
# # 		if os.path.isdir(s):
# # 			copytree(s, d, symlinks, ignore)
# # 		else:
# # 			if not os.path.exists(d) or os.stat(s).st_mtime - os.stat(d).st_mtime > 1:
# # 				d =  ".".join((d.split(".")[:-1])) + "_created_" + datetime.datetime.strftime(datetime.datetime.fromtimestamp(os.path.getmtime(s)) ,'%Y-%m-%dT%H_%M_%S_%f') + "." + s.split(".")[-1]
				
# # 				shutil.copy2(s , d)

# # copytree("G:\\Digit", "G:\\abc\\Digit")



# # class Indian:
# # 	def __init__(self, name, aadhaar_no = None):
# # 		self.name = name
# # 		self.aadhaar_no = aadhaar_no
	
# # 	def vote(self):
# # 		if self.get_age() == 18:
# # 			return "apply for voter ID card"
# # 		if self.get_age() > 18:
# # 			return "You can vote"
# # 		return "wait for {} more years".format(18 - self.get_age())
	
# # 	def work(self, *args):
# # 		raise NotImplementedError("the person is jobless")

# # class Employee(Indian):
# # 	no_of_emp = 0
# # 	def __init__(self,name, aadhaar_no, emp_id, skill):
# # 		super().__init__(name, aadhaar_no)
# # 		self.id = emp_id
# # 		self.__age = None
# # 		self.skill = skill # aggregation
	
# # 	def emp_mail(self):
# # 		return  "pass"  + "@gmail.com"

# # 	def set_name(self, age):
# # 		self.__age = age

# # 	def get_age(self):
# # 		if self.__age is not None:
# # 			return self.__age
# # 		return 18

# 	# def work(self, job):
# 	# 	if job in ["jobless", None]:
# 	# 		return "Apply for a job"

# # 	def return_department(self, skill1):
# # 		if skill1.lower() in [i.lower() for i in self.skill.skill_set]:
# # 			return "valid skill"
# # 		return "invalid skill"

# # 	def work_on(self, comp): # association
# # 		if comp.computer_number.startswith("Z"):
# # 			return "You can only do organizational tasks"
# # 		return "You can access anything"

# # class Skill:
# # 	def __init__(self, skill_set):
# # 		self.skill_set = skill_set

# # class Computer:
# # 	def __init__(self, computer_number):
# # 		self.computer_number = computer_number

# # it_skill_set = Skill(["Python", "Java"])
# # hr_skill_set = Skill(["Management", "HR"])

# # emp1 = Employee("Suresh", "123654789", 554477, it_skill_set)
# # emp2 = Employee("pk", "789654123", 221144,  hr_skill_set)

# # comp1 = Computer("ZX1234")

# # print(emp1.skill.skill_set, emp2.skill.skill_set)
# # print(emp1.return_department("python"))

# # print(emp1.work_on(comp1))

# # print(emp1.name, emp1.aadhaar_no, emp2.name, emp2.aadhaar_no)

# # print(emp1.vote(), emp2.vote())

# # print(emp1.work(None))


# s = """def calc_num(a, b):
# 	print("abc")
# 	return a + b, a - b

# # a = calc_num(5,10)

# # print("addition and substraction of 5 and 10 is {} and {}".format(a[0], a[1] ))

# i, j = calc_num(5,10)
# print(i, j)"""


# def max_freq(d):
# 	max_num = 0
# 	max_char = ""
# 	for i in d:
# 		if d[i] > max_num : 
# 			max_char, max_num = i, d[i]
# 	return max_char, max_num

# def freq_char(s):
# 	d = {}
# 	for i in s:
# 		if i not in d:
# 			d[i] = 1
# 		else:
# 			d[i] += 1  # d[i] = d[i] + 1
# 	return d

# s = "my name is prasant mishra"

# print(max_freq(freq_char(s)))





# # function definition
# def add_num(a1, a2):
# 	return a1 + a2

# def sub_num(a, b):
# 	if a == b:
# 		return 0
# 	elif a > b:
# 		return a - b
# 	else:
# 		return b - a

# def mult_num(a, b):
# 	return a * b

# def div_num(a, b):
# 	if a == b:
# 		if a == 0:
# 			return "0/0 Not possible"
# 		else:
# 			return 1
# 	elif a > b: # 4, 1
# 		if b == 0:
# 			return "Division Not possible, b is 0"
# 		return a / b
# 	else:
# 		if a == 0:
# 			return "Division Not possible, a is 0"
# 		else:
# 			return b / a

# # inputs declaration
# a = int(input("Enter a : "))
# b = int(input("Enter b : "))

# # function call
# print(div_num(a, b))

"""
looping / iterating is an operation where we work upon a group of values which form a data set

for loops are mainly of 2 types
	looping by values
		only accessing of values are permitted
		we can't change the values
	looping by index
		can access the values, by index
		can change the values

"""

# looping by values
"""
for iterator in iterable:
	perform iteration

"""

# l = [1,2,3,4,5]
# for i in l:
# 	print(i)


# range(start = 0, end, (direction  = +)step = 1)
# range(5) = range(0, 5)

l = [1,2,3,4,5]
for i in range(len(l)):
	print(i, l[i])

for i in range(len(l)): # l has changed
	l[i] = l[i] + 2
	print(l[i])


"""
>>> chr(65)
'A'
>>> ord("A")
65
for i in range(0, 256):
	print(i, chr(i))

type, id, ord, chr, range, len
"""