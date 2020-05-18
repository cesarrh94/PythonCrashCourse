""" In Object Oriented Programming (OOP) you write classes that represent real-world 
things ans situations, and you create objects bases on these classes. When you create individual 
objects from the class, each object is automatically equipped with hte general behavior.

Making an object from a class is called: instantiation, and you work with instances of a class. """

# example of a simple class
class Dog:
    """ A simple attemp to model a dog! """

    # the _init_ method is: similar to a constructor in Java
    # self: references to the instance itself it gives the individual instance
    # access to the attributes and methods in the class; "similar to THIS in Java"
    def __init__(self, name, age):
        self.name = name.title()
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting!")

    def roll_over(self):
        print(f"{self.name} rolled over!")


# making an instance of a class:
# to access the attributes of an instance, you use dot notation.

# creating multiple instances:
my_dog = Dog('benji', 3)
your_dog = Dog('vaquita', 10)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

# calling a method!
my_dog.sit()
my_dog.roll_over()

print(f"My dog's name is {your_dog.name}.")
print(f"My dog is {your_dog.age} years old.")
your_dog.sit()
your_dog.roll_over()




