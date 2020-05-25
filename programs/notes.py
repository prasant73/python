
# else block in try-except only works when no exceptions are thrown
# similar to for-else block
# else block in for-else executes when the loop encounters no breaks i.e. if we don't break out of the for loop
# try:
#     age = int(input("Enter age : "))
#     l = 10 / age
# except (ValueError, ZeroDivisionError) as e : 
#     print("You didn't enter a valid age : " , e)
# else:
#     print("No exceptions were thrown...")

# most ideal scenario to use finally would be in the case where we want to close file connections or network connections 

# with statement is used to automatically close external resources

# with open("filename", "mode") as f1, open("file2", "w") as f2:
#     # do something
#     pass


# # how to check the execution time of a code
# from timeit import timeit
# code1 = """

# from inputs import list_input
# from math import floor, sqrt, ceil
# # import math

# def isPrime(n):
# 	for i in range(2, floor(n/2) + 1):
# 		if n % i == 0:
# 			return False
# 	else:return True
# # print(isPrime(67))

# def prime_factors(num):
# 	factors = [1]
# 	if isPrime(num):
# 		factors.append(num)
# 		return factors
# 	else:
# 		for i in range(2, ceil(num/2)):
# 			if (num % i == 0) and (isPrime(i)):
# 				factors.append(i)
# 	return factors


# def main():
# 	dict_of_factors = {}
# 	l1 = list_input(int(input("enter the number of numbers you want to find the prime factors of : ")))
# 	# l1 = [1,2,3,4]

# 	for i in l1:
# 		dict_of_factors[i] = prime_factors(i)
# 	print(dict_of_factors)

# print("Inside prime factors", __name__)
# if __name__ == "__main__":
# 	try:
# 		main()
# 	except MemoryError as m:
# 		print("memory Error", m)
# 	except OSError as os:
# 		print("oserror", os)
# 	except Exception as e:
# 		print("Inside main's Exception")
# 		print(e)
# 	finally:
# 		print("Inside prime factors finally", __name__)


# """
# print("first code : ", timeit(code1, number=100000))


"""
isinstance method

isinstance(data, datatype)

isinstance(5, int)
>> true
"""

# command line code
# while True:
#     print(">>>", end = "")
#     command = input()
#     if command == "quit()":
#         break
#     else:
#         print(command)
#         continue
# else:
#     print("exiting console")

# self is a reference to the current object

# class Point:
# 	default_color = "yellow"
# 	def __init__(self, x, y):
# 		self.x = x
# 		self.y = y
	
# 	def __str__(self):
# 		return f"({self.x}, {self.y})"
   
# 	def __eq__(self, other): # doesn't need to be explicitly called, called when == is used
# 	   return (self.x == other.x) and (self.y == other.y)
	
# 	def __gt__(self, other):
# 		return self.x > other.x and self.y > other.y
	   
# 	def __lt__(self, other):
# 		return self.x < other.x and self.y < other.y
	
# 	def __add__(self, other):
# 		return Point(self.x + other.x, self.y + other.y)

# 	def __sub__(self, other):
# 		return Point(self.x - other.x, self.y - other.y)

# 	@classmethod # decorators extend the behaviour of a class
# 	def zero(cls):
# 		return cls(0,0)

# 	def draw(self):
# 		print(f"Point ({self.x}, {self.y})")

# point = Point(1, 2)
# other = Point(3, 4)
# point.z = 4
# point.draw()
# point = Point.zero()
# point.draw()
# print(point == other) # prints false because the equality operator 
# print(point)
# print(point < other) # less than need not be explicitly written, __gt__ if written, it takes care of __lt__ also
# print(point + other) 

# combined = point + other
# print(combined) # addition and substraction in returning a object, so it can be returned to a variable which becoms an object



# making custom container types : like lists, dictionaries etc
# i.e. data types are also contanier types

# class TagCloud:
# 	def __init__(self):
# 		self.tags = {}
	
# 	def add(self, tag):
# 		self.tags[tag.lower()] = self.tags.get(tag, 0) + 1 
# 		# self.tags[tag.lower()] = self.tags.get(tag, 0) + 1
	
