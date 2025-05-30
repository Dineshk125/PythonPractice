# # set() is unorderd, mutable, store unique value, it does not have INDEX.
# p_set = {2, 23.6, 896, -89, "Dinesh"}
# print(p_set)
# x = list(p_set)
# print(x, type(x))
# print(type(p_set))


# # type Conversion

# a = [1, 2, 3, 4, 4, 4, 4, 6, 7, 8, 9, 9, 9, 9, 9, 0, 0, 8]
# print(a)

# b = set(a)
# print(b)
# c = list(b)
# print(c)

# Methods in set union/ intersection

# my_set1 = {1, 2, 2, 3, 5, 5, 4}
# my_set2 = {0, 1, 1, 2, 6}

# print(my_set1)
# print(my_set2)

# print(my_set1.union(my_set2))
# print(my_set1.intersection(my_set2))

# print(my_set1.union(my_set2) - my_set1.intersection(my_set2))

# list comman

# a = [1, 2, 3, 4, 5]
# b = [4, 5, 6, 7, 8, 9]

# c = set(a)
# d = set(b)

# print(c.union(d))
# print(c.intersection(d))

# e = list(c.union(d))
# f = list(c.intersection(d))

# print(e)
# print(f)


# b = {3, 4, 5, 6, 7, 8, 9}

# print(b)
# b.add(100)
# b.pop()
# b.remove(9)
# # b.clear()
# print(b)

# b = set()
# print(b)

# b.add(200)
# print(b)

# Menbership Method

b = {4, 5, 6, 7, 8, 9}

num = int(input("Enter a number = "))

if num in b:
    print("yes")
else:
    print("no")

# f = False
# for i in b:
#     if i == num:
#         f = True

# if f:
#     print("yes")
# else:
#     print("No")
