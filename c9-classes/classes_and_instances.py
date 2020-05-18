class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        # setting a default value for an attribute
        self.odometer_reading = 0 

    # getter method
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    # setter method
    def update_odometer(self, mileage):
        self.odometer_reading = mileage

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    # incrementing an attribute value through method
    def increment_odometer(self, miles):
        self.odometer_reading += miles



my_new_car = Car('audi', 'a4', 2019)
print("car description: " + my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# modifying attribute value --> Directly
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# modifying attribute value --> through a setter method:
my_new_car.update_odometer(1000)
my_new_car.read_odometer()

my_used_car = Car('subaru', 'outback', 2015)
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(23_500)
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer()
