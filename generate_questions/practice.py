import random
from global_list import list_ques_numbers
import os
solved = []
count = 0
min, max = 1, 63

# generate random numbers
def generate_number(min, max):
    return random.randint(min, max)

# select the question in the given range
def question_selector(n):
    d = {}
    for i in n:
        splitting_values = i.split(".", 1)
        d[splitting_values[0]] = splitting_values[1]
    count = 0
    while count<5:
        print("{}".format(count+1), random.choice(list(d.values())))
        count += 1
    # global list_ques_numbers, count
    # l = []
    # while (count<5):    
    #     i = generate_number(min, max)
    #     if i not in list_ques_numbers:
    #         l.append(i)
    #         count += 1
    # print("the questions selected for you are : ")
    # for i in l:
    #     print(i)
    # return l

'''
input the topic, 
according to topic, generate the numbers and append them to its corresponding list

'''
def topic_selector(topic, n):
    question_list = []
    file = topic + "_questions"
    if topic == "list":
        if os.path.isfile(file):
            with open(file, "r") as f:
                # question_list.append(f.readlines())
                a = f.read()
        else:
            print("No {} file".format(file))
            return None
    a = a.split("\n\n")
    return question_selector(a)


topic = input("enter the topic you want to solve amongst list/string/dictionary : ")
n = int(input("Enter the number of questions you want to solve : "))
topic_selector(topic, n)


