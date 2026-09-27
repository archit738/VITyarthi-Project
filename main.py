# Python Quiz game
import time

questions = (("How many bones are there in the human body ?"),
             ("How many planets are there in the solar system"),
             ("How many elements are there in the periodic table"),
             ("Which animal lies the largest egg ?"),
             ("What type of animal is the Cow ?"))

options = (("A. 206","B. 207","C. 208", "D. 209"),
           ("A. 8","B. 9","C. 10","D.11"),
           ("A. 117","B. 120","C.210", "D. 118"),
           ("A. Elephant", "B. Ostrich", "C. Lion", "D. Peacock"),
           ("A. Herbivore","B. Carnivore", "C. Omnivore","D. None of the above"))

answers = ("A","A","D","B","A")

guesses = []
score = 0
question_num = 0

for question in questions:
    print(question)
    for option in options[question_num]:
        print(option)
    
    guess = input("Enter your guess (A,B,C,D) = ").upper()
    guesses.append(guess)
    
    if guess == answers[question_num]:
        print("Correct !")
        score += 1
    else:
        print("Incorrect !")
    
    question_num += 1
    
    
print("========================")
print("        Results         ")
print("========================")

result = int(score/len(questions)*100)

print(f"You got your {result}% right.")

print("The correct answers are = ")
print()

print(answers)
time.sleep(1)
print("Thanks for playing the quiz game .")
        
        
   

