import json

filename = 'c10-files-and-exceptions\\files\\username.json'

with open(filename) as f:
    username = json.load(f)
    print(f"Welcome back, {username}!")