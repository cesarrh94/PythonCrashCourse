import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'c10-files-and-exceptions\\files\\numbers.json'

with open(filename, 'w') as f:
    # json.dump(), takes two arguments: a piece of data to store and a file object it can use to
    # store the data. 
    json.dump(numbers, f)