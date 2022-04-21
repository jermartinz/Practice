#6.1 and #6.7

import numbers


member = {'first_name': 'john', 'last_name': 'davis', 'age': 22}
    
astronaut = {'first_name': 'elon', 'last_name': 'hinton', 'age': 35}

pilot = {'first_name': 'david', 'last_name': 'ward', 'age': 38}

person = [member, astronaut, pilot]

for crew_member in person[:3]:
    print(f"\n{crew_member}")


#6.2
favorite_numbers = {
    'liam': [7, 2],

    'amelia':[4, 10],

    'benjamin': [12, 20],

    'violet': [8, 16],

    'olivia': [9, 32]
    
}
for people, favorite_n in favorite_numbers.items():
    print(f"\n{people.title()}'s favorite number is:")
    for favorite in favorite_n:
        print(f"\t{favorite}")

#6.3
glossary = {
    'insert': 'You can add a new element at any position in your list by using the insert method',
    'pop': 'You can use pop to remove an item from any position in a list',
    't': 'To add a tab to your text, use this character combination',
    'n': 'To add a newline in a string, use this character combination',
    'tuple': 'A tuple looks just like a list except you use parentheses instead of square brackets'
    
}

#6.4
for word, meaning in glossary.items():
    print (f"\n {word.title()}: {meaning}")

#6.5
rivers = {
    'ganges': 'india',
    'nile': 'egypt',
    'misuri': 'usa'
}

for river, country in rivers.items():
    print(f'\nThe {river.title()} runs trough {country.title()}')


for river in rivers.keys():
    print(river.title())

for country in rivers.values():
    print(country.title())


favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'jack': 'c++',
    'chris': None,
    'sophia': None

}
#6.6
for person, language in favorite_languages.items():
    if language == None:
        print(f'Please take the poll {person.title()}')
    else:
        print(f'Thanks {person.title()} for respond the poll. Your vote was {language.title()}.')
