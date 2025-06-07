## Without List comprihantion

x = int(input("X = "))
y = int(input("Y = "))
z = int(input("Z = "))
n = int(input("N = "))

result = []

for i in range(0, x + 1):
    for j in range(0, y + 1):
        for k in range(0, z + 1):
            print(i, j, k)
            if i + j + k != n:
                print(i, j, k, end=" ")


# with list comprihantion

x = int(input("X = "))
y = int(input("Y = "))
z = int(input("Z = "))
n = int(input("N = "))

result = [
    [i, j, k]
    for i in range(0, x + 1)
    for j in range(0, y + 1)
    for k in range(0, z + 1)
    if i + j + k != n
]

print(result)
