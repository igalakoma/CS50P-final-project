import sys
import random
from word_list import words
import string

# QUIZ (A B C D)
# function that poses a question to user and user responds
# it also checks if the user's answer is correct

def game_1():
    # opening the csv file with questions
    with open("questions_q1.csv", "r") as csv_file:
        lines = csv_file.readlines()

    i = 1
    score = 0

    while i < 11:
        # choosing a random line from the list of questions
        random_line = random.choice(lines)

        # removing the chosen line from the list to prevent repetition
        lines.remove(random_line)

        # splitting the line in order to print only the question
        random_line = random_line.split(",")

        # printing the question
        print(f"Question {i}")
        print(random_line[1])
        # printing the possible answers
        for _ in range(2, 6):
            print(random_line[_])
        print("To answer, please type only the letter, eg. A, B, C or D")

        # user chooses an answer
        answer = input("Your answer: ").upper().strip()

        # makes user enter correct format ("A", "B", "C" or "D")
        while answer not in ["A", "B", "C", "D"]:
            print("Enter correct format: A, B, C or D")
            answer = input("Your answer: ").upper().strip()

        # finding the correct answer in the csv file
        correct_answer = random_line[6].upper().strip()

        # checking if user's answer is correct
        if answer == correct_answer:
            print("CORRECT! :)")
            print()
            score += 1
        else:
            print("NOT CORRECT :(")
            print()

        i += 1

    print(f"Your score: {score}/10")
    score = score * 30
    if score == 0:
        print("You didn't earn any Pypoints. Try out next game :)")
    else:
        print(f"CONGRATULATIONS!!! You received {score} Pypoints!")

    return score



# HANGMAN

def get_word():
    word = random.choice(words)
    word = word.upper()
    return word

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




# ROCK PAPER SCISSORS

# function that changes the words into images
def rps_convert(word):
    # Rock
    rock = ("""
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    """)

    # Paper
    paper = ("""
        _______
    ---'    ____)_
            ______)
            _______)
            _______)
    ---.__________)
    """)

    # Scissors
    scissors = ("""
        _______
    ---'   ____)__
            ______)
        __________)
        (____)
    ---.__(___)
    """)

    if word == "rock":
        word = rock
    elif word == "paper":
        word = paper
    elif word == "scissors":
        word = scissors
    return word

# function that tells a score
def rps_score(u, p):
    # u - user's input
    # p - choice (python's choice)
    user = 0
    python = 0
    if (u == "rock" and p == "paper") or (u == "paper" and p == "scissors") or (u == "scissors" and p == "rock"):
        python += 1
    elif (u == "rock" and p == "scissors") or (u == "paper" and p == "rock") or (u == "scissors" and p == "paper"):
        user += 1
    return user, python

# the actual game
def game_3():

    elements = ["rock","paper","scissors"]

    i = 0
    users_score = 0
    pythons_score = 0

    while i < 3:
        print("What's your choice? Rock, paper or scissors? ")
        users_input = input().strip().lower()

        choice = random.choice(elements)

        # checks if user's input is rock, paper or scissors
        if (users_input == "rock") or (users_input == "paper") or (users_input == "scissors"):
            # when the user's input is the same as program's choice, nobody gets a point
            if users_input == choice:
                choice_con = rps_convert(choice)
                users_input_con = rps_convert(users_input)
                print(f"Your choice is: {users_input_con}")
                print(f"Python's choice is:  {choice_con}")
                print("Try once again")
            # when the user's input is diffrent than computer's choice,
            # program gives winner one point
            else:
                user, python = rps_score(users_input, choice)
                users_score += user
                pythons_score += python
                choice_con = rps_convert(choice)
                users_input_con = rps_convert(users_input)
                print(f"Your choice is: {users_input_con}")
                print(f"Python's choice is: {choice_con}")

                print(f"Your score: {users_score}")
                print(f"Python: {pythons_score}")
                i += 1

        # when user's input is invalid, program prints a message in order to repeat
        else:
            print("\nInvalid input. Type \"rock\", \"paper\" or \"scissors\"\n")

    if users_score < pythons_score:
        print("YOU LOST :( ")
        score = 0
    else:
        print("CONGRATULATIONS! YOU WON! :) ")
        score = 300

    return score


