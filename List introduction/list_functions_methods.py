# Mutable/ Immutable Data type

a = [1,2,3,4,5,-6,7,8,-9]
print(a)

# Append method - add in a list on last position

a = [1, 2, 3, 4, 5, -6, 7, 8, -9]
a.append("Code")
a.append(23)
print(a)

# Insert method - add values in a list any position

a = [1, 2, 3, 4, 5, -6, 7, 8, -9]
a.insert(2, "Code")
a.insert(5, 100)
a.insert(100, 200) # add value in last position whene index number is not in a list.
print(a)

# Update method - add values on index position in a list.

a = [1, 2, 3, 4, 5, -6, 7, 8, -9]
a[0] = 100
a[8] = -19
print(a)

# pop method - remove values in a list any position by the index.

a = [1, 2, 3, 4, 5, -6, 7, 8, -9]
a.pop() # when the pop is impty it remove last position value by default
a.pop(1) # It remove the value according to the index number
print(a)

# remove method - Remove index by the value in a list any position

a = [1, 2, 3, 4, 5, -6, 7, 8, -9]
a.remove(-9)
a.remove(5)
print(a)

# del method - del values in a list any position by index

a = [1, 2, 3, 4, 5, -6, 7, 8, -9]
del a[1]
del a[0]
del a[5]
print(a)

# clear method - It remove all the values into the list, delete by index , it perorm the list is empty.

a = [1, 2, 3, 4, 5, -6, 7, 8, -9]
a.clear()
print(a)


# pos method
a = [55, 65, -95, 55.6, -95]
pos = a.index(-95)
print(pos)

# sort methos

a = [55, 65, -95, 55.6, -95]

a.sort()
a.sort(reverse=True)
print(a)

# reverse method

a = [55, 65, -95, 55.6, -95]

a.reverse()
print(a)

# append and extend method

a = [55, 65, -95, 55.6, -95]

# a.append(["hello", "hii", 2, 5])
a.extend(["hello", "hii", 2, 5])

print(a)

# clear method
a = ["hello", "hii", 2, 5]
a.clear()
print(a)
