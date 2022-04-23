'''prompt = "\nTell me something, and I wil repeat it back to you:"
prompt += "\nEnter  'quit' to end the program. "

active = True

while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)
'''

'''
prompt = "\nPlease enter the name of a city you have visited"
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(f"I'd love to go {city.title()}")
'''
#7.4
'''
pizza_toppings = "\nEnter a toppings for you pizza:"
pizza_toppings +="\nEnter 'quit' to end "

active = True
while active:
    message = input(pizza_toppings)

    if message == 'quit':
        active = False
    else:
        print(f"You added {message}")
'''
#7.5



movie_tickets = "\nHi, welcome to the cinema! How old are you? (input 0 to exit) "
while movie_tickets :
    client = int(input(movie_tickets))
    if client <= 3 and client > 0:
        print("\nThe ticket is free")
    elif client <= 12 and client > 0:
        print("\nThe ticket is $10")
    elif client > 12 and client > 0:
        print("\nThe ticket is $15")
    else:
        break

