#HANGMAN

import random
from word_list import words
import string

def get_word():
    word = random.choice(words)
    word = word.upper()
    return word

#print(get_word())

def game_2():
    word = get_word()
    letters = set(word)   #a list of letters of the word
    alphabet = set(string.ascii_uppercase) #a list of letters in the alphabet
    used = set()
    lives = 10

    #getting input from the user
    #keeps going until there will be no more letters
    while len(letters) > 0 and lives > 0:
        #showing how the current guess looks like
        current_guess = []

        for letter in word:
            if letter in used:
                current_guess.append(letter)
            else:
                current_guess.append("-")

        print("Word: ", " ".join(current_guess))

        prompt_letter = input("Choose a letter: ").upper()
        if prompt_letter in alphabet - used:
            used.add(prompt_letter)
            if prompt_letter in letters:
                letters.remove(prompt_letter)

            else:
                lives -= 1
                print("Your letter is not in the word.")

        elif prompt_letter in used:
            print("You have already used that letter. Try again.")
        else:
            print("Invalid character")


                #used letters
        print("Used letters: ", ",".join(used))
        print(f"You have: {lives} lives")
        print()


    if lives == 0:
        print(f"You have died :( . The word was {word}.")
        score = 0
    else:
        score = 300
        print(f"CONGRATULATIONS!!! You have guessed the word. It was {word}!")
        print(f"You received {score} Pypoints!")
    return score



