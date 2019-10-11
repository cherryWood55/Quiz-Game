#!/usr/bin/env python3
# pylint: disable=no-member
from topics import *

def ask_one_question(question):
    print(question)
    ans = input()
    return ans

def score_one_result(meta):
    actual = meta["answer"]
    if meta["user_response"].lower() == actual.lower():
        print("Q.1 Absolutely Correct!")
        return 5
    else:
        print("Q.1 Incorrect!")
        print("Right Answer is " + actual)
        print ("For more information, check out " + meta["more_info"] + "\n")
        return -1


def test(questions):
    score = 0
    print("General Instructions:\n1. Please enter only the choice number corresponding to the correct answer.\n2. Each question carries 5 points\n3. Wrong anwer leads to -1 marks per question\nGood Luck!\n")
    for key, meta in questions.items():
        questions[key]["user_response"] = ask_one_question(meta["question"])
    for key, meta in questions.items():
        score += score_one_result(meta)
    print("Your Score:", score, "/15")

def play_quiz():
    print("Welcome to Today's Quiz!\nChoose your domain of interest:\nA. Science and Technology\nB. History of India\nC. Commerce\nD. World GK Question\nEnter your choice:")

    count = 0
    while(count < 4):
        choice = input()
        if choice.lower() == 'a':
            test(topics.science.questions)
            break
        elif choice.lower() == 'b':
            test(topics.history.questions)
            break
        elif choice.lower() =='c':
            test(topics.commerce.questions)
            break
        elif choice.lower() =='d':
            test(topics.worldgk.questions)
            break
        else:
            print("Invalid choice. Enter again")
        count += 1

def user_begin_prompt():
    print("Wanna test your GK?\nA. Yes\nB. No")
    play = input()
    if play.lower() == 'a':
        play_quiz()
    else:
        print("Ok! See you later!")

def execute():
    user_begin_prompt()

if __name__ == '__main__':
    execute()
