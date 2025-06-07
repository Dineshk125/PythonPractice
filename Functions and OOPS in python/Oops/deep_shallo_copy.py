## Deep and Shallo Copy
import copy

a = [[1, 2, 3], [10, 34, 56], [223, 56, 78, 97], [9, 8, 7]]

b = a

print("a = b")
print(a)
print(b)
print()


## Shallo copy

a = [[1, 2, 3], [10, 34, 56], [223, 56, 78, 97], [9, 8, 7]]

b = a.copy()

print(
    "it is shallo copy of a in b, which mean both zero index number change same time, it has also different id's"
)
print()

print(a, id(a))
print(b, id(b))

a[0][0] = 100
print(a, id(a))
print(b, id(b))


## Deep Copy

a = [[1, 2, 3], [10, 34, 56], [223, 56, 78, 97], [9, 8, 7]]

b = copy.deepcopy(a)

print()
print(
    "it is deep copy a in b , which mean we using copy.deepcopy(a) it it change only a[0] index position not change on b[0] index , it has also different id's."
)

print()

print(a, id(a))
print(b, id(b))

print()

a[0][0] = 100
print(a, id(a))
print(b, id(b))
