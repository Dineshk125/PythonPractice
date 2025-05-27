# String - it is Iterable and Mutable

# string = "Dinesh Kumawat"

# x = string[0]
# print(x)
# print(string)

# iterate by value ans index

# By value ->

string = "Dinesh Kumawat"

# for value in range(0, len(string)):
#     print(string[value], end=" ")

# by index -> it show the index number of string

# for index in string:
#     print(index, end=" ")

# reverse string

for i in range(len(string) - 1, -1, -1):
    print(string[i], end=" ")
