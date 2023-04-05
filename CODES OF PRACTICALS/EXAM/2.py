n=int(input())
students=[]

for i in range(n):
    name=input()
    grade=float(input())
    students.append([name,grade])
    
students.sort(key=lambda x:x[1])

second_lowest_grade=sorted(list(set([s[1] for s in students])))[1]

for s in sorted([s[0] for s in students if s[1] ==second_lowest_grade]):
    print(s)