""" Q 1.
    ask 5 marks from user.
    calculate percentage and print it.

    91-100 -> A grad
    81-90  -> B grad
    71-80  -> C grad
    61-70  -> D grad
    0-60   -> Fail
    INVALID

"""

maths = int(input("Enter maths marks: "))
Science = int(input("Enter Science marks: "))
english = int(input("Enter english marks: "))
hindi = int(input("Enter hindi marks: "))
history = int(input("Enter history marks: "))

total =  maths + Science + english + hindi + history

percentage = (total/500)*100
print(f"percentage scored = {percentage}")

if percentage >=91 and percentage <= 100:
    print("A grade")
elif percentage >=81 and percentage <= 90:
    print("B grade")
elif percentage >=71 and percentage <= 80:
    print("C grade")
elif percentage >=61 and percentage <= 70:
    print("D grade")
elif percentage >=1 and percentage <= 60:
    print("Fail")
else:
    print("INVALID INPUT")

""" Q 2.print if the number is odd or even """

num = int(input("enter a number"))

if num == 0:
    print("the number is zero")
elif num % 2 == 0:
    print("the number is even")
else:
    print("the number is odd")

""" Q 3. Write a program to check if number is divisible by 2 and 3 but not 8.  """

num = int(input("Enter a number: "))

if num % 2 == 0 and num % 3 == 0 and num % 8 != 0:
    print(f"The number {num} is divisible by 2 and 3 but not 8")
elif num % 2 == 0 and num % 3 == 0 and num % 8 == 0:
    print(f"The number {num} is divisible by 2 and 3 and 8")
else:
    print("The number is not divisible by 2 and 3 and 8")


""" Q 4. wap to print the last digit of number. (NOT A If Else Question)

    Example 1
    input: 45321
    output: 1

    Example 2
    input: 459094
    output: 4

"""
digit = int(input("Enter a number: "))
print(digit%10)

""" Q 5. The year is leap or not"""

year = int(input("Enter a year: "))

if year % 4 ==0 and year % 100 !=0 or year % 400 ==0:
    print(f"The year {year} is leap year")
else:
    print(f"The year {year} is not leap year")

""" Q 6. Write a program to check if the ast digit of a number  is divesible by 5 or not. """

num = int(input("Enter a number: "))

if num % 10 % 5 == 0:
    print(f"The last digit of {num} is divisible by 5")
else:
    print(f"The last digit of {num} is not divisible by 5")


""" Q 7. Write a program to calculate the bill. ask the final amount  from the user. you have to give discount and print the final bill after discount.

    50000 above - 30% discount
    40000 - 49999 above - 25% discount
    30000 - 39999 above - 20% discount
    10000 - 29999 above - 10% discount
    0-9999 - no discount


    print the discount and the final amount to be paid

"""

final_amount = int(input("Enter your bill amount: "))
if final_amount >= 50000:
    final_amount = final_amount - final_amount*30/100
    print(final_amount)

elif final_amount >= 40000 and final_amount <= 49999:
    final_amount = final_amount - final_amount%25/100
    print(final_amount)

elif final_amount >= 30000 and final_amount <= 39999:
    final_amount = final_amount - final_amount*20/100
    print(final_amount)

elif final_amount >= 10000 and final_amount <= 29999:
    final_amount = final_amount - final_amount*10/100
    print(final_amount)

elif final_amount >= 0 and final_amount <= 9999:
    print(final_amount)

else:
    print("INVALID INPUT")

""" Q 8. Ask 4 number from user. make sure all number entered by user are different. Print samallest number and largest number """


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
num4 = int(input("Enter fourth number: "))

if num1 < num2 and num1 < 3 and num1 < num4:
    print(f"The smallest number is {num1}")
elif num2 < num1 and num2 < num3 and num2 < num4:
    print(f"The smallest number is {num2}")
elif num3 < num1 and num3 < num2 and num3 < num4:
    print(f"The smallest number is {num3}")
elif num4 < num1 and num4 < num2 and num4 < num3:
    print(f"The smallest number is {num4}")

else:
    print("INVALID INPUT")


""" Q 9. Ask a number from user.

    print "fizz" if the number is divided by 3.
    print "buzz" if the number is divided by 5.
    print "fizzbuzz" if the number is divided by both 3 and 5.
    print the number if the number is not divided by 3 and 5.

"""

num = int(input("Enter a number: "))

if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
elif num % 3 != 0 and num % 5 != 0:
    print("none of the condition true")
else:
    print("INVALID INPUT")

""" Q 10. A student will not be allowed to sit in exam if his/ her attendance is less than 75%. 

    a. Take following input from user
        i. Number of classes held
        ii. Number of classes attended.
    b. print percentage of class attended.
    c. print is student is allowed to sit in exam or not.

"""

held = int(input("Enter the number of classes held by student: "))
attended = int(input("Enter the number of classes attended by the student: "))

percentage = int((attended/held)*100)

print("Total percentage",percentage)

if percentage >= 75:
    print("The student is allowed to sit in the exam")
else:
    print("The student is not allowed in the exam")

""" Q 11. Take salary as input from user and Update the salary of an employee.

    -> salary less than 10000, 5 % increment
    -> salary Between 10000 and 20000, 10 % increment
    -> salary between 20000 and 50000, 15 % increment
    -> salary more than 50000, 20 % increment

"""

salary = float(input("Enter your salary: "))

if salary < 10000:
    salary = salary + salary * 5/100
    print(salary)
elif salary >= 10000 and salary <= 20000:
    salary = salary + salary * 10/100
    print(salary)
elif salary >= 20000 and salary <= 50000:
    salary = salary + salary * 15/100
    print(salary)
elif salary > 50000:
    salary = salary + salary * 20/100
    print(salary)
else:
    print("INVALID INPUT")

""" Q 12. Take therr numbers as input from user and print which one is grater or the euual. """


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
if num1 != num2 and num1 != num3 and num2 != num3:
    if num1 > num2 and num1 > num3:
        print(f"The largest number is {num1}")
    elif num2 > num1 and num2 > num3:
        print(f"The largest number is {num2}")
    elif num3 > num1 and num3 > num2:
        print(f"The largest number is {num3}")
if num1 == num2 and num1 == num3 and num2 == num3:
    print(f"All numbers are equal {num1}")
else:
    print("Any tow numbers are equal")

""" Q 13. An extra day is added to the calendar almost every four year as february 29, and the day is called a leap day. a leap year contains a leap day.

    -> if the year can be evenly divided by 4, its then a leap year.
    -> but if the year is evenly divided by 4 and also by 100 , thwn it is not a leap year.
    -> but if the year is evenly divided by 4, 100, and 400, then it is a leap year.

    This mean the years 2000 and 2400 are leap year , whole 1800, 1900, 2100, 2200, 2300 and 2500 are not leap year

    Ask a year input from user. and tell if the year entered by user is leap or not.

    
"""

year  = int(input("Enter a year: "))

if year % 4 ==0 and year % 100 != 0 or year % 400 == 0 :
    print(f"The year {year} is leap year")
else:
    print(f"The year {year} is not leap year")
