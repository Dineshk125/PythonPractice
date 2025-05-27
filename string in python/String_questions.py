"""
Q1. Ask a string from user Count how many alphabets are there in that string.

"""

string = input("Enter a string: ")

c = 0
for i in range(0, len(string)):
    if string[i].isalpha():
        c = i + 1
print(f"the alphabets are in string is {c}")

"""
Q2. Ask a string from user. Count the number of uppercase and lowercase characters in that String.

"""

string = input("Enter a string: ")

c = 0
c2 = 0
for i in range(0, len(string)):

    if string[i].isupper():
        c = c + 1
print(c)

for j in range(0, len(string)):
    if string[j].islower():
        c2 = c2 + 1
print(c2)

method 2

string = input("Enter a string: ")

c = 0
c2 = 0
for i in range(0, len(string)):

    if string[i].isupper():
        c = c + 1

    elif string[i].islower():
        c2 = c2 + 1
print(f"Total number in upper case is: {c}")
print(f"Total number in lower case is: {c2}")


"""
Q3. Ask a string from user. Convert all the alphabets to uppercase.

"""

string = input("Enter a string: ")

a = string.upper()
print(a)

"""
Q4. Ask a string from user. Convert all the alphabets to lowercase.

"""
string = input("Enter a streing: ")

a = string.lower()
print(a)

"""
Q5. Ask a string from user. Convert uppercase to
lowercase and convert lowercase to uppercase and don't change the other letters.

"""
string = input("Enter a string: ")

a = string.swapcase()
print(a)

"""
Q6. Count the number of spaces in a string entered by user.

"""

string = input("Enter a string: ")

c = 0

for i in string:
    if i.isspace():
        c = c + 1
print(c)


"""
Q137. Ask a string from user. Print the count of how many 
alphabets, digits, spaces and symbols (everything else) are there in that string. 

"""
string = input("Enter a string: ")

c = 0
c1 = 0
c2 = 0
c3 = 0

for i in string:
    if i.isalpha():
        c = c + 1

    elif i.isdigit():
        c1 += 1
    elif i.isspace():
        c2 += 1
    else:
        c3 += 1
print(f" Total number of alphabates in srting is : {c}")
print(f" Total number of gigits in srting is : {c1}")
print(f" Total number of spaces in srting is : {c2}")
print(f" Total number of symbols(Everything) in srting is : {c3}")
