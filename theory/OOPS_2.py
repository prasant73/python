
# class MeetingRoom:
#     # __meeting_rooms = ["Ramanujan", "C V Raman", "Vishveshwaraiya", "Newton"]
#     __meeting_rooms = []

#     def __init__(self, name, booked, no_of_seats, projector = None):

#         self.name = name
#         MeetingRoom.__meeting_rooms.append(name)
#         self.booked = booked
#         self.seats = no_of_seats
#         self.projector = projector

#     def __str__(self):
#         return self.name

#     def booking(self, hours, seats_rqd, projector_rqd = False):
#         if self.booked is True or seats_rqd > self.seats:

#             return False
#         if projector_rqd:
#             if self.projector is None:
#                 return False
#         else:
#             self.booked = True
#         return True


# class System:
#     def __init__(self, system, ram, hardware_issue = None):
#         self.system_type = system
#         self.ram = ram
#         self.hardware_issue = hardware_issue

#     @staticmethod
#     def change_of_system_required(problem, type = "minimal"):
#         if problem in ["monitor", "body"] and type == "minimal":
#             return False
#         return True

#     def request_for_change_of_system(self, problem, type,  issue = ["ram", "keyboard", "mouse"]):
#         if problem not in issue:
#             self.hardware_issue = problem
#             if System.change_of_system_required(self.hardware_issue, type):
#                 setattr(self, input("Laptop / Desktop"), "8gb")
#                 return "Hardware changed, type : {}, ram : {}".format(self.system_type, self.ram)
#         return "submit the system, it will be resolved by tomorrow"


# class Employee(): # class declaration
#     # no_of_emp = 0 # class variable declaration
#     __no_of_emp = 0 # private class variable declaration

#     def __init__(self, name, emp_id1, desg): # name, age, emp_id1 -> instance variables
        
#         self.name = name # name, age, emp_id -> public object variables, instance variables are getting assigned to the public object variables
#         self.__age = None # private object variable declaration
#         self.emp_id = emp_id1
#         self.desg = desg
#         self.__salary = None
#         print("{}".format(self), "in employee class")
#         Employee.__no_of_emp += 1

#     def __str__(self):
#         return self.name + " " + self.desg +  " " + str(self.emp_id)

#     @staticmethod
#     def return_number_of_employees():
#         return IT_Emp.__no_of_emp

#     # setters(mutators) and getters(accessors)

#     def set_salary(self, salary):
#         self.__salary = salary

#     def get_salary(self):
#         return self.__salary

#     #setter
#     def set_age(self, age):
#         self.__age = age

#     def get_age(self):
#         return self.__age



# class Manager(Employee):
#     __no_of_manager = 0
#     def __init__(self, name, emp_id, desg = "Manager"):
#         super().__init__(name, emp_id, desg)
#         Manager.__no_of_manager += 1
    
#     @staticmethod
#     def return_no_of_manager():
#         return Manager.__no_of_manager




# class IT_Emp(Employee): # class declaration
#     # no_of_emp = 0 # class variable declaration
#     __no_of_it_emp = 0 # private class variable declaration

#     def __init__(self, name, emp_id1, desg, system, manager): # name, age, emp_id1 -> instance variables
#         # self.name = name # name, age, emp_id -> public object variables, instance variables are getting assigned to the public object variables
#         # self.__age = None # private object variable declaration
#         # self.emp_id = emp_id1
#         # self.desg = desg
#         # self.__salary = None
#         self.manager = manager
#         super().__init__(name, emp_id1, desg)
#         self.timesheet = {}
#         self.system = system
        
#         IT_Emp.__no_of_it_emp += 1

#     def __str__(self):
#         return self.name + " " + self.desg + " " + self.manager.name


#     @staticmethod
#     def return_number_of_it_employees():
#         return IT_Emp.__no_of_it_emp

#     # setters(mutators) and getters(accessors)

#     def set_salary(self, salary):
#         self.__salary = salary

#     def get_salary(self):
#         return self.__salary

#     #setter
#     def set_age(self, age):
#         self.__age = age

#     def get_age(self):
#         return self.__age

#     def fill_timesheet(self, week, hours):
#         self.week = week
#         # self.timesheet = timesheet
#         self.timesheet[self.week] = hours

#     def count_hours_worked(self, month):
#         hours_worked = 0
#         for i in self.timesheet:

#             if i in range(4 * (month - 1) + 1, 4 * month + 1 ):
#                 print(self.timesheet[i], i, "asdf")
#                 hours_worked = hours_worked + sum(self.timesheet[i])
#                 print(hours_worked)
#         return hours_worked

#     def eligibility_for_w4h(self):
#         if self.system.system_type == "Laptop":
#             return "Eligible"
#         return "Not Eligible"

#     def book_meeting_room(self, meeting_room):
#         hours = int(input("Enter the number of hours for which you require to book {}".format(meeting_room)))
#         seats_rqd = int(input("Enter number of seats rqd : "))
#         projector_rqd = bool(input("Projector rqd : True/False : "))
#         if meeting_room.booking(hours, seats_rqd, True):
#             meeting_room.booked = True
#             return "Meeting Room Booked"
#         else:
#             return "Try a different Meeting Room"

