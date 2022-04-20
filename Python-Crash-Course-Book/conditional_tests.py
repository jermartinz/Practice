#5.2
word = 'bottle'
word2 = 'BOTTLE'
print(word == word2)

print(word == word2.lower())

number = 10
number2 = 2

if number > 1 and number2 > 1:
    print('This numbers are greater than 1')

if number > 20 or number2 > 1:
    print('This number are greater than 1')


brands_phones = ['apple', 'samsung', 'huawei']

apple = 'apple'

if apple in brands_phones:
    print('apple is a brand phone')

if 'Xiamoi' not in brands_phones:
    print('Add to brand phone list')

