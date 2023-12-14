from dicts import MENU
from func import show_stock, make_coffee
import os
import time


while True:
    choice = input("What would you like? (latte/espresso/cappuccino) ").lower()

    if choice == 'report':
        show_stock()
    elif choice in MENU:
        make_coffee(choice)
        cont = input("Press 'y' to continue..")
        if cont != 'y':
            print("Thank you for your patronage..")
            time.sleep(3.5)
            break
        os.system('cls')
    elif choice == "exit":
        exit()
    else:
        print("Invalid command please try again")
