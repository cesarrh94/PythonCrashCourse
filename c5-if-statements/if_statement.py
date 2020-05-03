# example: if-else statement
age = 25
if age >= 18:
    print('You are old enough')
    print('Do you have your ID already?')
else:
    print('Sorry, You are too young!')
    print('You need 18 ayo to request an ID!')


# example: if-elif-else chain
""" Often, you will need to test more than two possible situations, and to evaluate
these you can use if-elif-else chain. """

age = 3

if age < 4:
    print('Your admission cost is $0')
elif age < 18:
    print('Your admission cost is $25')
else:
    print('Your admission cost is $40')