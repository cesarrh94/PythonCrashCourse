# rental car
car = input('What type of car are looking for? ')
print(f'ok, let me see if I have {car.title()} available!')


# restaurant reading
people = input('How many people are in their dinner group? ')
people = int(people)

if people > 8:
    print('Sorry but you will have to wait!')
else:
    print('Come in please, the table is ready!')