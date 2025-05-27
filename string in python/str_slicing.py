# x = "Dinesh Kumawat"

# y = x[0:5:2] # output -> Dns

# y = x[0:-5:2] # output -> Dns u

# reverse String -> tawamuK hseniD
# y = x[::-1]

# print(y)

"""

Q1. WAP to print the given string is palindrom or not.

"""

string = input("Enter a string : ")

if string == string[::-1]:
    print(f"The {string} is palindrom")

else:
    print(f"The String {string} is not palindrom.")
