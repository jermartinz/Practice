
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.rest_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        print(f"Restaurant name: {self.rest_name}"
        f"\nCuisine type: {self.cuisine_type}")
    def open_restaurant(self):
        print(f"The restaurant {self.rest_name} is open!")
    def set_number_served(self, served):
        self.number_served = served
        print(f"Customers has been served: {served}")
    def increment_number_served(self, customer ):
        self.number_served += customer
        print(f"Customer has been served it has increased to: {self.number_served}")

restaurant = Restaurant('Momoko', 'Sushi')
restaurant.describe_restaurant()
restaurant.open_restaurant()
#9.4
restaurant.set_number_served(10)
restaurant.increment_number_served(20)

#9.2
mexican_restaurant = Restaurant('Los establos', 'Mexican food')
chinese_restaurant = Restaurant('Fu San', 'Chine food')
vegan_restaurant = Restaurant('Vital', 'Vegan food')

mexican_restaurant.describe_restaurant()
chinese_restaurant.describe_restaurant()
vegan_restaurant.describe_restaurant()
