guests = ['jenni', 'aldo', 'ricardo']
# changing invitation of ricardo to maritza
guests[2] = 'maritza'

# adding to the begging, in the middle and at the end!
guests.insert(0, 'martin')
guests.insert(2, 'itzel')
guests.append('aram')

# for loop to print invitation.
for guest in guests:
    print(f'Hi, {guest.capitalize()} tonight dinner in my house!')


# popping elements
print(f'guests list: {guests}')
popped_element = guests.pop()
print(f'popped element: {popped_element}')
print('You guys still invited: ' + str(guests))

popped_element = guests.pop()
print(f'popped element: {popped_element}')
print('You guys still invited: ' + str(guests))

popped_element = guests.pop()
print(f'popped element: {popped_element}')
print('You guys still invited: ' + str(guests))

popped_element = guests.pop()
print(f'popped element: {popped_element}')
print('You guys still invited: ' + str(guests))

del guests[0]
print(f'guests list: {guests}')
del guests[0]
print(f'guests list: {guests}')