# FINAL GAME
# A QUIZ WITH BETTING MONEY (PYPOINTS)

def final_game(pypoints):
    with open("questions_q4.csv", "r") as csv_file:
        lines = csv_file.readlines()

    print("\nWelcome to the final game!")
    print("You will face 3 questions with 4 possible answers: A, B, C or D.")
    print("The game might seem similar to the first game but it isn't.")
    print("Instead of answering A, B, C or D you can bet certain amount of Pypoints for every answer.")
    print("Even if you dont know the answer, you can bet on every question, so you will not lose all you Pypoints.")
    print("But if you are sure about the answer (or if you want to risk), you can put all of your Pypoints for that answer.")
    print("To answer, please type only the amount of Pypoints you want to bet, eg. 500.")
    print("In the end, depending on how many Pypoints you will save, you will receive a virtual prize.")
    print("Let's start :)\n")

    print(f"Your Pypoints: {pypoints}\n")

    i = 0

    while i < 3:
        #choosing a random like from csv file with a question
        random_line = random.choice(lines)

        #removing the chosen line from the list to prevent repetition
        lines.remove(random_line)

        #spliting the line in order to print only the question
        random_line = random_line.split(",")

        #printing the question
        print(random_line[1])
        #printing the possible answers
        for _ in range(2,6):
            print(random_line[_])
        print("\nTo answer, please type only the amount of Pypoints you want to bet, eg. 500\n")

        #user chooses an answer
        answer_a = input("Your bet on A: ").strip()
        dict_a = {"A":answer_a}
        answer_b = input("Your bet on B: ").strip()
        dict_b = {"B":answer_b}
        answer_c = input("Your bet on C: ").strip()
        dict_c = {"C":answer_c}
        answer_d = input("Your bet on D: ").strip()
        dict_d = {"D":answer_d}


        #checks if user spend the exact number of Pypoints they had
        while (int(answer_a) + int(answer_b) + int(answer_c) + int(answer_d)) != int(pypoints):
            if (int(answer_a) + int(answer_b) + int(answer_c) + int(answer_d)) < int(pypoints):
                print("\nSpend all of your Pypoints.\n")

            elif (int(answer_a) + int(answer_b) + int(answer_c) + int(answer_d)) > int(pypoints):
                print("\nDon't spend more Pypoints than you have.\n")

            answer_a = input("Your bet on A: ").strip()
            dict_a = {"A":answer_a}
            answer_b = input("Your bet on B: ").strip()
            dict_b = {"B":answer_b}
            answer_c = input("Your bet on C: ").strip()
            dict_c = {"C":answer_c}
            answer_d = input("Your bet on D: ").strip()
            dict_d = {"D":answer_d}

        #finding correct answer in the csv file
        correct_answer = random_line[6].upper().strip()


        #checking is user's answer is correct
        #a
        if list(dict_a.keys())[0] == correct_answer:
            print("\nAnswer A is CORRECT")
            pypoints = answer_a
        #b
        elif list(dict_b.keys())[0] == correct_answer:
            print("\nAnswer B is CORRECT")
            pypoints = answer_b
        #c
        elif list(dict_c.keys())[0] == correct_answer:
            print("\nAnswer C is CORRECT")
            pypoints = answer_c
        #d
        elif list(dict_d.keys())[0] == correct_answer:
            print("\nAnswer D is CORRECT")
            pypoints = answer_d

        print(f"Your Pypoints: {pypoints}\n")

        if int(pypoints) == 0:
            print("GAME OVER :( ")
            print("""

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡛⠛⠷⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⡇⠀⠀⠀⠙⠻⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠟⠀⠀⠀⠀⠀⠀⠈⣹⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⣠⡴⠞⠉⠈⠻⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣿⡧⠤⠤⠶⠖⠋⠉⠀⠀⠀⠀⠀⢹⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⠞⠉⠀⠉⠙⠻⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⣀⣀⣀⠀⠀⠀⠀⢀⣠⡴⠞⠉⠀⢀⣀⣀⣀⠀⠀⠘⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⣿⣆⣴⠟⠉⠉⠉⠛⢶⡖⠛⠉⠁⠀⠀⢠⡾⠋⠉⠈⠉⠻⣦⣰⣿⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣤⣾⠟⠋⡿⠁⢀⣾⣿⣷⣄⠈⢿⡀⠀⠀⠀⢠⡟⠀⢠⣾⣿⣷⡄⠘⣿⠉⠛⢿⣦⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢠⣿⠏⠀⠀⢸⡇⠀⢸⣿⣿⣿⣿⠀⢸⡇⠀⠀⠀⢸⡇⠀⣿⣿⣿⣿⣧⠀⢹⡇⠀⠀⠙⣿⡆⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⡏⠀⠀⠀⠘⣧⠀⠘⣿⣿⣿⡟⠀⣸⠇⠀⣀⣤⢾⣇⠀⠹⣿⣿⣿⠇⠀⣾⠁⠀⠀⠀⢸⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⣷⠀⠀⠀⠀⠹⣧⡀⠈⠉⠁⢀⣴⠿⠞⠋⠉⠀⠀⠻⣦⡀⠈⠉⠁⣠⡾⠃⠀⠀⠀⠀⣾⡏⠀⠀⠀⠀
⠀⠀⢀⣠⣶⠿⠛⠛⠛⠛⠛⠛⠉⠙⠛⠒⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠚⠛⠉⠀⠀⠀⠀⢀⡼⠿⢷⣦⣄⠀⠀
⠀⣠⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣟⠛⠛⠒⠶⠶⠶⠶⠶⠶⠶⠖⠚⠛⢛⡷⠀⠀⠀⣀⡴⠋⠀⠀⠀⠈⠻⣷⡄
⢰⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢷⣄⡀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡶⠛⢁⣠⡴⠞⠋⠀⠀⠀⠀⠀⠀⠀⠘⣿
⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠓⠶⠶⠦⠶⠶⣚⣫⡥⠶⠚⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿
⠈⢿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⡤⠴⠖⠚⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⡿⠃
⠀⠈⠛⣷⣦⣤⣤⣤⣤⣤⣤⣶⡶⠾⠿⠟⠿⠿⠿⠶⣶⣶⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣶⠶⠿⠛⠉⠀⠀

                  """)
            print("Try once again\n")
            break
        else:
            i += 1
            continue



    if int(pypoints) != 0:
        print(f"You have collected {pypoints} Pypoints.")
        print("Here is your prize: \n")
        pypoints = int(pypoints)
        if pypoints == 1000:
            print(f"CONGRATULATIONS! YOU WON A UNICORN!" )
            print("""

                                                 ,/
                                                //
                                              ,//
                                  ___   /|   |//
                              `__/\\_ --(/|___/-/
                           \\|\\_-\\___ __-_`- /-/ \\.
                          |\\_-___,-\\_____--/_)' ) \\
                           \\ -_ /     __ \\( `( __`\\|
                           `\\__|      |\\)\\ ) /(/|
   ,._____.,            ',--//-|      \\  |  '   /
  /     __. \\,          / /,---|       \\       /
 / /    _. \\  \\        `/`_/ _,'        |     |
|  | ( (  \\   |      ,/ '__/'/          |     |
|  \\  \\`--, `_/_------______/           \\(   )/
| | \\  \\_. \\,                            \\___/\\
| |  \\_   \\  \\                                 \\
\\ \\    \\_ \\   \\   /                             \\
 \\ \\  \\._  \\__ \\_|       |                       \\
  \\ \\___  \\      \\       |                        \\
   \\__ \\__ \\  \\_ |       \\                         |
   |  \\_____ \\  ____      |                        |
   | \\  \\__ ---' .__\\     |        |               |
   \\  \\__ ---   /   )     |        \\              /
    \\   \\____/ / ()(      \\          `---_       /|
     \\__________/(,--__    \\_________.    |    ./ |
       |     \\ \\  `---_\\--,           \\   \\_,./   |
       |      \\  \\_ ` \\    /`---_______-\\   \\     /
        \\      \\.___,`|   /              \\   \\    \\
         \\     |  \\_ \\|   \\              (   |:    |
          \\    \\      \\    |             /  / |    ;
           \\    \\      \\    \\          ( `_'   \\  |
            \\.   \\      \\.   \\          `__/   |  |
              \\   \\       \\.  \\                |  |
               \\   \\        \\  \\               (  )
                \\   |        \\  |              |  |
                 |  \\         \\ \\              I  `
                 ( __;        ( _;            ('-_';
                 |___\\        \\___:            \\___:
                          -valkyrie-


                """)

        if 800 < pypoints < 1000:
            print("""

                                  __
                               _.-~  )
                    _..--~~~~,'   ,-/     _
                 .-'. . . .'   ,-','    ,' )
               ,'. . . _   ,--~,-'__..-'  ,'
             ,'. . .  (@)' ---~~~~      ,'
            /. . . . '~~             ,-'
           /. . . . .             ,-'
          ; . . . .  - .        ,'
         : . . . .       _     /
        . . . . .          `-.:
       . . . ./  - .          )
      .  . . |  _____..---.._/ ____ Seal _
~---~~~~----~~~~             ~~

                  """)
        if 600 < pypoints < 800:
            print("""

                            .d$$b
                          .' TO$;\\
                         /  : TP._;
                        / _.;  :Tb|
                       /   /   ;j$j
                   _.-"       d$$$$
                 .' ..       d$$$$;
                /  /P'      d$$$$P. |\\
               /   "      .d$$$P' |\\^"l
             .'           `T$P^\\"\\"\\"\\"\\"  :
         ._.'      _.'                ;
      `-.-".-'-' ._.       _.-"    .-"
    `.-" _____  ._              .-"
   -(.g$$$$$$$b.              .'
     ""^^T$$$P^)            .(:
       _/  -"  /.'         /:/;
    ._.'-'`-'  ")/         /;/;
 `-.-"..--""   " /         /  ;
.-" ..--""        -'          :
..--""--.-"         (\\      .-(\\
  ..--""              `-\\(\\/;`
    _.                      :
                            ;`-
                           :\\
                           ;  bug


                  """)
        if 400 < pypoints < 600:
            print("""

           __.
        .-".'                      .--.            _..._
      .' .'                     .'    \\       .-""  __ ""-.
     /  /                     .'       : --..:__.-""  ""-. \\
    :  :                     /         ;.d$$    sbp_.-""-:_:
    ;  :                    : ._       :P .-.   ,"TP
    :   \\                    \\  T--...-; : d$b  :d$b
     \\   `.                   \\  `..'    ; $ $  ;$ $
      `.   "-.                 ).        : T$P  :T$P
        \\..---^..             /           `-'    `._`._
       .'        "-.       .-"                     T$$$b
      /             "-._.-"               ._        '^' ;
     :                                    \\.`.         /
     ;                                -.   \\`."-._.-'-'
    :                                 .'\\   \\ \\ \\ \\
    ;  ;                             /:  \\   \\ \\ . ;
   :   :                            ,  ;  `.  `.;  :
   ;    \\        ;                     ;    "-._:  ;
  :      `.      :                     :         \\/
  ;       /"-.    ;                    :
 :       /    "-. :                  : ;
 :     .'        T-;                 ; ;
 ;    :          ; ;                /  :
 ;    ;          : :              .'    ;
:    :            ;:         _..-"\\     :
:     \\           : ;       /      \\     ;
;    . '.         '-;      /        ;    :
;  \\  ; :           :     :         :    '-.
'.._L.:-'           :     ;    bug   ;    . `.
                     ;    :          :  \\  ; :
                     :    '-..       '.._L.:-'
                      ;     , `.
                      :   \\  ; :
                      '..__L.:-'

                  """)
        if 200 < pypoints < 400:
            print("""

       ,
       \\`-._           __
        \\  `-..____,.'  `.
         :`.         /    \\`.
         :  )       :      : \\
          ;'        '   ;  |  :
          )..      .. .:.`.;  :
         /::...  .:::...   ` ;
         ; _ '    __        /:\\
         `:o>   /\\o_>      ;:. `.
        `-`.__ ;   __..--- /:.   \\
        === \\_/   ;=====_.':.     ;
         ,/'`--'...`--....        ;
              ;                    ;
            .'                      ;
          .'                        ;
        .'     ..     ,      .       ;
       :       ::..  /      ;::.     |
      /      `.;::.  |       ;:..    ;
     :         |:.   :       ;:.    ;
     :         ::     ;:..   |.    ;
      :       :;      :::....|     |
      /\\     ,/ \\      ;:::::;     ;
    .:. \\:..|    :     ; '.--|     ;
   ::.  :''  `-.,,;     ;'   ;     ;
.-'. _.'\\      / `;      \\,__:      \\
`---'    `----'   ;      /    \\,.,,,/
                   `----`              fsc

                  """)
        if 0 < pypoints < 200:

            print("""


                              ___,--------,____
                      __--~~~~                 ~~---,_
                   ,-'                  __,--,_       `\\,___,-,__
                ,-'                 __/'/-~~~\\  `  ` . '    , |  `~~\\
             _/`      _/~~      '~~   \\,_\\_ O /        '  '~_/'      `\\
           /'        '                   =-'~~  _  /  ~   /'          `\\
        _/'  /~                            ,--,____,-----|,_,-,_       `\\
    _,/'    '              ,-'      _      `~'------'~~~~~--    `~~~~\\  |
 ,-'             /~       '    ,-~~~         _,       ,-=~~~~~~~~~~~~'| |
~              .'             '         ,   '      /~`                |/
                                  /' ,/'       _/~'
                   ,       /    /`          _/~
        /~        /      /`               /'
      .'                                /'
                       /'      .      /
                      `       /'     |
                                    '
                  """)


        print("Thank you for playing this game :)")
        print("Feel welcomed to try once again if you want to :)")


