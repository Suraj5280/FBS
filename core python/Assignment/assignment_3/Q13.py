units = float(input("Enter electricity units: "))

if units <= 50:
    bill = units * 0.50
elif units <= 150:
    bill = 50 * 0.50 + (units - 50) * 0.75
elif units <= 250:
    bill = 50 * 0.50 + 100 * 0.75 + (units - 150) * 1.20
else:
    bill = 50 * 0.50 + 100 * 0.75 + 100 * 1.20 + (units - 250) * 1.50

surcharge = bill * 0.20
total_bill = bill + surcharge

print("Electricity Bill =", bill)
print("Surcharge =", surcharge)
print("Total Bill =", total_bill)


#bijli ka bill tera father bharega?
#if bill less than 50unit = .50 rupee per unit
#if bill less than 150unit = .75 rupee per unit
#if bill less than 250unit = 1.20 rupee per unit
#if bill greater than 250unit = 1.50 rupee per unit
