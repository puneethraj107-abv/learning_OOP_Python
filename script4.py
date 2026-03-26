#static attributes

class User:
    user_count=0

    def __init__(self,username,email):
        self.username=username
        self.email=email
        User.user_count+=1

    def display_user(self):
        print(f"Username: {self.username}, Email: {self.email}")

user1=User('dan','dan@gmail.com')
user2=User('lia','lia@gmail.com')

print(User.user_count)
print(user2.user_count)
