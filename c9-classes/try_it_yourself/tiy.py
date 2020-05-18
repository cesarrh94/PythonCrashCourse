# Restaurant
class Restaurant:

    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.name} serves {self.cuisine_type} food!")


""" my_restaurant = Restaurant('tortas rafa', 'mexican')
print(f"Restaurant name: {my_restaurant.name}")
print(f"Cuisine type: {my_restaurant.cuisine_type}")
my_restaurant.describe_restaurant() """


# Users
class User:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def greet_user(self):
        full_name = f"{self.first_name} {self.last_name}"
        print(f"Hello, {full_name.title()}")

    def describe_user(self):
        print(f"first name: {self.first_name}")
        print(f"last name: {self.last_name}")


""" user1 = User("cesar", "rodriguez")
user1.greet_user()
user1.describe_user()
print('\n')
user2 = User("aldo", "vazquez")
user2.greet_user()
user2.describe_user() """


# Ice Cream Stand
class IceCreamStand(Restaurant):

    def __init__(self, name, cuisine_type):
        super().__init__(name, cuisine_type)
        self.flavors = ['chocolate', 'vanilla', 'strawberry']

    def get_flavors(self):
        print("list of ice cream flavors:")
        for flavor in self.flavors:
            print(f"- {flavor}")

new_ice_cream_stand = IceCreamStand('sugar island', 'desserts')
new_ice_cream_stand.describe_restaurant()
new_ice_cream_stand.get_flavors()


class Privileges():

    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print("showing admin privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

# Administrator
class Admin(User):

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()


admin = Admin('cesar', 'rodriguez')
admin.greet_user()
# admin.describe_user()
admin.privileges.show_privileges()
