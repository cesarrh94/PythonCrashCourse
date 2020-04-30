# the range() function make it easy to generate a series of numbers.
""" In this example the for loop only prints the numbers 1 through 100,
but stops when it reach the second value provided! """
for value in range(1, 100):
    if(value % 2 == 0):
        print(f'{value} is even')
    else:
        print(f'{value} is odd')


# How to create a list of numbers using the list() and range() functions.
numbers = list(range(1, 10))
print(numbers)

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)
print(f'min in squares: {min(squares)}')
print(f'max in squares: {max(squares)}')
print(f'sum in squares: {sum(squares)}')
