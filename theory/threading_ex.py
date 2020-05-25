'''
    What is a Thread?
    In Computer Science, threads are defined as the smallest unit of work 
    which is scheduled to be done by an Operating System.

    Some points to consider about Threads are:

    Threads exists inside a process.
    Multiple threads can exist in a single process.
    Threads in same process share the state and memory of the parent process.

   A thread lies only in one of the shown states at any instant:
      New.
      Runnable.
      Blocked.
      Waiting.
      Timed Waiting.
      Terminated.
'''

# # import time
# from time import time, sleep
# from threading import Thread
# # import threading

# def calc_square(num):
#    print("calculating square of numbers")
#    for n in num:
#       sleep(0.2)
#       print("square : ", n * n)

# def calc_cube(num):
#    print("calculating cube of numbers")
#    for n in num:
#       sleep(0.2)
#       print("cube : ", n * n * n)

# l = [2, 4, 6, 8]
# t = time()

# # calc_square(l)
# # calc_cube(l)

# t1 = Thread(target = calc_square, args = (l,))  # declaration of thread
# t2 = Thread(target = calc_cube, args = (l,))

# t1.start()
# t2.start()

# print(type(t1))

# t1.join() # wait until the other program is done
# t2.join()

# print("done in : ", time() - t)



# import time
# # import threading
# from threading import Thread

# def sleepMe(i):
#     print("Thread %i going to sleep for 3 seconds." % i)
#     time.sleep(3)
#     print("Thread %i is awake now." % i)

# for i in range(10):
#     th = Thread(target=sleepMe, args=(i, ))
#     th.start()

# while 1:
#    pass




# import _thread
# import time

# # Define a function for the thread
# def print_time( threadName, delay):
#    count = 0
#    while count < 5:
#       time.sleep(delay)
#       count += 1
#       print ("%s: %s" % ( threadName, time.ctime(time.time()) ))

# # Create two threads as follows
# try:
#    _thread.start_new_thread( print_time, ("Thread-1", 2, ) )
#    _thread.start_new_thread( print_time, ("Thread-2", 4, ) )
# except:
#    print ("Error: unable to start thread")

# while 1:
#    pass
'''
Running several threads is similar to running several different programs concurrently, 
but with the following benefits −

Multiple threads within a process share the same data space with the main thread and 
can therefore share information or communicate with each other more easily than if they 
were separate processes.

Threads are sometimes called light-weight processes and they do not require much memory 
overhead; they are cheaper than processes.

A thread has a beginning, an execution sequence, and a conclusion. It has an instruction 
pointer that keeps track of where within its context is it currently running.

It can be pre-empted (interrupted).

It can temporarily be put on hold (also known as sleeping) while other threads are running - 
this is called yielding.

There are two different kind of threads −

kernel thread
user thread

Kernel Threads are a part of the operating system, while the User-space threads are not 
implemented in the kernel.

There are two modules which support the usage of threads in Python3 −

_thread
threading

The thread module has been "deprecated" for quite a long time. Users are encouraged to use 
the threading module instead. Hence, in Python 3, the module "thread" is not available anymore. 
However, it has been renamed to "_thread" for backwards compatibilities in Python3.

from threading import thread
or 
import _thread

Starting a New Thread
To spawn another thread, you need to call the following method available in the thread module −

_thread.start_new_thread ( function, args[, kwargs] )
This method call enables a fast and efficient way to create new threads in both Linux and Windows.

The method call returns immediately and the child thread starts and calls function with the 
passed list of args. When the function returns, the thread terminates.

Here, args is a tuple of arguments; use an empty tuple to call function without passing any 
arguments. kwargs is an optional dictionary of keyword arguments.
'''

# !/usr/bin/python python3.4

# import _thread
# import time

# # Define a function for the thread
# def print_time( threadName, delay):
#    count = 0
#    print(threadName ,time.ctime(time.time()))
#    while count < 5:
#       time.sleep(delay)
#       count += 1
#       print ("%s: %s" % ( threadName, time.ctime(time.time()) ))

# # Create two threads as follows
# try:
#    _thread.start_new_thread( print_time, ("Thread-1", 2, ) )
#    _thread.start_new_thread( print_time, ("Thread-2", 4, ) )
# except:
#    print ("Error: unable to start thread")

