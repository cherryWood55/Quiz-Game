#!/usr/bin/env python3
from topics import *

def ask_one_question(question):
    print("\n" + question)
    choice = input("Enter Choice [a/b/c/d]: ")
    while(True):
        if choice.lower() in ['a', 'b', 'c', 'd']:
            return choice
        else:
            print("Invalid choice. Enter again")
            choice = input("Enter Choice [a/b/c/d]: ")

def score_one_result(key, meta):
    actual = meta["answer"]
    if meta["user_response"].lower() == actual.lower():
        print("Q.{0} Absolutely Correct!\n".format(key))
        return 5
    else:
        print("Q.{0} Incorrect!".format(key))
        print("Right Answer is ({0})".format(actual))
        print ("Learn more @ " + meta["more_info"] + "\n")
        return -1


def test(questions):
    score = 0
    print("General Instructions:\n1. Please enter only the choice number corresponding to the correct answer.\n2. Each question carries 5 points\n3. Wrong anwer leads to -1 marks per question\nGood Luck!\n")
    for key, meta in questions.items():
        questions[key]["user_response"] = ask_one_question(meta["question"])
    print("\n***************** RESULT ********************\n")
    for key, meta in questions.items():
        score += score_one_result(key, meta)
    print("Your Score:", score, "/", (5 * len(questions)))

def play_quiz():
    print("Welcome to Today's Quiz!\nChoose your domain of interest:\n(a). Science and Technology\n(b). History of India\n(c). Commerce\nEnter your choice:")

    count = 0
    while(count < 3):
        choice = input("Enter Choice [a/b/c]: ")
        if choice.lower() == 'a':
            test(topics.science.questions)
            break
        elif choice.lower() == 'b':
            test(topics.history.questions)
            break
        elif choice.lower() =='c':
            test(topics.commerce.questions)
            break
        else:
            print("Invalid choice. Enter again")
        count += 1
        print("")

def user_begin_prompt():
    print("Wanna test your GK?\nA. Yes\nB. No")
    play = input()
    if play.lower() == 'a' or play.lower() ==  'y':
        play_quiz()
    else:
        print("Ok! See you later!")

def execute():
    user_begin_prompt()

if __name__ == '__main__':
    execute()
