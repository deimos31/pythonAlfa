from importlib.resources import is_resource
from coffe_maker import CoffeMaker
from menu import *
from money_machine import MoneyMachine

import os

"""Lets create all the objects we'll use"""
#creamos el objeto
coffee_maker = CoffeMaker()
menu = Menu()
money_machine= MoneyMachine()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f'What would you like to order?{options}')

    if choice == 'off':
        is_on = False
    
    elif choice == 'report':
        money_machine.report()
        coffee_maker.report()

    else:
        drink = menu.find_drink(choice)

        if coffee_maker.is_resources_sufficient(drink) == True and money_machine.make_payment(drink.cost) == True:
            coffee_maker.make_coffee(drink)

    os.system('clear')