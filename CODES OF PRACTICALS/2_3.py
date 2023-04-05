import random
n = random.randint(0, 99)
guess = int(input("Enter your guess :"))
while True:
    if guess < n:
        print("Your guess is too low")
        guess = int(input("Enter your guess :"))
    elif guess > n:
        print("Your guess is too high")
        guess = int(input("Enter your guess :"))
    else:
        print("You guessed it right!!")
        print("Yes, the number is ", guess)
        print("------------------------------------")
        break
