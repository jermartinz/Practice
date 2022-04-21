pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

print(f"You ordered a {pizza['crust']}-crust pizza "
    "with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")


#many_user.py
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")


#6.8

pet_one = {
    'kind': 'dog',
    'name': 'firulais',
    'owner': 'jack',
}

pet_two = {
    'kind': 'fish',
    'name': 'nemo',
    'owner': 'elon',
}
pet_three = {
    'kind': 'cat',
    'name': 'michi',
    'owner': 'louis',
}

pets = [pet_one, pet_two, pet_three]

for pet in pets:
    print(f"{pet}")

#6.9 
favorite_places = {
    'fanny': ['brazil', 'paris'],
    'hector': ['korea', 'japan'],
    'jeremy': ['california', 'barcelona', 'dubai'],
}
for friend, places in favorite_places.items():
    print(f"\nThe favorite places of {friend.title()} is:")
    for place in places:
        print(f"\t{place.title()}")
#6.11
cities = {
    'paris': {
        'country': 'france',
        'population': '2.161 millions',
        'fact':'city of fashion',
    },
    'california': {
        'country': 'united states',
        'population': '39.967 millions',
        'fact':'hollywood',
    },
    'santiago':{
        'country': 'chile',
        'population': '5.161 millions',
        'fact':'los andes',
    },
}

for city, city_info in cities.items():
    print(f"\nCity: {city.title()}")
    print(f"\tCountry: {city_info['country'].title()}")
    print(f"\tPopulation: {city_info['population']}")
    print(f"\tFact: {city_info['fact'].title()}")

