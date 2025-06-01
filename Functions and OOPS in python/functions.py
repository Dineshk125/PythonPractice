# def greet():
#     print("hello")
#     print("ok")
#     print("Done")


# greet()
# greet()


# """
# Types of function

# -> Without Parameters, Without Return
# -> With Parameters, Without Return
# -> Without Parameters, With Retirn
# -> With Parameters, With Return.

# """

## Parameters / Arguments


# ## Scoping in functions

# #Parameters 1

# def additionn(p1, p2):  # -> Parameters
#     total = p1 + p2
#     print(total)


# additionn(20, 40)  # -> Arguments

## Parameters 2


# def addi_list(x):
#     c = 0
#     for i in x:
#         c = c + i
#     print(c)


# my_list = [30, 50, 10, 20]

# addi_list(my_list)

# # addi_list([20, 40, 50])


# def additionn(p1, p2):  # -> Parameters
#     total = p1 + p2
#     print(total)
#     return total


# additionn(1, 3)

# additionn(20, 40)  # -> Arguments

## return 2


def add(n1, n2):
    total = n1 + n2
    return total


def check(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")


n1 = int(input("Enter a  number : "))
n2 = int(input("Enter a  number : "))

s = add(n1, n2)

check(s)
