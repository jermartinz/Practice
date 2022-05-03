def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)

#8.12
def sandwiches(*toppings):
    for topping in toppings:
        print(f"You have added {topping} to your sandwich ")
    print(f"Your sandwich has these toppings: {toppings}")

sandwiches('tomato')
sandwiches('tomato','lettuce')
sandwiches('tomato','lettuce', 'tuna')

#8.13
my_profile = build_profile('jeremy', 'martinz', favorite_place='madrid', 
                            favorite_language= 'python', aspiring='developer')
print(my_profile)
def make_car(**kwargs):
    return kwargs

car = make_car(manufacture='BMW', model='M4', color='grey', kilometers= 0)
print(car)