def add(n1, n2, n3):
    return n1 + n2 + n3


print(add(2, 4, 6))

# using lambda function


y = lambda n1, n2, n3: n1 + n2 + n3
print(y(23, 5, 3))

"""Q1. take aargument which will be a number.make a list 0 to N."""

y = lambda n: [i for i in range(0, n + 1)]

length = int(input("Enter a length list1: "))
length1 = int(input("Enter a length of list2: "))
list1 = y(length)
list2 = y(length1)
print(list1)
print(list2)

"""Q2. even odd number"""

y = lambda n: print("Even") if n % 2 == 0 else print("Odd")

y(100)
y(9)

"""Even return true else false"""

y = lambda num: num % 2 == 0

if y(100):
    print("Even/ True")
else:
    print("Odd / False")
