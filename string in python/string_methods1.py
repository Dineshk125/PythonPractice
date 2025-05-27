"""String Methods -> 1

Title, capitalized, upper, lower, swapcase,
isupper, islower, isalpha, isalnum, isspace.

"""

# title
a = "Dinesh"
b = a.title()
print(b)

# capitalized

# upper and lower
a = "Dinesh"
b = a.upper()
c = a.lower()
print(c)
print(b)

# swapcase

a = "Dinesh Kumawat"

b = a.swapcase()
print(b)

# isupper -> it true whene all characteors are capitals otherwise it false

a = "DINESH"  # output -> True
a = "DINESh"  # output -> false
a = "DIN23ESH12"  # output -> True
a = "DINE S H"  # output -> True

b = a.isupper()
print(b)


# islower -> it true whene all characteors in lower order otherwise it false

a = "DINESH"  # output -> false
a = "DINESh"  # output -> false
a = "din23esh12"  # output -> True
a = "dinesh"  # output -> True
a = "dine s h"  # output -> True

b = a.islower()
print(b)


# isalpha -> it true whene all characteors are alphabatic otherwise it false.

a = "DINESH"  # output -> True
a = "DINESh"  # output -> True
a = "din23esh12"  # output -> False
a = "dinesh"  # output -> True
a = "dine s h"  # output -> False

b = a.isalpha()
print(b)


# isalnum -> it true whene all characteors are alphabatic and numeric otherwise it false.

a = "DINESH"  # output -> True
a = "DINESh"  # output -> True
a = "din23esh12"  # output -> True
a = "dinesh"  # output -> True
a = "dine s h"  # output -> False

b = a.isalnum()
print(b)


# isspace -> it true whene space in sring otherwise it false.

a = "      "  # output -> True
a = "DINESH"  # output -> false
a = "DINESh"  # output -> false
a = "din23esh12"  # output -> false
a = "dinesh"  # output -> false
a = "dine s h"  # output -> False

b = a.isspace()
print(b)
