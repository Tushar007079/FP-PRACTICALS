import random
magic_num=random.randint(0,100)
num_attempts=0

while True:
    guess=int(input("Enter Your Guess : "))
    num_attempts+=1
    
    if guess==magic_num:
        print("Yes the Number is : ",guess)
        print("Your Total Number of Guess is : ",num_attempts)
        break
    elif guess<magic_num:
        print("Your Guess is Low.")
    else:
        print("Your Guess is to High.")