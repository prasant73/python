#!/usr/bin/python
import time;  # This is required to include time module.

ticks = time.time()
print ("Number of ticks since 12:00am, January 1, 1970:", ticks)

# localtime = time.localtime(time.time())
# print ("Local current time :", localtime)

# localtime = time.asctime( time.localtime(time.time()) )
# print ("Local current time :", localtime)

import calendar

# cal = calendar.month(2008, 1)
# print ("Here is the calendar:")
# print (cal)

# print(time.altzone)
# print(time.clock( ))
# print(time.process_time())
# print(time.ctime())
# print(time.asctime(localtime(secs)))




# print(calendar.calendar(2018,w=2,l=1,c=6))
# print(calendar.isleap(2018))
# print(calendar.leapdays(1999, 2017))




# datetime module
import datetime
print(datetime.MINYEAR)
print(datetime.MAXYEAR)
print(datetime.datetime.now())

# datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)

# from datetime import timedelta
# d = timedelta(microseconds=-1)
# (d.days, d.seconds, d.microseconds)
# (-1, 86399, 999999)

'''
>>> from datetime import timedelta
>>> year = timedelta(days=365)
>>> another_year = timedelta(weeks=40, days=84, hours=23,
...                          minutes=50, seconds=600)  # adds up to 365 days
>>> year.total_seconds()
31536000.0
>>> year == another_year
True
>>> ten_years = 10 * year
>>> ten_years, ten_years.days // 365
(datetime.timedelta(days=3650), 10)
>>> nine_years = ten_years - year
>>> nine_years, nine_years.days // 365
(datetime.timedelta(days=3285), 9)
>>> three_years = nine_years // 3
>>> three_years, three_years.days // 365
(datetime.timedelta(days=1095), 3)
>>> abs(three_years - ten_years) == 2 * three_years + year
True
'''

'''
>>> import time
>>> from datetime import date
>>> today = date.today()
>>> today
datetime.date(2007, 12, 5)
>>> today == date.fromtimestamp(time.time())
True
>>> my_birthday = date(today.year, 6, 24)
>>> if my_birthday < today:
...     my_birthday = my_birthday.replace(year=today.year + 1)
>>> my_birthday
datetime.date(2008, 6, 24)
>>> time_to_birthday = abs(my_birthday - today)
>>> time_to_birthday.days
202
'''


'''
>>> from datetime import date
>>> d = date.fromordinal(730920) # 730920th day after 1. 1. 0001
>>> d
datetime.date(2002, 3, 11)
>>> t = d.timetuple()
>>> for i in t:     
...     print(i)
2002                # year
3                   # month
11                  # day
0
0
0
0                   # weekday (0 = Monday)
70                  # 70th day in the year
-1
>>> ic = d.isocalendar()
>>> for i in ic:    
...     print(i)
2002                # ISO year
11                  # ISO week number
1                   # ISO day number ( 1 = Monday )
>>> d.isoformat()
'2002-03-11'
>>> d.strftime("%d/%m/%y")
'11/03/02'
>>> d.strftime("%A %d. %B %Y")
'Monday 11. March 2002'
>>> 'The {1} is {0:%d}, the {2} is {0:%B}.'.format(d, "day", "month")
'The day is 11, the month is March.'
'''



'''
>>> from datetime import datetime
>>> datetime.now().isoformat(timespec='minutes')   # doctest: +SKIP
'2002-12-25T00:00'
>>> dt = datetime(2015, 1, 1, 12, 30, 59, 0)
>>> dt.isoformat(timespec='microseconds')
'2015-01-01T12:30:59.000000'
'''


# import datetime
# from dateutil.parser import parse

# date_data = '19/Jan-22 15:23:42.993752'
# # print(date_data.strptime())
# date_data = datetime.datetime.now()
# date_data = date_data.strptime('19/Jan-22 15:23:42.993752', '%y/%b-%d %H:%M:%S.%f')
# print(date_data, type(date_data))

# dt = parse('2018-12-29 12:09:58.544347')
# print(dt, type(dt))
