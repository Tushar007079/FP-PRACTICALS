import random
dict1 = {"ostrich": 0, "koala": 0, "giraffe": 0, "capybara": 0,"hippo": 0,"tiger": 0, "rhino": 0, "elephant": 0, "jaguar": 0, "lion": 0}
l1 = []
startrandom = 1
endrandom = 10
endloop = len(dict1)
for i in range(endloop):
    x = random.randint(startrandom, endrandom)
    l1.append(x)
if (x == 1):
    index = i
    dict1['lion'] = 1
    startrandom = 2
    endloop = endloop-1
    print(l1)
    j = 0
    for item in dict1:
        if (l1[j] == 1):
            a = l1[9]
            l1[j] = a
            l1[9] = 1
            dict1[item] = l1[j]
            j += 1
if 1 not in l1:
    dict1['lion'] = 1
    l1[9] = 1
    print("LION WAS ASSIGNED CAGE 10")
else:
    print("LION WAS ASSGINED CAGE", index+1)
print(dict1)
