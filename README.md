# PYTHONSHIPS
#### Video Demo:  https://youtu.be/WVorigYI3OY
#### Description: A final Python project for Harvard CS50P course.

## Introduction

Welcome to my Python project for CS50P course! It is an interactive game tournament
called "PYTHONSHIPS" that includes four different games:

1. Quiz
    - Test your general knowledge by answering questions correctly.

2. Hangman
    - Guess the word before you run out of lives.

3. Rock, Paper, Scissors
    - A classic battle against the computer.

4. Final Game: The Betting Quiz
    - The last quiz in the tournament where you can bet your earned Pypoints.

Throughout the tournament, you will earn special points called Pypoints,
which will be crucial in the final game to win the grand prize!


## Features

* Play four different games, each with unique rules and challenges.

* After each game you will earn and accumulate Pypoints to participate
in the final betting game.

* In the final game you will be able to use your gained Pypoints
to answer questions with 4 possible answers.
If you do well, you will be able to save all of the points you have gained
throughout the whole game, win some of the points you've gained or be left
with nothing (if your bets are wrong).

* Engaging and interactive text-based gameplay.

* Randomized questions and words for a fresh experience each time.

* Simple and easy-to-follow instructions.


## Installation

### Requirements

1. Python 3 installed on your OS.
2. Installation of files:
    * project.py
    * questions_q1.csv
    * questions_q1.csv
    * word_list.csv

    All of the files above are required for the whole game to run properly.

3. \* Installation of the additional files (not required):
    * g1.py
    * g2.py
    * g3.py
    * g4.py
    * test_project.py

    Installation of the files g1.py, g2.py, g3.py, g4.py is completely optional.
    Those files are not essential for the game to run properly, but it is a nice bonus.
    These are all the games that the file project.py contains, but each of them
    is coded separately, allowing users to play them individually if they choose.

    File test_project.py consists of 7 test functions that check if the game
    funtions correctly. It is not needed for the project.py to work.

4. Basic knowledge of how to run Python scripts.

5. \* It is recommended, but not required, to use VSCode to run the game.


### Steps to Install and Run

1. Download all the required files to your computer.

2. Ensure you have all necessary files installed and place all of them
in a desired folder.

3. Open the folder from step 2 (where you put required files).
You can use the terminal using the following command:

    ```
    cd folder_name
    ```

    Where *folder_name* is the name of the folder mentioned in step 2.

4. Run the script using the following command:

    ```
    python project.py
    ```

5. Everything is done. The game should print a welcoming prompt.
If it did not happen, check if you did all the above steps correctly
and if you did not make a typo in executing a command.
If the problem still occurs, try using a different compiler to run the game.

## Description of games and how to play them


### Game 1: Quiz

#### Description

This is a simple multiple-choice quiz game that allows you to answer 10 randomly
selected questions from a CSV file (questions_q1.csv).
Each question has four possible answers (A, B, C, or D), and you must choose
the correct one. Pypoints are awarded based on the number of correct answer.
For each correct answer you will get 30 Pypoints. The questions do not repeat
throughout the game, which enables you to play the game multiple times if you
want to, because each game can be different from the other.
At the end of the game, the amount of Pypoints you obtained will be revealed
to you. You can get no more than 300 Pypoints.

#### Features

1. Reading questions from a CSV file.

2. Random selection of 10 questions per game session.

3. Ensuring no question is repeated within a single game session.

4. Validating user input to accept only A, B, C, or D.

5. Awards points based on correct answers.

6. Providing feedback for each question.

#### How to Play

1. The game randomly selects 10 questions. Each question has four possible answers
(A, B, C or D).

2. To respond, enter your answer by typing **only** the letter corresponding to your
choice, when the program asks you for your answer, for example:

    ```
    Question 1:
    What is the capital of France?
    A) Berlin
    B) Madrid
    C) Paris
    D) Rome
    To answer, please type only the letter, e.g., A, B, C, or D
    Your answer: C
    ```

3. Then, the program prints a message "CORRECT! :)" or "NOT CORRECT :("

4. If your answer is correct, you will earn 30 Pypoints. If the answer is incorrect,
no Pypoints are awarded.

5. At the end, your total Pypoints are calculated. You can get maximum of 300 Pypoints
if all the answers are correct.


### Game 2: Hangman

#### Description

This is a text-based Hangman game where you try to guess a word.
The word is randomly chosen from the list in the python file (word_list.py).
You have 10 lives and must guess all the letters to reveal the hidden word.
The game provides feedback on guessed letters and keeps track of used ones.

#### Features

* Random word selection from a word list.

* Limited number of lives to guess the word.

* Tracking used letters.

* Prevention of duplicate guesses.

