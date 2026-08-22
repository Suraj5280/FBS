total = 0

for i in range(5):
    marks = float(input("Enter marks: "))
    total = total + marks

percentage = total / 5

print("Percentage =", percentage)

if percentage >= 75:
    print("Distinction")
elif percentage >= 60:
    print("First Class")
elif percentage >= 50:
    print("Second Class")
elif percentage >= 35:
    print("Pass")
else:
    print("Fail")


#percentage based on 5 sub marks