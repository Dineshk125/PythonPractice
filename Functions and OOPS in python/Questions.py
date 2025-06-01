# """
# Q1. Write a Python function to reverse a string using slicing and return it.

# """


# def reverse(string=""):

#     return string[::-1]


# x = reverse("Dinesh")
# print(x)


# """
# Q2. Write a Python function that accepts a string and counts the number of upper and lower case letters. 1

# """


# def st_count(string=""):
#     u = 0
#     l = 0
#     for i in string:
#         if i.isalpha():
#             if i.isupper():
#                 u += 1
#             else:
#                 l += 1
#     print(f"Total upper latters are: {u}")
#     print(f"Total  lower latters are: {l}")


# st_count("DinesH &*()%$#JHUI")

# """
# Q3. Write a Python function that takes a list and returns a new list with distinct elements from the first list.

#     Sample List: [10,20,20,20,10,10,50]

#     Unique List: [10,20,50]

# """


# def si_list(l=[]):
#     new_list = []
#     for i in l:
#         if i not in new_list:
#             new_list.append(i)
#     print(f"The disting elements are: {new_list}")


# si_list([10, 10, 20, 30, 30])


# def si_list(l=[]):
#     sett = set(l)
#     new_list = list(sett)

#     print(f"The Distingt element are: {new_list}")


# si_list([10, 20, 20, 30, 30, 10])


# """
# Q4. Write a Python function that takes a number as a parameter and checks whether the number is prime or not.

# """


# def numb(n1):
#     c = 0
#     for i in range(1, n1 + 1):
#         if n1 % i == 0:
#             c = c + 1
#     if c == 2:
#         print("The number is prime ")
#     else:
#         print("The number is not prime")
# numb(13)


# """
# Q5. Write a Python function that takes start_number and end_number as a parameter.
#     Now print all the prime numbers between start_number to end_number.

# """


# def is_prime(st_no=0, end_no=0):
#     new_list = []
#     for i in range(st_no, end_no + 1):
#         c = 0
#         for j in range(1, i + 1):
#             if i % j == 0:
#                 c += 1
#         if c == 2:
#             new_list.append(i)
#     print(f"The prime number from {st_no} to {end_no} is : {new_list}")


# is_prime(1, 10)


"""
Q6. Python function to print even length words in a string.

"""


def count_length(s=""):
    l = s.split()
    new_list = []

    for i in l:
        c = 0
        for j in i:
            c += 1
        if c % 2 == 0:
            new_list.append(i)
    print(f"Even length of word in string is : {new_list}")


count_length("hii i am dinesh kumawat ")
