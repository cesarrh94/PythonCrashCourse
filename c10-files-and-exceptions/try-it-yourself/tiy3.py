# addition calculator
while True:

    num1 = input("number 1: ")
    num2 = input("number 2: ")
    
    try:
        num1 = int(num1)
        num2 = int(num2)
    except ValueError:
        print("You can't add letters\n")
        break
    else:
        result = num1 + num2
        print(f"result: {result}\n") 

# cats and dogs
def read_file(file):
    try:
        with open(file) as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"\nSorry, the file {file} does not found!\n")
        # pass
    else:
        print(f"\nContents of {file}:\n")
        print(contents)

cats = "c10-files-and-exceptions\\files\\cat.txt"
dogs = "c10-files-and-exceptions\\files\\dogs.txt"

read_file(cats)
read_file(dogs)