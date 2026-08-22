total = 0

for i in range(5):
    age = int(input("Enter age: "))
    amount = float(input("Enter ticket amount: "))

    if age < 12:
        amount = amount - amount * 30 / 100
    elif age > 59:
        amount = amount - amount * 50 / 100

    total = total + amount

print("Total Ticket Amount =", total)

# ticket price acoording to age
#jeshta nagrik discount
#under 12 discount