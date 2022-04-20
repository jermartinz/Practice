#5.8
users = ['admin', 'user000', 'user001','user002', 'user003', 'user004']

for user in users:
    if user == 'admin':
        print('Hello admin, would you like to see a status report?')
    else:
        print(f'Hello {user}, thank you for logging in again.')

#5.9
no_users = []
if len(no_users) <= 0:
    print('We need to find some users!')

#5.10
current_users = ['Oliver', 'William', 'Charlotte', 'Noah', 'Sophia']
current_users_upper = ['OLIVER', 'WILLIAM', 'CHARLOTTE', 'NOAH', 'SOPHIA']
new_users = ['Jack', 'Grace', 'Mia', 'Charlotte', 'Lucas', 'Sophia']

for new_user in new_users:
    if new_user in current_users or new_user in current_users_upper:
        print('You need enter a new username because this is has already been used')
    else:
        print(f'The user name {new_user}, is available!')

#5.11
ordinal_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9,]

for numbers in ordinal_numbers:
    if numbers == 1:
        print(f'{numbers}st')
    elif numbers == 2:
        print(f'{numbers}nd')
    elif numbers == 3:
        print(f'{numbers}rd')
    else:
        print(f'{numbers}th')