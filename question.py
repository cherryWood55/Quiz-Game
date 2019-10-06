# coding: utf-8
def test(questions, answers):
    print ("General Instructions:\n1. Please enter only the choice number corresponding to the correct answer.\n2. Each question carries 5 points\n3. Wrong anwer leads to -1 marks per question\nGood Luck!\n")
    print (questions[0])
    ans1 = input()
    print (questions[1])
    ans2 = input()
    print (questions[2])
    ans3 = input()
    print (questions[3])
    ans4 = input()
    score = 0
    if ans1 == answers[0] or ans1 == answers[0].upper():
        score += 5
        print ("Q.1 Absolutely Correct!")
    else:
        score -=1
        print ("Q.1 Incorrect!")
        print ("Right Answer is " + answers[0])
    if ans2 == answers[1] or ans2 == answers[1].upper():
        score += 5
        print ("Q.2 Absolutely Correct!")
    else:
        score -=1
        print ("Q.2 Incorrect!")
        print ("Right Answer is " + answers[1])
    if ans3 == answers[2] or ans3 == answers[2].upper():
        score += 5
        print ("Q.3 Absolutely Correct!")
    else:
        score -=1
        print ("Q.3 Incorrect!")
        print ("Right Answer is " + answers[2])
    if ans4 == answers[3] or ans4 == answers[3].upper():
        score += 5
        print ("Q.3 Absolutely Correct!")
    else:
        score -=1
        print ("Q.4 Incorrect!")
        print ("Right Answer is " + answers[3])
    print ("Your Score:", score, "/15")

def play_quiz():
    print ("Welcome to Today's Quiz!\nChoose your domain of interest:\nA. Science and Technology\nB. History of India\nC. Commerce\nEnter your choice:")

    count = 0
    while(count < 3):
        choice = input()
        if choice == 'A' or choice == 'a':
            test(science_questions, science_answers)
            break
        elif choice == 'B' or choice == 'b':
            test(history_questions, history_answers)
            break
        elif choice == 'C' or choice =='c':
            test(commerce_questions, commerce_answers)
            break
        else:
            print ("Invalid choice. Enter again")
        count += 1

science_questions = ["Which one of the following is India's permanent research station in Antarctica?\n(a) Ganga\n(b) Agni\n(c) Maitri\n(d) None of the above\n", "Identify India's first indigenous Satellite Launch Vehicle (SLV):\n(a)SLV-1\n(b)PSLV\n(c)SLV-3\n(d)GSLV\n","Where is India's Central Rice Research Institue located?\n(a)Bengaluru\n(b)Kanpur\n(c)Coimbatore\n(d)Cuttack\n","Which dam withhold the largest water reservoir in India?\n(a)Bhakra Dam\n(b)Indrisagar Dam\n(c)Hirakud Dam\n(d)Tehri Dam\n"]
science_answers = ['c', 'c', 'd', 'b']
history_questions = ["The Indian National Congress was founded by:\n(a) A.O.Hume\n(b) Bal Gangadhar Tilak\n(c) Motilal Nehru\n(d) Surendranath Banerjee\n", "The author of 'Poverty and Un-British Rule in India is\n(a) R. C. Dutt\n(b) Dadabhai Naoroji\n(c) Lala Lajpat Rai\n(d) Surendra Nath Banerjee\n", "Who among the following was popularly known as the ‘Frontier Gandhi’?\n(a) Hasrat Mohani\n(b) Maulana Abul Kalam Azad\n(c) Khan Abdul Ghaffar Khan\n(d) Iqbal Khan\n"]
history_answers = ['a', 'b', 'c']
commerce_questions = ["Which one among the following has the largest share of exports from India?\n(a) Agriculture and Allied Commodity\n(b) Gems and Jewellery\n(c) Handicrafts\n(d) Electronic Goods\n", "Which of the following is not a logical data structure?\n(a) Chain\n(b) Tree\n(c) Stack\n(d) List\n", "The income from the sale of a machinery used in business is treated as?\n(a) Income from business and profession\n(b) Short-term capital gain\n(c) Long-term capital gain\n(d) Income from other sources\n"]
commerce_answers = ['b', 'a', 'b']
print ("Wanna test your GK?\nA. Yes\nB. No")
play = input()
if play == 'A' or play =='a':
    play_quiz()
else:
    print ("Ok! See you later!")



    

    
    
    