# 	def __getitem__(self, tag):
# 		return self.tags.get(tag, 0) # return self.tags.get(tag.lower(), 0)
	
# 	def __setitem__(self, key, value):
# 		self.tags[key] = value  # self.tags[key.lower()] = value
	
	
# 	def __len__(self):
# 		return len(self.tags)
	
# 	def __str__(self):
# 		print(f"({self.tags})")
	
# 	def __iter__(self):
# 		return iter(self.tags)

# cloud = TagCloud()
# cloud.add("Python")
# cloud.add("python")
# cloud.add("python")
# print(cloud.tags)
# print(cloud["python"]) # getitem
# cloud["abc"] = 5 # setitem
# print(cloud["abc"])
# print(len(cloud))
# print(cloud.tags)
# for i in cloud.tags:
# 	print(i, cloud.tags[i])
# print(cloud.__dict__) # to see whats inside



# # better way to getters and setters
# class Product:
# 	def __init__(self, price):
# 		# self.__price = price
# 		# self.set_price(price)
# 		self.__price = price
# 	# def get_price(self):
# 	# 	return self.__price
# 	@property
# 	def price(self):
# 		return self.__price
	
# 	@price.setter
# 	def set_price(self, price):
# 		if price < 0:
# 			raise ValueError("Price should be greater than zero")
# 		self.__price = price
# 	# def set_price(self, price):
# 	# 	if price < 0:
# 	# 		raise ValueError("Price should be greater than zero")
# 	# 	self.__price = price
# 	# price = property(get_price, set_price)

# product = Product(50)
# print(product.price)




# def join_function(li,sep):
#     # li2=[""]
#     # for i in range(len(li)):
#     #     if li[i] not in li2:
#     #         li2[0]+=li[i]+str
# 	st = ""
# 	for i in range(len(li)-1):
# 		st = st + str(li[i]) + sep
# 		print(st)
# 	return st + li[-1]

#     # return li2

# li = ["my","name","is","gaya3"]
# # l = len(li)
# sep = input("enter the seperator")

# print(join_function(li, sep))


"""
Task 
Given an integer,n , and n space-separated integers as input, create a tuple,t, of those n integers. Then compute and print the result of hash(t).

Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.

Input Format

The first line contains an integer,n , denoting the number of elements in the tuple. 
The second line contains n space-separated integers describing the elements in tuple t.

Output Format

Print the result of hash(t).

Sample Input 0

2
1 2
Sample Output 0

3713081631934410656
"""

# if __name__ == '__main__':
#     n = int(input())
#     integer_list = map(int, input().split()[:n])
#     print(tuple(integer_list), hash(tuple(integer_list)))



# procedural

# a =  # input takes string by default
# b = 
# print(
# 	int(input("Enter a : ")) + 
# 	int(input("Enter b : "))
# 	)

"""
procedural
functional
structural
OOPs
"""
# l = [1,2,3,4,5]
# i = iter(l)
# while True:
# 	try:
# 		print(i.__next__()) # next(i)
# 	except StopIteration:
# 		break


# from random import shuffle

# def main():

# 	test_cases = int(input())
# 	for i in range(test_cases):
# 		number_of_heroes_and_villians = int(input())
# 		powers_of_villians = [i for i in map(int, input().split(" ", number_of_heroes_and_villians)[:number_of_heroes_and_villians])]
# 		powers_of_heroes = [i for i in map(int, input().split(" ", number_of_heroes_and_villians)[:number_of_heroes_and_villians])]
# 		shuffle(powers_of_heroes)
# 		shuffle(powers_of_villians)
# 		count = 0
# 		for i,j in zip(powers_of_heroes, powers_of_villians):
# 			if i >= j:
# 				count += 1
# 				continue
# 			else:
# 				break
# 		if count == number_of_heroes_and_villians:
# 			print("WIN")
# 		else:
# 			print("LOSE")
# main()


# l = [i if i % 2 == 0 else i * 3 for i in range(20)]

"""map
zip
filter -> functools  from functools import filter
reduce"""

# ([i for i in  map(str, { i : j for i, j in zip([i for i in range(10)], [i for i in range(20)])}) if ord(i) < 54])




