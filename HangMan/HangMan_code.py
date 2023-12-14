#Step 1 

import os            
import random
import time
from HangMan_art import stages
from HangMan_art import logo
from HangMan_words import word_list
lives = 6


#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
ans = []

print(logo)

#Test Code
# print(f"Psstt, the answer is {chosen_word}")

for i in chosen_word:
    ans.append("__")
EOF = False
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
while(not EOF):
    guess = input("Enter Your Guess :").lower()

    os.system('cls'if os.name== 'nt' else clear)

    #TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
    if guess in ans:
        print("that is already chosen, Try another word.")

    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            ans[i] = guess

    if guess not in chosen_word:
        lives -= 1
        print("That's not in the word, you lose a life.")

        if lives == 0:
            EOF = True
            print(f"the word is {chosen_word}")
            print("You Lose!")
    
    
    print(stages[lives])

    print(f"{' '.join(ans)}")
    if "__" not in ans:
        EOF = True
        print("You Win!")


time.sleep(10)


