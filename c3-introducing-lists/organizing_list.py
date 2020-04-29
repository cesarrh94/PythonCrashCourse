# sorting a list permantely with sort() method.
cars = ['subaru', 'toyota', 'mazda', 'nissan', 'mitsubishi']
# cars.sort()
# print(f'permantely sort: {cars}')
print(f'original list: {cars}')
cars.sort(reverse = True) # reverse sorting but permantely as well!
print(cars)


# sorting a list temporarily with the sort() function
new_cars = ['audi', 'volkswagen', 'bmw', 'porsche']
print(f'original list: {new_cars}')
print(f'sorted list: {sorted(new_cars)}')
print(f'original list: {new_cars}')


# printing reverse order
vocals = ['i', 'u', 'o', 'a', 'e']
print(f'original list: {vocals}')
vocals.reverse()
print(f'reversed list: {vocals}')

# finding the length of the list:
print(f'the total of vocals in the list is: {len(vocals)}')