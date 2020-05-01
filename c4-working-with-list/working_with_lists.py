# slicing a list
""" to make a slice, you specify the index of the first and last elements you want to
work with. """
players = ['cesar', 'jenni', 'marcos', 'rosalba', 'rafa']
print(players[0:3])

""" if you omit the first index, python automatically starts your slice at the beginning 
of the list. Is the same case if you omit the second index it will stop at the end of 
the list."""
print(players[:4])
print(players[1:])

# returns the last two elements!
print(players[-2:]) 

# looping through a slice
print('The most skillful players are: \n')
for player in players[:3]:
    print(player.title())


""" To copy a list, you can make a slice that includes the entire original list by 
omitting the first index and second index ([:])"""
my_foods = ['tacos', 'pizza', 'hamburger']
friend_foods = my_foods[:]
print(f'My favorite foods are: {my_foods}')
print(f'My friends favorite foods are: {friend_foods}')