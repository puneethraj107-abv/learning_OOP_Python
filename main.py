class Dog:
    def __init__(self,name,breed,owner):
        self.name=name
        self.breed=breed
        self.owner=owner

    def bark(self):
        print("woof woof")

class Owner:
    def __init__(self,name,address,contact_number):
        self.name=name
        self.address=address
        self.Phone_number=contact_number



owner1=Owner('people with common sense','somewhere on earth','9148773959')
dog1=Dog('dhruv_rathee','german shepherd',owner1)
dog1.bark()
print(dog1.breed)
print(dog1.name)
print('the name of the owner of dog1 is',dog1.owner.name)

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def greet(self):
        print(f'hello my name is {self.name} & I am {self.age} years old')


person1=Person('rajashekar',22)
person1.greet()

person2=Person('geetha',26)
person2.greet()
