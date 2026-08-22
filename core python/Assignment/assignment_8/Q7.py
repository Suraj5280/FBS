def sumdigit(n):
    s = 0

    while(n > 0):
        digit = n % 10
        s = s + digit
        n = n // 10

    return s

n = int(input("Enter number: "))

print("Sum of digits =",sumdigit(n))