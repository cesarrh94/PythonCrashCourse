import json

filename = 'c10-files-and-exceptions\\files\\favorite_number.json'

with open(filename) as f:
    favorite_number = json.load(f)

print(f"I know your favorite number! It's {favorite_number}")