def main():
    print("\nHello! Welcome to my final project:)\n")
    print("You will experience 3 simple games ( or maybe not so simple ;) )")
    print("Fourth game will be the Grand Final where you will be able to win million dollars!")
    print("During the whole tournament you will be getting fictional points called Pypoints")
    print("After every of 3 games you will be able to get 300 Pypoints (if you succeed fully in each of them)")
    print("If you get 900 Pypoints after all 3 games, you will get a bonus of 100 Pypoints")
    print("You will need Pypoints in the Grand Final. You will be using Pypoints for bets in order to win a million!")
    print("Rules of the Grand Final will be explained later.")
    print("Are you ready to start?")

    # starting the game (or exit)
    _ = 0
    while _ < 1:
        start = input().lower()

        if "yes" in start:
            print("Alright! Let's start then. Good luck! :)")
            _ += 1
        elif start == "y":
            print("Alright! Let's start then. Good luck! :)")
            _ += 1
        elif "no" in start:
            sys.exit("Bye bye then, maybe next time :(")
        elif start == "n":
            sys.exit("Bye bye then, maybe next time :(")
        else:
            print("Answer \"yes\" or \"no\". ")

    print()
    print("\n---> GAME 1. QUIZ")
    print()
    score_1 = game_1()
    print(f"Your current score: {score_1} Pypoints.")


    print()
    print("---> GAME 2. HANGMAN")
    print()
    score_2 = game_2()
    print(f"Your current score: {score_1+score_2} Pypoints.")

    print()
    print("---> GAME 3. ROCK, PAPER, SCISSORS")
    print()
    score_3 = game_3()
    print(f"Your current score: {score_1+score_2+score_3} Pypoints.")

    f_score = score_1 + score_2 + score_3

    # bonus points for all good answers
    if f_score == 900:
        f_score = f_score + 100
    else:
        f_score = f_score

    print()
    print("---> GRAND FINAL")
    print()
    if f_score > 0:
        final_game(f_score)
    else:
        print("Unfortunately you dont have enough Pypoints to play the final game :( ")



if __name__ == "__main__":
    main()

