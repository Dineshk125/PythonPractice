# slicing in lists
a = [1, 2, 3, 4, 5, 6, 7, 8]
b = a[0:4]
print(b)

list = [i for i in range(1, 21)]
b = list[::]
print(b)

list = [i for i in range(1, 21)]
b = list[::-1]
print(b)

list = [i for i in range(1, 21)]
b = list[:5]
print(b)

list = [i for i in range(1, 21)]
b = list[7:3:-1]
print(b)

list = [i for i in range(1, 21)]
b = list[1:6:-1]
print(b)

list = [i for i in range(1, 21)]
b = list[-1::-1]
print(b)

list = [i for i in range(1, 21)]
b = list[-1::]
print(b)

list = [i for i in range(1, 21)]
b = list[1::2]
print(b)

list = [i for i in range(1, 21)]
b = list[0::2]
print(b)
