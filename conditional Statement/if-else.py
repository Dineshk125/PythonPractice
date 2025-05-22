age = int(input("Enter your age: "))

if age >= 18:
    print("you can vote")
else:
    print("you can't vote")


""" Q 1.print if the number is odd or even """

num = int(input("enter a number"))

if num % 2 == 0:
    print("the number is even")
else:
    print("the number is odd")

""" Q 2. print pass, if student is pass both subjects (physics and chemistry) otherwise fail   """


physics = int(input("Enter physics marks: "))
chemistry = int(input("Enter chemistry marks: "))

if physics >=33 and chemistry >= 33:
    print("Student pass both subjects")
else:
    print("d\student fail both subjects")

print("total present marks", ((physics + chemistry)/200)*100)

""" Q 3. wap that takes an integer input and prints wether its positive, nagive. (consider 0 as positive) """ 

num = int(input("Enter a number: "))

if num  >= 0:
    print("the number is positive")
else:
    print("The number is nagitive")


""" Q 4. wap that takes a character as input and prints wether its a vowel or consonant. (multiple OR will be used) """

char = input("Enter a character: ")

if char =="a" or char == "e" or char == "i" or char == "o" or char == "u":
    print ("the character is a vovels")
else:
    print("the character is consonant")

""" Q 5. wap that takes two numbers as input and check if the sirst number is divisible by the second number"""

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 % num2 == 0:
    print("The first number is divisible by the second number ")
else: 
    print("The first number is not divisible by the second number")

""" Q 6. A student will not be allowed to sit in exam is his/her attendance is less than 75%.

    Take followingg input from user
    -> Number of classes held
    -> Number of classes attended.

    1. print percentage of class attended
    2. print is stident is allowed to sit in exam or not.

"""

held = int(input("Enter the number of classes held by student: "))
attended = int(input("Enter the number of classes attended by the student: "))

percentage = int((attended/held)*100)

print("Total percentage",percentage)

if percentage >= 75:
    print("The student is allowed to sit in the exam")
else:
    print("The student is not allowed in the exam")