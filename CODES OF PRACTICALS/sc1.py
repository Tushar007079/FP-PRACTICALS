if __name__ == '__main__':
    n = int(input())
    # Create a list to store student records
    records = []
    # Loop through each student and their grade, and add them to the records list
    for i in range(n):
        name = input()
        grade = float(input())
        records.append([name, grade])
    # Find the second lowest grade
    grades = set([record[1] for record in records])
    second_lowest_grade = sorted(grades)[1]
    # Find the students with the second lowest grade
    second_lowest_students = [record[0] for record in records if record[1] == second_lowest_grade]
    # Sort the student names and print them
    for student in sorted(second_lowest_students):
        print(student)
