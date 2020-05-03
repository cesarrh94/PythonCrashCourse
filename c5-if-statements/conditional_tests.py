car = 'bmw'

""" to check for equality use == 
depending the comparasion it wll return a True or False. """
print(car == 'bmw') # True
print(car == 'audi') # False

""" Ignoring case comparasions when checking for equality, can use
the string methods: upper, title y lower """
car = 'ToyoTa'
print(car.lower() == 'toyota')
print(car == 'toyota')

# To check for inequality, you can combine an exclamation point and an equal sign.
mexican_team_soccer = 'atlas'

if (mexican_team_soccer != 'atlas'):
    print('you know of soccer!')
else:
    print('you are fucked!')


# Checking for multiple conditions:
""" If you want to check multiple conditions at the same time we can use the 
keyword AND in the other hand OR allows to check multiple conditions as well, but it
passes when either or both of the individual test pass! """


# checking whether a value is in a list
pizzas_toppings = ['pepperoni', 'pinapple', 'salami']
print('pepperoni' in pizzas_toppings)


# checking whether a value is NOT in a list
pizzas_toppings = ['pepperoni', 'pinapple', 'salami']
print('ham' not in pizzas_toppings)



