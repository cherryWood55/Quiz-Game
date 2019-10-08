import random

def test(questions):
    print ("General Instructions:\n1. Please enter only the choice number corresponding to the correct answer.\n2. Each question carries 5 points\n3. Wrong anwer leads to -1 marks per question\nGood Luck!\n")
    #using the random module and keeping the range upto len of the questions. This will shuffle the questions of a specific genre ex. science, commerce etc.
    index = random.randrange(len(questions))
    one = questions[index]
    # direct deletion, no search needed
    # after one question is popped on screen, deleting it from the pool of questions so that it doesn't appear twice to the user.
    del questions[index]
    print(one)
    ans1=input()
  
    index = random.randrange(len(questions))
    two = questions[index]
    # direct deletion, no search needed
    del questions[index]
    print(two)
    ans2 = input()
    
    index = random.randrange(len(questions))
    three = questions[index]
    # direct deletion, no search needed
    del questions[index]
    print(three)
    ans3 = input()
  
    score = 0
    # comparing the ans stored above by the user input in ans1,ans2 and ans3 and then comparing it with the correct answer using dictionary search in d. If the value of the question asked ex. d[one] (where one is the question asked above) matches the ans1 entered by the user then, give them points as per criterion otherwise deduct or do as stated in marking policy.
    if ans1 == d[one] or ans1 == d[one].upper():
        score += 5
        print ("Q.1 Absolutely Correct!")
    else:
        score -=1
        print ("Q.1 Incorrect!")
        print ("Right Answer is " + d[one])
    if ans2 == d[two] or ans2 == d[two].upper():
        score += 5
        print ("Q.2 Absolutely Correct!")
    else:
        score -=1
        print ("Q.2 Incorrect!")
        print ("Right Answer is " + d[two])
    if ans3 == d[three]  or ans3 == d[three].upper():
        score += 5
        print ("Q.3 Absolutely Correct!")
    else:
        score -=1
        print ("Q.3 Incorrect!")
        print ("Right Answer is " + d[three])
    print ("Your Score:", score, "/15")

def play_quiz():
    print ("Welcome to Today's Quiz!\nChoose your domain of interest:\nA. Science and Technology\nB. History of India\nC. Commerce\nEnter your choice:")

    count = 0
    while(count < 3):
        choice = input()
        if choice == 'A' or choice == 'a':
            test(science_questions)
            break
        elif choice == 'B' or choice == 'b':
            test(history_questions)
            break
        elif choice == 'C' or choice == 'c':
            test(commerce_questions)
            break
        else:
            print ("Invalid choice. Enter again")
        count += 1
#Created the dictionary with all the questions from science, history and commerce. This will be used for searching & finding if the answer is correct or not by seeing the key, value.
d={"Which one of the following is India's permanent research station in Antarctica?\n(a) Ganga\n(b) Agni\n(c) Maitri\n(d) None of the above\n":'c' , "Identify India's first indigenous Satellite Launch Vehicle (SLV):\n(a)SLV-1\n(b)PSLV\n(c)SLV-3\n(d)GSLV\n":'c' , "Where is India's Central Rice Research Institue located?\n(a)Bengaluru\n(b)Kanpur\n(c)Coimbatore\n(d)Cuttack\n" :'d', "The Indian National Congress was founded by:\n(a) A.O.Hume\n(b) Bal Gangadhar Tilak\n(c) Motilal Nehru\n(d) Surendranath Banerjee\n":'a',"The author of 'Poverty and Un-British Rule in India is\n(a) R. C. Dutt\n(b) Dadabhai Naoroji\n(c) Lala Lajpat Rai\n(d) Surendra Nath Banerjee\n":'b',"Who among the following was popularly known as the ‘Frontier Gandhi’?\n(a) Hasrat Mohani\n(b) Maulana Abul Kalam Azad\n(c) Khan Abdul Ghaffar Khan\n(d) Iqbal Khan\n":'c',"Which one among the following has the largest share of exports from India?\n(a) Agriculture and Allied Commodity\n(b) Gems and Jewellery\n(c) Handicrafts\n(d) Electronic Goods\n":'b',"Which of the following is not a logical data structure?\n(a) Chain\n(b) Tree\n(c) Stack\n(d) List\n":'a',"The income from the sale of a machinery used in business is treated as?\n(a) Income from business and profession\n(b) Short-term capital gain\n(c) Long-term capital gain\n(d) Income from other sources\n":'b'}
science_questions = ["Which one of the following is India's permanent research station in Antarctica?\n(a) Ganga\n(b) Agni\n(c) Maitri\n(d) None of the above\n", "Identify India's first indigenous Satellite Launch Vehicle (SLV):\n(a)SLV-1\n(b)PSLV\n(c)SLV-3\n(d)GSLV\n","Where is India's Central Rice Research Institue located?\n(a)Bengaluru\n(b)Kanpur\n(c)Coimbatore\n(d)Cuttack\n"]
science_answers = ['c', 'c', 'd']
history_questions = ["The Indian National Congress was founded by:\n(a) A.O.Hume\n(b) Bal Gangadhar Tilak\n(c) Motilal Nehru\n(d) Surendranath Banerjee\n", "The author of 'Poverty and Un-British Rule in India is\n(a) R. C. Dutt\n(b) Dadabhai Naoroji\n(c) Lala Lajpat Rai\n(d) Surendra Nath Banerjee\n", "Who among the following was popularly known as the ‘Frontier Gandhi’?\n(a) Hasrat Mohani\n(b) Maulana Abul Kalam Azad\n(c) Khan Abdul Ghaffar Khan\n(d) Iqbal Khan\n"]
history_answers = ['a', 'b', 'c']
commerce_questions = ["Which one among the following has the largest share of exports from India?\n(a) Agriculture and Allied Commodity\n(b) Gems and Jewellery\n(c) Handicrafts\n(d) Electronic Goods\n", "Which of the following is not a logical data structure?\n(a) Chain\n(b) Tree\n(c) Stack\n(d) List\n", "The income from the sale of a machinery used in business is treated as?\n(a) Income from business and profession\n(b) Short-term capital gain\n(c) Long-term capital gain\n(d) Income from other sources\n"]
commerce_answers = ['b', 'a', 'b']
print ("Wanna test your GK?\nA. Yes\nB. No")
play = input()
if play == 'A' or play == 'a':
    play_quiz()
else:
    print ("Ok! See you later!")
