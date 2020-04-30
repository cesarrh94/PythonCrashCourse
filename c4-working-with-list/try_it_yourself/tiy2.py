for n in range(1, 21):
    print(n)

""" for n in range(1, 1_000_000):
    print(n) """


list_to_millon = []
for value in range(1, 1000000):
    number_to_append = value
    list_to_millon.append(number_to_append)
    
print(sum(list_to_millon))