# while 1:
#    pass

'''Output
When the above code is executed, it produces the following result −

Thread-1: Fri Feb 19 09:41:39 2016
Thread-2: Fri Feb 19 09:41:41 2016
Thread-1: Fri Feb 19 09:41:41 2016
Thread-1: Fri Feb 19 09:41:43 2016
Thread-2: Fri Feb 19 09:41:45 2016
Thread-1: Fri Feb 19 09:41:45 2016
Thread-1: Fri Feb 19 09:41:47 2016
Thread-2: Fri Feb 19 09:41:49 2016
Thread-2: Fri Feb 19 09:41:53 2016
'''
'''Program goes in an infinite loop. You will have to press ctrl-c to stop

Although it is very effective for low-level threading, the thread module is very limited 
compared to the newer threading module.

The Threading Module
The newer threading module included with Python 2.x provides much more powerful, 
high-level support for threads than the thread module discussed in the previous section.

The threading module exposes all the methods of the thread module and provides some 
additional methods −

threading.activeCount() − Returns the number of thread objects that are active.

_thread
threading.currentThread() − Returns the number of thread objects in the caller's thread control.

threading.enumerate() − Returns a list of all thread objects that are currently active.

In addition to the methods, the threading module has the Thread class that implements threading. 
The methods provided by the Thread class are as follows −

run() − The run() method is the entry point for a thread.

start() − The start() method starts a thread by calling the run method.

join([time]) − The join() waits for threads to terminate.

isAlive() − The isAlive() method checks whether a thread is still executing.

getName() − The getName() method returns the name of a thread.

setName() − The setName() method sets the name of a thread.

'''

'''Creating Thread Using Threading Module
To implement a new thread using the threading module, you have to do the following −

Define a new subclass of the Thread class.

Override the __init__(self [,args]) method to add additional arguments.

Then, override the run(self [,args]) method to implement what the thread should do when started.

Once you have created the new Thread subclass, you can create an instance of it and then start a new thread by invoking the start(), which in turn calls the run() method.
'''


#!/usr/bin/python3

# import _thread
# import time

# exitFlag = 0

# class myThread (_thread):
#    def __init__(self,  name, counter):
#       _thread.__init__(self)
#       self.threadID = None
#       self.name = name
#       self.counter = counter
#    def run(self):
#       print ("Starting " + self.name)
#       print_time(self.name, self.counter, 5)
#       print ("Exiting " + self.name)

# def print_time(threadName, delay, counter):
#    while counter:
#       if exitFlag:
#          threadName.exit()
#       time.sleep(delay)
#       print ("%s: %s" % (threadName, time.ctime(time.time())))
#       counter -= 1

# # Create new threads
# thread1 = myThread( "Thread-1",1)
# thread2 = myThread( "Thread-2",2)

# # Start new Threads
# thread1.start()
# thread2.start()
# thread1.join()
# thread2.join()
# print ("Exiting Main Thread")

# Result
# When we run the above program, it produces the following result −

# Starting Thread-1
# Starting Thread-2
# Thread-1: Fri Feb 19 10:00:21 2016
# Thread-2: Fri Feb 19 10:00:22 2016
# Thread-1: Fri Feb 19 10:00:22 2016
# Thread-1: Fri Feb 19 10:00:23 2016
# Thread-2: Fri Feb 19 10:00:24 2016
# Thread-1: Fri Feb 19 10:00:24 2016
# Thread-1: Fri Feb 19 10:00:25 2016
# Exiting Thread-1
# Thread-2: Fri Feb 19 10:00:26 2016
# Thread-2: Fri Feb 19 10:00:28 2016
# Thread-2: Fri Feb 19 10:00:30 2016
# Exiting Thread-2
# Exiting Main Thread


'''Synchronizing Threads
The threading module provided with Python includes a simple-to-implement locking mechanism 
that allows you to synchronize threads. A new lock is created by calling the Lock() method, 
which returns the new lock.

The acquire(blocking) method of the new lock object is used to force the threads to run 
synchronously. The optional blocking parameter enables you to control whether the thread 
waits to acquire the lock.

If blocking is set to 0, the thread returns immediately with a 0 value if the lock cannot be 
acquired and with a 1 if the lock was acquired. If blocking is set to 1, the thread blocks 
and wait for the lock to be released.

The release() method of the new lock object is used to release the lock when it is 
no longer required.
'''

