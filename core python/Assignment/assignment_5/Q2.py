n = int(input("Enter number of students: "))

total_percentage = 0

for i in range(1, n + 1):
    print("Student", i)

    total = 0

    for j in range(1, 6):
        marks = float(input("Enter marks of subject: "))
        total = total + marks

    percentage = total / 5
    print("Percentage =", percentage)

    total_percentage = total_percentage + percentage

average = total_percentage / n

print("Average Percentage =", average)



#percentage of student and avrage percentage of student marks