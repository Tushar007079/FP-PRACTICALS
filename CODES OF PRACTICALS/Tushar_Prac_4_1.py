# Tushar's Prac 4.1
name = input("Please enter your name: ")
while name == "" or name.isdigit():
    print("Name cannot be empty")
    name = input("Please enter your name: ")
address = input("Please enter your address: ")
while address == "":
    print("Address cannot be empty")
    address = input("Please enter your address: ")
contact_no = input("Please enter your contact number: ")
while not contact_no.isdigit() or len(contact_no) != 10:
    print("Contact number must be 10 digits")
    contact_no = input("Please enter your contact number: ")
pin_code = input("Please enter your pin code: ")
while not pin_code.isdigit() or len(pin_code) != 6:
    print("Pin code must be 6 digits")
    pin_code = input("Please enter your pin code: ")
hobbies = input("Please enter your hobbies: ")
while hobbies == "":
    print("Hobbies cannot be empty")
    hobbies = input("Please enter your hobbies: ")
life_goal = input("Please enter your life goal: ")
while life_goal == "":
    print("Life goal cannot be empty")
    life_goal = input("Please enter your life goal: ")
age = input("Please enter your age: ")
while not age.isdigit():
    print("Age must be a number")
    age = input("Please enter your age: ")
if int(age) < 18:
    print("You are eligible for education camps schemes")
elif int(age) >= 18 and int(age) < 25:
    print("You are eligible for educational scholarship scheme")
elif int(age) >= 25:
    print("You are eligible for retirement plans")
