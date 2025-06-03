def add(x: int, y: int) -> int:
    total = x + y
    print(total)


def add2(name: str, age: int, percent: float):
    print(name)
    print(age)
    print(percent)


add2("Dinesh", 23, 99.99)


a = [1, 2, 7, 7, 34, 5, 67, 7]

a.sort()
print(a)

c = a.count(7)
print(c)


# def sumof(n1: int, n2: int, n3: int):
def sum_of(n1):
    print(sum(n1))


sum_of([1, 2, 3, 4])
from typing import *


def sum_of_list(x: list[int]):
    print(sum(x))


sum_of_list([1, 2, 3])
