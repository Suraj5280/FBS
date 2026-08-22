n = int(input("Enter a number: "))

sum = 0

for i in range(1, n):
    if n % i == 0:
        sum = sum + i

if sum == n:
    print("Perfect Number")
else:
    print("Not a Perfect Number")

#perfect number program
#A number is perfect if the sum of its factors excluding itself equals the number.
# Ex: 6=1+2+3