#7.8
sandwich_orders = ['Chicken Sandwich','pastrami sandwich', 'pastrami sandwich', 'pastrami sandwich','Egg Sandwich','Seafood Sandwich']
finished_sandwiches = []
while sandwich_orders:
    current_order = sandwich_orders.pop()
    print(f"I made your {current_order.title()}")
    finished_sandwiches.append(current_order)

print("\nWe made these sandwiches today!")
for sandwich in finished_sandwiches:
    print(sandwich.title())

print("\nDeli of Pastrami Sandwich has run out")

while 'pastrami sandwich' in sandwich_orders:
    sandwich_orders.remove('pastrami sandwich')

print(sandwich_orders)

dream_vacation = {}

poll_activate = True

while poll_activate:
    name = input("\nWhat is your name? ")
    vacation = input("What are your dream vacations? ")

    dream_vacation[name] =  vacation

    repeat = input("Would you like to let another person respond?(yes/no)")
    if repeat == 'no':
        poll_activate = False

print("---Poll results---")
for name, vacation in dream_vacation.items():
    print(f"{name} would like to go on vacation to {vacation}.")