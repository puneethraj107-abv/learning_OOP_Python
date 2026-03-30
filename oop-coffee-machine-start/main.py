
from menu import Menu,MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu=Menu()
coffeemaker=CoffeeMaker()
moneymachine=MoneyMachine()

machine_operation=True

while machine_operation:
    options=menu.get_items()
    print('\nwelcome to the coffee machine\n')
    choice=input(f'what drink would you like to have {options}')
    if choice=='off':
        print('turing OFF the machine')
        machine_operation=False
    elif choice=='report':
        coffeemaker.report()
        moneymachine.report()
    else:
        drink = menu.find_drink(choice)
        if coffeemaker.is_resource_sufficient(drink):

            if moneymachine.make_payment(drink.cost):
                coffeemaker.make_coffee(drink)
