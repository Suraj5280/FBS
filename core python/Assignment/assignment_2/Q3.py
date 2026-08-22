feet = float(input("Enter distance in feet: "))
inches = float(input("Enter distance in inches: "))

total_inches = (feet * 12) + inches

centimeter = total_inches * 2.54
meter = centimeter / 100

print("Distance in meter =", meter)
print("Distance in centimeter =", centimeter)


# feet inche to foot code