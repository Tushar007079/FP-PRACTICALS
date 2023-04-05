# Quiz program
import time

# List of questions
questions = [
    {"question": "What is the capital of France?", "options": [
        "Paris", "London", "Rome", "Madrid"], "answer": "Paris"},
    {"question": "What is the largest planet in our solar system?", "options": [
        "Earth", "Jupiter", "Saturn", "Mars"], "answer": "Jupiter"},
    {"question": "What is the smallest country in the world?", "options": [
        "Vatican City", "Monaco", "Nauru", "Tuvalu"], "answer": "Vatican City"},
    {"question": "What is the name of the longest river in the world?",
        "options": ["Amazon", "Nile", "Yangtze", "Mississippi"], "answer": "Nile"}
]

# List to store correct answers
correct_answers = []

# Start time of the quiz
start_time = time.time()

# Iterate through the questions
for question in questions:
    print(question["question"])
print("Options:")
for option in question["options"]:
    print(option)
# Get the student's answer
student_answer = input("Enter your answer: ")
# Check if the answer is correct
if student_answer == question["answer"]:
    print("Correct!")
    correct_answers.append(True)
else:
    print("Incorrect.")
    correct_answers.append(False)

# End time of the quiz
end_time = time.time()

# Calculate the time spent on the quiz
time_spent = end_time - start_time

# Print the number of correct answers
print("You got " + str(correct_answers.count(True)) +
      " out of " + str(len(questions)) + " questions correct.")

# Print the time spent on the quiz
print("Time spent on the quiz: " + str(time_spent) + " seconds.")

# Report the correct answers
print("Correct answers:")
for i in range(len(questions)):
    if correct_answers[i]:
        print(questions[i]["answer"])
else:
    print("Incorrect.")