# mn1 = Manager("Nick", 4545454)
# mn2 = Manager("Prem Kumar", 546587, "Senior Manager")
# mn1 = Manager("Sick", 74545)

# m1 = MeetingRoom("Ramanujan", False, 10, True)
# m2 = MeetingRoom("Vishveshwaraiya", False, 8, True)
# m3 = MeetingRoom("C V Raman", False, 25, True)
# m4 = MeetingRoom("Newton", False, 5, False)

# s1 = System("Laptop", "8gb")
# s2 = System("Desktop", "4gb")

# e1 = IT_Emp("pk", 5004, "SE-1", s1, mn1)
# e2 = IT_Emp("kp", 5665, "SE-2", s2, mn2)

# print(e1.desg)

# print(IT_Emp.return_number_of_it_employees(), 
#     Manager.return_no_of_manager(),
#     Employee.return_number_of_employees(), sep = "\n")


# print(e1, e2, sep = "\n")

# print(e1.system.system_type, e1.system.ram)
# print(e2.system.system_type, e2.system.ram)

# print(e1.eligibility_for_w4h())
# print(e2.eligibility_for_w4h())


# print(e1.system.request_for_change_of_system("monitor", "not minimal"))

# print(e1.book_meeting_room(m1))
# print(e2.book_meeting_room(m4))


# print("a", IT_Emp.return_number_of_employees())
# e1 = IT_Emp("pk", 5004, "SE-1") # object declaration
# print("b", e1.no_of_emp) # not a preffered way, class variables should not be accesswed using the objects
# print("a", IT_Emp.return_number_of_employees())
# e2 = IT_Emp("kp", 5665, "SE-2")
# print("c", IT_Emp.no_of_emp)
# print("b", e1.return_number_of_employees())
# print("a", IT_Emp.return_number_of_employees())
# e1.set_age(45)
# print(e1.get_age())

# print(e1.name, e1.desg,  e1.emp_id, e1.get_age())
# print(e2.name, e2.desg, e2.emp_id, e2.get_age())

# def emp_fill_timesheet(obj, week, hours):
#     obj.fill_timesheet(week, hours)
#     # try:
#     #     if getattr(obj, "timesheet"):
#     #         obj.fill_timesheet(week, [9.5, 9.5, 9.5, 9.5, 9.5], obj.timesheet)
#     # except AttributeError:
#     #     obj.fill_timesheet(week, [9.5, 9.5, 9.5, 9.5, 9.5])
#
#     # if week == 1:
#     #     obj.fill_timesheet(week, hours)
#     # else:
#     #     obj.fill_timesheet(week, hours, obj.timesheet)
#
# # emp_fill_timesheet(e1, 1, [9.5, 9.5, 9.5, 9.5, 9.5])
# emp_fill_timesheet(e1, 2, [9.5, 9.5, 9.5, 9.5, 9.5])
# emp_fill_timesheet(e1, 3, [9.5, 9.5, 9.5, 9.5, 9.5])
#
# emp_fill_timesheet(e2, 1, [9.5, 9.5, 9.5, 9.5, 9.5])
# emp_fill_timesheet(e2, 2, [9.5, 9.5, 9.5, 9.5, 9.5])
# emp_fill_timesheet(e2, 3, [9.5, 9.5, 9.5, 9.5, 9.5])
# emp_fill_timesheet(e2, 13, [9.5, 9.5, 9.5, 9.5, 9.5])
# emp_fill_timesheet(e2, 14, [9.5, 9.5, 9.5, 9.5, 9.5])
# emp_fill_timesheet(e2, 15, [9.5, 9.5, 9.5, 9.5, 9.5])
# emp_fill_timesheet(e2, 16, [9.5, 9.5, 9.5, 9.5, 9.5])
# emp_fill_timesheet(e2, 17, [9.5, 9.5, 9.5, 9.5, 9.5])
# emp_fill_timesheet(e2, 18, [9.5, 9.5, 9.5, 9.5, 9.5])
#
#
# print(e1, e1.timesheet)
# print(e2, e2.timesheet)
#
# # setattr(e1, "abc", "def") # e1.abc = def
# # print(getattr(e1, "abc"))
#
# print(e2.count_hours_worked(4))

# print(getattr(e1, "name"))

# try:
#     if getattr(e1, "timesheet"):
#         e1.fill_timesheet(1, [9.5, 9.5, 9.5, 9.5, 9.5], e1.timesheet)
#
# except AttributeError:
#     e1.fill_timesheet(1, [9.5, 9.5, 9.5, 9.5, 9.5])
#
# try:
#     if getattr(e1, "timesheet"):
#         e1.fill_timesheet(2, [9.5, 9.5, 9.5, 9.5, 9.5], e1.timesheet)
#
# except AttributeError:
#     e1.fill_timesheet(2, [9.5, 9.5, 9.5, 9.5, 9.5])




l = [1,2,3,4,5]
iter_obj = iter(l)
while True:
    try:
        print(next(iter_obj))
    except StopIteration:
        # print("Elements exhausted")
        break