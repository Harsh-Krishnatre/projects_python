print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
choice1 = input('You\'re at a crossroad, where do you want to go? Type "left" or "right". ').lower()
if choice1 == 'left':
    choice2 = input('You have arrived at a canal, do you want to "swim" or "wait" for a boat. ').lower()
    if choice2 == 'wait':
        choice3 = input('You have now spooted a boat with a no one inside, you row the boat to other side where three mysterious door of three diffrent metals stood straight, they are "gold", "silver" and "iron", choose a gate to enter. ').lower()
        if choice3 == 'iron':
            print("You are now standing in a ancient room full of gold and treasures. You Win. ")
        elif choice3 == 'gold':
            print("You are thrown into lava, your screams agonizes even the dead. You Lose. ")
        elif choice3 == 'silver':
            print('You found a chest full of gold, In greed you ignore your surrounding and a spider as big as your greed grabs you in its silk and drags you down to make his own collection. You Lose. ')
        else:
            print('You\'ve waited too long to admire the gate and the elderlitch horror too scary even for nightmares appear infront of your boat and swallow you to wait for death. You Lose. ')
    else:
        print('You\'ve chosen to swim but after jumping into river you somehow forgot how to do so, what a genius you are! You Lose. ')
else:
    print('Your instincts scream at your foolishness but you keep going toward right, After who knows how long you saw a light. After reaching the light at your fastest you saw something even hell would cute compared to, An entity you can\'t comprehend attacks you. You Lose.')
