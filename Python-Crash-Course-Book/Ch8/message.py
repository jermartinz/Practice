#8.1
def display_message():
    print("I learning about basics functions")

display_message()

#8.2 
def favorite_book(title):
    print(f"One of my favorite books is {title}.")

favorite_book("Alice in Wonderland")
#8.3 and #8.4
def make_shirt(size, text='I love Python'):
    print(f"The size of your shirt it will be {size} and the text '{text}'.")

make_shirt("S")
make_shirt("M")
make_shirt("S", "Space")
#8.5
def describe_city(city="Madrid", country="Spain"):
    print(f"{city} is in {country}")

describe_city()
describe_city("Barcelona")
describe_city("Seattle")
