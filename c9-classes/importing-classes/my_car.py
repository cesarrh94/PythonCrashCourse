# import a single class
""" from car import Car

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name()) """


# importing multiple classes from a module
from car import Car, ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'cybertruck', 2020)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

# importing an entire module
""" import car 

my_beetle = car.Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name()) 

my_tesla = car.ElectricCar('tesla', 'model x', 2020)
print(my_tesla.get_descriptive_name()) """

# importing all classes from a module
# from module_name import *