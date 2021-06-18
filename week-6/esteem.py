def questions():
    answers = []
    questions = [
    "1. I feel that I am a person of worth, at least on an equal plane with others.",
    "2. I feel that I have a number of good qualities.",
    "3. All in all, I am inclined to feel that I am a failure.",
    "4. I am able to do things as well as most other people.",
    "5. I feel I do not have much to be proud of.",
    "6. I take a positive attitude toward myself.",
    "7. On the whole, I am satisfied with myself.",
    "8. I wish I could have more respect for myself.",
    "9. I certainly feel useless at times.",
    "10. At times I think I am no good at all.",
    ]
 
    for i in questions:
        vaild_anwser = False
        while vaild_anwser == False:
            answer = input(f"{i} ")
 
            if answer == "D" or answer == "d" or answer == "a" or answer == "A":
                vaild_anwser = True
                answers.append( answer )
            else:
                print( "Invaild anwser. Please try again." )
 
    return answers

def compute(answers):
    score = 0
    for i in answers:
        score += answers[i]
    return score

def convert(answers):
    set1 = answers[0,1,3,5,6]
    set2 = answers[2,4,7,8,9]

    for i in set1:
        if answers[i] == "D":
            answers[i] = 0
        elif answers[i] == "d":
            answers[i] = 1
        elif answers[i] == "a":
            answers[i] = 2
        else:
            answers[i] = 3

    for i in set2:
        if answers[i] == "D":
            answers[i] = 3
        elif answers[i] == "d":
            answers[i] = 2
        elif answers[i] == "a":
            answers[i] = 1
        else:
            answers[i] = 0

    return answers

def main():
    answers = questions()
    answers = convert(answers)
    final = compute(answers)