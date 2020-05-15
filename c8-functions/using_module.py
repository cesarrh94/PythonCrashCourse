""" Storing functions in modules:
One advantage of functions is they way they separate blocks of code from your main program.
An 'import' statement tells Python to make the code in a module available in the currently running
file. 

Storing your functions in a separate file allows you to hide the details of your program’s code and 
focus on its higher-level logic. It also allows you to reuse functions in many different programs."""

# also you can import a specific function from a module. 
# from module_name import function_name

import module

module.make_pizza(16, 'pepperoni')
module.make_pizza(12, 'pepperoni', 'mushrooms', 'sausage')