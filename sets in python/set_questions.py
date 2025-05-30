"""

Q1. Given two lists a, b. Check if two lists have at least one element common in them.

"""

a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7, 8, 9]

c = set(a)
d = set(b)

e = c.intersection(d)
f = d.intersection(c)
if e == f:
    print(f"yes the {list(e)} common element present list")
else:
    print("No the comman element not present ")


"""
# Q2. Python program to find common elements in three lists using sets

# """

a = [1, 2, 3, 4, 5]
b = [1, 4, 5, 6, 7, 8, 9]
c = [8, 9, 0, 1, 2]

"""
Q3. Create 3 sets of your own, find the union of three sets.

"""

x, y, z = set(a), set(b), set(c)

p = x.intersection(y).intersection(z)


print(list(p))

"""
Q4. Write a Python program to remove all elements from a given set.

"""

b = {1, 4, 5, 6, 7, 8, 9}

b.clear()
print(b)


"""
Q5. Write a Python program to find the length of a set

"""

b = {1, 4, 5, 6, 7, 8, 9}

c = 0
for i in b:
    c += 1
print(c)

# method 2

# a = len(b)

# print(a)

"""
Q6. Write a Python program to check if two given sets have no elements in common.

"""


a = {1, 2, 3, 4}
b = {4, 5, 6}

MEthod 1

if not a.isdisjoint(b):
    print("Yes")
else:
    print("No")

Method 2

if not (a & b):
    print("No")
else:
    print("Yes")


"""
Q7. Write a Python program to find elements in a given set that are not in another set.

"""

a = {1, 4, 6}

b = {6, 7, 8, 9, 1, 4}

Method 1
c = b - a
print(c)

Method 2
x = a.intersection(b)
y = a - x
print(y)

"""
Q165. Ask a string from user, remove all the duplicates from that
      string and print that string again (order does'nt matter).

"""

string1 = input("Enter a string: ")

print(string1, type(string1))

s = set(string1)
print(s, type(s))

c = ""
for i in s:
    c = c + i
print(c, type(c))
