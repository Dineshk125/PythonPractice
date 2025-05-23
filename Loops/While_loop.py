num = 1

while num <= 2:
    print("Hello World!")
    num += 1

""" Q1. Write a program to print the number from 1 to 10 using while loop """

num = 1
while num <=10:
    print(num)
    num = num+1

""" Q 2. print even number from 1 to 100 """

num = 1
while num < 100:
    if num % 2 == 0:
        print(num, end=" ")
    num = num+1

""" Q3. Factorial of a number """

num = int(input("Enter a number: "))
i = num
factorial = 1
while i > 0:
    factorial = factorial * i
    i = i -1

print(f"The factorial of {num} is {factorial}")

""" Q4. Ask a number from user . print all the numbers from 1 to that number """

num = int(input("Enter a number: "))

i = 1

while i <= num:
    print(i)


""" Q5. Ask a number (N) From user, print all the number from N to 1."""

N = int(input("Enter a number: "))

while N >=1:
    print(N)
    N = N-1

""" Q6. Ask start Number and end number from user. print all the numbers from start to nnd using while loop."""

start = int(input("Enter a start number: "))
end = int(input("Enter a end number: "))

while start <= end:
    print(start)
    start = start+1 

""" Q 7. Calculte the sum of all the numbers from 1 or user input to 10 or  user input ."""

num = int(input("Enter a number: "))
end = int(input("Enter a end number: "))
sum = 0

while num <= end:
    sum = sum + num
    num +=1

print(sum)

""" Q8. Calculate the product of all the numbers from 1 to 100. """

num = int(input("Enter a number: "))
end = int(input("Enter a end number: "))
product = 1

while num <= end:
    product = product * num
    num += 1
print(product)

""" Q9. Calculate how many numbers are divisible by 7 from 1 to 100."""

num  = 1
count = 0

while num <= 100:
    if num % 7 == 0:
        count  = count + 1
    num = num + 1

print(f"{count} numbers are divisable by 7." )


""" Q10. Calculate how many numbers are divisible by bith 6 and 7 between 1 to 200. """

num = 1
count = 0

while num <= 200:
    if num % 6 == 0 and num % 7 == 0:
        count += 1
    num += 1
print(f"{count} numbers are divisible by both 6 and 7.")


""" Q11. WAP to calculate the sum of all the numbers divisible by 4 from 20 to 50."""

num =20
count = 0
sum = 0

while num <= 50:
    if num % 4 == 0:
        
        count += 1
        sum += num
        print(f"{num} is divisible by 4")
    num += 1
print(f"The sum of all the numbers divisible by 4 from {num} to 50 is {sum} and total numbers are {count}")

""" Q12. WAP to calculate the sum of all the numbers divisible by 4 from 20 to 50."""

num =20
count = 0
sum = 0

while num <= 100:
    if num % 6 == 0 and num % 7 == 0:
        
        count += 1
        sum += num
        print(f"{num} is divisible by 6 and 7")
    num += 1
print(f"The sum of all the numbers divisible by 6 and 7 from {num} to 100 is {sum} and total numbers are {count}")

""" Q13. Ask a number from user. print the Multiplication table of that number.

    Example 

    Enter a number = 8
    8*1 = 8
    8*2 = 16
    8*3 = 24
    8*4 = 32
    8*5 = 40
    8*6 = 48
    8*7 = 56
    8*8 = 64
    8*9 = 72
    8*10 = 80

"""

num = int(input("Enter a number: "))

i = 1

while i <= 10:
    print(f"{num}*{i} = {num*i}")
    i += 1


""" Q14 Ask to numbers x and y from the user. if x<y then print all the numbers from x to y, but if y<x then print all the numbers from y to x."""

x = int(input("Enter a number: "))
y = int(input("Enter a number: "))

if x < y:
    while x < y:
        print(x, end=" ")
        x += 1
elif y < x:
    while y < x:
        print(y, end=" ")
        y += 1

else:
    print("Both numbers are equal")
    