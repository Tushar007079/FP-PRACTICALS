n = int(input())
records = [["Upavan", 20], ["Krutagna", 50], ["Jainil", 50]]
for i in range(n):
    name = input()
    grade = float(input())
    records.append([name, grade])

# Sort the records by grade in ascending order
sorted_records = sorted(records, key=lambda x: x[1])

# Find the second lowest grade
second_lowest_grade = sorted(set([record[1] for record in sorted_records]))[1]

# Print the names of students with the second lowest grade
for record in sorted_records:
    if record[1] == second_lowest_grade:
        print(record[0])
