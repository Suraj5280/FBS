n = int(input("Enter a number: "))

temp = n
sum = 0

while temp > 0:
    digit = temp % 10

    fact = 1
    for i in range(1, digit + 1):
        fact = fact * i

    sum = sum + fact
    temp = temp // 10

if sum == n:
    print("Strong Number")
else:
    print("Not a Strong Number")



#Strong number program
#A Strong Number is a number whose sum of factorials of its digits equals the number.
#Ex: 145 = 1! + 4! + 5!