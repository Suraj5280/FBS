n = int(input("Enter a number: "))

temp = n
digits = 0

while(temp > 0):
    digits = digits + 1
    temp = temp // 10

temp = n
sum = 0

while(temp > 0):
    digit = temp % 10
    sum = sum + digit ** digits
    temp = temp // 10

if(sum == n):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")


#Armstrong number program
#An Armstrong number is a number where the sum of each digit raised to the power of the total number of digits 
# equals the original number.
# EX: 153 is armstrong 1^3 + 5^3 + 3^3 = 153
#                       1     125   27  = 153