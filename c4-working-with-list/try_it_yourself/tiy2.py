for n in range(1, 21):
    if (n % 2 == 0):
        print(f'{n} is even')
    else:
        print(f'{n} is odd')

""" for n in range(1, 1_000_000):
    print(n) """


list_to_millon = []
for value in range(1, 1000000):
    number_to_append = value
    list_to_millon.append(number_to_append)
    
print(sum(list_to_millon))


for n in range(3, 31):
    if (n % 3 == 0):
        print(n)
    

cubes_list = []
for value in range(1, 11):
    cube = value ** 3
    cubes_list.append(cube)

print(cubes_list)


cubes = [value ** 3 for value in range(1, 11)]
print(cubes)

