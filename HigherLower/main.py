import random
import time
import os
from art import logo,vs
from game_data import data


def format_data(account):
    account_name = account['name']
    account_descr = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_descr}, from {account_country}"

def checkanswer(guess,a_follower_count,b_follower_count):
    if a_follower_count > b_follower_count :
        return guess == 'a'
    else:
        return guess == 'b'        



score = 0
EOF = False
print(logo)
account_a = random.choice(data)
while not EOF:
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.ckoice(data)
    else:
        print(f"Compare A: {format_data(account_a)}")
        print(vs)
        print(f"Compare B: {format_data(account_b)}")  

    guess = input("Who has more followers? Type 'A' or 'B' : ").lower()
    a_follower_count = account_a['follower_count']
    b_follower_count = account_b['follower_count']

    is_correct = checkanswer(guess, a_follower_count, b_follower_count)

    if is_correct:
        score += 1
        os.system('cls')
        print(logo)
        print(f"You're right! Current Score {score}")
        account_a = account_b
        
    else:
        os.system('cls')
        print(logo)
        print(f"Sorry! That's wrong. Final Score {score}")    
        EOF = True        
        time.sleep(4)    




