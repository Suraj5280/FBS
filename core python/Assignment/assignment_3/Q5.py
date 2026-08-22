a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

if a == b and b == c:
    print("Equilateral")
elif a == b or b == c or a == c:
    print("Isosceles")
else:
    print("Scalene")


#are bhai tu trangleach ahe ka, konta vala ahe Equilateral vala ka Isosceles vala ka tu Scalene ahe
#(lamb raha mazhay pasun parat disu nako)