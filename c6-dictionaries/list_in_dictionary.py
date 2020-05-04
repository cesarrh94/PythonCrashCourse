# Working a list in a dictionary


# example 1: Storing information about a pizza being ordered
pizza = {
    'crust': 'thin',
    'toppings': ['ham', 'pepperoni', 'italian sausage']
}

print(f"you order a {pizza['crust']}-crust pizza")

for topping in pizza['toppings']:
    print(f"{topping}")


# example 2: programming languages

favorite_languages = {
    'jenni': ['javascript', 'java'],
    'aldo': ['java'],
    'cesar': ['python', 'javascript', 'java']
}

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")

    for language in languages:
        print(f"\t{language.upper()}")