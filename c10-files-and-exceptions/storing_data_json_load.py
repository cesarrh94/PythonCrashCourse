import json

filename = 'c10-files-and-exceptions\\files\\numbers.json'

with open(filename) as f:
    # json.load(), is to load the information store in the json file and then assign it to a variable.
    numbers = json.load(f)

print(numbers)