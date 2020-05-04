cities = {
    'tokyo': {
        'country': 'japan',
        'population': 13_929_280,
        'fact': 'tokyo is the largest metropolitan in the world.'
    },
    'guadalajra': {
        'country': 'mexico',
        'population': 1_460_148,
        'fact': 'the land of the mariachi and tequila.'
    },
    'Los Angeles': {
        'country': 'united states',
        'population': 3_976_322,
        'fact': 'it is the second-most populous city in the united states, after new york.'
    }
}

for cities, cities_info in cities.items():
    print(f'city: {cities}')

    country = cities_info['country']
    population = cities_info['population']
    fact = cities_info['fact']

    print(f"\tcountry: {country}")
    print(f"\tpopulation: {population}")
    print(f"\tfact: {fact}\n")