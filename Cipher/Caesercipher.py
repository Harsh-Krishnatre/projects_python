alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
import time
import os
from logo import logo
def caesar(command,text,shift):
    new_text = ""
    for letter in text:
        if letter in alphabet:
            if command == 'encode':
                new_pos = alphabet.index(letter) + shift
                while new_pos > 26 :
                    new_pos -= 26
            elif command == 'decode':
                new_pos = alphabet.index(letter) - shift
                while new_pos < 0 :
                    new_pos += 26
            else:
                print("Enter the correct command.")
            new_text += alphabet[new_pos]
        else:
            new_text += letter
    print(f"The {command}d text is {new_text}\n")
EOF = False

print(logo)
while not EOF:
    direction = input("\nEnter 'encode' for encryting the data and enter 'decode' for decrypting the data. \n").lower()
    data = input("Enter your Data.\n")
    key = int(input("Enter the shift number.\n"))
    caesar(direction,data,key)
    end = input("Want to continue? press'yes' else 'no'\n").lower()
    if end == 'yes':
        os.system('cls')
        print(logo)
        pass
    elif end == 'no':
        EOF = True
        print("Thanks for your patronage.")
        time.sleep(5)
        




    