# """ Q1. Write a program to print the number from 1 to 10 using for loop"""

# for i in range(1, 11):
#     print(i, end=" ")

# """ Q2. print 1 to 20 ...1 3 5 7 9 11 13 15 17 19"""

# for i in range(1, 21, 2):
#     print(i, end=" ")

#     """ OR """

#     """ Print 1 to 10 using for loop """

# for i in range(1, 20):
#     if i % 2 != 0:
#         print(i, end=" ")

# """ Q3. print 10 to 1 """
# x = int(input("Enter start number: "))
# y = int(input("Enter end number: "))
# for i in range(10, 0, -1):
#     print(i, end=" ")

# """Q4. Print hello world 5 times using for loop """
# for num in range(1,6):
#     print("Hello World!")
#     num += 1


# """ Q5. print even number from 1 to 100 """

# for i in range(1,101):
#     if i % 2 == 0:
#         print(i, end=" ")

# """ Q6. Factorial of a number """

# num = int(input("Enter a number: "))
# i = num
# factorial = 1
# for i in range(1, num+1):
#     factorial = factorial * i
# print(f"Factorial of {num} is {factorial}")

# """ Q7. Ask a number from user . print all the numbers from 1 to that number """

# num = int(input("Enter a number: "))

# i = 1

# for i in range(1, num +1):
#     print(i, end=" ")


# """ Q8. Ask a number (N) From user, print all the number from N to 1."""

# N = int(input("Enter a number: "))

# for i in range(N, 0, -1):
#     print(i, end=" ")

# """ Q9. Ask start Number and end number from user. print all the numbers from start to nnd using while loop."""

# start = int(input("Enter a start number: "))
# end = int(input("Enter a end number: "))

# for i in range(start, end + 1):
#     print(i, end=" ")
# if start > end:
#     for i in range(end, start):
#         print(i, end=" ")


# """ Q 10. Calculte the sum of all the numbers from 1 or user input to 10 using for loop ."""

# num = int(input("Enter a number: "))
# end = int(input("Enter a end number: "))
# sum = 0

# for i in range(num, end + 1):
#     sum = sum + num
#     num +=1

# print(sum)

# """ Q11. Calculate the product of all the numbers from 1 to 100. """

# end = int(input("Enter a end number: "))
# product = 1

# for i in range(1 , end +1):
#     product = product * i
# print(f"Product of numbers is {product}")

# """ Q12. Calculate how many numbers are divisible by 7 from 1 to 100."""

# num  = 1
# count = 0

# for i in range(1, 101):
#     if num % 7 == 0:
#         count  = count + 1
#     num = num + 1

# print(f"{count} numbers are divisable by 7." )


# """ Q13. Calculate how many numbers are divisible by bith 6 and 7 between 1 to 200. """

# num = 1
# count = 0

# for i in range(1, 201):
#     if num % 6 == 0 and num % 7 == 0:
#         count += 1
#     num += 1
# print(f"{count} numbers are divisible by both 6 and 7.")


# """ Q14. WAP to calculate the sum of all the numbers divisible by 4 from 20 to 50."""

# num =20
# count = 0
# sum = 0

# for i in range(20, 51):
#     if num % 4 == 0:
        
#         count += 1
#         sum += num
#         print(f"{num} is divisible by 4")
#     num += 1
# print(f"The sum of all the numbers divisible by 4 from {num} to 50 is {sum} and total numbers are {count}")

# """ Q15. WAP to calculate the sum of all the numbers divisible by 4 from 20 to 100."""

# num =20
# count = 0
# sum = 0

# for i in range(20, 100):
#     if num % 6 == 0 and num % 7 == 0:
        
#         count += 1
#         sum += num
#         print(f"{num} is divisible by 6 and 7")
#     num += 1
# print(f"The sum of all the numbers divisible by 6 and 7 from {num} to 100 is {sum} and total numbers are {count}")

# """ Q13. Ask a number from user. print the Multiplication table of that number.

#     Example 

#     Enter a number = 8
#     8*1 = 8
#     8*2 = 16
#     8*3 = 24
#     8*4 = 32
#     8*5 = 40
#     8*6 = 48
#     8*7 = 56
#     8*8 = 64
#     8*9 = 72
#     8*10 = 80

# """

# num = int(input("Enter a number: "))

# i = 1

# for i in range(1, 11):
#     print(f"{num}*{i} = {num*i}")


# """ Q14 Ask to numbers x and y from the user. if x<y then print all the numbers from x to y, but if y<x then print all the numbers from y to x."""

# x = int(input("Enter a number: "))
# y = int(input("Enter a number: "))

# if x < y:
#     for i in range(x, y + 1):
#         print(x, end=" ")
#         x += 1
# elif y < x:
#     for i in range(y, x + 1):
#         print(y, end=" ")
#         y += 1

# else:
#     print("Both numbers are equal")
    
