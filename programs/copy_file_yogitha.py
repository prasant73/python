
# import os
# import datetime
# from shutil import copy, copy2

# # return the modification date of the file


# def modification_date(filename):
#     t = os.path.getmtime(filename)  # getting the creation date
#     # returning the creation date in datetime format
#     return datetime.datetime.fromtimestamp(t)


# def show_path(path):
#     os.chdir(path)  # altering the terminal path to the given location
#     # saving the contents of the given path in the p variable
#     p = os.listdir(path)
#     files = [j for j in (map(modification_date, [i for i in p]))]
#     # print(p, files)
#     return p, files


# def copy_directory_to_path():
#     entered_path = input("Enter path : ")
#     dest = input("Kindly enter destination : ")

#     if not os.path.isdir(dest):
#         print("destination non existant, creating a new directory...")
#         os.makedirs(dest)

#     files_and_creation_date = show_path(entered_path)
#     new_names = []

#     for i, j in zip(files_and_creation_date[0], files_and_creation_date[1]):
#         new_names.append("".join(i.split(
#             ".")[:-1]) + "_" + datetime.datetime.strftime(j, '%Y-%m-%dT%H_%M_%S_%f'))

#     num = 0

#     for i in os.listdir(entered_path):
#         copy(i,  dest + "\\" + new_names[num] +
#              "." + "".join(i.split(".")[-1]))
#         num = num + 1


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

#         file_to_move = input()

#         dest = input("Kindly enter destination : ")
#         if not os.path.isdir(dest):
#             print("destination non existant, creating a new directory...")
#             os.makedirs(dest)
#         copy(file_to_move, dest + "\\" + "".join(file_to_move.split(".")[:-1]) + "_" + datetime.datetime.strftime(
#             modification_date(file_to_move), '%Y-%m-%dT%H_%M_%S_%f') + "." + file_to_move.split(".")[-1])


# def copytree(src, dst, symlinks=False, ignore=None):
#     if not os.path.exists(dst):
#         os.makedirs(dst)
#     for item in os.listdir(src):
#         s = os.path.join(src, item)
#         d = os.path.join(dst, item)
#         if os.path.isdir(s):
#             copytree(s, d, symlinks, ignore)
#         else:
#             if not os.path.exists(d) or os.stat(s).st_mtime - os.stat(d).st_mtime > 1:
#                 d = ".".join((d.split(".")[:-1])) + "_created_" + datetime.datetime.strftime(
#                     datetime.datetime.fromtimestamp(os.path.getmtime(s)), '%Y-%m-%dT%H_%M_%S_%f') + "." + s.split(".")[-1]

#                 copy2(s, d)


# def copy_network_to_path():
#     print("""Kindly enter the drive location in the following format
# 			\\\\HOST\\share\\path\\to\\file""")
#     source_path = input("Enter source network drive : ")
#     destination_path = input("Enter source network drive : ")

#     copytree(source_path, destination_path)


# def main():
#     file_or_directory = input("""Enter 
# 			"file" to move a file, 
# 			"dir" to enter a directory,
# 			"net" if working with a network drive
# 			""")

#     if file_or_directory.lower() == "file":
#         copy_file_to_path()
#     elif file_or_directory.lower() == "dir":
#         copy_directory_to_path()
#     elif file_or_directory.lower() == "net":
#         copy_network_to_path()


# if __name__ == "__main__":
#     try:
#         main()
#     except Exception as e:
#         print(e)



import os
import time
import schedule
import datetime

from shutil import copy, copy2

# return the modification date of the file


def modification_date(filename):
	t = os.path.getmtime(filename)  # getting the creation date
	# returning the creation date in datetime format
	return datetime.datetime.fromtimestamp(t)


def show_path(path):
	os.chdir(path)  # altering the terminal path to the given location
	# saving the contents of the given path in the p variable
	p = os.listdir(path)
	files = [j for j in (map(modification_date, [i for i in p]))]
	# print(p, files)
	return p, files


def copy_directory_to_path():
	entered_path = input("Enter path : ")
	dest = input("Kindly enter destination : ")

	if not os.path.isdir(dest):
		print("destination non existant, creating a new directory...")
		os.makedirs(dest)

	files_and_creation_date = show_path(entered_path)
	new_names = []

	for i, j in zip(files_and_creation_date[0], files_and_creation_date[1]):
		new_names.append("".join(i.split(
			".")[:-1]) + "_" + datetime.datetime.strftime(j, '%Y-%m-%dT%H_%M_%S_%f'))

	num = 0

	for i in os.listdir(entered_path):
		copy(i,  dest + "\\" + new_names[num] +
			 "." + "".join(i.split(".")[-1]))
		num = num + 1


def copy_file_to_path():
	entered_path = input("Enter directory : ")
	if not os.path.isdir(entered_path):
		print("source directory non existant...")
		exit()
	else:
		os.chdir(entered_path)
		print("Amongst the file names mentioned, mention the name you want to rename and move : ")
		for i in os.listdir("."):
			if os.path.isfile(i):
				print(i)

		file_to_move = input()

		dest = input("Kindly enter destination : ")
		if not os.path.isdir(dest):
			print("destination non existant, creating a new directory...")
			os.makedirs(dest)
		copy(file_to_move, dest + "\\" + "".join(file_to_move.split(".")[:-1]) + "_" + datetime.datetime.strftime(
			modification_date(file_to_move), '%Y-%m-%dT%H_%M_%S_%f') + "." + file_to_move.split(".")[-1])


def copytree(dst , src, symlinks=False, ignore=None):
	if not os.path.exists(dst):
		os.makedirs(dst)
	for item in os.listdir(src):
		s = os.path.join(src, item)
		d = os.path.join(dst, item)
		if os.path.isdir(s):
			copytree(s, d, symlinks, ignore)
		else:
			if not os.path.exists(d) or os.stat(s).st_mtime - os.stat(d).st_mtime > 1:
				d = ".".join((d.split(".")[:-1])) + "_created_" + datetime.datetime.strftime(
					datetime.datetime.fromtimestamp(os.path.getmtime(s)), '%Y-%m-%dT%H_%M_%S_%f') + "." + s.split(".")[-1]

				copy2(s, d)


def copy_network_to_path():
	print("""Kindly enter the drive location in the following format
			\\\\HOST\\share\\path\\to\\file""")
	source_path = input("Enter source network drive : ")
	destination_path = input("Enter destination network drive : ")

	copytree(source_path, destination_path)

def main():
	file_or_directory = input("""Enter 
		"file" to move a file, 
		"dir" to enter a directory,
		"net" if working with a network drive
		""")

	if file_or_directory.lower() == "file":
		copy_file_to_path()
	elif file_or_directory.lower() == "dir":
		copy_directory_to_path()
	elif file_or_directory.lower() == "net":
		copy_network_to_path()
	else:
		exit()


if __name__ == "__main__":
	try:
		main()
	except Exception as e:
		print(e)

# \\lousamwps05\ftproot\ControlMonitorReports\
# \\lousamwps01\bindview\splunkuat\




