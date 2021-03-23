# A list is collection of items in particular order.
bicycles = ['trek', 'cannondale', 'redline', 'specialized']

""" I used a f-string in order to print the structure wether not I had to used 
a str() function to convert the list to string!"""
print(f'bicycles list: {bicycles}')
# using str function to print the values of the list
list_to_string = str(bicycles)
print('content of list to string: ' + list_to_string)

# print the first any element of the list using indexes
print(f'first element of the list: {bicycles[0].title()}')
print(f'last element of the list: {bicycles[-1].title()}')