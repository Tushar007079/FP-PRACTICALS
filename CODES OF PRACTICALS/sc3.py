n = int(input())
students = [["Upavan", 20], ["Krutagna", 50], ["Jainil", 50]]

for i in range(n):
    name = input()
    score = float(input())
    students.append([name, score])

# Sort the list of students by grade (second element)
students.sort(key=lambda x: x[1])

# Find the second lowest grade
second_lowest_grade = sorted(list(set([s[1] for s in students])))[1]

# Find and print the names of the students with the second lowest grade
for s in sorted([s[0] for s in students if s[1] == second_lowest_grade]):
    print(s)
