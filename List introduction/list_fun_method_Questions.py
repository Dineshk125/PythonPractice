# """ " Q1. Example
# Input the length of the list : 4
# Enter number = 7
# Enter number = 14
# Enter number = 21
# Enter number = 28

# Answer = [7,14,21,28]
# """

# x = int(input("Input the length of the list: "))

# List = []
# for i in range(0, x):
#     num = int(input("Enter number : "))
#     List.append(num)
# print(List)

# """Q2. Create a list andd prompt the user for an old number followed by a 'new number'. If the old number exists in the list , relace it  with the new number provided by user.

# list = [5,10,15,20,15]
# Entet the old number : 15
# Enter new Number : 25

# updated list : [5,10,15,20,25]

# """
# list = [5, 10, 15, 20, 15]

# old_no = int(input("Enter the old Number: "))
# new_no = int(input("Enter the new Number: "))

# for i in range(0, len(list)):
#     if list[i] == old_no:
#         list[i] = new_no
# print(list)

# """Q2.: [5,10,25,20,25]

# Remove all even number in the list

# """
# list = [5, 10, 15, 20, 15]

# new_list = []
# for i in range(0, len(list)):
#     if list[i] % 2 != 0:
#         new_list.append(list[i])
# print(new_list)

# """Q3. Ask the user for a number. Then, from a list of numbers, remove all the numbers that can be divided by the number the user entered. (Do on your own).

# my_list = [10, 15, 20, 25, 30]

# Enter a number: 5

#     OUTPUT:[15,25]
# """

# my_list = [10, 15, 20, 25, 30]

# num = int(input("Enter a number: "))
# new_list = []
# for i in range(0, len(my_list)):
#     if my_list[i] % num != 0:
#         new_list.append(my_list[i])
# print(new_list)

# """
# Q4. Generate a list of at least 10 numbers. Then, create two separate lists called 'odd' and 'even. Put all the odd numbers from the original list into the 'odd' list, and all the even numbers into the 'even' list.

# ...

# my_list=[3, 8, 12, 17, 22, 30, 35, 41, 48, 50]

# # Output

# Odd [3, 17, 35, 41]

# Even [8, 12, 22, 30, 48, 50]

# """

# my_list = [3, 8, 12, 17, 22, 30, 35, 41, 48, 50]

# even = []
# odd = []

# for i in range(0, len(my_list)):
#     if my_list[i] % 2 == 0:
#         even.append(my_list[i])
#     else:
#         odd.append(my_list[i])
# print("The even numbers in list are : ", even)
# print("The odd numbers in a list are : ", odd)


# """
# 05. Start by creating two separate lists with random numbers. Then, create a third list that merges the numbers from the first and second lists together.

# list1 = [5, 8, 12, 15]

# list2 [3, 10, 18, 21]

# # OUTPUT

# Merged list: [5, 8, 12, 15, 3, 10, 18, 21]

# """

# list1 = [5, 8, 12, 15]

# list2 = [3, 10, 18, 21]

# list3 = []

# for i in range(0, len(list1)):
#     list3.append(list1[i])

# for i in range(0, len(list2)):
#     list3.append(list2[i])
# print(list3)
