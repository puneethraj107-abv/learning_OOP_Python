from datetime import datetime

class User:
    def __init__(self,username,email):
        self.username=username
        self._email=email

    def clean__email(self):
        return self._email.lower().strip()

    def say_hi_to_user(self,user):
        print(f"sending hi to {user.username}: Hi {user.username}\n it's {self.username}")

    def get_email(self):
        print(f'email accessed at {datetime.now()} ')
        return self._email

    def set_email(self,new_email):
        if '@' in new_email and '.com' in new_email:
            self._email=new_email
        else:
            print('invalid email address')

user1=User('dantheman','   Ddan@gmail.com   ')
print(user1._email)
print('email before change',user1.clean__email())
user1.set_email("puneeth@gmail.com")
print('email after change',user1.get_email())
