# """
#         * 
#       * *
#     * * *
#   * * * *
# * * * * *

# """


# for i in range(1,6):
#     for j in range(i,5):
#         print(" ",end=" ")

#     for k in range(1, i+1):
#         print("*",end=" ")
#     print()

# """
#         1 
#       1 2
#     1 2 3
#   1 2 3 4
# 1 2 3 4 5

# """
# for i in range(1,6):
#     for j in range(i,5):
#         print(" ",end=" ")

#     for k in range(1, i+1):
#         print(k,end=" ")
#     print()



# """ Logic 1
#         * 
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *

# """
# for i in range(1,10,2):
#     for j in range(i,9):
#         print("",end=" ")

#     for k in range(1, i+1):
#         print("*",end=" ")
#     print()


# """ Logic 2
#         * 
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *

# """

# for i in range(1,6):
#     for j in range(i,5):
#         print(" ",end=" ")

#     for k in range(1, i+1):
#         print("*",end=" ")

#     for l in range(1,i):
#         print("*", end=" ")

#     print()

# """
#     * 
#    * *
#   * * *
#  * * * *
# * * * * *

# """

# for i in range(1,6):
#     for j in range(i,5):
#         print("",end=" ")

#     for k in range(1, i+1):
#         print("*",end=" ")
#     print()



# """
#         * 
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *

# """
for i in range(1,10,2):
    for j in range(i,9):
        print("",end=" ")

    for k in range(1, i+1):
        print("*",end=" ")
    print()

for m in range(4,0,-1):
    for n in range(5,m,-1):
        print(" ",end=" ")
    for o in range((m*2)-1):
        print("*",end=" ")
    print()
        