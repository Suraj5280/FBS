n = int(input("Enter number of passengers: "))
cost = float(input("Enter ticket cost per passenger: "))

total = 0

for i in range(1, n + 1):
    age = int(input("Enter age of passenger: "))

    if age < 12:
        amount = cost - (cost * 0.30)
    elif age > 59:
        amount = cost - (cost * 0.50)
    else:
        amount = cost

    total = total + amount

print("Total Ticket Amount =", total)



#multiple passnger ticket cost