rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

print()
#enter te input 👇
choice = int(
    input(
        "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"
    ))
option = [rock, paper, scissors]

# Generating Computer Choice 👇
opt = random.choice(option)
if (choice == 0):
    ipt = rock
elif (choice == 1):
    ipt = paper
elif (choice == 2):
    ipt = scissors

# Basic Output 👇
print(ipt)
print("Computer Choice:")
print(opt)

# Conditional Output 👇
if ((opt == option[0] and ipt == paper)
        or (opt == option[1] and ipt == scissors)
        or (opt == option[2] and ipt == rock)):
    print("You Win!")

elif ((opt == option[0] and ipt == scissors)
      or (opt == option[1] and ipt == rock)
      or (opt == option[2] and ipt == paper)):
    print("You Lose!")
elif ((opt == option[0] and ipt == rock) or (opt == option[1] and ipt == paper)
      or (opt == option[2] and ipt == scissors)):
    print("Draw!")
else:
    print("You entered an Invalid Choice. You Lose!")
