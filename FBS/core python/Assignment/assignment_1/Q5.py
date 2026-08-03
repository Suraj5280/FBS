p = int(input("Enter principal: "))
t = int(input("Enter time: "))
r = int(input("Enter rate: "))

amount = p * (1 + r / 100) ** t

ci = amount - p
print("Compound Interest =", ci)