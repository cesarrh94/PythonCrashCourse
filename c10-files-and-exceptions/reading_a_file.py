# NOTE: Windows use double back-slash for file paths.
filename = 'c10-files-and-exceptions\\files\\demo1.txt'

# open(argument = file): open the file and access to it
# keyword WITH: close the file once access to it in no longer needed.
with open(filename) as file_object:
    """ read(): use to read the entire contents of the file and store it as 
    contents = file_object.read() """

    """ read  the file line by line
    print("reading the file line by line: \n")
    for line in file_object:
        print(line.rstrip()) """

    """ making a list of lines from a file """
    lines = file_object.readlines()

""" the rstrip() method, its fuse is to delete the right space at the ending of the string to to match the original content of the file.
print("reading the entire file: \n\n" + contents.rstrip()) """

print(f"content of the list: {lines}\n")
print("looping through the list of lines from a file:")
for line in lines:
    print(line)
