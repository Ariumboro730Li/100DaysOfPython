from menu import MENU, resources
from colorama import init, Fore
import os


init()


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def compare_resources(the_choice):
    menu_resource = MENU[the_choice]['ingredients']
    is_resource_sufficient = False
    for resource in menu_resource:
        is_resource_sufficient = (resources[resource] >= menu_resource[resource])
        if not is_resource_sufficient:
            print(f"Sorry there is not enough {resource}")
            break

    return is_resource_sufficient


def make_the_coffee():
    menu_resource = MENU[choice]['ingredients']
    for resource in menu_resource:
        resources[resource] -= menu_resource[resource]


def insert_coins():
    global coins
    # quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
    #  E.g. 1 quarter, 2 dimes, 1 nickel, 2 pennies
    #  = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
    coins += float(input(f"{Fore.BLUE}How many quarters ?")) * 0.25
    coins += float(input(f"{Fore.BLUE}How many dimes ?")) * 0.10
    coins += float(input(f"{Fore.BLUE}How many nickles ?")) * 0.05
    coins += float(input(f"{Fore.BLUE}How many pennies ?")) * 0.01
    return coins


def compare_cost():
    global changes
    global coins
    global choice
    global cost
    cost += MENU[choice]['cost']
    changes = float(format(coins - cost, ".2f"))
    return coins >= cost


def available_menu():
    the_menu = []
    for menu in MENU:
        numb_comparison = 1
        for item in MENU[menu]['ingredients']:
            if not resources[item] >= MENU[menu]['ingredients'][item]:
                numb_comparison = 0
                break

        if numb_comparison > 0:
            the_menu.append(menu)

    return the_menu


is_machine_on = True
incomes = 0
ordered_menu = []
# clear_terminal()

while is_machine_on:
    cost = 0
    coins = 0
    changes = 0
    choice = input(f"{Fore.LIGHTGREEN_EX}What ☕ would you like? (espresso/latte/cappuccino):").lower()
    if choice == 'off':
        is_machine_on = False
    elif choice == 'report':
        print(f"{Fore.RESET}Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${incomes}")
        print(f"Ordered Menu: {ordered_menu}")
    elif choice == 'menu':
        print(f"the available menus are {available_menu()}")
    elif choice == 'clear':
        clear_terminal()
    elif compare_resources(choice):
        print(f"{Fore.RESET}Please insert your coin(s):")
        coins = insert_coins()
        if compare_cost():
            make_the_coffee()
            incomes += float(format(coins - changes, ".2f"))
            print(f"{Fore.CYAN}Here is your {choice}")
            ordered_menu.append(choice)
            if changes > 0:
                print(f"{Fore.CYAN}Here is your changes : {changes}")
                changes = 0
            print(f"{Fore.MAGENTA}Thank You for using this Coffe Machine")
        else:
            print(f"Coins is not enough for {choice} : {cost} , refunded {coins}")
