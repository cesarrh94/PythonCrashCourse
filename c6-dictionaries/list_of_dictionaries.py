# Working with a list of dictionaires

# 1. make an empty list for storing
persons = []

# 2. make 10 persons
for person_number in range(10):
    new_person = {
        'name': 'cesar',
        'age': 25,
        'job': 'software engineer'
    }

    persons.append(new_person)

# 3. show the first 5 persons
for person in persons[:5]:
    print(person)

# 4. show how many persons have been created
print(f'Total number of persons: {len(persons)}')