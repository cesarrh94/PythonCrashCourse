import json

username = input("What is your name? ")

filename = 'c10-files-and-exceptions\\files\\username.json'
with open(filename, 'w') as f:
    json.dump(username, f)
    print(f"We'll remember you when you come back, {username}!\n")