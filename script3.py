#2.Properties

from datetime import datetime

class User:
    def __init__(self,username,email):
        self.username=username
        self._email=email

    @property
    def email(self):
        print("Email is accessed")
        return self._email
    @email.setter
    def email(self,new_email):
        if "@" in new_email:
            self._email=new_email
        else:
            print('invalid email')

user1=User('dantheman','   Ddan@gmail.com   ')
user1.email="This is not a email"
print(user1.email)
