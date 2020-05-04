user_0 = {
    'username': 'ciruspunk',
    'firstname': 'cesar',
    'lastname': 'rodriguez',
    'email': '94cesarrh@gmail.com'
}


# looping through using ITEMS() method, return the list with all dictionary keys with values.
print('printing keys and values --> using items() method')
for key, value in user_0.items():
    print(f'Key: {key}')
    print(f'Value: {value}\n')


""" looping through using KEYS() method, is useful when you do not need to work with all of the values
in a dictionary. """

print('printing keys --> using keys() method')
for key in user_0.keys():
    print(f'{key}\n')


""" looping through using VALUES() method, return a list of values without any keys. """

print('printing values --> using values() method')
for value in user_0.values():
    print(f'{value}\n')