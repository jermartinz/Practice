
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

my_foods = ['pizza', 'falafel', 'carrot cake']
friends_foods = my_foods[:]

my_foods.append('cannoli')
friends_foods.append('ice cream')

#4.12
print('My favorite foods are:')
for foods in my_foods:
    print(foods.title())



print("\n My friend's foods are:")

for food in friends_foods:
    print(food.title())

#4.10
print(f"The first three items in the list are:{my_foods[0:3]}")
print(f"Three items from the middle of the list are:{players[1:3]}")
print(f"The last three items in the list are:{players[2:5]}")

#4.11
pizzas = ['pepperoni', 'margherita', 'mushrooms']
friend_pizzas = ['pepperoni', 'margherita', 'mushrooms']
pizzas.append('chicken')
friend_pizzas.append('veggie')

print('My favorites pizzas are:')
for pizza in pizzas:
    print(pizza.title())

print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza.title())




