""" """

from datetime import datetime
from time import sleep


def cal_time(func):
    def wrapper(*args):
        starttime = datetime.now()
        print("start wrapper")
        sleep(1)
        func(*args)
        endtime = datetime.now()
        print("End wrapper")
        print(endtime - starttime)

    return wrapper


@cal_time
def sum_of(*args):
    print(sum(args))


sum_of(2, 3, 4)
