unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    current_users = unconfirmed_users.pop()

    print(f"Verifying user: {current_users.title()}")
    confirmed_users.append(current_users)

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

#pets.py 
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

#mountain_poll.py

responses = {}

polling_activate = True

while polling_activate:
    name = input("\nWhat is your name?")
    response = input("Which mountain would you like to climb someday?")

    responses[name] = response

    repeat = input("Would you like to let another person respond?(yes/no)")
    if repeat == 'no':
        polling_activate = False

print("\n---Poll Results---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")
