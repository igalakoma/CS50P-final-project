# ROCK PAPER SCISSORS

import random

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


