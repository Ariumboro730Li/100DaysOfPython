from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
# Add new menu 
menu.menu.append(
    MenuItem(name="teh_kotak", water=200, milk=150, coffee=24, cost=2.5),
)
coffe_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_machine_on = True
while is_machine_on:
    choice = input(f"What ☕ would you like? {menu.get_items()}:").lower()
    if choice == 'off':
        is_machine_on = False
    elif choice == "report":
        coffe_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if drink:
            if coffe_maker.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffe_maker.make_coffee(drink)

