import random

t = random.randint(1, 10)
k = random.randint(1, 5)
f = t**k
print(t, "^ ? = ", f)
u = int(input("Enter Value for ? : "))
if (t == 1):
    print("Correct Answer.")
elif (u == k):
    print("Correct Answer.")
else:
    print("Wrong Answer!")
