import random
import os
from art import logo
import time

def deal_card():
    """Return a random card from the deck."""
    cards = ([11,2,3,4,5,6,7,8,9,10,10,10,10])
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Take the cards in a hand calculate sum of cards and check whether the hand is bust"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)    

def compare_cards(user_score,comp_score):
    if user_score == comp_score:
        return "Draw. 😐"
    elif comp_score == 0:
        return "You Lose. Opponent has BlackJack. 🥲"
    elif user_score == 0:
        return "You Win. You have BlackJack. 😎"
    elif comp_score > 21:
        return "Opponent Went Over. You Win. 🤩"
    elif user_score > 21:
        return "You Went Over. You Lose. 🫠"
    elif user_score > comp_score:
        return "You Win. 😁"
    else:
        return "You Lose. 😑"
def play_game():

    print(logo)

    user_score = 0
    comp_score = 0
    comp_hand = []
    user_hand = []
    EOF = False


    for _ in range(2):
        user_hand.append(deal_card())
        comp_hand.append(deal_card())

    while not EOF:
        user_score = calculate_score(user_hand)
        comp_score = calculate_score(comp_hand)

        print(f"Your cards: {user_hand}, current scores: {user_score}")
        print(f"Computer's first cards: {comp_hand[0]}")

        if calculate_score(comp_hand) == 0 or calculate_score(user_hand) == 0 or calculate_score(user_hand) > 21:
            EOF = True
        else:
            user_should_deal = input("Do you want to draw another card? type 'y' for yes and 'n' for pass.: ").lower()
            if user_should_deal == 'y':
                user_hand.append(deal_card())
            else:
                EOF = True

    while comp_score != 0 and comp_score < 17:
        comp_hand.append(deal_card())
        comp_score = calculate_score(comp_hand)
    print(f"    Your Final Hand is: {user_hand}, final score: {user_score}")
    print(f"    Computer's Final Hand is: {user_hand}, final score: {comp_score}")
    print(compare_cards(user_score,comp_score))

while input("Do you want to play the game of Black Jack? Type 'y' or 'n' ,: ") == 'y':
    os.system('cls')
    play_game()

print("Thank you for your time.")
time.sleep(4)



    





