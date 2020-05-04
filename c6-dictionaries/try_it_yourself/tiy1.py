pets = []

pet1 = {
    'type': 'dog',
    'pet_name': 'benji',
    'pet_age': 3,
    'owner_name': 'jennifer'
}

pet2 = {
    'type': 'cat',
    'pet_name': 'silvestre',
    'pet_age': 10,
    'owner_name': 'cristian'
}

pet3 = {
    'type': 'dog',
    'pet_name': 'buck',
    'pet_age': 1,
    'owner_name': 'diego'
}

pets.append(pet1)
pets.append(pet2)
pets.append(pet3)

for pet in pets:
    for k, v in pet.items():
        print(f'{k}: \t{v}')
    print('\n')
