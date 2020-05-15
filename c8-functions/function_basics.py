# function without arguments
def greet():
    print('Hello World!')

greet()

""" What it is an argument?
an argument is a piece of information that's passed from a function call to a function. """
# passing information to a function
def greet_user(username):
    print(f'Hello, {username.title()}!')

greet_user('ciruspunk')


""" passing arguments --> positional arguments:
when you call a function, Python must match each argument in the function call with a parameter 
in the function definition. The simplest way to do this is based on the order of the arguments
provided! 

NOTE: ORDER MATTERS IN POSITIONAL ARGUMENTS """

def describe_animal(animal_type, pet_name):
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}")

# keyword arguments: is a name-value pair that you pass to a function, you directly associate
# the name and the value within the argument, so when you pass the arguments to the function,
# so there's no confusion!
describe_animal(animal_type = 'dog', pet_name = 'benji')


""" return values: a function does not always have to display its output directly. Instead, it
can process some data and then return a value or set of value. the RETURN statement takes a value
from inside a function and sends it back to the line that called the function. """

def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()

print(get_formatted_name('cesar', 'rodriguez'))

# returning a dictionary:
def build_person(first_name, last_name):
    person = {'first': first_name, 'last': first_name} 
    return person

musician = build_person('jimmy', 'hendrix')
print(musician)

# using a function with a while loop
while True:

    print('\nPlease tell me your name:')
    print("(Enter 'q' at any time to quit)")

    f_name = input('First name: ')
    if f_name == 'q':
        break

    l_name = input('Last name: ')
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f'\nHello, {formatted_name}')


# passing a list
def greet_users(names):
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['cesar', 'jennifer', 'marcos']
greet_users(usernames)


# modifying a list in a function:
def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)


# using arbitrary keyword arguments:
def build_profile(first, last,  **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('cesar', 'rodriguez', location='princeton', field='physics')

print(user_profile)