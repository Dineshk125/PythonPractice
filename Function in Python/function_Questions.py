"""
Q166. Write a function that accepts an integer and prints the
multiplication table for that number up to 10.

"""


def table(n):
    for i in range(1, 11):
        print(f"{n} * {i} = {n*i} ")


## call by value
table(10)

## call by reference

a = 29
table(a)

"""
Q167. Write a function that accepts an integer and prints whether it is odd
        or even.

"""


def maxi(n):
    if n % 2 == 0:
        print(f"The {n} is even number.")
    else:
        print(f"The {n} is odd number.")


maxi(10)

"""
Q168. Write a function that takes three numbers as parameters and prints
the largest among them.

"""


def largest(x, y, z):

    if x > y and x > z:
        print(f"The largest number is {x}")
    elif y > z and y > x:
        print(f"The largest number is {y}")
    else:
        print(f"Largest Number is {z}")


largest(12, 45, 67)


"""
Q169. Write a function that takes an integer and prints whether it is a
prime number.

"""


def prime(p):
    c = 0
    for i in range(1, p + 1):
        if p % i == 0:
            c += 1
    if c == 2:
        print(f"The number {p} is prime number.")

    else:
        print(f"The number {p} is not Prime Number.")


prime(2)

"""
Q170. Write a function that takes a list of numbers and prints the sum and
average of these numbers.

"""


def list1(listt=[]):
    summ = 0
    for i in listt:
        summ += i
    print(f"sum of list is : {summ}")
    print(f"average of list is: {summ/len(listt)}")


list1(listt=[10, 30, 40])

"""
Q171. Write a function that accepts a string and prints the frequency of
each character in the string

"""


def f_string(s=""):
    d = {}
    for i in s:
        d[i] = s.count(i)
    for k, v in d.items():
        print(f"The frequence of {k} is {v}")
    print(d)


f_string("Hello")

"""
Q172. Write a function that takes a string and prints whether it is a
palindrome.
QUESTIONS 166 - 172
FUNCTIONS IN PYTHON


"""


def is_palindrome(p=""):

    if p == p[::-1]:
        print(f"the number {p} is palindrome")
    else:
        print(f"The number {p} is not prime.")


is_palindrome("121")
