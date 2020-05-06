""" HOW input() WORKS?
the input() function pauses the program ans waits for the user to enter some text. Once Python
receives the user's input, it assigns that input to a variable to make it convenient to work with.

this function only takes one argument: the PROMPT or instructions, that we want to display
to the user so they know what to do! """

# NOTE: by default the input() function interprets everything the user as a string!

name = input('Give me your name: ')
print(f'Hi, {name.title()} nice to meet you!')

# the int() function converts a string representation of a number to a numerical representation.
age = input('\nHow old are you? ')
age = int(age)
print(f'You are legal: {age >= 18}')


number = input('\nEnter a number and I will tell you if it\'s even or odd: ')
number = int(number)

if number % 2 == 0:
    print(f'\nThe number {number} is even.')
else:
    print(f'\nThe number {number} is odd.')
