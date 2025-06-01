## Scoping in functions


def additionn():
    # Scoping
    num1 = int(input("Enter a value: "))
    num2 = int(input("Enter a value: "))

    print(f"Addition {num1+num2}")


additionn()
# print(num1) # name 'num1' is not defined, it is define outside of the function


def subtractionn():
    num1 = int(input("Enter a value: "))
    num2 = int(input("Enter a value: "))

    print(f"Addition {num1-num2}")


subtractionn()


def greet():
    name = input("Enter a value: ")  # this is store in different memory
    print(f"Your name is {name}")


name = "xyz"  # this is store in different memory
greet()
print(name)
