 #* Python quiz game
questions=("How many elements are there in periodic table?: ",
           "Which animal lays the largest eggs?: ",
           "Which planet we live in?: ",
           "Which is the hottest planet in solar system?: ")
options=(("A. 116","B. 117 ","C. 118 ","D. 119"),
         ("A. Whale","B. Hen","C. Ostrich ","D. Crocodile "),
         ("A. Earth","B. Mars ","C. Jupiter","D. Saturn"),
         ("A. Mercury","B. Venus","C. Earth ","D. Mars "))
answers=("C","C","A","B")
guesses=[]
score=0
question_num=0

for question in questions:
    print("--------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D):").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score+=1
        print("--CORRECT!--")
    else:
        print("--INCORRECT!--")
        print(f"{answers[question_num]} is the correct answer")
    question_num+=1

print("--------------------------------")
print("            RESULTS                     ")
print("--------------------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end="")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end="")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")