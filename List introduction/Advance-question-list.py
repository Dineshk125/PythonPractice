# """
# Q1. Make a list of your own. And remove all the duplicates element from that list.

# my_list=[5, 1, "Code and Debug", 5, 10, 20, 5, 1, 1]

# #OUTPUT [5, 1, "Code and Debug", 10, 20]

# """

# my_list = [5, 1, "Code and Debug", 5, 10, 20, 5, 1, 1]

# up_list = []

# for i in range(0, len(my_list)):
#     if my_list[i] not in up_list:
#         up_list.append(my_list[i])
# print(up_list)

# """
# Q2. Make a list. Then ask a number from user. If number exists in that list then print the position of the element else print -1.

# my_list=[5, 1, 5, 10, 20, 5, 1, 1]

# Enter value = 10

# #OUTPUT=3

# Enter value = 5

# OUTPUT 0

# Enter value 160

# OUTPUT-1

# #"""

# my_list = [5, 1, 5, 10, 20, 5, 1, 1]

# num = int(input("Enter a number: "))

# for i in range(0, len(my_list)):
#     if num == my_list[i]:
#         print(i)
#     elif num not in my_list:
#         print(-1)
#         break


# """
# 03. Take 10 integer inputs from user and store them in a list. Now, copy all the elements in another list but in reverse order.

# my_list=[5, 1, 5, 10, 20, 5, 1, 1]

# Output

# """
# # method 1

# my_list = [5, 1, 5, 10, 20, 5, 1, 1]
# rev = []

# for i in range(0, 10):
#     new_list = int(input("Enter values : "))
#     my_list.extend([new_list])
# print("new list added in my list", my_list)

# my_list.reverse()
# rev = my_list
# print("reverse both list in another list :", rev)

# ## method 2

# my_list = [5, 1, 5, 10, 20, 5, 1, 1]
# rev = []

# for i in range(0, 10):
#     new_list = int(input("Enter values : "))
#     my_list.extend([new_list])
# print("new list added in my list", my_list)

# for i in range(len(my_list) - 1, -1, -1):
#     rev.append(my_list[i])
# print("reverse both list in another list :", rev)


# """
# Q4. Write a program to find the average of all the numbers present in the list. (Do on your own)

# """

# list = [1, 2, 3, 5, 6, 8, 6, 7, 2, 46, 456, 9, 659, 8]

# average = sum(list) / len(list)
# print(average)


# """
# Q5. Write a Python code to find the occurrence of each element in a list and print the element with the highest occurrence

# """

# list = [1, 8, 6, 8, 6, 7, 5, 2, 3, 5, 3, 6, 7, 64, 64, 2, 3, 5, 6, 8]
# print(list)
# new = []

# for i in range(0, len(list)):
#     if list[i] not in new:
#         new.append(list[i])
# print(new)
# occur_Ele = 0
# occ_count = 0

# for j in new:
#     c = list.count(j)
#     print(f"{j} is occur in {c} times")
#     if c > occ_count:
#         occ_count = c
#         occur_Ele = j
# print(f"highest element occerence : {occur_Ele}")

# """

# Q6. Write a program that has two lists and make a new list that contains only the common elements between them without duplicates.

# # Example 1

# list1= [1, 2, 3, 4, 5]

# list2 [3, 4, 5, 6, 7]

# # Output

# [3, 4, 5]

# # Example 2

# list1 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# list2 [5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

# # Output

# [5, 6, 7, 8, 9,

# 10]

# """

# list1 = [1, 2, 3, 4, 5, 1, 5, 3]

# list2 = [3, 4, 5, 6, 7]

# list3 = []

# for i in list1:
#     for j in list2:
#         if i == j:
#             list3.append(i)
# print(list3)

# new = []

# for i in range(0, len(list3)):
#     if list3[i] not in new:
#         new.append(list3[i])
# print(new)

# # #method 2

# list1 = [1, 2, 3, 4, 5, 1, 5, 3, 3, 33, 3, 3, 3, 3, 3, 3]

# list2 = [3, 4, 5, 6, 7]

# list3 = []

# for i in list1:
#     if i in list2:
#         if i not in list3:
#             list3.append(i)
# print(list3)


# """

# Q7. Write a Python code to find the second largest element in a list without sorting.


# """

# list = [3, 4, 5, 6, 3, 298, 7, 23, 90, 100, 29, 101]

# larg = list[0]
# secondLarg = -1

# for i in range(1, len(list)):
#     if list[i] > larg:
#         larg = list[i]
#     elif list[i] > secondLarg and list[i] != larg:
#         secondLarg = list[i]
# print(secondLarg)

# ## method 2

# list = [3, 4, 5, 6, 3, 298, 7, 23, 90, 100, 29, 101]

# larg = list[0]

# for i in range(0, len(list)):
#     if list[i] > larg:
#         larg = list[i]
# print(list)

# slarg = list[0]

# for i in range(0, len(list)):
#     if list[i] > slarg:
#         slarg = list[i]
# print(slarg)

# """

# Q8. Make a program that takes a list of integers and returns the product of all the elements.

# """

# n = int(input("Enter the length: "))

# list = []

# for i in range(1, n + 1):
#     m = float(input(f"Enter the {i} element : "))
#     list.append(m)
# print(list)

# product = 1

# for i in range(0, n):
#     product = product * list[i]
# print("The product of list is : ", product)


# """

# 09. Write a program to find and print all prime numbers within a given

# man List 12, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 151

# """

# list = [12, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 151]

# list2 = []

# for i in range(0, len(list)):
#     factor = 0
#     for j in range(1, i + 1):
#         if i % j == 0:
#             factor += 1
#     if factor == 2:
#         list2.append(i)
# print(list2)

# """

# # Q10. Write a program to split a given list into two halves. (Do on your own)


# # """

list = [12, 3, 4, 6, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

n = len(list)
hl = int(n / 2)

list1 = []
list2 = []

for i in range(0, hl + 1):
    list1.append(list[i])
for j in range(hl + 1, n):
    list2.append(list[j])

print(list1)
print(list2)


# """

# 0120. Write a program that swaps the first and last elements of a given list.

# num_list = [32, 10, "Anirudh", 55.90, "xyz"]

# Output

# ["xyz", 10, "Anirudh", 55.90, 32]

#  Example 2

# num_list = [100, 900]

#  Output

#  [900, 100

#  """


# num_list = [32, 10, "Anirudh", 55.90, "xyz"]
# temp = num_list[0]
# num_list[0] = num_list[len(num_list) - 1]
# num_list[len(num_list) - 1] = temp
# print(num_list)