# def expand_list(num):
# 	l = []
# 	for i in range(num):
# 		l.append(i)
# 	return l

# def zip_ops(l1, l2):
# 	l = []
# 	for i in range(len(l2)):
# 		l.append((l1[i], l2[i]))
# 	return l

# def zip_func(l1, l2):
# 	if len(l1) > len(l2):
# 		zip_ops(l1, l2)
# 	else:
# 		zip_ops(l2, l1)



# import os
# from fnmatch import fnmatch

# root = "F:\\"
# pattern = "*.txt"
# l = []
# for path, subdirs, files in os.walk(root):
#     for name in files:
#         if fnmatch(name, pattern):
#             l.append(os.path.join(path, name))

# for i in l:
# 	print(i)







# import os
# import datetime
# from shutil import copy, copy2
# # return the modification date of the file
#
#
# def modification_date(filename):
# 	t = os.path.getmtime(filename)  # getting the creation date
# 	# returning the creation date in datetime format
# 	return datetime.datetime.fromtimestamp(t)
#
#
# def show_path(path):
#     os.chdir(path)  # altering the terminal path to the given location
#     # saving the contents of the given path in the p variable
#     p = os.listdir(path)
#     files = [j for j in (map(modification_date, [i for i in p]))]
#     # print(p, files)
#     return p, files
#
#
# def copy_directory_to_path():
#     entered_path = input("Enter path : ")
#     dest = input("Kindly enter destination : ")
#
#     if not os.path.isdir(dest):
#         print("destination non existant, creating a new directory...")
#         os.makedirs(dest)
#
#     files_and_creation_date = show_path(entered_path)
#     new_names = []
#
#     for i, j in zip(files_and_creation_date[0], files_and_creation_date[1]):
#         new_names.append("".join(i.split(
#             ".")[:-1]) + "_" + datetime.datetime.strftime(j, '%Y-%m-%dT%H_%M_%S_%f'))
#
#     num = 0
#
#     for i in os.listdir(entered_path):
#         copy(i,  dest + "\\" + new_names[num] +
#              "." + "".join(i.split(".")[-1]))
#         num = num + 1
#
#
# def copy_file_to_path():
#     entered_path = input("Enter directory : ")
#     if not os.path.isdir(entered_path):
#         print("source directory non existant...")
#     else:
#         os.chdir(entered_path)
#         print("Amongst the file names mentioned, mention the name you want to rename and move : ")
#         for i in os.listdir("."):
#             if os.path.isfile(i):
#                 print(i)
#
#         file_to_move = input()
#
#         dest = input("Kindly enter destination : ")
#         if not os.path.isdir(dest):
#             print("destination non existant, creating a new directory...")
#             os.makedirs(dest)
#         copy(file_to_move, dest + "\\" + "".join(file_to_move.split(".")[:-1]) + "_" + datetime.datetime.strftime(
#             modification_date(file_to_move), '%Y-%m-%dT%H_%M_%S_%f') + "." + file_to_move.split(".")[-1])

# def copytree(src = r"C:\Users\Prasant\Desktop\Ratan - Copy"):
# 	paths = (os.path.join(root, filename)
# 		for root, subdir, filenames in os.walk(src)
# 		for filename in filenames if "Workday" not in [root, subdir, filenames])

# 	for path in paths:
# 		try:
# 			if isinstance(datetime.datetime.strptime(path.split(".")[-1][-15:], '%Y%m%d_%H%M%S%f'), datetime.datetime):
# 				if modification_date(path) > datetime.datetime.strptime(path.split(".")[-1][-15:]) : 
# 					newname = ".".join((path.split(".")[:-1])) + "_created_" + datetime.datetime.strftime(
# 							datetime.datetime.fromtimestamp(os.path.getmtime(path)), '%Y%m%d_%H%M%S') + "." + path.split(".")[-1]
# 				else: 
# 					continue
# 			else:
# 				newname = ".".join((path.split(".")[:-1])) + "_created_" + datetime.datetime.strftime(
# 							datetime.datetime.fromtimestamp(os.path.getmtime(path)), '%Y%m%d_%H%M%S') + "." + path.split(".")[-1]
# 		except IndexError:
# 			pass
# 		except ValueError:
# 			continue
# 		if newname != path:
# 			os.rename(path, newname)

