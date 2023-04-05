import random

magic_number = random.randint(0, 100)
num_attempts = 0

print("Guess a magic number between 0 and 100")

while True:
    guess = int(input("Enter your guess: "))
    num_attempts += 1
    
    if guess == magic_number:
        print("Yes, the number is", guess)
        print("Your total number of guesses is:", num_attempts)
        break
    elif guess < magic_number:
        print("Your guess is too low")
    else:
        print("Your guess is too high")
