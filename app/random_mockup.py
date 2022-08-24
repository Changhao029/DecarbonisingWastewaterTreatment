import random
from random import randrange
from datetime import timedelta
from datetime import datetime

d1 = datetime.strptime('1/1/2008 1:30 PM', '%m/%d/%Y %I:%M %p')
d2 = datetime.strptime('1/1/2009 4:50 AM', '%m/%d/%Y %I:%M %p')


def random_date(start, end, num):
    list_random_time = list()
    delta = end - start
    total_sec = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(total_sec)
    for i in range(num):
        random_time = start + timedelta(seconds=random_second)
        str_random_time = random_time.strftime('%m/%d/%Y %I:%M %p')
        list_random_time.append(str_random_time)
    return list_random_time


print(random_date(d1, d2, 6))

list_a = ["231824A", "231825A", "231826A", "231827A", "231828A"]
def random_type(a, b):
    list1 = []

    for i in range(a):
        tmp = random.choice(b)
        list1.append(tmp)
    return list1

print(random_type(10, list_a))


def random_float(first_num, end_number, decimal, times):
    number_list = []
    for i in range(times):
        tmp = round(random.uniform(first_num, end_number), decimal)
        number_list.append(tmp)
    return number_list


print(random_float(1.0, 100.0, 4, 4))


