# Method 1
num1 = input("Enter First Number : ")
num2 = input("Enter Second Number : ")

Total = num1 + num2
print(Total, type(Total))


# Method 2
num1 = input("Enter First Number : ")
num2 = input("Enter Second Number : ")

total  = int(num1) + int(num2)
print(total, type(total))

# Method 3
num3 = float(input("Enter First Number : "))
num4 = int(input("Enter Second Number : "))
sum  = num3 + num4
print(sum, type(sum))

# method 4
num3 = float(input("Enter First Number : "))
num4 = int(input("Enter Second Number : "))
num5 = int(input("Enter Third Number : "))
num6 = float(input("Enter Fourth Number : "))
sum  = num3 + num4 + num5 + num6
print(f"Total Sum is {sum}", type(sum))