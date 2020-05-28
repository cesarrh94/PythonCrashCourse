import json

favorite_number = int(input("What is your favorite number? "))

filename = "c10-files-and-exceptions\\files\\favorite_number.json"

with open(filename, 'w') as f:
    json.dump(favorite_number, f)