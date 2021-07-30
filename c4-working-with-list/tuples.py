""" List works well for storing collections of items that can change throughout
the life of a program. However, sometimes you'll want to create a list of items
that cannot change. Tuples allow you to do just that. Python refers to values that
cannot change as immutable, and an immutable list is called a tuple!"""

# this is a tuple
dimensions = (200, 50)
""" print(dimensions[0])
print(dimensions[1]) """

# TypeError: 'tuple' object does not support item assignment
# dimensions[0] = 250

# loop through all values in a tuple
print('Original dimensions:')
for dimension in dimensions:
    print(dimension)


""" although you can modify a tuple, you can assign a new value to a variable that
represents a tuple. So if we wanted to change our dimensions, we could
redefined the entire tuple. """
dimensions = (400, 200)
print('Modified dimensions:')
for dimension in dimensions:
    print(dimension)