# def copytree(dst = r"C:\Users\Prasant\Desktop\testing", 
#     src = r"C:\Users\Prasant\Desktop\docs2", symlinks=False, ignore=None):
#     if not os.path.exists(dst):

#         os.makedirs(dst)
#     for item in os.listdir(src):
#         s = os.path.join(src, item)
#         d = os.path.join(dst, item)
#         print(s, d, sep = "\n")
#         if os.path.isdir(s):
#             copytree(s, d, symlinks, ignore)

#         else:
#             if not os.path.exists(d) or os.stat(s).st_mtime - os.stat(d).st_mtime > 1:
				
#                 print("hi")
				# d = ".".join((d.split(".")[:-1])) + "_created_" + datetime.datetime.strftime(
				#     datetime.datetime.fromtimestamp(os.path.getmtime(s)), '%Y-%m-%dT%H_%M_%S_%f') + "." + s.split(".")[-1]


#                 copy2(s, d)


# def copy_network_to_path():
# 	# print("""Kindly enter the drive location in the following format
# 		# 	\\\\HOST\\share\\path\\to\\file""")
# 	# source_path = input("Enter source network drive : ")
# 	# destination_path = input("Enter destination network drive : ")

# # 	copytree()

# # def main():
# 	# file_or_directory = input("""Enter
# 	# 	"file" to move a file,
# 	# 	"dir" to enter a directory,
# 	# 	"net" if working with a network drive
# 	# 	""")

# 	# if file_or_directory.lower() == "file":
# 	#     copy_file_to_path()
# 	# elif file_or_directory.lower() == "dir":
# 	#     copy_directory_to_path()
# 	# elif file_or_directory.lower() == "net":
# # 	copy_network_to_path()

# # main()

# #if __name__ == "__main__":
# #
# # try:
# #     main()
# # except Exception as e:
# #     print(e)


# # source path:    \\lousamwps05\ftproot\ControlMonitorReports\


# #destination path :\\lousamwps01\Bindview\SplunkUAT\Renamefileupdate



# class ExtendedList(list):
# 	def __init__(self):
# 		self.l = []

# 	def append(self, elem):
# 		pass
	
# 	def list_input(self, n):
# 		for _ in range(n):
# 			self.l.append(int(input("ENter number : ")))
# 		return self.l

# # print(dir(ExtendedList))
# l1 = ExtendedList()

# print(l1.list_input(5))


# def dict_cube(n):
# 	return {i : i * i for i in range(n) if i % 2 == 0}

# print(dict_cube(int(input("Enter range : "))))


# combine_dictionaries_adding_values_to_common_keys'

# def combine_dictionaries_adding_values_to_common_keys(d1, d2):
# 	for i in d2:
# 		if i in d1:
# 			d1[i] = d1[i] + d2[i]
# 			print("in if :",i, d1)
# 		else:
# 			d1[i] = d2[i]
# 			print("in else : ",i,  d1)
# 	return d1

# d1 = {"a" : 100, "b" : 200, "c" : 300}
# d2 = {"a" : 300, "b" : 200, "d" : 400}
# print(combine_dictionaries_adding_values_to_common_keys(d1, d2))


# pair of elements in a list which count equals n

# def pair_of_elements_in_a_list_which_count_equals_n(l, n):
# 	l1 = []
# 	for i in range(len(l)):
# 		if l[i] < n:
# 			for j in range(i + 1, len(l)):
# 				if l[j] == (n - l[i]):
# 					l1.append([l[i], l[j]])
# 	return l1

# print(pair_of_elements_in_a_list_which_count_equals_n([1,3,2,2,5], 4))



# remove the elements in a list whhose length is equal to n

# def remove_the_elements_in_a_list_whose_length_is_equal_to_n(l, n):
# 	# print(l, n)
# 	list_of_index = []
# 	for i in range(len(l)):
# 		if len(l[i]) == n:
# 			list_of_index.append(i)
# 		# if len(l[i]) == n:
# 		# 	l.remove(l[i])
# 	return l

