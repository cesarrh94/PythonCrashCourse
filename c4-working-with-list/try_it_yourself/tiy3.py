laptop_brands = ['apple', 'lenovo', 'hp', 'dell', 'asus']
print(laptop_brands[:3])
print(laptop_brands[1:4])
print(laptop_brands[-3:])

my_pizzas = ['hawaiian', 'pepperoni', 'supreme']
friends_pizzas = my_pizzas[:]

print(my_pizzas)
print(friends_pizzas)

my_pizzas.append('meat lover')
friends_pizzas.append('vegetarian')

print(f'My favorite pizzas are: {my_pizzas}')
print(f'My friends favorite pizzas are: {friends_pizzas}')