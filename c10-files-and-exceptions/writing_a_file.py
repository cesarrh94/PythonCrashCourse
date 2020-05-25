filename = 'c10-files-and-exceptions\\files\\demo3.txt'

# these are the modes:
#  'r' --> reads, 'w' --> write, 'a' --> append
with open(filename, 'w') as file_object:
    file_object.write("writing in a file.\n")
    file_object.write("writing another line in a file.\n")

# appending mode: 'a'
with open(filename, 'a') as fileObject:
    fileObject.write("appending line 1.\n")
    fileObject.write("appending line 2.\n")