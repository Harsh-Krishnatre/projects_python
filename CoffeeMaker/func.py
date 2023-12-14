from dicts import resources, MENU


def show_stock():
    """show the stock of ingredients in the Coffee machine."""
    for x in resources:
        print(f"{x} : {resources[x]}")


def make_coffee(coffee):
    """Take the currency and brew the coffee"""
    if check_resources(coffee) == 1:
        print("Please insert cash :")
        rupee_10 = int(input("Enter the number of 10 rupee notes :"))
        rupee_20 = int(input("Enter the number of 20 rupee notes :"))
        rupee_50 = int(input("Enter the number of 50 rupee notes :"))
        rupee_100 = int(input("Enter the number of 100 rupee notes :"))
        rupee_200 = int(input("Enter the number of 200 rupee notes :"))
        total_rupee = rupee_10 * 10 + rupee_20 * 20 + rupee_50 * 50 + rupee_100 * 100 + rupee_200 * 200
        if total_rupee >= MENU[coffee]["cost"]:
            change = total_rupee - MENU[coffee]["cost"]
            print(f"Here is your ₹{change} in change")
            print(f"Enjoy your {coffee} 🍵.")
        else:
            print("Insufficient currency give. Money Refunded . ")
            return 0


def check_resources(coffee):
    """Check if the resources required to brew coffee is present in machine."""
    flag = 0
    for x in resources:
        if resources.get(x) >= MENU[coffee]["ingredients"].get(x):
            flag += 1

    if flag == 3:
        for x in resources:
            resources[x] -= MENU[coffee]["ingredients"][x]
        return 1
    elif flag < 3:
        for x in resources:
            if resources[x] < MENU[coffee]["ingredients"][x]:
                print(f"Sorry! there is not enough {x}.")
        return 0