* Showing the word with correctly guessed letters.

* Awards points upon successful completion.

#### How to Play

1. The program randomly selects a word for you, which is displayed as dashes.

2. You must guess it letter by letter. You enter one letter per turn in order
to guess the word. Remember to answer **only** with a letter that you think
appears in the given word.

3. You start with 10 lives. If a letter that you proposed does not appear
in the guessing word, you lose one life, like below:

    ```
    ---> GAME 2. HANGMAN

    Word:  - - - - - -
    Choose a letter: o
    Your letter is not in the word.
    Used letters:  O
    You have: 9 lives

    Word:  - - - - - -
    Choose a letter:
    ```

    If you guess a correct letter, it fills in the blanks.

    ```
    Word:  - - - - - -
    Choose a letter: i
    Used letters:  O,I
    You have: 9 lives

    Word:  I - - - - -
    ```
    As you can see, the game shows you what letter you already used so you
    do not need to remember them.
    But do not worry, if you type the same letter twice,
    the program will remind you about that and you will not lose another life.

4. The game continues until you guess the word or run out of lives.

5. By guessing the word you will get 300 Pypoints. If you do not guess the word,
you will not receive any Pypoints.


### Game 3: Rock, Paper, Scissors

#### Description

This is a simple Rock, Paper, Scissors game.
In this game you play against the computer (Python),
where the winner is determined based on the classic game rules.

#### Features

* Converts Rock, Paper, and Scissors choices into ASCII art for better visualization.

* Compares user and computer choices to determine the winner.

* Keeps track of the score for a best-of-three match.

* Checks if the user provided a correct input. If not, it prints
a proper message and repeats the question.

#### How to play

1. The program will ask you to choose "rock", "paper" or "scissors".
Choose only one option by typing "rock", "paper" or "scissors".
For example:

    ```
    What's your choice? Rock, paper or scissors?
    rock
    ```
2. Next, the program will randomly select an option for the computer
and print the result - ASCII art images of the selected options
and the current score.

    ```
    Your choice is:
            _______
        ---'   ____)
            (_____)
            (_____)
            (____)
        ---.__(___)

    Python's choice is:
            _______
        ---'   ____)__
                ______)
            __________)
            (____)
        ---.__(___)

    Your score: 1
    Python: 0
    What's your choice? Rock, paper or scissors?
    ```

3. The winner is chosen based on the game rules:

* Rock beats scissors

* Scissors beats paper

* Paper beats rock

4. If you put an invalid input do not worry, the program will ask you to make
the choice once again. It will also do it if the computer chooses the same
input as yours.

    ```
    What's your choice? Rock, paper or scissors?
    milk

    Invalid input. Type "rock", "paper" or "scissors"

    What's your choice? Rock, paper or scissors?
    ```

    ```
    What's your choice? Rock, paper or scissors?
    scissors
    Your choice is:
            _______
        ---'   ____)__
                ______)
            __________)
            (____)
        ---.__(___)

    Python's choice is:
            _______
        ---'   ____)__
                ______)
            __________)
            (____)
        ---.__(___)

    Try once again
    What's your choice? Rock, paper or scissors?
    ```

5. The winner of each round earns one point.
The player that wins 2 rounds wins the game and gets 300 Pypoints.


### Final Game: The Betting Quiz

#### Description

This is a betting game where you can wager Pypoints (that you
have gained in the previous 3 games) on multiple-choice questions.
The game consists of three rounds, in which you must distribute your current Pypoints
among the answer choices. If you bet correctly, you keep your bet
Pypoints. Otherwise, you lose them. The goal is to finish the game with
as many Pypoints as possible, which are then converted into a virtual prize.

#### Features

* Interactive gameplay with betting mechanics.

* Three-question rounds with randomized selection.

* Flexible wagering system allowing strategic betting.

* Automatic validation of total Pypoints distribution.

* Conversion of Pypoints to a virtual prize.

* Ability to replay the game.

#### How to play

1. The game starts with a welcome message explaining the rules.

