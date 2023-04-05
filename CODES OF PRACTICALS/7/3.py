txt = "Swachh Bharat Mission\n"

with open('circular.txt', 'w') as f:
    f.write(txt)

with open('circular.txt', 'r') as f:
    circular = f.read()
    print(circular)

while True:
    suggestion = input("Enter Your Suggestion : \n")
    with open('circular.txt', 'a') as f:
        f.write(f"\n{suggestion}")
    confirm = input("Enter Another Suggestion?[Y/N] :")
    if confirm == 'N':
        break
    elif confirm != 'Y':
        print("ERROR : Invalid Input!")
        break
