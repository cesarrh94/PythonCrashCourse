filename = 'c10-files-and-exceptions\\files\\demo4.txt'

""" name = input("Type your name: ")

with open(filename, 'w') as file_object:
    file_object.write(f"name: {name.capitalize()}.\n") """


message = "Type your name and favorite book to add to the file.\n"
message += "Or type 'quit' to finish the program.\n"

while True:
    
    print(message)
    
    n = input("name: ")
    if n.lower() == 'quit':
        break

    book = input("book: ")
    if book.lower() == 'quit':
        break

    with open(filename, 'a') as fileObject:
        fileObject.write(f"name: {n}, book: {book}.\n")
