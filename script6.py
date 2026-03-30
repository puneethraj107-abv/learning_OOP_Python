from turtle import Turtle,Screen

timmy=Turtle()
print(timmy)

myscreen=Screen()
print(myscreen.canvheight)
timmy.shape('turtle')
timmy.color('coral')
timmy.forward(100)
myscreen.exitonclick()


from prettytable import PrettyTable

table=PrettyTable()
table.add_column('Pokemon name',['pikachu','charmander','squirtle'])
table.add_column('Type',['Electric','Fire','Water'])
table.align='l'
print(table)
