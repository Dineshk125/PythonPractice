for i in range(1 , 5):
    print(i)
    for j in range(10,14):
        if j == 11:
            break
        print(j)

""" Print following pattern

    * * * * * 
    * * * * *
    * * * * *
    * * * * *
    * * * * *    

"""

for i in range(1, 6):
    for j in range(1, 6):
        print("*", end=" ")
    print()

""" Print following pattern
enter a number: 5
1 2 3 4 5 
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
 """

num  = int(input("enter a number: "))

for i in range(1, num+1):
    for j in range(1, num+1):
        print(j, end=" ")
    print()


""" Print following pattern
enter a number: 5
1 1 1 1 1 
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5
 """

for i in range(1,6):
    for j in range(1, 6):
        print(i, end=" ")
    print()



"""
5 4 3 2 1 
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1

"""
for i in range(5, 0, -1):
    for j in range(5, 0, -1):
        print(j, end=" ")
    print()

"""
5 5 5 5 5 
4 4 4 4 4
3 3 3 3 3
2 2 2 2 2
1 1 1 1 1

"""
for i in range (5, 0, -1):
    for j in range(5, 0, -1):
        print(i, end=" ")
    print()


"""
Enter a number: 8
1 1 1 1 1 
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5
6 6 6 6 6
7 7 7 7 7
8 8 8 8 8

"""
num = int(input("Enter a number: "))

for i in range(1,num+1):
    for j in range(1,6):
        print(i, end=" ")
    print()


"""

Enter a number: 6
6 6 6 6 6 
5 5 5 5 5
4 4 4 4 4
3 3 3 3 3
2 2 2 2 2
1 1 1 1 1

"""

N = int(input("Enter a number: "))
for i in range(N,0, -1):
    for j in range(5, 0, -1):
        print(i, end=" ")
    print()