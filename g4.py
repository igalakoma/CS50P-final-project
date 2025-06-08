import csv
import random


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


final_game(1000)