# print(remove_the_elements_in_a_list_whose_length_is_equal_to_n(["abc", "def", "fgij"], 3))



# import numpy

# my_array = numpy.array([i for i in map(int,input().split()[:9])])
# print (numpy.reshape(my_array,(3,3)))



# import numpy

# my_array = numpy.array([[1,2,3],
#                         [4,5,6]])
# print (numpy.transpose(my_array))
# print (my_array.flatten())


# import collections
# from random import choice
# Card = collections.namedtuple('Card', ['rank', 'suit'])
# class FrenchDeck:    
# 	ranks = [str(n) for n in range(2, 11)] + list('JQKA')    
# 	suits = 'spades diamonds clubs hearts'.split()
# 	def __init__(self):        
# 		self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
# 	def __len__(self):        
# 		return len(self._cards)
# 	def __getitem__(self, position):        
# 		return self._cards[position]
# # fd = FrenchDeck()
# # print(len(fd))
# # print(fd.__getitem__(2))
# # print(fd.ranks)
# # print(fd.suits)

# # beer_card = Card('7', 'diamonds')
# # print(beer_card)

# deck = FrenchDeck()
# # print(len(deck))
# print(choice(deck))


# def replace_first_character(s, pat):
# 	ret_str = ""
# 	if s[0] in s[1:]:
# 		for i in range(len(s)):
# 			if i == 0:
# 				ret_str = s[i]
# 			else:
# 				if s[i] == s[0]:
# 					ret_str = ret_str + pat 
# 				else:
# 					ret_str = ret_str + s[i]
# 			print (ret_str)
# 	else:	
# 		return "first chracter not repeated"
# 	return ret_str
# print(replace_first_character(input("Enter string : "), input("Enter the replacing character : ")))

# class abc:
# 	a = 0
# 	b = 0
# 	def __init__(self):
# 		self. c = self.a + self.b
# a1 = abc()
# print(a1.c)






# class Human:
# 	def __init__(self, gender, breed, color):
# 		self.gender = gender
# 		self.breed = breed
# 		self.color = color

# 	def __str__(self):
# 		return self.gender + " " + self.breed + " " + self.color

# 	def define_first_task(self):
# 		if self.breed == "IT-Emp":
# 			return "Learn MS-Excel"
# 		elif self.breed == "pink":
# 			return "I loooooooove pink"
# 		else:
# 			return "cry"
	
# 	def breathe(self):
# 		raise NotImplementedError("you have forgotten to breathe..")

# 	def sleep(self, hours):
# 		print("sleep for {} hours".format(hours))

# # With Private Variable
# class Employee(Human):
# 	__no_of_emp = 0       # Class Variable

	

# 	def __init__(self, name, designation, gender, breed, color, proj = "Bench"):
# 		super().__init__(gender, breed, color)
# 		self.name = name
# 		self.designation = designation
# 		self.proj = proj
# 		self.__age = None
# 		self.__salary = 0
# 		Employee.__no_of_emp += 1

# 	def __str__(self):
# 		return self.name + " " + self.designation

# 	@staticmethod                       #Inbuilt Decorator
# 	def return_no_of_emp():
# 		return Employee.__no_of_emp

# 	def set_age(self, age):
# 		self.__age = age

# 	def get_age(self):
# 		return self.__age
	
# 	def set_salary(self, salary):
# 		self.__salary = salary

# 	def get_salary(self):
# 		return self.__salary

# 	def inc_salary(self, designation):
# 		if self.designation == "SE-II":
# 			self.__salary = self.__salary + self.__salary*.15
# 		return self.__salary

# 	def check_eligibility_for_w4h(self, system):
# 		if system.system_type == "Laptop":
# 			return "Eligible"
# 		else:
# 			return "bhai tu office aa..."

# 	def system_broke(self, system):
# 		if system.system_os in ["Windows", "Linux", "iOS"]:
# 			return "Fine : " + system.determine_fine(system.system_os)

# 	def weekend_pay(self, weekend_time):
# 		return 150 * weekend_time

