from restaurants import Restaurant
#9.10
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['salted caramel toffe', 'spicy mango','strawberry blondie']
    def show_flavors(self):
        print('We have these ice cream flavors:')
        for flavor in self.flavors:
            print(f"{flavor.title()} ice cream.")

ice_cream_stand = IceCreamStand('Red Button','Creamery')
ice_cream_stand.describe_restaurant()
ice_cream_stand.open_restaurant()
ice_cream_stand.show_flavors()
