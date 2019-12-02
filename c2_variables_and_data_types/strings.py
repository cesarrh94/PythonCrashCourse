# what is a string??
# a string is a series of characters, anything inside single or double quotes is a string in python.

single_quotes_string = 'cesar'
double_quotes_string = "cesar"

name = 'cesar ivan rodriguez hernandez'

# title() method change the string to a capitalized version
print(name.title()) # output: Cesar Ivan Rodriguez Hernandez

# upper() method change the string to an uppercased version
print(name.upper()) # output: CESAR IVAN RODRIGUEZ HERNANDEZ

# lower() method change the string to an lowercased version
print(name.lower()) # output: cesar ivan rodriguez hernandez


# this is a way to used variables in a string
first_name = 'cesar'
last_name = 'rodriguez'
full_name = f'Hello, {first_name} {last_name}' #f-strings and the f stands for "format"
print(full_name)


# adding whitespaces to string with tabs or newlines
print('Python') # no tab
print('\tPython') # with tab

print('Python is the best!') # no newlines
print('Python \nis the \nbest!') # 3 newlines


# stripping whitepaces
favorite_language = 'python '
print(favorite_language)
# rstrip() method removes the right whitespaces of the string (ending)
favorite_language = favorite_language.rstrip() 
print(favorite_language)

favorite_language = ' python'
# lstrip() method removes the left whitespaces of the string (beginning)
favorite_language = favorite_language.lstrip() 
print(favorite_language)
