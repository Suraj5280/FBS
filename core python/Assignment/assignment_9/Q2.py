def digits(n):
    if(n == 0):
        return 0
    else:
        return 1 + digits(n // 10)

def armstrong(n,d):
    if(n == 0):
        return 0
    else:
        digit = n % 10
        return digit ** d + armstrong(n // 10,d)

n = int(input("Enter number: "))

d = digits(n)

if(n == armstrong(n,d)):
    print("Armstrong Number")
else:
    print("Not Armstrong Number")