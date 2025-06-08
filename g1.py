#QUIZ (A B C D)

import csv
import random

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

