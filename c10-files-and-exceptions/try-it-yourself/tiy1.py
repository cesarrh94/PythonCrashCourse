filename = 'c10-files-and-exceptions\\files\\demo2.txt'

with open(filename) as file_object:
    contents = file_object.read()

print(f"printing the entire file: \n{contents.rstrip()}")


with open(filename) as fileObject:
    print("\nprinting content line by line:")
    for line in fileObject:
        print(line)


with open(filename) as fo:
    lines = fo.readlines()

print(f"printing the list's content: \n{lines}")


# this block is used to modified the original content of the list
s = ''
for line in lines:
    s += line.rstrip()

print("\noriginal list content:\n" + s)
print("\nmodified list content:\n" + s.replace('Python', 'Java'))

