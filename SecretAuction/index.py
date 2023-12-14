from logo import logo
import os
import time

EOF = False
bid={}


while not EOF:
    
    print(logo)

    name = input('What is your name? ')
    value = int(input("What is your bid? $"))
    bid[name] = value

    choice = input("Are there any other bidders? type 'yes' or 'no'  \n").lower()
    if choice == 'no':
        EOF = True
        os.system('cls')
    elif choice == 'yes':
        os.system('cls')
    else:
        print("Wrong answer")
        time.sleep(4)
        exit()

highest = 0
for winner in bid:
    high = bid[winner]
    if high > highest:
        highest = high
        
print(f"the winning price of auction is ${highest} from {winner}")
time.sleep(5)
    
