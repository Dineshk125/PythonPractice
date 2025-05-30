# try:
#     s = [1, 2, 3, 4, 5, 6]

#     print(s[1])
#     print(s[4])
#     print(s[65])
#     print(s[2])
#     print(10 / 0)
# except:
#     print("Some Error Occored")

# print("Done")

## multipal Exception Handling

try:
    s = [1, 2, 3, 4, 5, 2]
    print(s[1] / s[-1])
    print(s[99])
    print(s[3])

except IndexError:
    print("Idex Error ")
except ZeroDivisionError:
    print("You cannot divide by zero")
except:
    print("Some Error Occured")
else:
    print("Everythings is fine")
finally:
    print("This is finally clause")
