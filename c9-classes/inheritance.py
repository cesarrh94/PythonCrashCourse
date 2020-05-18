""" INHERITANCE
you don't always have to start from scratch when writing a class. If the class you're writing is a 
specialized version of another class you wrote, you can use inheritance. When one class inherits from
another, it takes on the attributes and methods of the first class.

The original class is called the parent class, and the new class is the child class. The child class can 
inherits any or all of the attributes and methods of its parent class, but its also free to define
new attributes and methods of its own. """

class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def fill_gas_tank(self):
        print("filling gas tank...")


class Battery:

    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery")

# example of INHERITANCE:
class ElectricCar(Car):
    
    def __init__(self, make, model, year):
        # calling the  constructor (_init_ method) of the parent class.
        super().__init__(make, model, year)
        
        # defining attributes and methods of the child class
        # self.battery_size = 75
        
        # instances as attributes
        self.battery = Battery()

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    """ to OVERRIDE A METHOD from a parrent class: define a method in the child class with the same
    name as the methods you want to override in the parent class. Python will disregard the parent
    class method and only pay attention to the method you define in the child class. """
    def fill_gas_tank(self):
        print("this car doesn't need a gas tank!")


my_tesla = ElectricCar('tesla', 'model s', 2019)
print("description: " + my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.fill_gas_tank()











