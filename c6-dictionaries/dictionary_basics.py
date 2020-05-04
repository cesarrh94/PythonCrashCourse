""" A dictionary is collection of key-value pairs. Each key is connected to a value,
and you can use a key to access the value associated with that key. """

# example of a dictionary
person = {
    'first_name': 'cesar',
    'last_name': 'rodriguez',
    'age': 25
}

# printing values of the dictionary:  dictionary_name[key_name]
print(person['first_name'])
print(person['last_name'])
print(person['age'])


""" Adding new key-value pairs:
Dictionaries are dynamic structures, and you can add new key-value pairs to a 
dictionary at anytime, to add new key-value pair, you would give the name of the 
dictionary follwed by the new jey in square brackets along with the new value! """

person['genre'] = 'male'
person['nationality'] = 'mexican'

print(person['genre'])
print(person['nationality'])


# Modifying values in a dictionary: just give the name if the dictionary with the key
# in square brackets and then the new value you want to associated with that key. 
person['nationality'] = 'japanese'
print(f"change of nationality: {person['nationality'].title()}")


# removing key-value pairs, use the DEL keyword
print(f'original dictionary: {person}')

del person['genre']
del person['nationality']

print(f'dictionary after remove 2 key-value: {person}')


""" using GET() method to access values: this method requires a key as first argument. as a
second argument, you can pass the value to be returned if the key doesn't exist! """

programming_languages = {
    'python': 'guido',
    'java': 'james',
    'c': 'dennis'
    }

# this line throws an error because it does not a key with that name!
# print(programming_languages['ruby']) 

pl_value = programming_languages.get('python', 'no programming language found!')
print(pl_value.title())

pl_value = programming_languages.get('ruby', 'no programming language found!')
print(pl_value.title())