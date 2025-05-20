p = int(input("give physics marks: "))
c = int(input("give chemistry marks: "))
b = int(input("give biology marks: "))

print(p > 33 and c > 33 and b > 33)
print(p > 33 or c > 33 or b > 33)
print(not(p >33 and c > 33 and b > 33))