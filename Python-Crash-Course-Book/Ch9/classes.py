class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sit(self):
        print(f"{self.name} is now sitting.")
    def roll_over(self):
        print(f"{self.name} rolled over!")

my_dog = Dog('Willie', 6)
print(f"My dog's name is {my_dog.name}")
print(f"My dog is {my_dog.age} years old")
my_dog.sit()
my_dog.roll_over()

your_dog = Dog('Lucy', 3)
print(f"\nYour dog's name is {your_dog.name}")
print(f"Your dog is {your_dog.age} years old")
your_dog.sit()
your_dog.roll_over()

#9.1
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.rest_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(f"Restaurant name: {self.rest_name}\nCuisine type: {self.cuisine_type}")
    def open_restaurant(self):
        print(f"The restaurant {self.rest_name} is open!")

restaurant = Restaurant('Momoko', 'Sushi')
restaurant.describe_restaurant()
restaurant.open_restaurant()

#9.2
mexican_restaurant = Restaurant('Los establos', 'Mexican food')
chinese_restaurant = Restaurant('Fu San', 'Chine food')
vegan_restaurant = Restaurant('Vital', 'Vegan food')

mexican_restaurant.describe_restaurant()
chinese_restaurant.describe_restaurant()
vegan_restaurant.describe_restaurant()

#9.3
class User:
    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
    def describe_user(self):
        print(f"User Name: {self.first_name} {self.last_name}\nAge: {self.age}\nLocation: {self.location}")
    def greet_user(self, greeting):
        self.greeting = greeting
        print(f"Greeting: {greeting}")
    
first_user = User('Stephen', 'Bolton', 26, 'California')
first_user.describe_user()
first_user.greet_user('Sup!')