# moving items from ome list to another

unconfirmed_users = ['cesar', 'aldo', 'jenni']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f'Verifying user: {current_user.title()}')
    confirmed_users.append(current_user)

print(f'\nThe following users have been confirmed:')
for confirmed_user in confirmed_users:
    print(confirmed_user.title())


print(f'\nunconfirmed_users: {unconfirmed_users}')
print(f'confirmed_users: {confirmed_users}')


# removing all instances of specific values from a list

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(f'\n\npets before remove: {pets}')

while 'cat' in pets:
    pets.remove('cat')

print(f'\npets after remove: {pets}')


# filling a dictionary with user input

responses = {}
polling_active = True

while polling_active:
    name = input('\nWhat is your name? ')
    response = input('Which NBA team are you fan? ')

    responses[name] = response
    print(responses)

    repeat = input('Would you like to let another person respond? (yes/no) ')
    if repeat.lower() == 'no':
        polling_active = False

print('\n--- Poll Results ---')
for name, response in responses.items():
    print(f"{name.title()} is a {response.title()}'s fan!")