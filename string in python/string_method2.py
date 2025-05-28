"""
Methods part -> 2

Count, Startwith, Endwith,
Index, Find, Replace, Strip

"""

# Count Method -> Return the number of non-overlapping occurrences of substring sub in string S[start:end].

my_string = "Hello World"

c = my_string.count("l")
print(c)

# Startwith method -> Return True if the string starts with the specified prefix, False otherwise.

c = my_string.startswith("H")
print(c)

# Endwith method -> Return True if the string ends with the specified suffix, False otherwise.


c = my_string.endswith("d")
print(c)

# Index method -> Return the lowest index in S where substring sub is found, such that sub is contained within S[start:end].


c = my_string.index("l")
print(c)

# Find method -> Return the lowest index in S where substring sub is found, such that sub is contained within S[start:end].


c = my_string.find("lo")
print(c)

# Replace method -> Return a copy with all occurrences of substring old replaced by new.

c = my_string.replace("l", "z")
print(c)

# Strip method -> Return a copy of the string with leading and trailing whitespace removed.
# If chars is given and not None, remove characters in chars instead.

my_string1 = "      Hello World      "
c = my_string1.strip()
print(c)
