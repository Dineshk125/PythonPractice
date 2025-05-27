# split method -> to convert string in to list

# string = "hello i am Dinesh"

# string.split() # split give output as a list and it split default by space(" ")
# print(string)

# string = "hello i am Dinesh"

# list = string.split() # split the string and make element of list.
# print(list)

# string = "-hello-i-am-Dinesh"

# m_list = string.split("-")
# print(m_list, type(m_list))


# joi() -> it convert list in to the string, by joining list element.

# string = "hello-i-am-Dinesh"
# print("original string: ", string)

# list = string.split("-")
# print("str to list ", list, "\n", type(list))

# string2 = "-".join(list)

# print("list to string : ", string2, "\n", type(string2))

# list = ["Dinesh", "birth", "date", "is", 19]
# # str = " ".join(list) #TypeError: sequence item 4: expected str instance, int found
# str = " ".join(str(i) for i in list)
# print(str)

# reverse string

# list = ["Dinesh", "birth", "date", "is", 19]
# str = " ".join(str(i)[::-1] for i in list)
# print(str)

# """
# Q1. Write a program to reverse the order of words.

# #Example 1

# my_string = "Hello World"

# #Output

# World Hello

# #Example 2

# my_string="python is good"

# #Output

# good is python

# """

# string = input("Enter a string: ")
# list = string.split()
# list.reverse()
# strr = " ".join(list)
# print(strr)

# """
# Q2. Write a program that reverses each word in a sentence while maintaining the word order. For example, "Hello World" should become

# "olleH dlroW".

# """


# string = input("Enter a string: ")
# list = string.split()
# strr = " ".join(str(i)[::-1] for i in list)
# print(strr)

# """
# Q3. Write a program that accepts a string and capitalizes
# the first letter of each word while converting all other letters to lowercase.

# #Example 1

# my_string = "hello WORLD"

# #Output

# Hello World

# #Example 2

# my_string="python is good"

# #Output

# Python Is Good

# """

# string = input("Enter a string: ")
# list = string.split()
# new = " ".join(i.capitalize() for i in list)
# print(new)

# """
# Q4. Write a program that converts a string in camelCase to snake_case.

# For example, converting "helloWorldHowAreYou" should result in "hello_world_how_are_you".

# """

# string = input("Enter a string: ")

# list = []

# c = 0

# for i in range(len(string)):
#     if string[i].isupper():
#         list.append(string[c:i])
#         c = i
# list.append(string[c:])
# print(list)
# strr = "_".join(i.lower() for i in list)
# print(strr)
