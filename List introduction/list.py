"""To store multipal values in a single variable."""

# list = [1, 2, 3, 4, 5, 745, 34, 3]
# print(list, type(list))


# list = [1, 3, "jhon", "deo", -34, 32.56, False, True, 323, 89]

# print(list[0], type(list[1]))
# print(list[-3], type(list[-3]))
# print(list[5], type(list[5]))
# print(list[3], type(list[3]))

# """ Iteration of list """
# list = [1, 3, "jhon", "deo", -34, 32.56, False, True, 323, 89]
# # n = len(list)
# # for i in range(0, n):
# #     print(list[i], end=" ")

# for i in range(0, len(list)):
#     print(list[i])

# """ Iterate by value.
#     Iterate by index/position.
#  """

# a = [1, 2, 3, 4, 5, 6, 7]

# for i in range(0, len(a)):
#     print(a[i])


# """ Q1. reverse a list. """

# a = [1, 3, 5, 6, 7, 9, "str", True, 44.22, 10]

# for i in range(len(a) - 1, -1, -1):
#     print(a[i])

# """ Q2. print all even number present in the list. """
## iteration by value
# a = [1, 3, 5, 6, 7, 9, True, 44.22, 10]
# count = 0
# for i in a:
#     if i % 2 == 0:
#         print(i, end=" ")

# """ Q2. print all even number present in the list. """
## iteration by index

# a = [1, 3, 5, 6, 7, 9, True, 44.22, 10]
# count = 0
# for i in range(0, len(a)):
#     if a[i] % 2 == 0:
#         print(count, end=" ")

# """ Q3. print how many even number present in the list. """

# a = [1, 3, 5, 6, 7, 9, True, 44.22, 10]
# count = 0
# for i in range(0, len(a)):
#     if a[i] % 2 == 0:
#         count += 1
# print(count, end=" ")

# """ Q4. print sum of all even numbers present in the list. """

# a = [1, 3, 5, 6, 7, 9, True, 44.22, 10]
# sum = 0
# for i in range(0, len(a)):
#     if a[i] % 2 == 0:
#         sum = sum + a[i]
# print(sum, end=" ")


# """ Q5. print sum of all even numbers that are divisible by 2 and 5 in the list. """

# a = [1, 3, 5, 6, 7, 9, True, 44.22, 10]
# sum = 0
# for i in range(0, len(a)):
#     if a[i] % 2 == 0 and a[i] % 5 == 0:
#         sum = sum + a[i]
# print(sum, end=" ")


# """ Q6. print all even numbers that are divisible by 2 and 5 in the list. """

# a = [1, 3, 5, 6, 7, 9, True, 44.22, 10]
# sum = 0
# for i in range(0, len(a)):
#     if a[i] % 2 == 0 and a[i] % 5 == 0:
#         print(a[i], end=" ")


# """ Q7. print sum of all even numbers that are divisible by 3 and 4 in the list. """

# a = [1, 3, 5, 6, 7, 9, True, 44.22, 10, 12]
# sum = 0
# for i in range(0, len(a)):
#     if a[i] % 3 == 0 or a[i] % 4 == 0:
#         sum = sum + a[i]
# print(sum, end=" ")

# """ Q8. print sum of all even numbers that are divisible by 3 and 4 in the list. """

# a = [1, 3, 5, 6, 7, 9, True, 44.22, 10, 12]
# for i in range(0, len(a)):
#     if a[i] % 3 == 0 or a[i] % 4 == 0:
#         print(a[i], end=" ")

# """ Q9. print sum of all odd numbers that are present in the list. """

# a = [1, 3, 5, 6, 7, 9, True, 44.22, 10, -1, 12]
# for i in range(0, len(a)):
#     if a[i] % 2 != 0:
#         print(a[i], end=" ")

# """ Q10. print all even numbers that are present in the even index position in a list. """

# a = [1, 3, 5, 6, 7, 9, True, 44.22, 10, -1, 12]
# for i in range(0, len(a)):
#     if i % 2 == 0:
#         print(a[i], end=" ")


# """ Q11. Make your own list. Print how many positive and negative numbers are here. (Do on your own) """

# a = [1, -3, -5, -6, 7, 9, True, 44.22, 0, 0, 10, -1, 12]
# Positive = 0
# Nagitive = 0
# Zero = 0
# for i in range(0, len(a)):
#     if a[i] > 0:
#         Positive += 1
#     elif a[i] < 0:
#         Nagitive += 1
#     else:
#         Zero += 1
# print("Total number are positive in a list: ", Positive)
# print("Total number are nagitive in a list is: ", Nagitive)
# print("Total number are in a list is: ", Zero)

# """
# Q102. Make your own list. Print the largest number present in that list.

# my_list = [51, 85, 1748, 52, 44, 100, 200]

# # Output

# #1748


# """

# my_list = [51, 85, 1748, 52, 44, 100, 200]
# large = my_list[0]
# for i in range(0, len(my_list)):
#     if large <= my_list[i]:
#         large = my_list[i]
# print(large)

"""
Q102. Make your own list. Print the samllest number present in that list.

my_list = [51, 85, 1748, 52, 44, 100, 200]

# Output

#1748


"""

my_list = [51, 85, 1748, 52, 44, 100, 200]
large = my_list[0]
for i in range(0, len(my_list)):
    if large >= my_list[i]:
        large = my_list[i]
print(large)
