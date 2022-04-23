#7.1

rental_car = input("What kind of rental car would you like? ")
print(f"Let me see if i can find you a {rental_car.title()}.")

#7.2
restaurant_seating = input("How many people are in your dinner group? ")
restaurant_seating = int(restaurant_seating)
if restaurant_seating >= 8:
    print("You must wait for a table")
else:
    print("The table is ready!")
#7.3
multiples_ten = input('Give me a number! ')
multiples_ten = int(multiples_ten)
if multiples_ten % 10 == 0:
    print('Your number is multiple of 10!')
else:
    print('Your number is not multiple of 10.')