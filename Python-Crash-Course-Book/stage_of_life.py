#5.6
age = 67

if age < 2:
    print('You are a baby')
elif age == 2 or age <= 4:
    print('You are toddler')
elif age == 4 or age <= 13:
    print('You are a kid')
elif age == 13 or age <= 20:
    print('You are a teenager')
elif age == 20 or age <= 65:
    print('You are adult')
elif age >= 65:
    print('You are a elder')