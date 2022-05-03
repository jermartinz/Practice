
#9.12
class User:
    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.login_attempts = 0
    def describe_user(self):
        print(f"User Name: {self.first_name} {self.last_name}\nAge: {self.age}\nLocation: {self.location}")
    def greet_user(self, greeting):
        self.greeting = greeting
        print(f"Greeting: {greeting}")
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attemps(self):
        self.login_attempts = 0

first_user = User('Stephen', 'Bolton', 26, 'California')
first_user.describe_user()
first_user.greet_user('Sup!')

first_user.increment_login_attempts()
first_user.increment_login_attempts()
first_user.increment_login_attempts()
first_user.increment_login_attempts()
login = first_user.login_attempts
print(f"Logins: {login}")
first_user.reset_login_attemps()
reset_login = first_user.login_attempts
print(f"Logins: {reset_login}")