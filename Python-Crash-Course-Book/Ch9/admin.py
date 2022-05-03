from user import User
#9.11
class Admin(User):
    def __init__(self, first_name, last_name, age, location):
        super().__init__(first_name, last_name, age, location)
        self.privileges = Privileges()

#9.8 
class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]
    def show_privileges(self):
        print('You have this privileges:')
        for privilege in self.privileges:
            print(privilege.title())

admin_user = Admin('Jeremy', 'Martinz', 22, 'California')
admin_user.describe_user()
admin_user.privileges.show_privileges()
#9.5
