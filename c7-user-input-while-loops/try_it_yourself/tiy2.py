# pizza toppings 
prompt = '\nPlease enter your pizza topping that you want.'
prompt += '\nEnter"quit" when you finished. '

flag = True

while flag:
    pizza_topping = input(prompt)

    if pizza_topping == 'quit':
        flag = False
    else:
        print(f'\nadding {pizza_topping.title()} to your pizza!')


# movie trackers
p = '\nDepending your age is how much the ticket will cost.'
p += '\nHow old are you? '
active = True

while active:
    age = input(p)
    age = int(age)

    if (age <= 12 and age >= 3):
        print('The cost of the ticket is $10')
        active = False
    else:
        print('The cost of the ticket is $15')
        active = False

