#range
for value in range(1, 6):
    print(value)

#squares
squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)

#List Comprehensions
squares = [value**2 for value in range(1, 11)]
print(squares)

#4.3
for value in range(1, 21):
    print(value)

#4.4
million = [value for value in range(1, 100001)]
print(million)
#4.5
print(min(million))
print(max(million))
print(sum(million))

#4.6
for value in range(1, 20, 3):
    print(value)
#4.7
threes = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
for value in threes:
    print(value)
#4.8
cubes = []
for value in range(1, 11):
    cubes.append(value**3)
print(cubes)
#4.9
cubes = [value**3 for value in range(1, 11)]
print(cubes)
