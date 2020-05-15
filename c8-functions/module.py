# this function is using an arbitrary number of arguments
""" the asterisk * in the parameter tells Python to make an empty tuple to pack whatever values
it receives into this tuple. """

def make_pizza(size, *toppings):
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"-{topping}")