''' write a program to calculate the area og a rectangle using user input for length'''

# length = input("Enter the length of ractangle : ")
# width  = input("Enter the width of the ractangle : ")

# area = int(length) * int(width)

# print(f"The area of the ractangle is {area}")


""" WAP that converts a temprature from celsius to fahrenheit in fahrenheit to celsius """

# # celsius = input("Enter the temprature in celcius : ")
# fahrenheit  = input("Enter the temprature in fahrenheit : ")

# # celcius_to_fahrenheit = (int(celsius) * 9/5) + 32
# fahrenheit_to_celcius = (int(fahrenheit) - 32) * 5/9

# # print(f"The temprature in fahrenheit is {celcius_to_fahrenheit}")
# print(f"The {fahrenheit} temprature in celcius is {fahrenheit_to_celcius}")

""" Ask number of games played in a tournment. ask the user number of wins 
    and losses and calculate the number of tie
    and total points.
    (1 win = 4 points, 1 tie = 2 point)  
"""
total_games  = int(input("Enter the number of games played : "))
winner = int(input("Enter the number of wins : "))
losses = int(input("Enter the number of losses : "))

ties = total_games - winner - losses
total_points = winner * 4 + ties * 2

print(f"The total points is {total_points}")
print(f"The number of ties is {ties}")  
