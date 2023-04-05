import random
characterset = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

charactersetsmall = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                     'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
t = len(characterset)
t3 = []
t1 = []
t2 = []
for i in range(100):
    f = random.randrange(t)
    temp = characterset[f].lower()
    t1.append(temp)
    t3.append(characterset[f])

print(t3)
for i in range(len(charactersetsmall)):
    temp2 = t1.count(charactersetsmall[i])
    t2.append(temp2)

print("The Occurence of each letter are :")
for i in range(len(charactersetsmall)):
    print(t2[i], charactersetsmall[i], end="   ")
