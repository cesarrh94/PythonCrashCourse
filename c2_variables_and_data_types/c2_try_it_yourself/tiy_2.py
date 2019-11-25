#  2.3 Personal Message:
name = 'cesar'
personal_message = f'Hello {name.title()}, would you like to learn some Python today?'
print(personal_message)

# 2.4 Name Cases: 
name2 = 'cesar Ivan'
print('lowercase: ' + name2.lower())
print('uppercase: ' + name2.upper())
print('titlecase: ' + name2.title())

# 2.5 & 2.6 Famous Quote
famous_person = 'Escanor'
quote = 'I will protect my comrades no matter what!'
print(f'{famous_person} once said, "{quote}"')

# 2.7 Stripping Names
nnt_name = '   Elizabet Liones'
print(nnt_name)
print(nnt_name.lstrip())
nnt_name = 'Elizabet Liones   '
print(nnt_name)
print(nnt_name.rstrip())
nnt_name = '   Elizabeth Liones   '
print(nnt_name)
print(nnt_name.strip())