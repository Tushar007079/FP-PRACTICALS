# Tushar's Practical 1
from datetime import date
from datetime import datetime
import random
import calendar


def calculateAge(birthDate):
    today = date.today()
    age = today.year - birthDate.year - \
        ((today.month, today.day) < (birthDate.month, birthDate.day))

    return age


# ------------------1------------
print("----------1-----------")
print("Age of Shyam's grandfather is :")
print(calculateAge(date(1947, 6, 5)), "years")
y = 1947
m = 6
print("\nCalander of month which Shyam's Grandfather was born:\n")
print("------------------------")
print(calendar.month(y, m))
print("------------------------")
# -----------------2------------
print("----------2-----------")
name = input("Enter your name: ")
age = int(input("Enter your age:"))
print("---------------------")
print("Your Name is: ", name)
print("\nYour Age is : ", age)
now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("\nCurrent Time =", current_time)

# -----------------3------------
print("----------3-----------")


def getSum(n):
    sum = 0
    for digit in str(n):
        sum += int(digit)
    return sum


n = input("Enter a number between 0 and 1000: ")
print("\nThe sum of the digits is :", getSum(n))