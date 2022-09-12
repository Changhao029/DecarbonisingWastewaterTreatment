import random
from random import randrange
from datetime import timedelta
from datetime import datetime


class RandomFakeData():

    def random_int(self):
        return random.randint(80,200)

    def random_date(self):
        d1 = datetime.strptime('2008-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
        d2 = datetime.strptime('2009-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
        delta = d2 - d1
        # total_sec = (delta.days * 24 * 60 * 60) + delta.seconds
        total_sec = (delta.days * 24 * 60 * 60)
        random_second = randrange(total_sec)
        random_time = d1 + timedelta(seconds=random_second)
        str_random_time = random_time.strftime('%Y-%m-%d %H:%M:%S')
        return random_time

    def random_station(self):
        station = random.randint(1,5)
        return station

    def random_float(self, decimal):
        number_list = list()
        float = round(random.uniform(80, 200), decimal)
        return float
        # print(random_float(1.0, 100.0, 4, 4))
