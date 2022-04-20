#5.7
favorite_fruits = ['apple', 'banana', 'peach']
if 'apple' in favorite_fruits:
    print('You really like apples!')
if 'pineapple' in favorite_fruits:
    print('You really like pineapples!')
if 'banana' in favorite_fruits:
    print('You really like bananas!')
if 'mango' in favorite_fruits:
    print('You really like mango!')
if 'peach' in favorite_fruits:
    print('You really like peach!')

requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f'Adding {requested_topping}.')
    print('\n Finished making your pizza!')
else:
    print('Are you sure you want a plain pizza?')

available_toppings = ['mushrooms', 'olives', 'green pepers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f'Adding {requested_topping}.')
    else:
        print(f"Sorry, we don't have {requested_topping}.")
print("\nFinished making your pizza")
