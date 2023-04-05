import random
t1 = {"Panther": 0, "Tiger": 0, "Cheetah": 0, "Gorilla": 0, "Elephant": 0,
      "Bear": 0, "Panda": 0, "Bengal Tiger": 0, "Jaguar": 0, "Lion": 0}
k1 = []
beginrandom = 1
endrandom = 10
endloop = len(t1)
for i in range(endloop):
    p = random.randint(beginrandom, endrandom)
    k1.append(p)
    if (p == 1):
        index = i
        t1['Lion'] = 1
        beginrandom = 2
        endloop = endloop-1
print(k1)
j = 0
for item in t1:
    if (k1[j] == 1):
        a = k1[9]
        k1[j] = a
        k1[9] = 1
        t1[item] = k1[j]
        j += 1
if 1 not in k1:
    t1['Lion'] = 1
    k1[9] = 1
    print("Lion was Assigned Cage 10.")
else:
    print("Lion was Assigned Cage :", index+1)
    print(t1)
