import random
LOGO = """ _______           _______  _______  _______             _______           _______    _                 _______  ______   _______  _______ 
(  ____ \|\     /|(  ____ \(  ____ \(  ____ \  |\     /|(  ___  )|\     /|(  ____ )  ( (    /||\     /|(       )(  ___ \ (  ____ \(  ____ )
| (    \/| )   ( || (    \/| (    \/| (    \/  ( \   / )| (   ) || )   ( || (    )|  |  \  ( || )   ( || () () || (   ) )| (    \/| (    )|
| |      | |   | || (__    | (_____ | (_____    \ (_) / | |   | || |   | || (____)|  |   \ | || |   | || || || || (__/ / | (__    | (____)|
| | ____ | |   | ||  __)   (_____  )(_____  )    \   /  | |   | || |   | ||     __)  | (\ \) || |   | || |(_)| ||  __ (  |  __)   |     __)
| | \_  )| |   | || (            ) |      ) |     ) (   | |   | || |   | || (\ (     | | \   || |   | || |   | || (  \ \ | (      | (\ (   
| (___) || (___) || (____/\/\____) |/\____) |     | |   | (___) || (___) || ) \ \__  | )  \  || (___) || )   ( || )___) )| (____/\| ) \ \__
(_______)(_______)(_______/\_______)\_______)     \_/   (_______)(_______)|/   \__/  |/    )_)(_______)|/     \||/ \___/ (_______/|/   \__/
                                                                                                                                           """

CORRECT_ANSWER = random.randint(1,100)
print(LOGO)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
# print(f"PSSHT the correct answer is {CORRECT_ANSWER}")

def game():
    lives = 10
    mode = input("Choose the difficulty. Type 'easy' or 'hard': ").lower()
    if mode == 'hard':
        lives = 5
    print(f"You have {lives} attempts remaining to guess the number.")
    while lives > 0:
        guess = int(input("Make a guess: "))
        if guess == CORRECT_ANSWER:
            print(f"You got it! The answer is {guess}")
            break
        elif guess > CORRECT_ANSWER:
            print("TOO HIGH!")
        else:
            print('TOO LOW!')
        lives -= 1
        print(f"You have {lives} attempts remaining to guess the number.")
    if lives == 0:
        print("You run out of turns. You Lose.")
    else:
        print('YOU WIN!!')
    return

game()