#!/usr/bin/python3

# import threading
# import time

# class myThread (threading.Thread):
#    def __init__(self, threadID, name, counter):
#       threading.Thread.__init__(self)
#       self.threadID = threadID
#       self.name = name
#       self.counter = counter
#    def run(self):
#       print ("Starting " + self.name)
#       # Get lock to synchronize threads
#       threadLock.acquire()
#       print_time(self.name, self.counter, 3)
#       # Free lock to release next thread
#       threadLock.release()

# def print_time(threadName, delay, counter):
#    while counter:
#       time.sleep(delay)
#       print ("%s: %s" % (threadName, time.ctime(time.time())))
#       counter -= 1

# threadLock = threading.Lock()
# threads = []

# # Create new threads
# thread1 = myThread(1, "Thread-1", 1)
# thread2 = myThread(2, "Thread-2", 2)

# # Start new Threads
# thread1.start()
# thread2.start()

# # Add threads to thread list
# threads.append(thread1)
# threads.append(thread2)

# # Wait for all threads to complete
# for t in threads:
#    t.join()
# print ("Exiting Main Thread")

# Output
# When the above code is executed, it produces the following result −

# Starting Thread-1
# Starting Thread-2
# Thread-1: Fri Feb 19 10:04:14 2016
# Thread-1: Fri Feb 19 10:04:15 2016
# Thread-1: Fri Feb 19 10:04:16 2016
# Thread-2: Fri Feb 19 10:04:18 2016
# Thread-2: Fri Feb 19 10:04:20 2016
# Thread-2: Fri Feb 19 10:04:22 2016
# Exiting Main Thread

'''Multithreaded Priority Queue
The Queue module allows you to create a new queue object that can hold a specific number of items. There are following methods to control the Queue −

get() − The get() removes and returns an item from the queue.

put() − The put adds item to a queue.

qsize() − The qsize() returns the number of items that are currently in the queue.

empty() − The empty( ) returns True if queue is empty; otherwise, False.

full() − the full() returns True if queue is full; otherwise, False.
'''
#!/usr/bin/python3

# import queue
# import threading
# import time

# exitFlag = 0

# class myThread (threading.Thread):
#    def __init__(self, threadID, name, q):
#       threading.Thread.__init__(self)
#       self.threadID = threadID
#       self.name = name
#       self.q = q
#    def run(self):
#       print ("Starting " + self.name)
#       process_data(self.name, self.q)
#       print ("Exiting " + self.name)

# def process_data(threadName, q):
#    while not exitFlag:
#       queueLock.acquire()
#       if not workQueue.empty():
#          data = q.get()
#          queueLock.release()
#          print ("%s processing %s" % (threadName, data))
#       else:
#          queueLock.release()
#          time.sleep(1)

# threadList = ["Thread-1", "Thread-2", "Thread-3"]
# nameList = ["One", "Two", "Three", "Four", "Five"]
# queueLock = threading.Lock()
# workQueue = queue.Queue(10)
# threads = []
# threadID = 1

# # Create new threads
# for tName in threadList:
#    thread = myThread(threadID, tName, workQueue)
#    thread.start()
#    threads.append(thread)
#    threadID += 1

# # Fill the queue
# queueLock.acquire()
# for word in nameList:
#    workQueue.put(word)
# queueLock.release()

# # Wait for queue to empty
# while not workQueue.empty():
#    pass

# # Notify threads it's time to exit
# exitFlag = 1

# # Wait for all threads to complete
# for t in threads:
#    t.join()
# print ("Exiting Main Thread")

'''Output
When the above code is executed, it produces the following result −

Starting Thread-1
Starting Thread-2
Starting Thread-3
Thread-1 processing One
Thread-2 processing Two
Thread-3 processing Three
Thread-1 processing Four
Thread-2 processing Five
Exiting Thread-3
Exiting Thread-1
Exiting Thread-2
Exiting Main Thread

'''