def total_marks(maths, english, hindi, science):
    total = maths + hindi + english + science
    print(total)


total_marks(100, 80, 89, 99)
# positional arguments

total_marks(hindi=90, english=99, science=89, maths=100)
