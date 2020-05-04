favorite_places = {
    'cesar': ['jalisco', 'nayarit'],
    'maritza': ['michoacan', 'colima'],
    'martin': ['sonora']
}

for k, v in favorite_places.items():
    name = k.title()
    print(f"{name}'s favorite places are: ")
    
    for places in v:
        print(f'\t{places}')