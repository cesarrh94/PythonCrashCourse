#  working a dictionary in a dictionary:

users = {
    1: {
        'name': 'lu bu housen',
        'country': 'china'
    },

    2: {
        'name': 'adan',
        'country': 'paradise'
    },

    3: {
        'name': 'sasaki, kojiro',
        'country': 'japan'
    }
}

for user_number, user_info in users.items():
    print(f"\nuser_number: {user_number}")
    
    name = user_info['name']
    country = user_info['country']

    print(f"\tname: {name.title()}")
    print(f"\tcountry: {country.title()}")