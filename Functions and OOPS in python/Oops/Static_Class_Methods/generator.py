# yield is a generator -. it gives values 1 by 1


def numbers():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
    yield 6
    yield 7
    yield 8


x = numbers()

print(x)

print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
# print(next(x)) # -> there it gives error of stopIteration

for i in numbers():
    print(i)

# # How to rise an error

raise ZeroDivisionError
