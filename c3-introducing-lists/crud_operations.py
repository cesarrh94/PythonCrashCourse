# example list:
motorcycles = ['honda', 'yamaha', 'suzuki']
print(f'motorcycles list (initial state): {motorcycles}')

# modifying an element
motorcycles[-1] = 'ducatti'
print(f'motorcycles list (last element modified): {motorcycles}')

# adding element to the end of the list
motorcycles.append('vemon')
print(f'motorcycles list (element add): {motorcycles}')

# adding elements into a list (any position)
motorcycles.insert(2, 'suzuki')
print(f'motorcycles list (element add): {motorcycles}')

# removing elements using the del statement
del motorcycles[2]
print(f'motorcycles list (removing using del --> "suzuki"): {motorcycles}')

# removing the last element using the pop() method
# NOTE: the pop() method can also remove any element of the list, only using its index!
print(f'motorcycles list (BEFORE popping last element): {motorcycles}')
removed_element = motorcycles.pop()
print(f'element popped: {removed_element}')
print(f'motorcycles list (AFTER popping last element): {motorcycles}')


# removing an element by value using remove() method.
motorcycles.remove('yamaha')
print(f'motorcycles list (removing using remove() --> "yamaha"): {motorcycles}')



