import time
import random
import datetime
# ----------------------1-----------------------
print("----------------------1-----------------------")
ranks = ['Ace', '2', '3', '4', '5', '6', '7',
         '8', '9', '10', 'Jack', 'Queen', 'King']
suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
num = random.randint(1, 52)
print(num)
tk = num//13
print(suits[tk])
tk = num % 13
print(ranks[tk-1])

print(" The card you picked is the ", ranks[tk-1], "of", suits[tk])
print("\n")
print("----------------------------------------------")
# ----------------------2-----------------------
print("----------------------2-----------------------")


def first_day_of_month(year, first_day_of_year):

    first_days_of_month = []

    for month in range(1, 13):

        first_day = datetime.date(year, month, 1)
        day_name = first_day.strftime("%A")
        first_days_of_month.append(
            f"{first_day.strftime('%B')} 1, {year} is {day_name}")
    return first_days_of_month


year = 2021
first_day_of_year = 5  # Friday
z = first_day_of_month(year, first_day_of_year)
for txt in z:
    print(txt)
print("----------------------------------------------")
print("\n")
# ----------------------3-----------------------
print("----------------------3-----------------------")

# create a list to store the questions and options
quiz = []

# gather input from the faculty member
num_questions = int(input("Enter the number of questions for the quiz: "))
for i in range(num_questions):
    question = input("Enter question " + str(i+1) + ": ")
    options = input("Enter options for question " + str(i+1) +
                    " (separated by commas): ").split(",")
    correct_answer = input(
        "Enter the correct answer for question " + str(i+1) + ": ")
    quiz.append({"question": question, "options": options,
                "correct_answer": correct_answer})

# administer the quiz to the student
start_time = time.time()
score = 0
for i in range(num_questions):
    print("Question " + str(i+1) + ": " + quiz[i]["question"])
    print("Options: " + ", ".join(quiz[i]["options"]))
    answer = input("Enter your answer: ")
    if answer == quiz[i]["correct_answer"]:
        score += 1
end_time = time.time()

# report the results to the student
print("Quiz complete! You scored " +
      str(score) + " out of " + str(num_questions))
print("Time spent on the test: " + str(end_time - start_time) + " seconds")
