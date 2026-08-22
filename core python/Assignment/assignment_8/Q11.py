def armstrong(n):
    temp = n
    digits = 0

    while(temp > 0):
        digits = digits + 1
        temp = temp // 10

    temp = n
    s = 0

    while(temp > 0):
        digit = temp % 10
        s = s + digit ** digits
        temp = temp // 10

    return s

n = int(input("Enter number: "))

if(n == armstrong(n)):
    print("Armstrong Number")
else:
    print("Not Armstrong Number")