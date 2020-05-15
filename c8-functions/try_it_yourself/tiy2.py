# t-shirt
def make_shirt(size = "l", message = 'i love python'):
    print(f"\nThe size of the t-shirt: {size.upper()}")
    print(f"The message to be printed on the t-shirt: {message.upper()}")
    
# make_shirt('xxl', 'I hate java')
# make_shirt(size = 'xxl', message = 'I hate java')

make_shirt()


# cities
def describe_city(city_name, country = 'united states'):
    print(f"{city_name.title()} is in {country.title()}")

describe_city('los angeles')
describe_city('vancouver', 'canada')
describe_city('tokyo', 'japan')