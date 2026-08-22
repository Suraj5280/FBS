a = float(input("Enter a: "))

sum = 0

for i in range(1, 11):
    sum = sum + (a ** i) / i

print("S =", sum)


#S = a + a²/2 + a³/3 + a⁴/4 + ... + a¹⁰/10
#keep adding this term till 10