2. You will be presented with three questions, each having four possible answers
(A, B, C or D). Instead of selecting one answer, you can distribute
your Pypoints across multiple answers.
To answer, put only the amount of Pypoints you want to bet eg. "300".
If you do not want to put any Pypoints on the answer, type "0".
For example:

    ```
    Welcome to the final game!
    You will face 3 questions with 4 possible answers: A, B, C or D.
    The game might seem similar to the first game but it isn't.
    Instead of answering A, B, C or D you can bet certain amount of Pypoints for every answer.
    Even if you dont know the answer, you can bet on every answer, so you will not lose all of your Pypoints.
    But if you are sure about the answer (or if you want to risk), you can put all of your Pypoints for that answer.
    To answer, please type only the amount of Pypoints you want to bet, eg. 500.
    In the end, depending on how many Pypoints you will save, you will receive a virtual prize.
    Let's start :)

    Your Pypoints: 450

    What is the smallest planet in our solar system?
    A: Mars
    B: Venus
    C: Mercury
    D: Pluto

    To answer, please type only the amount of Pypoints you want to bet, eg. 500

    Your bet on A: 0
    Your bet on B: 0
    Your bet on C: 300
    Your bet on D: 150
    ```

    If you are sure that the answer you are betting for is correct, you can put all of your available Pypoints on it. Remember, the more you risk on a correct answer, the greater the final award!

    ```
    Your Pypoints: 300

    What color is the blood of an octopus?
    A: Blue
    B: Red
    C: Grey
    D: Black

    To answer, please type only the amount of Pypoints you want to bet, eg. 500

    Your bet on A: 300
    Your bet on B: 0
    Your bet on C: 0
    Your bet on D: 0
    ```

3. Next, the program will show what was the correct answer and show you how many Pypoints you currently have. For example:

    ```
    Answer A is CORRECT
    Your Pypoints: 300
    ```

4. The total Pypoints you bet **must be equal** to Pypoints you currently have. Otherwise, the program will ask you to repeat the bet. You cannot spend more or less than the Pypoints you have. For example:

    ```
    Your Pypoints: 300

    Which type of electromagnetic wave has the longest wavelength?
    A: Gamma Rays
    B: Radio Waves
    C: X-rays
    D: Microwaves

    To answer, please type only the amount of Pypoints you want to bet, eg. 500

    Your bet on A: 0
    Your bet on B: 400
    Your bet on C: 0
    Your bet on D: 0

    Don't spend more Pypoints than you have.

    Your bet on A: 0
    Your bet on B: 200
    Your bet on C: 0
    Your bet on D: 0

    Spend all of your Pypoints.

    Your bet on A:
    ```
5. The game runs for three rounds or until you will run out of Pypoints.

6. At the end of the game, the remaining Pypoints are converted into a virtual prize.


## Scoring System

1. Game 1: Quiz:
    * 30 Pypoints for every correct answer.
    * 10 questions -> Maximum of 300 Pypoints.

2. Game 2: Hangman:
    * For guessing the word: 300 Pypoints.
    * For not guessing the word: 0 Pypoints.
    * Maximum of 300 Pypoints.

3. Game 3: Rock, Paper, Scissors:
    * For winning: 300 Pypoints.
    * For losing: 0 Pypoints.
    * Maximum of 300 Pypoints.

4. Bonus:
    * If you scored 900 Pypoints (you obtained 300 Pypoints in every previous game),
    you receive an extra 100 Pypoints.

5. Final Game: The Betting Quiz
    * You start with a maximum of 1000 Pypoints.
    * If you have 0 Pypoints, you cannot play the final game.


## Virtual prize

At the end of the tournament, you obtain a virtual prize, which is an ASCII art image.

Source: https://www.asciiart.eu/ (the animals)
https://emojicombos.com/poop-ascii-art (poop)

Authors of the images:
1. Unicorn: -valkyrie-
2. Dolphin: Unknown author
3. Wolf: Blazej Kozlowski
4. Dog: Blazej Kozlowski
5. Parrot: Morfina
6. Cat: Marcin Glinski
7. Poop: Unknown author


## Code Structure

* project.py:
    * Python main script containing all games.

* questions_q1.csv:
    * CSV file containing 34 questions for the quiz (Game 1).
    * Each line consists of:
        * number of a question
        * question itself
        * 4 possible answers (A, B, C, D)
        * the answer for the question

* questions_q4.csv:
    * CSV file containing 20 questions for the final game.
    * Each line consists of:
        * number of a question
        * question itself
        * 4 possible answers (A, B, C, D)
        * the answer for the question

* word_list.py:
    * Contains a list of 100 words used for Hangman (Game 2).

* g1.py:
    * Python program containing The quiz (game 1).

* g2.py:
    * Python program containing Hangman (game 2).

* g3.py:
    * Python program containing Rock, Paper, Scissors (game 3).

* g4.py:
    * Python program containing the final game (the betting quiz).

* test_project.py:
    * Python program containing 7 test functions that check if the game
    funtions properly.


## Possible Future Improvements

* Implementation of a database to track scores over multiple sessions.

* Expanding the question database for more variety.

* Adding difficulty levels for the games.


## Author

Created by Iga Łakoma.


## License

This project is open-source. Feel free to modify and use it for educational purposes.


## Note from the author

Enjoy the game and have fun!

