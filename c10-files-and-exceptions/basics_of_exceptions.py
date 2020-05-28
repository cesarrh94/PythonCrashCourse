""" EXCEPTIONS:
Python uses special objects called exceptions to manage errors that arise during a program's
execution. Whenever an error occurs that makes Python unsure what to do next, it creates an
exception object. If you write code that handles the exception, the program will continue 
running. If you don't handle the exception, the program will halt and slow a traceback, which
includes a report of the exception that was raised.

Exceptions are handled with try-except blocks. A try-except block asks Python to do something,
but only it also tells Python what to do if an exception is raised.
When you use a try-except blocks, your programs will continue running even if things start to 
go wrong. Instead of traceback, which can be confusing for users to read, users will see
friendly error message that you write."""


# handling the ZeroDivisionError exception
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!\n")

# using exceptions to prevent crashes
print("Give me to numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:

    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break

    second_number = input("Second number: ")
    if second_number == 'q':
        break

    # The try-except_else block works like this: Python attempts to run the code in the try block.
    # The only code that should go in a try block is code that might cause an exception to be raised.
    # Sometimes you'll have additional code that should run only if the try block was successful; this
    # code goes in the else block. The except block tells Python what to do in case a certain exception
    # arise when it tries to run the code in the try block.
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(answer)


# handling the FileNotFoundError exception
filename = 'c10-files-and-exceptions\\files\\demo4.txt'

try:
    with open(filename) as f:
        contents = f.read()
except FileNotFoundError:
    # print(f"\nSorry, the file {filename} does not exist.")
    
    # to make the program fail silently, you write a try block as usual, but you explicitly 
    # tell Python to do nothing in the except block. Python has a PASS statement that tells it
    # to do nothing in a block.
    pass
else:
    print(f"\ncontent of the file {filename}:\n")
    print(contents)