# 	def bonus(self, extra_time = 0):
# 		return 50 * extra_time

# 	def fill_timesheet(self, time_data = [9,9,9,9,9], weekend_time = 0):
# 		self.__salary = self.__salary + self.bonus(sum(time_data) - 45) + self.weekend_pay(weekend_time)
	
# 	def breathe(self):
# 		print("breathe")
	
	# def sleep(self, weekend_time):
	# 	if self.breed == "IT-Emp" and weekend_time > 0:
	# 		print("sleep with your system, have coffee as your drink")
	# 	elif self.breed == "pink":
	# 		print("Not Applicable")


# class Project:
# 	def __init__(self, name, client, id):
# 		self.proj_name = name
# 		self.proj_client = client
# 		self.proj_id = id


# class System:
# 	def __init__(self, type, id, os):
# 		self.system_type = type
# 		self.system_id = id
# 		self.system_os = os

# 	def determine_fine(self, system_os):
# 		if self.system_os == "Windows":
# 			return "10000"
# 		elif self.system_os == "Linux":
# 			return "khud se theek karr"
# 		elif self.system_os == "iOS":
# 			return "kidney"
# 		else:
# 			return "contact CCD"


# h1 = Human("male", "IT-Emp", "undefined")
# h2 = Human("female", "pink", "pinkish")

# # s1 = System("Desktop", "B4585", "Windows")
# # s2 = System("Laptop", "L4587", "iOS")

# p1 = Project("BS-Design", "Pepsi", "1231")
# p2 = Project("CDU-Design", "Cisco", "2321")


# e1 = Employee("PK", "SE-II", "male", "IT-Emp", "wheatish", p1)
# e2 = Employee("KP", "SE-I", "female", "pink", "pinkish", p2)

# e1.breathe()

# e1.sleep(5)
# e2.sleep(10)

# h1.sleep(24)

# print(e1, e2, h1, h2, sep = "\n")


# e1.set_salary(50000)
# e1.fill_timesheet([9.5, 9.5, 9.5, 10, 9.5], 20)

# print(e1.get_salary())


# print(e1.proj.proj_name)
# print(e2.proj.proj_client)
#
# print(e1.check_eligibility_for_w4h(s2))
# print(e2.check_eligibility_for_w4h(s1))
#
# print(e1.system_broke(s2))

# print(e1.gender, e2.breed, e1.define_first_task())


# Employee.__no_of_emp = 10                   #Although the same variable is defined but it will consider it as a new variable.
#                                             #Because we have made the variable in class as private.
# print(Employee.__no_of_emp)
# print(e1.return_no_of_emp())                #Not Prefferable
# e1.skills = ["Python", "C++"]               #We can define additional variable in the object.

# print(e1.name, e2.name)
# e1.set_age(25)
# print(e1.get_age())
# print(e1.inc_salary(e1.designation))
# print(Employee.return_no_of_emp())          #Preferred Way
# print(e1.skills)




# def abc():
#     print("in abc")

# def defg():
#     print("in defg")

# def call_func(func):
#     func()

# list_of_objects = [abc, defg]


# for i in list_of_objects:
#     call_func(i)


# def abc(a = None, b = None):
#     if not(a or b) :
#         print("Both a and b are None")
#     else:
#         if not a :
#             print("b is", b)
#         elif not b:
#             print("a is", a)
#         else:
#             print(a , b)

# abc()
# abc(1)
# abc(0, 2)
# abc(2,3)


# def abc(a , b = None):
#     if b is not None:
#         print(a, b)
#     else:
#         print(a)

# abc(2,3)
# abc(2)


# class Q:
# 	def __init__(self, w, e):
# 		self.w = w
# 		self.e = e

# 	def __eq__(self, obj2):
# 		return self.w == obj2.w and self.e == obj2.e

# 	def __gt__(self, obj2):
# 		return self.w > obj2.w and self.e > obj2.e

# q1 = Q(2, 4)
# q2 = Q(1, 2)

# print(q1 > q2) # q1.__gt__(q2)

# print(int(id(q1)) > int(id(q2)))

# print(q1 == q2)  # q1.__eq__(q2)


