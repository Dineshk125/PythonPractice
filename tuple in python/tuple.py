#  tupal is immutable which mean we cant delete, update, add any data in tupal.

# we perform only count and index method function in tuple

my_tuple = (1, 2, 34, 5, 6, 7, 1, 1, 8)
x = my_tuple[0]
print(x)
print(my_tuple[0])

# count method
y = my_tuple.count(1)
print(y)

# index method
z = my_tuple.index(1)
print(z)


"""
we can change data in tupal, first we convert tupal in list and then update the data and then convert list in to tupal.

in this step it override the original tupal

"""

my_tuple = (1, 2, 34, 5, 6, 7, 1, 1, 8)

my_list = list(my_tuple)  # convert my_tuple in to the list

my_list[5] = 100  # update values in list
my_list[1] = 200
print(my_list)

my_tuple = tuple(my_list)  # then convert list in to tuple
print(my_tuple)  # print updated tuple
