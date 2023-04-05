#______TUSHAR's PRCTICAL 2_______
import random
import time  
# ------------------1-------------
print("------------------1-------------")
amount = eval(input("Enter an amount in double, for example 12.56 : "))
remainingAmount = int(amount * 100)
numberOfOneDollars = int(remainingAmount / 100)
remainingAmount = int(remainingAmount % 100)
numberOfQuarters = int(remainingAmount / 25)
remainingAmount = remainingAmount % 25
numberOfDimes = int(remainingAmount / 10)
remainingAmount = remainingAmount % 10
numberOfNickels = int(remainingAmount / 5)
remainingAmount = remainingAmount % 5
numberOfPennies = remainingAmount

print("Your amount", amount, "consists of\n",
      "\t", numberOfOneDollars, "dollars\n",
      "\t", numberOfQuarters, "quarters\n",
      "\t", numberOfDimes, "dimes\n",
      "\t", numberOfNickels, "nickels\n",
      "\t", numberOfPennies, "pennies\n")
print("------------------------------------")


# ------------------2-------------
print("------------------2-------------")
user_num = 0
#lottery_num=random.randint(10,99)
lottery_num = 12

print("****Welcom to Lottery Program*****")
user_num = int(input("Please Enter a your two digit lottery number :"))
print("Calculating Results....")
for i in range(3):
    time.sleep(1)
    print(".")

    # calculate and output
    lottery_tens = lottery_num // 10
    lottery_ones = lottery_num % 10

    user_tens = user_num // 10
    user_ones = user_num % 10

    if lottery_num == user_num:
        print("All your numbers match in exact order! Your reward is $10,000!\n")
        break
    elif lottery_tens == user_ones and lottery_ones == user_tens:
        print("All your numbers match! Your reward is $5,000!\n")
        break
    elif lottery_tens == user_tens or lottery_ones == user_ones \
      or lottery_ones == user_tens or lottery_tens == user_ones:
        print("One of your number match the lottery. Your reward is $2,000\n")
        break
    else:
        print("Your numbers not match! sorry!!\n")
        print("BETTER LUCK NEXT TIME... ")
        print("------------------------------------")
        break
        
# ------------------3-------------
print("------------------3-------------")
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