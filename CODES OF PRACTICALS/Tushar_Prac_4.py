# Tushar's Prac 4.2
import string
def ispangram(str):
    bond = "abcdefghijklmnopqrstuvwxyz"
    for char in bond:
        if char not in str.lower():
            return False
    return True

string = input("Enter the String: ")
if (ispangram(string) == True):
    print("YES")
else:
    print("NO")
