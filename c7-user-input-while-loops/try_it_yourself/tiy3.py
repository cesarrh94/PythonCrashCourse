# deli

sandwich_orders = ['blt', 'italian', 'ham & cheese', 'peanut butter & jelly']
finished_sandwiches = []

while sandwich_orders:
    order = sandwich_orders.pop()
    finished_sandwiches.append(order)

for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)


# dream vacation
responses = {}
active = True

while active:
    name = input('\nWhat is your name? ')
    response = input('\nif you could visit one place in the world, where would you go? ')

    responses[name] = response

    repeat = input('\nWould you like to let another person respond? (yes/no)')
    if repeat.lower() == 'no':
        active = False
    
print('--- Printing Results ---')
for name, response in responses.items():
    print(f'{name.title()} would likes to visit {response.title()}')
