from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from clear_console import clear


menu = Menu()

# print(user_choice)

# print(user_choice)

logo = """

██████╗ ██╗   ██╗ ██████╗ ██████╗ ███████╗███████╗███████╗███████╗
██╔══██╗╚██╗ ██╔╝██╔════╝██╔═══██╗██╔════╝██╔════╝██╔════╝██╔════╝
██████╔╝ ╚████╔╝ ██║     ██║   ██║█████╗  █████╗  █████╗  █████╗  
██╔═══╝   ╚██╔╝  ██║     ██║   ██║██╔══╝  ██╔══╝  ██╔══╝  ██╔══╝  
██║        ██║   ╚██████╗╚██████╔╝██║     ██║     ███████╗███████╗
╚═╝        ╚═╝    ╚═════╝ ╚═════╝ ╚═╝     ╚═╝     ╚══════╝╚══════╝
                                                                  

"""

# print(result.ingredients)

get_coffee = CoffeeMaker()
get_money = MoneyMachine()


resource_status = True
while resource_status:
    # user_choice = menu.get_items()
    user_options = ''
    clear()
    print(logo)
    user_options= input(f"What would you like? ({menu.get_items()}):")
    if user_options == 'latte' or user_options == 'espresso' or user_options == 'cappuccino':
        user_choice = user_options

        result = menu.find_drink(user_choice)
        resource_status = get_coffee.is_resource_sufficient(result)
        # print(resource_status)
        if resource_status == True:
            get_money.make_payment(result.cost)
            get_coffee.make_coffee(result)
        else:
            do_continue = input("Do you wish to drink something else --> y to continue or n to exit --> n")
            if do_continue == 'y':
                resource_status = True
            else:
                resource_status = False
                
    else:
        user_report = get_coffee.report()
    

